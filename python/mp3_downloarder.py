import os
import sys
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# -----------------------------
#  Config / helpers
# -----------------------------

# Default download folder: ~/Music/MP3 Downloads
DEFAULT_DIR = os.path.join(os.path.expanduser("~"), "Music", "MP3 Downloads")


def ensure_default_dir():
    os.makedirs(DEFAULT_DIR, exist_ok=True)


def find_ffmpeg():
    """
Try to locate ffmpeg in the current PATH.
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


def download_mp3():
    url = url_var.get().strip()
    if not url:
        messagebox.showerror("Error", "Please paste a video URL first.")
        return

    folder = download_dir.get().strip()
    if not folder:
        messagebox.showerror("Error", "Please choose a download folder.")
        return

    # Ensure folder exists
    os.makedirs(folder, exist_ok=True)

    ffmpeg_path = find_ffmpeg()
    if not ffmpeg_path:
        messagebox.showerror(
            "ffmpeg not found",
            "Could not find ffmpeg.\n\n"
            "Make sure ffmpeg is in your virtual environment's 'bin' folder\n"
            "and that you activated the virtual environment before running this app."
        )
        return

    status_var.set("Downloading...")
    root.update_idletasks()

    # Output template for yt-dlp
    output_template = os.path.join(folder, "%(title)s.%(ext)s")

    # Build yt-dlp command
    cmd = [
        sys.executable,      # the Python inside the venv
        "-m", "yt_dlp",
        "--ffmpeg-location", ffmpeg_path,
        "-x",                # extract audio
        "--audio-format", "mp3",
        "-o", output_template,
        url,
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            # Include stderr so you can debug if something goes wrong
            error_msg = result.stderr.strip() or "Unknown error from yt-dlp."
            raise RuntimeError(error_msg)

    except Exception as e:
        status_var.set("Failed")
        messagebox.showerror("Download failed", str(e))
        return

    status_var.set("Done!")
    messagebox.showinfo("Success", "MP3 downloaded successfully!")


# -----------------------------
#  GUI setup
# -----------------------------

root = tk.Tk()
root.title("MP3 Downloader")
root.geometry("520x230")

url_var = tk.StringVar()
download_dir = tk.StringVar()
status_var = tk.StringVar(value="Ready")

ensure_default_dir()
download_dir.set(DEFAULT_DIR)

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill="both", expand=True)

# URL label + entry
tk.Label(frame, text="Video URL:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=url_var, width=52).grid(
    row=0, column=1, columnspan=2, sticky="we", pady=5
)

# Folder label + entry + browse button
tk.Label(frame, text="Download to:").grid(row=1, column=0, sticky="w")
tk.Entry(frame, textvariable=download_dir, width=40).grid(
    row=1, column=1, sticky="we", pady=5
)
tk.Button(frame, text="Browse…", command=pick_folder).grid(
    row=1, column=2, padx=5
)

# Download button
tk.Button(frame, text="Download MP3", command=download_mp3).grid(
    row=2, column=1, pady=12
)

# Status label
tk.Label(frame, textvariable=status_var, anchor="w").grid(
    row=3, column=0, columnspan=3, sticky="w"
)

frame.columnconfigure(1, weight=1)

root.mainloop()
