import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

def send_receipt():
    if r1_v.get() == "MorningEsp":
        print("Sending Balance sheet in the Morning in Spanish")
    elif r1_v.get() == "AfternoonEsp":
        print("Sending Balance sheet in the Afternoon in Spanish")
    elif r1_v.get() == "MorningEng":
        print("Sending Balance sheet in the Morning in English")
    elif r1_v.get() == "AfternoonEng":
        print("Sending Balance sheet in the Afternoon in English")
    else:
        print("No Radio Button selected")


root = tk.Tk()

root.title("Receipt Sender")
root.geometry("900x600")

#Here we create the frame to put in the root window
labelFrame = tk.Frame(root)
labelFrame.columnconfigure(0, weight=1)
labelFrame.columnconfigure(1, weight=1)

#Here we create the variable the radio button will hold 
r1_v = tk.StringVar() # it will hold value that is a String; Note: if its value attribute inside tk.RadioButton was an integer, you would do r1_v = tk.IntVar()
r1_v.set(None)

#Label added here
labelESPm = tk.Label(labelFrame, text=" Morning\n (ESP)", font=('Arial', 18))
labelESPm.grid(row=0, column=0, sticky=tk.W+tk.E, padx=20, pady=20)
#Radio button added here
r1=tk.Radiobutton(labelFrame, text='MorningEsp', variable=r1_v, value= 'MorningEsp')
r1.grid(row=1, column=0, padx=30, pady=30)

labelESPa = tk.Label(labelFrame, text=" Afternoon\n (ESP)", font=('Arial', 18))
labelESPa.grid(row=0, column=1, sticky=tk.W+tk.E, padx=20, pady=20)
#Radio button added here
r2=tk.Radiobutton(labelFrame, text='AfternoonEsp', variable=r1_v, value='AfternoonEsp')
r2.grid(row=1, column=1, padx=30, pady=30)

labelENGm = tk.Label(labelFrame, text=" Morning\n (ENG)", font=('Arial', 18))
labelENGm.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20, pady=20)
#Radio button added here
r3=tk.Radiobutton(labelFrame, text='MorningENG', variable=r1_v, value='MorningEng')
r3.grid(row=1, column=2, padx=30, pady=30)

labelENGa = tk.Label(labelFrame, text=" Afternoon\n (ENG)", font=('Arial', 18))
labelENGa.grid(row=0, column=3, sticky=tk.W+tk.E, padx=20, pady=20)
#Radio button added here
r4=tk.Radiobutton(labelFrame, text='AfternoonEng', variable=r1_v, value='AfternoonEng')
r4.grid(row=1, column=3, padx=30, pady=30)

#To show the Balance sheets progress sent and not found
columns = ('Balance sheet', 'Sent', 'Not Found')
tree = ttk.Treeview(labelFrame, columns=columns, show="headings") #Creating the TreeView
#Adding the heading titles on the TreeView
tree.heading('Balance sheet', text='Balance sheet')
tree.heading('Sent', text='Sent')
tree.heading('Not Found', text='Not Found')
tree.grid(row=2, column=0, columnspan=4, padx=20, pady=10) #Adding the TreeView to GUI

def File_dialog():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes= (("pdf files", "*.pdf"),("All Files","*.*")))
    label_file["text"] = filename

def Load_pdf_file():
    label_file["text"] = "PDF File uploaded into tree view"

#File Label frame
label_file = ttk.Label(labelFrame, text="No File Selected")
label_file.grid(row=3, columnspan=1, padx=36, pady=10)

#The Browse a file Button
BrowseButton = tk.Button(labelFrame, text="Browse a File", command=lambda: File_dialog())
BrowseButton.grid(row=4, column=2, padx=36, pady=10)

#The load a file Button
LoadButton = tk.Button(labelFrame, text="Load File", command=lambda: Load_pdf_file())
LoadButton.grid(row=4, column=3, padx=36, pady=10)

#The Send button
SendButton = tk.Button(labelFrame, text="SEND", font=('Arial', 18), command= send_receipt) #Creating the Send Button 
SendButton.grid(row=5, columnspan=4, sticky="news", padx=36, pady=10) #Adding the Send Button to GUI, the sticky="news" stands for north,east,west,south


labelFrame.pack()

root.mainloop()
