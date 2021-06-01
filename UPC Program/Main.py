# Library Imports
from tkinter import *
import requests
import json

# Main App Body
app = Tk()
app.geometry("330x200")
app.iconbitmap(os.path.join(sys._MEIPASS, "inventory.ico"))
app.title("Inventory System V0.1")
app.resizable(width=False, height=False)

# Labels
upcinput = Label(app, text="UPC INPUT",)
upcinput.grid(row=0,column=0,sticky="W",pady = "1")
consoleoutput = Label(app, text="CONSOLE OUTPUT")
consoleoutput.grid(row=2,column=0,sticky="W",pady = "1")

# Upc Input Box
upcbox = Entry(app, relief="solid")
upcbox.grid(padx=5, pady=1, ipady=5, ipadx=97, row=1, column=0,sticky="W")

# Console Output Box
console = Text(app, relief = "solid", width = "38", height = "6")
console.grid(padx=5, pady=1, ipady=5, ipadx=5, row=3, column=0,sticky="W")
console.config(state='disabled')

# Global variables
global upc
upc = ""
global apikey
apikey = "?apikey=C63F302D95C4A04A5961D08871978294"
global apicall
apicall = "https://api.upcdatabase.org/product/"

# Get UPC Function
def getupc(event=None):
    global upc
    upc = upcbox.get()
    upcbox.delete('0','end')
    console.config(state="normal")
    # console.delete('1.0','end')
    console.config(state="disabled")
    apicallfunc()

# Call API Function
def apicallfunc():
    global apicall
    apicall = "https://api.upcdatabase.org/product/"+upc+apikey
    response = requests.get(apicall)
    jprint(response.json())

# Print Product Info Into Console
def jprint(obj):
    success = json.dumps(obj["success"])
    if success == "false":
        console.config(state="normal")
        console.insert('end',"Invalid UPC")
        console.config(state="disabled")
    else:
        barcode = json.dumps(obj["barcode"])
        title = json.dumps(obj["title"])
        description = json.dumps(obj["description"])
        console.config(state="normal")
        console.insert('1.0', "barcode: "+barcode+'\n')
        console.insert('1.0', "title: "+title+'\n')
        console.insert('1.0', "description: "+description+'\n')
        console.config(state="disabled")

# Upc Input Box Entry
upcbox.bind('<Return>', getupc)

# Main App Render Loop
app.mainloop()