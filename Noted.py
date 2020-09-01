import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# App functions

#Opening files
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("Rich Text Format", "*.rtf"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open (filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Noted - {filepath}")

#Saving files
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("Rich Text Format", "*.rtf"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Noted - {filepath}")
    
# Format functions
# def cut_line
# def copy_line
# def paste_line


window = tk.Tk()
window.title('Noted')
#app.iconbitmap('path/to/ico/icon.ico')

window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=700, weight=1)

# Status bar color
# #B18904

#App background color
#window["bg"] = "#F2F5A9"
#window.row["fg"] = "#F2F5A9"

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)

#Menu options
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file)
#
#label= [func1]
#btn_cut = tk.Button(fr_buttons, text="Cut")
#btn_copy = tk.Button(fr_buttons, text="Copy")
#btn_paste = tk.Button(fr_buttons, text="Paste")

#label= [Alignment]
#btn_cut = tk.Button(fr_buttons, text="Left Align")
#btn_copy = tk.Button(fr_buttons, text="Center")
#btn_paste = tk.Button(fr_buttons, text="Right Align")

#Grid layout
btn_open.grid(row=0, column=0, sticky='ew', padx=2, pady=2)
btn_save.grid(row=0, column=1, sticky='ew', padx=2)

#btn_cut.grid(row=1, column=2, sticky='ew', padx=2, pady=2)
#btn_copy.grid(row=1, column=0, sticky='ew', padx=2, pady=2)
#btn_paste.grid(row=1, column=1, sticky='ew', padx=2, pady=2)


fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Row color


# Button colors


window.mainloop()