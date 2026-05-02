import subprocess
import sys
import shutil
import threading
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

class BatchStreamClipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Stream Clipper Pro")
        self.root.geometry("550x650") 
        self.root.resizable(False, False)

        self.check_dependencies()
        self.clip_counter = 1

        # --- 1. Source Section ---
        tk.Label(root, text="1. Source (YouTube URL or Local File):", font=("Arial", 10, "bold")).pack(pady=(10, 0), anchor="w", padx=20)
        source_frame = tk.Frame(root)
        source_frame.pack(fill="x", padx=20, pady=5)
        self.source_entry = tk.Entry(source_frame)
        self.source_entry.pack(side="left", fill="x", expand=True)
        tk.Button(source_frame, text="Browse", command=self.browse_file).pack(side="right", padx=(5, 0))

        self.full_stream_var = tk.BooleanVar()
        tk.Checkbutton(root, text="Download FULL stream first? (Saves bandwidth for multiple clips)", variable=self.full_stream_var).pack(anchor="w", padx=20)

        # --- 2. Advanced Plugins (The Dropdown) ---
        self.plugins_visible = False
        self.toggle_btn = tk.Button(root, text="⚙️ Show Advanced Automation Plugins", command=self.toggle_plugins, fg="blue", relief="flat")
        self.toggle_btn.pack(pady=5, anchor="w", padx=20)

        self.plugin_frame = tk.LabelFrame(root, text="Automation Modules", padx=10, pady=10)
        
        self.plug_live = tk.BooleanVar()
        self.plug_audio = tk.BooleanVar()
        self.plug_chat = tk.BooleanVar()
        self.plug_ocr = tk.BooleanVar()

        tk.Checkbutton(self.plugin_frame, text="Live Marker Tracker", variable=self.plug_live).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(self.plugin_frame, text="Audio Spike Detector", variable=self.plug_audio).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self.plugin_frame, text="Chat Hype Scanner", variable=self.plug_chat).grid(row=0, column=1, sticky="w", padx=10)
        tk.Checkbutton(self.plugin_frame, text="OCR Vision Scanner", variable=self.plug_ocr).grid(row=1, column=1, sticky="w", padx=10)
        
        ocr_subframe = tk.Frame(self.plugin_frame)
        ocr_subframe.grid(row=2, column=0, columnspan=2, sticky="w", pady=(5,0))
        tk.Label(ocr_subframe, text="OCR Target Text (e.g., 'YOU DIED'):", fg="gray").pack(side="left")
        self.ocr_target = tk.Entry(ocr_subframe, width=20)
        self.ocr_target.pack(side="left", padx=5)

        # --- 3. Manual Queue Section ---
        self.queue_container = tk.Frame(root)
        self.queue_container.pack(fill="both", expand=True)

        tk.Label(self.queue_container, text="3. Manual Queue (Overrides Plugins):", font=("Arial", 10, "bold")).pack(pady=(15, 5), anchor="w", padx=20)
        
        time_frame = tk.Frame(self.queue_container)
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

        tk.Button(time_frame, text="Add", command=self.add_to_queue, bg="#2196F3", fg="white").grid(row=1, column=3)

        columns = ("start", "end", "name")
        self.queue_tree = ttk.Treeview(self.queue_container, columns=columns, show="headings", height=5)
        self.queue_tree.heading("start", text="Start")
        self.queue_tree.column("start", width=80, anchor="center")
        self.queue_tree.heading("end", text="End")
        self.queue_tree.column("end", width=80, anchor="center")
        self.queue_tree.heading("name", text="Filename")
        self.queue_tree.column("name", width=250, anchor="w")
        self.queue_tree.pack(padx=20, pady=10, fill="x")

        # --- 4. Action Button & Status ---
        self.clip_button = tk.Button(root, text="Start Processing Engine", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=self.start_processing)
        self.clip_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Ready.", fg="gray", font=("Arial", 9, "italic"))
        self.status_label.pack()

    def toggle_plugins(self):
        if self.plugins_visible:
            self.plugin_frame.pack_forget()
            self.toggle_btn.config(text="⚙️ Show Advanced Automation Plugins")
            self.plugins_visible = False
            self.queue_container.pack(fill="both", expand=True)
        else:
            self.queue_container.pack_forget() 
            self.plugin_frame.pack(fill="x", padx=20, pady=5) 
            self.queue_container.pack(fill="both", expand=True) 
            self.toggle_btn.config(text="⚙️ Hide Advanced Automation Plugins")
            self.plugins_visible = True

    def check_dependencies(self):
        missing = [tool for tool in ["ffmpeg", "yt-dlp"] if not shutil.which(tool)]
        if missing:
            messagebox.showerror("Missing Dependencies", f"Missing: {', '.join(missing)}.\nPlease launch using the provided .bat or .sh launcher scripts.")
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
        if start and end and name:
            self.queue_tree.insert("", "end", values=(start, end, name))
            self.start_entry.delete(0, tk.END)
            self.end_entry.delete(0, tk.END)
            self.clip_counter += 1
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"clip_{self.clip_counter}.mp4")

    def set_status(self, text, color="black"):
        self.status_label.config(text=text, fg=color)
        self.root.update_idletasks()

    def start_processing(self):
        source = self.source_entry.get().strip()
        if not source:
            messagebox.showwarning("Input Error", "Please provide a source URL or file.")
            return

        active_plugins = {
            "live_marker": self.plug_live.get(),
            "audio_spike": self.plug_audio.get(),
            "chat_hype": self.plug_chat.get(),
            "ocr_vision": self.plug_ocr.get(),
            "ocr_target": self.ocr_target.get().strip()
        }

        manual_clips = [self.queue_tree.item(item, "values") for item in self.queue_tree.get_children()]

        if not manual_clips and not any(active_plugins.values()):
            messagebox.showwarning("No Tasks", "Add clips to the queue or enable an automation plugin.")
            return

        self.clip_button.config(state="disabled")
        threading.Thread(target=self.run_engine, args=(source, manual_clips, active_plugins), daemon=True).start()

    def run_engine(self, source, manual_clips, plugins):
        working_source = source
        is_link = source.startswith("http")
        
        try:
            if is_link and (self.full_stream_var.get() or any(plugins.values())):
                self.set_status("Downloading full stream... (This may take a while)", "blue")
                working_source = "temp_analysis_stream.mp4"
                subprocess.run(['yt-dlp', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '-o', working_source, source], check=True)
                is_link = False

            auto_clips = []
            
            # Placeholder for Plugin Processing Blocks
            if plugins["audio_spike"]:
                self.set_status("Analyzing audio spikes... (Plugin logic required)", "purple")
                pass 
                
            if plugins["ocr_vision"] and plugins["ocr_target"]:
                self.set_status(f"Scanning frames for '{plugins['ocr_target']}'... (Plugin logic required)", "purple")
                pass

            all_clips = manual_clips + auto_clips

            for index, (start, end, out_name) in enumerate(all_clips, 1):
                self.set_status(f"Exporting clip {index}/{len(all_clips)}: {out_name}", "blue")
                if is_link:
                    subprocess.run(['yt-dlp', '--download-sections', f'*{start}-{end}', '-o', out_name, source], check=True)
                else:
                    subprocess.run(['ffmpeg', '-y', '-i', working_source, '-ss', start, '-to', end, '-c', 'copy', out_name], check=True)

            self.set_status("All tasks completed successfully!", "green")

        except Exception as e:
            self.set_status("Error occurred during processing. Check console.", "red")
            print(f"Error: {e}")
        finally:
            self.clip_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = BatchStreamClipperApp(root)
    root.mainloop()
