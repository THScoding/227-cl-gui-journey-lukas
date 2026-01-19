# Importing necessary stuff
import subprocess
import os
import platform
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename



# Creating the command that gets the value from the selected command on the listbox and runs it on subprocess
def do_command():
    
    global output_widget
    global commandslistindex
    
    progressbar["value"] = 15
    output_widget.delete("1.0",tk.END)
    
    # If nothing is selected, the function will stop
    if not Command_ListBox.curselection():
        progressbar["value"] = 0
        return
    
    # Gets the selected command from the listbox
    commandslistindecies = Command_ListBox.curselection()
    commandslistindex = commandslistindecies[0]
    curcommand = Command_ListBox.get(commandslistindex)
    
    # Lets the user know that the program is starting
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, curcommand + " working....\n")
    output_widget.update()
    
    global url_entry

    # Takes the url value
    url_val = url_entry.get()
    
    # Makes Get Weather command automatically have a url
    if curcommand == "Get Weather":
        url_val = "http://wttr.in/"
        curcommand = "curl"
    
    # If url_entry is blank, use localhost IP address 
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"

    # Sets corresponding values for each function on things like the progressbar and the subprocess call
    if curcommand == "curl":
        with subprocess.Popen(curcommand + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, encoding= "utf-8",text= True, errors="replace") as p:
            for line in p.stdout:
                output_widget.insert(tk.END,line)
                output_widget.update()
                progressbar.step()
                
    if curcommand == "netstat":
        fullcommand = (curcommand, "-a" )
        with subprocess.Popen(
            fullcommand,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            encoding="utf-8",
            text= True,
            errors="ignore") as p:
            
            for line in p.stdout:
                output_widget.insert(tk.END,line)
                output_widget.update()
                progressbar.step()
    else:
         with subprocess.Popen(curcommand + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, encoding="utf-8",text= True, errors="ignore") as p:
            for line in p.stdout:
                output_widget.insert(tk.END,line)
                output_widget.update()
                progressbar.step(10)
        
            
    progressbar["value"] = 100
    output_widget.insert(tk.END, "DONE")
    output_widget.update()
    
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = output_widget.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()
            
            
# Creates a Window 
MAIN_WINDOW= tk.Tk()
MAIN_WINDOW.title("THE PYTHON TERMINATOR")
MAIN_WINDOW.geometry("900x360")


# Creates a frame
MAIN_FRAME = tk.Frame(MAIN_WINDOW, height= 500, width= 900, background="black")
MAIN_FRAME.pack()


# Configuring grid settings
MAIN_FRAME.rowconfigure(0, weight=1)
MAIN_FRAME.rowconfigure(1, weight=1)
MAIN_FRAME.rowconfigure(2, weight=1)
MAIN_FRAME.rowconfigure(3, weight=1)
MAIN_FRAME.columnconfigure(0, weight=1)
MAIN_FRAME.columnconfigure(1, weight=3)

# Variable Config for the command lisbox
commandslist = ["ping", "tracert", "netstat", "Get Weather", "nslookup", "curl"]
countervar = 0

# Creates a lisbox and inserts the values from the list onto the listbox
Command_ListBox = tk.Listbox(MAIN_FRAME, height= 5)
while countervar < len(commandslist):
    Command_ListBox.insert(tk.END, commandslist[countervar])
    countervar = countervar + 1
Command_ListBox.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

# Creates the start button
startbutton = tk.Button(MAIN_FRAME, text = "START", command=lambda:do_command(), foreground="red", font="comic")
startbutton.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

# Creates the progress bar
progressbar = ttk.Progressbar(MAIN_FRAME, orient="horizontal", mode="determinate")
progressbar.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

# Creates the Url Label
url_entry_label = tk.Label(MAIN_FRAME, text= "Enter the url:")
url_entry_label.grid(column=1, row=0, sticky=tk.EW )

# Creates the place to enter Url
url_entry = tk.Entry(MAIN_FRAME)
url_entry.grid(column=1, row=0, sticky=tk.SW, padx=5, pady=5)

# Creates a scrollable output widget
output_widget=tksc.ScrolledText(MAIN_FRAME,height=10,width=100,)
output_widget.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

# Creates a save button
save = tk.Button(MAIN_FRAME, text="SAVE", command=lambda:mSave(), foreground="blue")
save.grid()

# Loops the Window
MAIN_WINDOW.mainloop()