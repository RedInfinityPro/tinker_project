import tkinter as tk
from cpu_response import Story

window = tk.Tk()
window.minsize(160, 100)
# frame
frame = tk.Frame(master = window,width=600,height=190)
frame.pack()
# title
title = tk.Label(text = 'what would you like to do?')
title.place(x = 10,y = 30)
# send a message
message = tk.Label(text = '>')
message.place(x = 10,y = 80)
input_system = tk.Entry()
input_system.place(x = 30,y = 80)

# button
def display_text():
    display_box.insert(tk.END,'> ' + str(input_system.get()))
    read_story = Story(text = str(input_system.get()))
    display_box.insert(tk.END, read_story.story)

button = tk.Button(text = 'send'.upper(),width = 5,height = 1,command = display_text)
button.place(x = 60,y = 125)
# scroll bar
scroll_bar = tk.Scrollbar(window)
scroll_bar.place(x = 580,height = 180)
# input display box
display_box = tk.Listbox(window,yscrollcommand = scroll_bar.set,width = 63)
display_box.place(x = 195,y = 10)
scroll_bar.config(command = display_box.yview)
start_story = Story(text = 'start story')
display_box.insert(tk.END,start_story.story)
window.mainloop()
