import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import sys
import os

# Add parent directory to sys.path to import main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main

class AssistantUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Zudo Desktop Assistant")
        self.root.geometry("600x400")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(root, text="Start Listening", command=self.start_listening)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop Listening", command=self.stop_listening, state='disabled')
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.listening = False
        self.thread = None

    def start_listening(self):
        if not self.listening:
            self.listening = True
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')
            self.append_text("Assistant started listening...\n")
            self.thread = threading.Thread(target=self.listen_loop)
            self.thread.daemon = True
            self.thread.start()

    def stop_listening(self):
        if self.listening:
            self.listening = False
            self.start_button.config(state='normal')
            self.stop_button.config(state='disabled')
            self.append_text("Assistant stopped listening.\n")

    def append_text(self, text):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, text)
        self.text_area.see(tk.END)
        self.text_area.config(state='disabled')

    def listen_loop(self):
        self.root.after(100, self.process_commands)

    def process_commands(self):
        if not self.listening:
            return
        self.append_text("Listening...\n")
        query = main.takeCommand()
        if query.lower() != "none":
            self.append_text(f"You said: {query}\n")
            main.process_query(query)
        self.root.after(100, self.process_commands)

def main_ui():
    root = tk.Tk()
    app = AssistantUI(root)
    root.mainloop()

if __name__ == "__main__":
    main_ui()
