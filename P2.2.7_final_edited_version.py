import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command():
    global output_widget
    global commandslistindex
    
    commandslistindecies = Command_ListBox.curselection()
    
    commandslistindex = commandslistindecies[0]
    curcommand = Command_ListBox.get(commandslistindex)
    # Command_ListBox.see(commandslistindex)
    
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, curcommand + " working....\n")
    output_widget.update()
    
    global url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    
    # Makes curl command automatically have a url
    if curcommand == "curl":
        url_val = "http://wttr.in/"
        
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    if curcommand == "netstat":
      with subprocess.Popen(curcommand + ' ' + url_val, "-a", stdout=subprocess.PIPE,  bufsize=1, universal_newlines=True, encoding="utf-8",text= True, errors="ignore") as p:
        for line in p.stdout:
            output_widget.insert(tk.END,line)
            output_widget.update()
    
    else:
        with subprocess.Popen(curcommand + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, encoding="utf-8",text= True, errors="ignore") as p:
            for line in p.stdout:
                output_widget.insert(tk.END,line)
                output_widget.update()
            
MAIN_WINDOW= tk.Tk()
MAIN_WINDOW.title("THE PYTHON TERMINATOR")

# Variable Configuration
commandslist = ["ping", "tracert", "netstat", "curl", "start", "nslookup"]
countervar = 0
########

Command_selection = tk.Frame(MAIN_WINDOW, height=200, width= 50)
Command_selection.pack()

Command_ListBox = tk.Listbox(Command_selection, height= 5)
Command_ListBox.insert(tk.END, "nslookup")
while countervar < len(commandslist):
    Command_ListBox.insert(tk.END, commandslist[countervar])
    countervar = countervar + 1
    
Command_ListBox.pack()

startbutton = tk.Button(Command_selection, text = "START", command=lambda:do_command())
startbutton.pack()

#######

Command_entries= tk.Frame(MAIN_WINDOW)
Command_entries.pack()

url_entry = tk.Entry(Command_entries)
url_entry.pack()

output=tk.Frame(MAIN_WINDOW)
output.pack()

output_widget=tksc.ScrolledText(output,height=10,width=100)
output_widget.pack()

MAIN_WINDOW.mainloop()