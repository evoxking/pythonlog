import os
import psutil
import socket
import pyshark
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import scrolledtext, filedialog, Toplevel, Listbox
import threading
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pynput

class LogHandler(FileSystemEventHandler):
    def __init__(self, logger):
        self.logger = logger

    def on_modified(self, event):
        self.logger.log(f"Modified: {event.src_path}")

    def on_created(self, event):
        self.logger.log(f"Created: {event.src_path}")

    def on_deleted(self, event):
        self.logger.log(f"Deleted: {event.src_path}")

    def on_moved(self, event):
        self.logger.log(f"Moved: {event.src_path} to {event.dest_path}")

class Logger:
    def __init__(self, log_area):
        self.log_area = log_area
        self.stop_logging_flag = False

    def log(self, message):
        if not self.stop_logging_flag:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{timestamp} - {message}\n"
            self.log_area.configure(state=tk.NORMAL)
            self.log_area.insert(tk.END, log_message)
            self.log_area.configure(state=tk.DISABLED)
            self.log_area.yview(tk.END)

    def save_log(self, filepath):
        with open(filepath, 'w') as file:
            file.write(self.log_area.get('1.0', tk.END))

    def stop_logging(self):
        self.stop_logging_flag = True

class LogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate System Monitor")
        self.root.geometry("1200x800")

        self.log_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state=tk.DISABLED)
        self.log_area.pack(expand=1, fill='both')

        self.logger = Logger(self.log_area)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        self.start_button = tk.Button(self.control_frame, text="Start Logging", command=self.start_logging)
        self.start_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.control_frame, text="Save Log", command=self.save_log)
        self.save_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.control_frame, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)

        self.plot_cpu_usage = tk.Button(self.control_frame, text="Plot CPU Usage", command=self.plot_cpu)
        self.plot_cpu_usage.pack(side=tk.LEFT)

        self.plot_memory_usage = tk.Button(self.control_frame, text="Plot Memory Usage", command=self.plot_memory)
        self.plot_memory_usage.pack(side=tk.LEFT)

        self.open_apps_button = tk.Button(self.control_frame, text="Show Open Applications", command=self.show_open_applications)
        self.open_apps_button.pack(side=tk.LEFT)

        self.observer = Observer()

    def start_logging(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.logger.stop_logging_flag = False  # Reset the flag when starting logging
        self.logger.log("Starting file system logging...")
        self.start_file_logging()

        self.logger.log("Starting process monitoring...")
        self.start_process_monitoring()

        self.logger.log("Starting network monitoring...")
        self.start_network_monitoring()

        self.logger.log("Starting system performance monitoring...")
        self.start_system_monitoring()

        self.logger.log("Starting user activity monitoring...")
        self.start_user_activity_monitoring()

    def stop_logging(self):
        self.observer.stop()
        self.logger.stop_logging()
        self.logger.log("Stopped logging.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def save_log(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            self.logger.save_log(filepath)
            self.logger.log(f"Log saved to {filepath}")

    def start_file_logging(self):
        event_handler = LogHandler(self.logger)
        self.observer.schedule(event_handler, path='/', recursive=True)
        self.observer.start()

    def start_process_monitoring(self):
        def monitor_processes():
            while not self.logger.stop_logging_flag:
                for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
                    self.logger.log(f"Process: {proc.info}")
                time.sleep(5)
        threading.Thread(target=monitor_processes, daemon=True).start()

    def start_network_monitoring(self):
        def monitor_network():
            cap = pyshark.LiveCapture(interface='any')
            for packet in cap.sniff_continuously():
                if self.logger.stop_logging_flag:
                    break
                try:
                    ip_src = packet.ip.src
                    ip_dst = packet.ip.dst
                    protocol = packet.transport_layer
                    self.logger.log(f"Packet: {protocol} {ip_src} -> {ip_dst}")
                except AttributeError:
                    continue
        threading.Thread(target=monitor_network, daemon=True).start()

    def start_system_monitoring(self):
        def monitor_system():
            while not self.logger.stop_logging_flag:
                cpu_usage = psutil.cpu_percent(interval=1)
                memory_usage = psutil.virtual_memory().percent
                disk_usage = psutil.disk_usage('/').percent
                self.logger.log(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}%")
                time.sleep(5)
        threading.Thread(target=monitor_system, daemon=True).start()

    def start_user_activity_monitoring(self):
        def on_key_press(key):
            self.logger.log(f"Key Pressed: {key}")

        def on_click(x, y, button, pressed):
            if pressed:
                self.logger.log(f"Mouse Clicked at ({x}, {y}) with {button}")

        keyboard_listener = pynput.keyboard.Listener(on_press=on_key_press)
        mouse_listener = pynput.mouse.Listener(on_click=on_click)

        keyboard_listener.start()
        mouse_listener.start()

    def plot_cpu(self):
        cpu_usages = []

        def monitor_cpu_usage():
            while not self.logger.stop_logging_flag:
                cpu_usages.append(psutil.cpu_percent(interval=1))
                time.sleep(1)

        def plot_cpu_usage():
            plt.figure(figsize=(10, 6))
            plt.plot(cpu_usages, label='CPU Usage (%)')
            plt.xlabel('Time (s)')
            plt.ylabel('CPU Usage (%)')
            plt.title('CPU Usage Over Time')
            plt.legend()
            plt.show()

        threading.Thread(target=monitor_cpu_usage, daemon=True).start()
        threading.Thread(target=plot_cpu_usage, daemon=True).start()

    def plot_memory(self):
        memory_usages = []

        def monitor_memory_usage():
            while not self.logger.stop_logging_flag:
                memory_usages.append(psutil.virtual_memory().percent)
                time.sleep(1)

        def plot_memory_usage():
            plt.figure(figsize=(10, 6))
            plt.plot(memory_usages, label='Memory Usage (%)')
            plt.xlabel('Time (s)')
            plt.ylabel('Memory Usage (%)')
            plt.title('Memory Usage Over Time')
            plt.legend()
            plt.show()

        threading.Thread(target=monitor_memory_usage, daemon=True).start()
        threading.Thread(target=plot_memory_usage, daemon=True).start()

    def show_open_applications(self):
        open_apps_window = Toplevel(self.root)
        open_apps_window.title("Currently Open Applications")
        open_apps_window.geometry("400x300")

        listbox = Listbox(open_apps_window)
        listbox.pack(fill=tk.BOTH, expand=1)

        def update_open_apps():
            while not self.logger.stop_logging_flag:
                listbox.delete(0, tk.END)
                for proc in psutil.process_iter(['name']):
                    listbox.insert(tk.END, proc.info['name'])
                time.sleep(2)

        threading.Thread(target=update_open_apps, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = LogApp(root)
    root.mainloop()
