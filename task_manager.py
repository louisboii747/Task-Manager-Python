import tkinter as tk
import subprocess

def get_processes():
    result = subprocess.run(
        ["ps", "-eo", "pid,comm"],
        stdout=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip().split("\n")[1:]

def refresh():
    listbox.delete(0, tk.END)
    for proc in get_processes():
        listbox.insert(tk.END, proc)

def kill_process():
    selection = listbox.curselection()
    if not selection:
        return

    line = listbox.get(selection[0])
    pid = line.split()[0]

    subprocess.run(["kill", "-9", pid])
    refresh()

root = tk.Tk()
root.title("Python Task Manager")
root.geometry("700x500")

title = tk.Label(root, text="Task Manager", font=("Arial", 18))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
listbox.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

refresh_btn = tk.Button(root, text="Refresh", command=refresh)
refresh_btn.pack(pady=5)

kill_btn = tk.Button(root, text="Kill Process", fg="red", command=kill_process)
kill_btn.pack(pady=5)

refresh()
root.mainloop()
