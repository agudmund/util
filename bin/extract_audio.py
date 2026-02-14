#!/usr/bin/env python
#! *-* coding:utf-8 *-*
# extract_audio_wav_ffmpeg_parallel.py
#
# Created using a single shared braincell by Yours Truly and Grok ( February 2026)

import sys
from pathlib import Path
import subprocess
import concurrent.futures
import os
import datetime

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    def tqdm(iterable, *args, **kwargs):
        return iterable

# ==================== CONFIG ====================

VIDEO_EXTS = {
    '.mp4', '.mkv', '.mov', '.avi', '.webm',
    '.flv', '.wmv', '.mpeg', '.mpg', '.m4v',
    '.3gp', '.ts', '.m2ts', '.vob', '.ogv',
    '.mxf', '.asf', '.divx', '.xvid', '.rm',
    '.rmvb', '.f4v', '.mpv', '.m2v', '.mts',
    '.m4a', '.m2p', '.ps', '.dv', '.qt',
    '.swf', '.264', '.h264', '.hevc', '.h265'
}

RECURSIVE = True
MAX_WORKERS = min(8, os.cpu_count() or 4)

FALLBACK_SAMPLE_RATE = "44100"
FALLBACK_CHANNELS = "2"

COLLECT_IN_SUBFOLDER = True
SUBFOLDER_NAME = "Audio Samples"
MOVE_OR_COPY = "move"

# ================================================

def get_audio_info(video_path: Path) -> tuple[str | None, str | None]:
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=sample_rate,channels",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(video_path)
    ]
    try:
        output = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()
        if not output:
            return None, None
        lines = output.splitlines()
        return (lines[0] if lines else None), (lines[1] if len(lines) > 1 else None)
    except Exception:
        return None, None


def find_unique_wav_path(base_dir: Path, stem: str) -> Path:
    base_path = base_dir / f"{stem}.wav"
    if not base_path.exists():
        return base_path
    counter = 1
    while True:
        candidate = base_dir / f"{stem}_{counter:04d}.wav"
        if not candidate.exists():
            return candidate
        counter += 1


def extract_audio(video_path: Path, output_base: Path) -> tuple[bool, str, str, str | None]:
    """
    Returns: (success, console_msg, full_log_line, error_log_line or None)
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stem = video_path.name

    sample_rate, channels = get_audio_info(video_path)
    if sample_rate is None or channels is None:
        msg = f"Skip (no audio): {stem}"
        log_line = f"[{timestamp}] SKIPPED  {stem} → no audio track"
        return False, msg, log_line, None  # skips not considered errors

    ar = sample_rate or FALLBACK_SAMPLE_RATE
    ac = channels or FALLBACK_CHANNELS

    wav_path = find_unique_wav_path(output_base, video_path.stem)

    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(video_path),
        "-vn", "-acodec", "pcm_s16le",
        "-ar", ar, "-ac", ac,
        str(wav_path)
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        msg = f"✓ {wav_path.name} (SR: {ar} Hz, CH: {ac})"
        log_line = f"[{timestamp}] SUCCESS  {stem} → {wav_path.name} (SR:{ar} CH:{ac})"
        return True, msg, log_line, None
    except subprocess.CalledProcessError as e:
        err = e.stderr.decode().strip() or "ffmpeg reported error (no stderr captured)"
        msg = f"✗ Failed: {stem} → {err}"
        log_line = f"[{timestamp}] FAILED  {stem} → {err}"
        error_line = f"[{timestamp}] {stem}\n    → {err}\n"
        return False, msg, log_line, error_line
    except Exception as e:
        msg = f"✗ Error: {stem} → {type(e).__name__}"
        log_line = f"[{timestamp}] ERROR   {stem} → {type(e).__name__}"
        error_line = f"[{timestamp}] {stem}\n    → {type(e).__name__} - {str(e)}\n"
        return False, msg, log_line, error_line


def write_logs(output_base: Path, all_lines: list[str], error_lines: list[str]):
    # Main log (everything)
    log_path = output_base / "extraction_log.txt"
    header = [
        "=== Audio Extraction Log ===",
        f"Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Input folder: {input_dir}",
        f"Recursive: {RECURSIVE}",
        f"Workers: {MAX_WORKERS}",
        "-" * 70,
        ""
    ]
    footer = [
        "-" * 70,
        f"Finished: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        ""
    ]
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(header + all_lines + footer))

    print(f"Full log: {log_path}")

    # Errors-only log (only if there were real failures/errors)
    if error_lines:
        error_path = output_base / "errors_only.log"
        error_header = [
            "=== ERRORS ONLY - Audio Extraction ===",
            f"Run on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Source folder: {input_dir}",
            "-" * 70,
            ""
        ]
        error_footer = [
            "-" * 70,
            f"Total errors/failures: {len(error_lines)}",
            ""
        ]
        with open(error_path, "w", encoding="utf-8") as f:
            f.write("\n".join(error_header + error_lines + error_footer))
        print(f"Errors log (only failures): {error_path}")
    else:
        print("No errors/failures occurred → no errors_only.log created")


def main():
    global input_dir

    if len(sys.argv) > 1:
        input_dir = Path(sys.argv[1]).resolve()
    else:
        input_dir = Path.cwd()
        print("No path provided → using current directory")

    if not input_dir.is_dir():
        print(f"Error: {input_dir} is not a directory.")
        sys.exit(1)

    if COLLECT_IN_SUBFOLDER:
        output_base = input_dir / SUBFOLDER_NAME
        output_base.mkdir(exist_ok=True)
        print(f"Collecting all .wav files into: {output_base}")
    else:
        output_base = None
        print("Keeping .wav files next to each video")

    print(f"Scanning: {input_dir}")
    print(f"  → {'recursive' if RECURSIVE else 'top-level only'}")
    print(f"  → parallel workers: {MAX_WORKERS}\n")

    pattern = "**/*" if RECURSIVE else "*"
    videos = []
    for ext in VIDEO_EXTS:
        videos.extend(input_dir.glob(pattern + ext))
        videos.extend(input_dir.glob(pattern + ext.upper()))

    videos = sorted(set(videos))

    if not videos:
        print("No video files found.")
        return

    print(f"Found {len(videos)} video file(s)\n")

    all_log_lines = []
    error_log_lines = []
    success_count = failed_count = skipped_count = 0
    total = len(videos)

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_video = {}
        for v in videos:
            target_dir = output_base if COLLECT_IN_SUBFOLDER else v.parent
            future = executor.submit(extract_audio, v, target_dir)
            future_to_video[future] = v

        progress = tqdm(total=total, desc="Extracting", unit="video") if HAS_TQDM else None

        for future in concurrent.futures.as_completed(future_to_video):
            success, msg, log_line, error_line = future.result()
            print(msg)
            all_log_lines.append(log_line)
            if error_line:
                error_log_lines.append(error_line)

            if success:
                success_count += 1
            elif "Skip" in msg:
                skipped_count += 1
            else:
                failed_count += 1

            if progress:
                progress.update(1)

        if progress:
            progress.close()

    print(f"\nFinished: {success_count} successful | {skipped_count} skipped | {failed_count} failed  ({total} total)")

    if COLLECT_IN_SUBFOLDER and (success_count + failed_count + skipped_count) > 0:
        print(f"All extracted audio is in: {output_base}")
        write_logs(output_base, all_log_lines, error_log_lines)


if __name__ == "__main__":
    main()