import os
import sys
import shutil
import subprocess
import threading
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# -----------------------------
#  Config / helpers
# -----------------------------

# Default download folder: ~/Music/MP3 Downloads
DEFAULT_DIR = os.path.join(os.path.expanduser("~"), "Music", "MP3 Downloads")


def ensure_default_dir():
    os.makedirs(DEFAULT_DIR, exist_ok=True)


def find_ffmpeg():
    """Try to locate ffmpeg in the current PATH.
When you run this inside the virtual environment,
it should find Vertual_Enviroment/bin/ffmpeg.
    """
    path = shutil.which("ffmpeg")
    return path


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

    def set_status(text):
        status_var.set(text)

    def set_progress(pct):
        progress_var.set(pct)

    root.after(0, set_status, "Starting download…")
    root.after(0, set_progress, 0.0)

    # Output template for yt-dlp
    output_template = os.path.join(folder, "%(title)s.%(ext)s")

    # Build yt-dlp command
    cmd = [
        sys.executable,
        "-m", "yt_dlp",
        "--ffmpeg-location", ffmpeg_path,
        "-x",
        "--audio-format", "mp3",
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
            # Look for "NN.N%" in yt-dlp output
            m = re.search(r"(\d+(?:\.\d+)?)%", line)
            if m:
                pct = float(m.group(1))
                root.after(0, set_progress, pct)
                root.after(0, set_status, f"Downloading… {pct:.1f}%")

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
        messagebox.showinfo("Success", "MP3 downloaded successfully!")

    root.after(0, _on_success)


# -----------------------------
#  GUI setup
# -----------------------------

root = tk.Tk()
root.title("MP3 Downloader")
root.geometry("560x270")

url_var = tk.StringVar()
download_dir = tk.StringVar()
status_var = tk.StringVar(value="Ready")
progress_var = tk.DoubleVar(value=0.0)

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
    width=52,
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

# Download button
tk.Button(frame, text="Download MP3", command=start_download_thread).grid(
    row=2, column=1, pady=8
)

# Progress bar
progress_bar = ttk.Progressbar(
    frame,
    variable=progress_var,
    maximum=100,
    length=340,
    mode="determinate",
)
progress_bar.grid(row=3, column=0, columnspan=3, pady=8, sticky="we")

# Status label
tk.Label(frame, textvariable=status_var, anchor="w").grid(
    row=4, column=0, columnspan=3, sticky="w"
)

frame.columnconfigure(1, weight=1)

root.mainloop()
