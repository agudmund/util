#!/usr/bin/env python3
"""
Drag video file onto this script → extracts ~30 fps frames as PNGs
Output folder created next to the video file.
Also saves extraction_log.txt and extraction_errors.txt in the output folder.
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

if len(sys.argv) != 2:
    print("Drag exactly one video file onto this script.")
    input("Press Enter to close...")
    sys.exit(1)

video_path = Path(sys.argv[1])
if not video_path.is_file():
    print("Not a valid file:", video_path)
    input("Press Enter to close...")
    sys.exit(1)

# Output folder = same directory as video
output_dir = video_path.parent / f"frames_{video_path.stem}"
output_dir.mkdir(exist_ok=True)

output_pattern = output_dir / "frame_%05d.png"

log_file      = output_dir / "extraction_log.txt"
error_file    = output_dir / "extraction_errors.txt"

# Clear old logs if they exist (or append — your choice; here we overwrite)
with open(log_file, "w", encoding="utf-8") as f:
    f.write(f"Frame extraction started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Video: {video_path}\n")
    f.write(f"Output folder: {output_dir}\n")
    f.write(f"Target: ~30 fps PNG frames\n\n")

with open(error_file, "w", encoding="utf-8") as f:
    f.write(f"Errors & warnings log: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Video: {video_path}\n\n")

print(f"Video:   {video_path.name}")
print(f"Output:  {output_dir.name}")
print("Extracting ≈30 fps frames... (logs saved in output folder)")

try:
    # Run ffmpeg and split output: normal → log, errors/warnings → error log + console
    with (
        open(log_file,   "a", encoding="utf-8") as log_f,
        open(error_file, "a", encoding="utf-8") as err_f
    ):
        process = subprocess.Popen(
            [
                "ffmpeg",
                "-i", str(video_path),
                "-vf", "fps=30",
                "-q:v", "4",
                "-vsync", "0",
                "-hide_banner",
                "-loglevel", "info",
                str(output_pattern)
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        # Stream stdout → log file + minimal console feedback
        for line in process.stdout:
            log_f.write(line)
            # Only show important lines in console (optional filter)
            if "frame=" in line or "video:" in line or "Lsize=" in line:
                print(line.strip())

        # Capture stderr separately
        stderr_output = process.stderr.read()
        if stderr_output:
            err_f.write(stderr_output)
            # Show errors in console too
            print("\nffmpeg reported issues/warnings:")
            print(stderr_output.strip())

        return_code = process.wait()

    if return_code == 0:
        count = len(list(output_dir.glob("*.png")))
        success_msg = f"Done — {count} frames saved\nFinished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        print(success_msg)
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("\n" + success_msg)
    else:
        err_msg = f"ffmpeg exited with code {return_code} (check extraction_errors.txt)"
        print(err_msg)
        with open(error_file, "a", encoding="utf-8") as f:
            f.write(err_msg + "\n")

except FileNotFoundError:
    msg = "ERROR: ffmpeg not found. Install it and add to PATH.\nhttps://ffmpeg.org/download.html"
    print(msg)
    with open(error_file, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
except Exception as e:
    msg = f"Unexpected error: {str(e)}"
    print(msg)
    with open(error_file, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

input("\nPress Enter to close...")