import subprocess
import sys

def cut_local(input_path, start, end, output_name):
    print(f"[*] Slicing local file from {start} to {end}...")
    # '-c copy' tells ffmpeg to instantly copy the stream without re-encoding
    cmd = ['ffmpeg', '-y', '-i', input_path, '-ss', start, '-to', end, '-c', 'copy', output_name]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[+] Saved {output_name}")

def download_yt_section(url, start, end, output_name):
    print(f"[*] Fetching {start} to {end} directly from YouTube servers...")
    # This magic command downloads ONLY the requested timestamps
    cmd = [
        'yt-dlp',
        '--download-sections', f'*{start}-{end}',
        '--force-keyframes-at-cuts',
        '-o', output_name,
        url
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[+] Saved {output_name}")

def main():
    print("=== Fast Stream Clipper ===")
    source = input("Enter YouTube Link OR Local File Path (.mp4/.mkv): ").strip()
    is_link = source.startswith("http")

    local_stream_path = source
    full_download = False

    if is_link:
        save_full = input("Download the FULL stream as well? (y/n): ").strip().lower()
        if save_full == 'y':
            local_stream_path = "full_stream_download.mp4"
            print("\n[*] Downloading entire stream... grab a coffee.")
            subprocess.run(['yt-dlp', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '-o', local_stream_path, source])
            full_download = True
            print("[+] Full stream saved.")

    clip_count = 1
    while True:
        print(f"\n--- Clip {clip_count} ---")
        start = input("Start time (HH:MM:SS or seconds) [or 'q' to quit]: ").strip()
        if start.lower() == 'q':
            print("\nDone clipping!")
            break
        end = input("End time (HH:MM:SS or seconds): ").strip()
        
        output_name = f"highlight_{clip_count}.mp4"

        if is_link and not full_download:
            # Bypasses the full download and grabs just the chunk you need
            download_yt_section(source, start, end, output_name)
        else:
            # Instantaneous local cut
            cut_local(local_stream_path, start, end, output_name)
        
        clip_count += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
