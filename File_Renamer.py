from customtkinter import *

window = CTk()

mainFrame = CTkFrame(window)
mainFrame.pack(padx = 20, pady = 20)

folderField = CTkLabel(mainFrame, text = "Folder Location : ", width = 100, font=CTkFont(size=15))
folderField.grid(padx = (10, 0), pady = (10, 0), row = 0, column = 0)

folderInput = CTkEntry(mainFrame, placeholder_text = "Path to Folder", width = 340)
folderInput.grid(padx = (10, 0), pady = 10, row = 1, column = 0, columnspan = 2)

browseBtn = CTkButton(mainFrame, text = "Browse", width = 60)
browseBtn.grid(padx = 10, pady = 10, row = 1, column = 3)

fileField = CTkLabel(mainFrame, text = "File Name : ", width = 100)
fileField.grid(padx = (10, 0), pady = 10, row = 2, column = 0)

fileInput = CTkEntry(mainFrame, placeholder_text = "eg: Stranger Things", width = 300)
fileInput.grid(padx = (0, 10), pady = 10, row = 2, column = 1, columnspan = 4)

extensionField = CTkLabel(mainFrame, text = "Extension : ", width = 100)
extensionField.grid(padx = (10, 0), pady = 10, row = 3, column = 0)

extensionInput = CTkEntry(mainFrame, placeholder_text = "eg: .mp4", width = 300)
extensionInput.grid(padx = (0, 10), pady = 10, row = 3, column = 1, columnspan = 4)

startingIndexField = CTkLabel(mainFrame, text = "Starting Index : ", width = 100)
startingIndexField.grid(padx = (10, 0), pady = 10, row = 4, column = 0)

startingIndexInput = CTkEntry(mainFrame, placeholder_text = "eg: 1, 15, 23, etc.", width = 300)
startingIndexInput.grid(padx = (0, 10), pady = 10, row = 4, column = 1, columnspan = 4)

renameBtn = CTkButton(mainFrame, text = "Rename")
renameBtn.grid(padx = 10, pady = 10, row = 5, column = 0, columnspan = 4)



window.mainloop()