import subprocess
import sys
import shutil
import threading
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

class BatchStreamClipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Stream Clipper")
        self.root.geometry("550x550")
        self.root.resizable(False, False)

        self.check_dependencies()
        self.clip_counter = 1

        # --- UI Elements ---
        tk.Label(root, text="1. Source (YouTube URL or Local File):", font=("Arial", 10, "bold")).pack(pady=(10, 0), anchor="w", padx=20)
        
        source_frame = tk.Frame(root)
        source_frame.pack(fill="x", padx=20, pady=5)
        self.source_entry = tk.Entry(source_frame)
        self.source_entry.pack(side="left", fill="x", expand=True)
        tk.Button(source_frame, text="Browse", command=self.browse_file).pack(side="right", padx=(5, 0))

        self.full_stream_var = tk.BooleanVar()
        self.full_stream_check = tk.Checkbutton(root, text="Download FULL stream first? (For URLs - Downloads once, cuts instantly)", variable=self.full_stream_var)
        self.full_stream_check.pack(anchor="w", padx=20)

        # --- Add Clip Section ---
        tk.Label(root, text="2. Add Clips to Queue:", font=("Arial", 10, "bold")).pack(pady=(15, 5), anchor="w", padx=20)
        
        time_frame = tk.Frame(root)
        time_frame.pack(fill="x", padx=20)

        tk.Label(time_frame, text="Start (HH:MM:SS)").grid(row=0, column=0, sticky="w")
        self.start_entry = tk.Entry(time_frame, width=12)
        self.start_entry.grid(row=1, column=0, padx=(0, 10))

        tk.Label(time_frame, text="End (HH:MM:SS)").grid(row=0, column=1, sticky="w")
        self.end_entry = tk.Entry(time_frame, width=12)
        self.end_entry.grid(row=1, column=1, padx=(0, 10))

        tk.Label(time_frame, text="Output Name").grid(row=0, column=2, sticky="w")
        self.output_entry = tk.Entry(time_frame, width=15)
        self.output_entry.insert(0, f"clip_{self.clip_counter}.mp4")
        self.output_entry.grid(row=1, column=2, padx=(0, 10))

        tk.Button(time_frame, text="Add to Queue", command=self.add_to_queue, bg="#2196F3", fg="white").grid(row=1, column=3)

        # --- Queue Table (Treeview) ---
        columns = ("start", "end", "name")
        self.queue_tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
        self.queue_tree.heading("start", text="Start Time")
        self.queue_tree.column("start", width=100, anchor="center")
        self.queue_tree.heading("end", text="End Time")
        self.queue_tree.column("end", width=100, anchor="center")
        self.queue_tree.heading("name", text="Filename")
        self.queue_tree.column("name", width=250, anchor="w")
        self.queue_tree.pack(padx=20, pady=10, fill="x")

        # Queue Controls
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill="x", padx=20)
        tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).pack(side="left")
        tk.Button(btn_frame, text="Clear Queue", command=self.clear_queue).pack(side="left", padx=10)

        # --- Action Button & Status ---
        self.clip_button = tk.Button(root, text="Start Batch Processing", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=self.start_processing)
        self.clip_button.pack(pady=15)

        self.status_label = tk.Label(root, text="Ready.", fg="gray", font=("Arial", 9, "italic"))
        self.status_label.pack()

    def check_dependencies(self):
        missing = [tool for tool in ["ffmpeg", "yt-dlp"] if not shutil.which(tool)]
        if missing:
            messagebox.showerror("Missing Dependencies", f"Missing: {', '.join(missing)}.\nPlease install them.")
            sys.exit(1)

    def browse_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.webm")])
        if filepath:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, filepath)

    def add_to_queue(self):
        start = self.start_entry.get().strip()
        end = self.end_entry.get().strip()
        name = self.output_entry.get().strip()

        if not start or not end or not name:
            messagebox.showwarning("Input Error", "Please fill in Start, End, and Output Name.")
            return

        # Add to table
        self.queue_tree.insert("", "end", values=(start, end, name))
        
        # Clear inputs and auto-increment the default filename
        self.start_entry.delete(0, tk.END)
        self.end_entry.delete(0, tk.END)
        self.clip_counter += 1
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, f"clip_{self.clip_counter}.mp4")

    def remove_selected(self):
        for item in self.queue_tree.selection():
            self.queue_tree.delete(item)

    def clear_queue(self):
        for item in self.queue_tree.get_children():
            self.queue_tree.delete(item)
        self.clip_counter = 1
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, f"clip_{self.clip_counter}.mp4")

    def set_status(self, text, color="black"):
        self.status_label.config(text=text, fg=color)
        self.root.update_idletasks()

    def start_processing(self):
        source = self.source_entry.get().strip()
        queue_items = self.queue_tree.get_children()

        if not source:
            messagebox.showwarning("Input Error", "Please provide a source URL or file.")
            return
        if not queue_items:
            messagebox.showwarning("Input Error", "Your clip queue is empty!")
            return

        # Extract data from the Treeview
        clips = []
        for item in queue_items:
            clips.append(self.queue_tree.item(item, "values"))

        self.clip_button.config(state="disabled")
        threading.Thread(target=self.run_batch_clipper, args=(source, clips), daemon=True).start()

    def run_batch_clipper(self, source, clips):
        is_link = source.startswith("http")
        total_clips = len(clips)
        working_source = source

        try:
            # Handle full stream download FIRST if requested
            if is_link and self.full_stream_var.get():
                self.set_status("Downloading full stream... (This might take a while)", "blue")
                working_source = "temp_full_stream.mp4"
                subprocess.run(['yt-dlp', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '-o', working_source, source], check=True)
                is_link = False # Treat it as a local file from now on

            # Process the Queue
            for index, (start, end, out_name) in enumerate(clips, 1):
                self.set_status(f"Processing clip {index}/{total_clips}: {out_name}...", "blue")
                
                if is_link:
                    # Direct YouTube section download
                    cmd = ['yt-dlp', '--download-sections', f'*{start}-{end}', '--force-keyframes-at-cuts', '-o', out_name, source]
                    subprocess.run(cmd, check=True)
                else:
                    # Instant local slicing
                    cmd = ['ffmpeg', '-y', '-i', working_source, '-ss', start, '-to', end, '-c', 'copy', out_name]
                    subprocess.run(cmd, check=True)

            self.set_status(f"Batch complete! Successfully exported {total_clips} clips.", "green")

        except subprocess.CalledProcessError:
            self.set_status("Error occurred during processing. Check console.", "red")
            messagebox.showerror("Error", "Command failed. Make sure your timestamps are correct and the video exists.")
        finally:
            self.clip_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = BatchStreamClipperApp(root)
    root.mainloop()
