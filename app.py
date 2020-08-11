import tkinter as tk

app = tk.Tk()
app.iconbitmap('path/to/ico/icon.ico')

#app.geometry('700x700')

app.title("Noted")

# Status bar color
# #B18904

#App background color
app['bg'] = '#F2F5A9'

# Menu options
#open_bttn = ( text="Open")
#save_bttn = ( text="Save as")
#cut_bttn = ( text="Cut")
#copy_bttn = ( text="Copy")
#paste_bttn = ( text="Paste")
#format_bttn = ( text="Format")
#leftalign_bttn = ( text="Left")
#middlealign_bttn = ( text="Justify")
#rightalign_bttn = ( text="Right")

text_box = tk.Text()
text_box.pack()