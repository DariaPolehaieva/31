import socket
import threading
import tkinter as tk
from tkinter import messagebox

def scan_ports():
    host = entry_host.get()
    try:
        start_port = int(entry_start_port.get())
        end_port = int(entry_end_port.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid port numbers")
        return
    
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        messagebox.showerror("Error", "Port numbers must be between 1 and 65535 and start port must be less than end port")
        return

    listbox_ports.delete(0, tk.END)
    
    def check_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            listbox_ports.insert(tk.END, f"Port {port} is OPEN")
        sock.close()
    
    for port in range(start_port, end_port + 1):
        threading.Thread(target=check_port, args=(port,)).start()

root = tk.Tk()
root.title("Port Scanner")

tk.Label(root, text="Enter host address (IP or domain):").grid(row=0, column=0)
entry_host = tk.Entry(root)
entry_host.grid(row=0, column=1)

tk.Label(root, text="Start Port (for example 1):").grid(row=1, column=0)
entry_start_port = tk.Entry(root)
entry_start_port.grid(row=1, column=1)

tk.Label(root, text="End Port (for example 65535):").grid(row=2, column=0)
entry_end_port = tk.Entry(root)
entry_end_port.grid(row=2, column=1)

btn_scan = tk.Button(root, text="Scan Ports", command=scan_ports)
btn_scan.grid(row=3, column=0, columnspan=2)

listbox_ports = tk.Listbox(root, height=10, width=50)
listbox_ports.grid(row=4, column=0, columnspan=2)

root.mainloop()