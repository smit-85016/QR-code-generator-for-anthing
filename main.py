from tkinter import *
import requests

root = Tk()
root.geometry("400x400")
root.title("QR Code Generator")

keywordVar = StringVar()
fileNameVar = StringVar()

def generateQR():
    keyword = "programming"

    api = f"https://api.qrserver.com/v1/create-qr-code/?data={keywordVar.get()}&size=100x100"

    response = requests.get(api)

    image = response.content


    file = open(f"{fileNameVar.get()}.png" , "wb")
    file.write(image)
    file.close()

    Label(root , text = "QR Code Generated Successfully").pack()

    image = PhotoImage(file = f"{fileNameVar.get()}.png")

    imageLabel = Label(root , image = image)
    imageLabel.image = image 
    imageLabel.pack()
    

keywordLabel = Label(root , text = "Enter Keyword")
keywordLabel.pack()

keywordEntry = Entry(root , textvariable=keywordVar)
keywordEntry.pack()

fileNameLabel = Label(root , text = "Enter File Name")
fileNameLabel.pack()

fileNameEntry = Entry(root, textvariable=fileNameVar)
fileNameEntry.pack()

generateButton = Button(root , text = "Generate QR Code" , command = generateQR)
generateButton.pack()

root.mainloop()