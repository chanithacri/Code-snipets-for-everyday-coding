import os
import sys
import shutil
import subprocess
import threading
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

"""
MP3 / AAC Downloader with:
- Progress bar
- Friendly URL entry with placeholder
- "Music optimizing" profiles:
- Compact (MP3 128k)
- Balanced (MP3 192k)
- Studio (MP3 320k)
- Apple-like (AAC 256k, .m4a-style)
Assumes:
- yt-dlp is installed in the same virtualenv
- ffmpeg & ffprobe are available in PATH (e.g. venv/bin)
"""

# -----------------------------
#  Config / helpers
# -----------------------------

# Default download folder: ~/Music/MP3 Downloads
DEFAULT_DIR = os.path.join(os.path.expanduser("~"), "Music", "MP3 Downloads")

# Quality profiles: format, bitrate (kbps), codec
QUALITY_PROFILES = {
    "Compact (MP3 128k)": {
        "format": "mp3",
        "bitrate": 128,
        "codec": "libmp3lame",
    },
    "Balanced (MP3 192k)": {
        "format": "mp3",
        "bitrate": 192,
        "codec": "libmp3lame",
    },
    "Studio (MP3 320k)": {
        "format": "mp3",
        "bitrate": 320,
        "codec": "libmp3lame",
    },
    "Apple-like (AAC 256k)": {
        "format": "m4a",    # AAC in M4A container (Apple-y)
        "bitrate": 256,
        "codec": "aac",
    },
}


def ensure_default_dir():
    os.makedirs(DEFAULT_DIR, exist_ok=True)


def find_ffmpeg():
    """
Try to locate ffmpeg in the current PATH.
When you run this inside the virtual environment,
it should find venv/bin/ffmpeg.
    """
    return shutil.which("ffmpeg")


# -----------------------------
#  GUI callbacks
# -----------------------------

def pick_folder():
    folder = filedialog.askdirectory(initialdir=download_dir.get())
    if folder:
        download_dir.set(folder)


def start_download_thread():
    """Start the download in a background thread so the UI stays responsive."""
    t = threading.Thread(target=download_mp3_worker, daemon=True)
    t.start()


def download_mp3_worker():
    """Actual download logic (runs in a background thread)."""
    url = url_var.get().strip()
    # Handle case where placeholder text is still present
    if url == "Paste a video URL here…":
        url = ""

    if not url:
        root.after(0, lambda: messagebox.showerror("Error", "Please paste a video URL first."))
        return

    folder = download_dir.get().strip()
    if not folder:
        root.after(0, lambda: messagebox.showerror("Error", "Please choose a download folder."))
        return

    os.makedirs(folder, exist_ok=True)

    ffmpeg_path = find_ffmpeg()
    if not ffmpeg_path:
        def _no_ffmpeg():
            messagebox.showerror(
                "ffmpeg not found",
                "Could not find ffmpeg.\n\n"
                "Make sure ffmpeg is in your virtual environment's 'bin' folder\n"
                "and that you activated the virtual environment before running this app."
            )
        root.after(0, _no_ffmpeg)
        return

    # Get selected optimization profile
    profile_label = quality_var.get()
    profile = QUALITY_PROFILES.get(profile_label)

    if profile is None:
        # Fallback if something weird happens
        profile_label = "Balanced (MP3 192k)"
        profile = QUALITY_PROFILES[profile_label]

    audio_format = profile["format"]       # "mp3" or "m4a"
    bitrate_kbps = profile["bitrate"]      # 128 / 192 / 256 / 320
    codec = profile["codec"]              # "libmp3lame" or "aac"

    def set_status(text: str):
        status_var.set(text)

    def set_progress(pct: float):
        progress_var.set(pct)

    root.after(0, set_status, f"Starting download ({profile_label})…")
    root.after(0, set_progress, 0.0)

    # Output template for yt-dlp
    output_template = os.path.join(folder, "%(title)s.%(ext)s")

    # Postprocessor args to control codec + bitrate
    # This tells ffmpeg exactly how to encode the audio stream.
    pp_args = f"ffmpeg:-c:a {codec} -b:a {bitrate_kbps}k"

    # Build yt-dlp command
    cmd = [
        sys.executable,
        "-m", "yt_dlp",
        "--ffmpeg-location", ffmpeg_path,
        "-x",
        "--audio-format", audio_format,
        "--postprocessor-args", pp_args,
        "-o", output_template,
        url,
    ]

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        # Read yt-dlp output line by line and update progress
        for line in proc.stdout:
            line = line.strip()
            # Look for "NN.N%" pattern in yt-dlp output
            m = re.search(r"(\d+(?:\.\d+)?)%", line)
            if m:
                pct = float(m.group(1))
                root.after(0, set_progress, pct)
                root.after(0, set_status, f"Downloading… {pct:.1f}% ({profile_label})")

        proc.wait()
        if proc.returncode != 0:
            raise RuntimeError(
                f"yt-dlp exited with code {proc.returncode}. "
                "Check the URL, network connection, or yt-dlp version."
            )

    except Exception as e:
        def _on_error():
            progress_var.set(0.0)
            status_var.set("Failed")
            messagebox.showerror("Download failed", str(e))
        root.after(0, _on_error)
        return

    # Success
    def _on_success():
        progress_var.set(100.0)
        status_var.set("Done!")
        messagebox.showinfo(
            "Success",
            f"Audio downloaded successfully!\n\n"
            f"Profile: {profile_label}\n"
            f"Format: {audio_format.upper()}\n"
            f"Bitrate: {bitrate_kbps} kbps"
        )

    root.after(0, _on_success)


# -----------------------------
#  GUI setup
# -----------------------------

root = tk.Tk()
root.title("MP3 / AAC Downloader + Optimizer")
root.geometry("620x330")

url_var = tk.StringVar()
download_dir = tk.StringVar()
status_var = tk.StringVar(value="Ready")
progress_var = tk.DoubleVar(value=0.0)
quality_var = tk.StringVar(value="Balanced (MP3 192k)")

ensure_default_dir()
download_dir.set(DEFAULT_DIR)

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill="both", expand=True)

# -----------------------------
# Friendly URL Entry Setup
# -----------------------------

def clear_placeholder(event):
    if url_var.get() == "Paste a video URL here…":
        url_entry.config(fg="#000000")
        url_var.set("")


def add_placeholder(event):
    if not url_var.get().strip():
        url_entry.config(fg="#777777")
        url_var.set("Paste a video URL here…")


# URL label + friendly entry
tk.Label(frame, text="Video URL:", font=("SF Pro", 12, "bold")).grid(row=0, column=0, sticky="w")

url_entry = tk.Entry(
    frame,
    textvariable=url_var,
    width=55,
    font=("SF Pro", 13),
    fg="#777777",
    bd=2,
    relief="groove",
    highlightthickness=1,
    highlightcolor="#4A90E2",
    highlightbackground="#CCCCCC",
)
url_entry.grid(row=0, column=1, columnspan=2, sticky="we", pady=6)

# Add placeholder behavior
url_var.set("Paste a video URL here…")
url_entry.bind("<FocusIn>", clear_placeholder)
url_entry.bind("<FocusOut>", add_placeholder)

# Autofocus on app start
url_entry.focus_set()

# Folder label + entry + browse button
tk.Label(frame, text="Download to:", font=("SF Pro", 11)).grid(row=1, column=0, sticky="w")

tk.Entry(frame, textvariable=download_dir, width=40).grid(
    row=1, column=1, sticky="we", pady=5
)

tk.Button(frame, text="Browse…", command=pick_folder).grid(
    row=1, column=2, padx=5
)

# Quality / optimization profile
quality_label = tk.Label(frame, text="Optimize for:", font=("SF Pro", 11))
quality_label.grid(row=2, column=0, sticky="w", pady=(6, 0))

quality_combo = ttk.Combobox(
    frame,
    textvariable=quality_var,
    values=list(QUALITY_PROFILES.keys()),
    state="readonly",
)
quality_combo.grid(row=2, column=1, sticky="we", pady=(6, 0))
quality_combo.set("Balanced (MP3 192k)")

# Download button
tk.Button(frame, text="Download Audio", command=start_download_thread).grid(
    row=2, column=2, padx=5, pady=(6, 0)
)

# Progress bar
progress_bar = ttk.Progressbar(
    frame,
    variable=progress_var,
    maximum=100,
    length=380,
    mode="determinate",
)
progress_bar.grid(row=3, column=0, columnspan=3, pady=10, sticky="we")

# Status label
tk.Label(frame, textvariable=status_var, anchor="w").grid(
    row=4, column=0, columnspan=3, sticky="w"
)

frame.columnconfigure(1, weight=1)

root.mainloop()
