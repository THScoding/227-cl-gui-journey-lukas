import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename


    
# Modify the do_command function:
# to use the new button as needed
def do_command(command):
    global command_textbox
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    
    global url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"

    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"))
ping_btn.pack()

# Sets up command button for tracert
tracert = tk.Button(frame, text="tracert", command=lambda:do_command("tracert"))
tracert.pack()

# Sets up nslookup command button
nslookup = tk.Button(frame, text="nslookup", command=lambda:do_command("nslookup"))
nslookup.pack()

netstat = tk.Button(frame, text="netstat", command=lambda:do_command("netstat"))
netstat.pack()

# we already have a url http://wttr.in/
curl = tk.Button(frame, text="curl", command=lambda:do_command("curl"))
curl.pack()

start = tk.Button(frame, text="start", command=lambda:do_command("start"))
start.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root.mainloop()
