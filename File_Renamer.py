import os
from customtkinter import *
from tkinter import filedialog

# Opens browsing window
def browse():
    folderLocation = filedialog.askdirectory()
    folderInput.insert(0, folderLocation)

def rename():
    path = os.chdir(folderInput.get())
    filename = fileInput.get()
    extension = extensionInput.get()
    index = int(startingIndexInput.get())

    for file in os.listdir(path):
        newname =  filename + ' ' + str(index) + extension
        os.rename(file, newname)
        index = index + 1

    # Changing the Rename Button to 'Done' for 1 Second
    renameBtn.configure(text = "Done")
    renameBtn.after(1000, lambda: renameBtn.configure(text = "Rename"))

    # Resetting all the entry values to ''
    folderInput.delete(0, END)
    fileInput.delete(0, END)
    extensionInput.delete(0, END)
    startingIndexInput.delete(0, END)

# UI ----------------------------------------------------------------------------------------------

window = CTk()

# Disabling resizing
window.resizable(width = False, height = False)
window.title(' File renamer')

mainFrame = CTkFrame(window)
mainFrame.pack(padx = 20, pady = 20)

folderField = CTkLabel(mainFrame, text = "Folder Location : ", width = 100, font=CTkFont(size=15))
folderField.grid(padx = (20, 0), pady = (10, 0), row = 0, column = 0)

folderInput = CTkEntry(mainFrame, placeholder_text = "Path to Folder", width = 340)
folderInput.grid(padx = (20, 0), pady = 10, row = 1, column = 0, columnspan = 2)

browseBtn = CTkButton(mainFrame, command = browse , text = "Browse", width = 60)
browseBtn.grid(padx = 10, pady = 10, row = 1, column = 3)

fileField = CTkLabel(mainFrame, text = "File Name : ", width = 100)
fileField.grid(padx = (10, 0), pady = 10, row = 2, column = 0)

fileInput = CTkEntry(mainFrame, placeholder_text = "eg: Stranger Things episode", width = 300)
fileInput.grid(padx = (0, 10), pady = 10, row = 2, column = 1, columnspan = 4)

extensionField = CTkLabel(mainFrame, text = "Extension : ", width = 100)
extensionField.grid(padx = (10, 0), pady = 10, row = 3, column = 0)

extensionInput = CTkEntry(mainFrame, placeholder_text = "eg: .mp4", width = 300)
extensionInput.grid(padx = (0, 10), pady = 10, row = 3, column = 1, columnspan = 4)

startingIndexField = CTkLabel(mainFrame, text = "Starting Index : ", width = 100)
startingIndexField.grid(padx = (10, 0), pady = 10, row = 4, column = 0)

startingIndexInput = CTkEntry(mainFrame, placeholder_text = "eg: 1, 15, 23, etc.", width = 300)
startingIndexInput.grid(padx = (0, 10), pady = 10, row = 4, column = 1, columnspan = 4)

renameBtn = CTkButton(mainFrame, command = rename, text = "Rename")
renameBtn.grid(padx = 10, pady = (10, 20), row = 5, column = 0, columnspan = 4)

window.mainloop()