import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Default download location
DEFAULT_DIR = os.path.join(os.path.expanduser("~"), "Music", "MP3 Downloads")


def ensure_default_dir():
    os.makedirs(DEFAULT_DIR, exist_ok=True)


def pick_folder():
    folder = filedialog.askdirectory(initialdir=download_dir.get())
    if folder:
        download_dir.set(folder)


def download_mp3():
    url = url_var.get().strip()
    if not url:
        messagebox.showerror("Error", "Please paste a URL.")
        return

    folder = download_dir.get().strip()
    if not folder:
        messagebox.showerror("Error", "Please choose a download folder.")
        return

    os.makedirs(folder, exist_ok=True)

    status_var.set("Downloading...")
    root.update_idletasks()

    # Output filename template
    output_template = os.path.join(folder, "%(title)s.%(ext)s")

    # Use Python’s executable so the same environment is used
    cmd = [
        sys.executable,
        "-m", "yt_dlp",
        "-x",
        "--audio-format", "mp3",
        "-o", output_template,
        url
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            error = result.stderr.strip() or "Unknown error from yt-dlp."
            raise RuntimeError(error)

    except Exception as e:
        messagebox.showerror("Download failed", str(e))
        status_var.set("Failed")
        return

    status_var.set("Done!")
    messagebox.showinfo("Success", "MP3 downloaded successfully!")


# GUI setup
root = tk.Tk()
root.title("MP3 Downloader")
root.geometry("500x220")

url_var = tk.StringVar()
download_dir = tk.StringVar()
status_var = tk.StringVar(value="Ready")

# Prepare default folder
ensure_default_dir()
download_dir.set(DEFAULT_DIR)

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill="both", expand=True)

# URL entry
tk.Label(frame, text="Video URL:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=url_var, width=50).grid(
    row=0, column=1, columnspan=2, sticky="we", pady=5
)

# Folder select
tk.Label(frame, text="Download to:").grid(row=1, column=0, sticky="w")
tk.Entry(frame, textvariable=download_dir, width=40).grid(
    row=1, column=1, sticky="we", pady=5
)
tk.Button(frame, text="Browse…", command=pick_folder).grid(row=1, column=2, padx=5)

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
