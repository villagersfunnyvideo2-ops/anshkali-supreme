#!/usr/bin/env python3
"""
Ansh Kali Supreme Suite
------------------------
Master Automation Dashboard for Kali Linux:
- Security Tool Suites Installer (1000+ Tools)
- Full App Development Environment (VS Code, Flutter, Android Studio, Java)
- Auto Database & Driver Provisioning
- Sound Effects & RGB Visual Interface
- Automated GitHub Bot & Repo Integrator
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import threading
import os
import platform

class AnshKaliApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ansh Kali Supreme Suite - Automation Dashboard")
        self.root.geometry("850x650")
        self.root.configure(bg="#0d1117")

        # Color Palette
        self.bg_color = "#0d1117"
        self.fg_color = "#58a6ff"
        self.accent_color = "#238636"
        self.text_color = "#c9d1d9"
        self.log_bg = "#161b22"

        self.setup_ui()

    def play_sound(self, sound_type="beep"):
        """Plays sound feedback using sox/play or system beep."""
        def sound_thread():
            try:
                if sound_type == "beep":
                    subprocess.run(["play", "-n", "synth", "0.1", "sine", "800"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                elif sound_type == "success":
                    subprocess.run(["play", "-n", "synth", "0.2", "sine", "1000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                elif sound_type == "alert":
                    subprocess.run(["play", "-n", "synth", "0.3", "sine", "400"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                print("\a")
        threading.Thread(target=sound_thread, daemon=True).start()

    def setup_ui(self):
        # Header Frame
        header = tk.Frame(self.root, bg=self.bg_color)
        header.pack(fill="x", padx=15, pady=10)

        title = tk.Label(header, text="ANSH KALI SUPREME SUITE", font=("Helvetica", 18, "bold"), fg=self.fg_color, bg=self.bg_color)
        title.pack(side="left")

        subtitle = tk.Label(header, text="v1.0 | Cyberpunk Automation Panel", font=("Helvetica", 10, "italic"), fg="#8b949e", bg=self.bg_color)
        subtitle.pack(side="right", pady=5)

        # Main Layout (Notebook Tabs)
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook', background=self.bg_color, borderwidth=0)
        style.configure('TNotebook.Tab', background='#21262d', foreground='#c9d1d9', padding=[10, 5])
        style.map('TNotebook.Tab', background=[('selected', self.accent_color)], foreground=[('selected', '#ffffff')])

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=5)

        # Tab 1: System & Security Tools
        tab_sec = tk.Frame(notebook, bg=self.log_bg)
        notebook.add(tab_sec, text=" Security Tools ")
        self.build_sec_tab(tab_sec)

        # Tab 2: Development Environment
        tab_dev = tk.Frame(notebook, bg=self.log_bg)
        notebook.add(tab_dev, text=" Dev & Workspaces ")
        self.build_dev_tab(tab_dev)

        # Tab 3: GitHub Bot Integrator
        tab_bot = tk.Frame(notebook, bg=self.log_bg)
        notebook.add(tab_bot, text=" GitHub Bot Integrator ")
        self.build_bot_tab(tab_bot)

        # Console Output / Terminal Log Frame
        log_frame = tk.LabelFrame(self.root, text=" System Console Log ", fg=self.fg_color, bg=self.bg_color, font=("Consolas", 10, "bold"))
        log_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.log_text = tk.Text(log_frame, bg="#010409", fg="#3fb950", font=("Consolas", 9), insertbackground="white")
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)

    def log(self, message):
        """Append messages to the console log area."""
        self.log_text.insert(tk.END, f"[>] {message}\n")
        self.log_text.see(tk.END)

    def run_command(self, cmd_list, desc="Processing..."):
        """Executes a terminal command in a background thread."""
        self.play_sound("beep")
        self.log(f"Starting Task: {desc}")

        def task():
            try:
                process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                for line in iter(process.stdout.readline, ''):
                    if line:
                        self.log_text.insert(tk.END, line)
                        self.log_text.see(tk.END)
                process.stdout.close()
                process.wait()

                if process.returncode == 0:
                    self.log(f"SUCCESS: {desc} Completed successfully.")
                    self.play_sound("success")
                else:
                    self.log(f"ERROR: {desc} Failed with exit code {process.returncode}.")
                    self.play_sound("alert")
            except Exception as e:
                self.log(f"EXCEPTION: {str(e)}")
                self.play_sound("alert")

        threading.Thread(target=task, daemon=True).start()

    # --- TAB 1 BUILDER ---
    def build_sec_tab(self, parent):
        btn_frame = tk.Frame(parent, bg=self.log_bg)
        btn_frame.pack(fill="both", expand=True, padx=15, pady=15)

        tk.Button(btn_frame, text="Check System & VirtualBox Status", bg="#21262d", fg=self.fg_color, font=("Helvetica", 10, "bold"),
                  command=self.check_system).grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Button(btn_frame, text="Install Top 10 Kali Tools", bg="#21262d", fg="#ffffff", font=("Helvetica", 10, "bold"),
                  command=lambda: self.run_command(["sudo", "apt", "update", "&&", "sudo", "apt", "install", "-y", "kali-tools-top10"], "Top 10 Kali Tools Setup")).grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        tk.Button(btn_frame, text="Install EVERYTHING Suite (1000+ Tools)", bg=self.accent_color, fg="#ffffff", font=("Helvetica", 10, "bold"),
                  command=lambda: self.run_command(["sudo", "apt", "update", "&&", "sudo", "apt", "install", "-y", "kali-linux-everything"], "Full 1000+ Security Suite Setup")).grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        tk.Button(btn_frame, text="Initialize Metasploit & PostgreSQL DB", bg="#21262d", fg=self.fg_color, font=("Helvetica", 10, "bold"),
                  command=lambda: self.run_command(["sudo", "systemctl", "start", "postgresql", "&&", "sudo", "msfdb", "init"], "Metasploit DB Config")).grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        tk.Button(btn_frame, text="Auto-Load Realtek Wi-Fi Drivers", bg="#21262d", fg=self.fg_color, font=("Helvetica", 10, "bold"),
                  command=lambda: self.run_command(["sudo", "apt", "install", "-y", "realtek-rtl88xxau-dkms"], "Realtek Wi-Fi Driver Setup")).grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # --- TAB 2 BUILDER ---
    def build_dev_tab(self, parent):
        btn_frame = tk.Frame(parent, bg=self.log_bg)
        btn_frame.pack(fill="both", expand=True, padx=15, pady=15)

        tk.Button(btn_frame, text="Install Dev Suite (VS Code, OpenJDK 17, Snap)", bg="#21262d", fg=self.fg_color, font=("Helvetica", 10, "bold"),
                  command=lambda: self.run_command(["sudo", "apt", "update", "&&", "sudo", "apt", "install", "-y", "code", "openjdk-17-jdk", "snapd"], "Development Tools Setup")).grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Button(btn_frame, text="Install Flutter SDK (via Snap)", bg="#21262d", fg=self.fg_color, font=("Helvetica", 10, "bold"),
                  command=lambda: self.run_command(["sudo", "snap", "install", "flutter", "--classic"], "Flutter SDK Installation")).grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        tk.Button(btn_frame, text="Create New Flutter Workspace", bg=self.accent_color, fg="#ffffff", font=("Helvetica", 10, "bold"),
                  command=self.create_flutter_workspace).grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # --- TAB 3 BUILDER ---
    def build_bot_tab(self, parent):
        frame = tk.Frame(parent, bg=self.log_bg)
        frame.pack(fill="both", expand=True, padx=15, pady=15)

        tk.Label(frame, text="Target GitHub Repository URL:", fg=self.text_color, bg=self.log_bg, font=("Helvetica", 10)).pack(anchor="w")
        self.repo_url_entry = tk.Entry(frame, width=60, bg="#010409", fg="#ffffff", insertbackground="white")
        self.repo_url_entry.pack(fill="x", pady=5)
        self.repo_url_entry.insert(0, "https://github.com/username/example-bot.git")

        tk.Button(frame, text="Clone, Setup VirtualEnv & Auto-Install Requirements", bg=self.accent_color, fg="#ffffff", font=("Helvetica", 10, "bold"),
                  command=self.integrate_bot).pack(fill="x", pady=15)

    # --- HELPER ACTIONS ---
    def check_system(self):
        self.log("--- System Verification ---")
        self.log(f"OS Platform: {platform.system()} {platform.release()}")
        self.log(f"Architecture: {platform.machine()}")
        
        if os.path.exists("/.dockerenv"):
            self.log("Environment: Docker Container")
        elif "vbox" in platform.release().lower() or os.path.exists("/sys/class/dmi/id/product_name"):
            self.log("Environment: Virtualized / VirtualBox Environment Detected")
        else:
            self.log("Environment: Native / Bare Metal Hardware")

    def create_flutter_workspace(self):
        target_dir = filedialog.askdirectory(title="Select Location for New Flutter Project")
        if target_dir:
            project_name = "anshkali_app_project"
            cmd = ["flutter", "create", os.path.join(target_dir, project_name)]
            self.run_command(cmd, f"Creating Flutter Project '{project_name}'")

    def integrate_bot(self):
        url = self.repo_url_entry.get().strip()
        if not url or "example-bot" in url:
            messagebox.showerror("Error", "Please enter a valid GitHub Repository URL!")
            return

        target_dir = filedialog.askdirectory(title="Select Folder to Clone Repository")
        if target_dir:
            repo_name = url.split("/")[-1].replace(".git", "")
            clone_path = os.path.join(target_dir, repo_name)
            
            bash_script = f"""
            git clone {url} "{clone_path}"
            cd "{clone_path}"
            python3 -m venv venv
            source venv/bin/activate
            if [ -f "requirements.txt" ]; then
                pip install -r requirements.txt
            fi
            code .
            """
            self.run_command(["bash", "-c", bash_script], f"Integrating GitHub Bot: {repo_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnshKaliApp(root)
    root.mainloop()
              
