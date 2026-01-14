import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global output_widget
    
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, command + " working....\n")
    output_widget.update()
    
    global url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    
    # Makes curl command automatically have a url
    if command == "curl":
        url_val = "http://wttr.in/"
        
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            output_widget.insert(tk.END,line)
            output_widget.update()
            
MAIN_WINDOW= tk.Tk()
Command_selection=tk.Frame()
Command_selection.pack()



output=tk.Frame()
output.pack()

output_widget=tksc.ScrolledText(output,height=10,width=100)
output_widget.pack()
