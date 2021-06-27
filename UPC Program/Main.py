# Library Imports
import tkinter
import mysql.connector
import threading
from time import sleep

# Main app body
app = tkinter.Tk()
app.geometry("330x200")
# app.iconbitmap(os.path.join(sys._MEIPASS, "inventory.ico"))
app.title("Inventory System V0.1")
app.resizable(width=False, height=False)

# Database Connection
dbconfig = {
  "host":"localhost",
  "user":"admin",
  "password":"admin",
  "database":"DCIS"
}

# Global variables
global selectcansquery
global updatecansquery
global printcansquery
global selectboxesquery
global updatecansquery
global printboxesquery
global upc
global upc2
selectcansquery = "SELECT * FROM cans WHERE barcode = %s"
updatecansquery = "UPDATE cans SET qoh = qoh - 1 WHERE barcode = %s"
printcansquery = "SELECT title FROM cans WHERE barcode = %s"
selectboxesquery = "SELECT * FROM boxes WHERE barcode = %s"
updateboxesquery = "UPDATE cans SET qoh = qoh + (SELECT pack_count FROM boxes WHERE barcode = %s) WHERE barcode = (SELECT can_upc FROM boxes WHERE barcode = %s)"
printboxesquery = "SELECT cans.title, boxes.pack_count FROM boxes INNER JOIN cans WHERE boxes.barcode = %s AND cans.barcode = boxes.can_upc"
upc = ""
upc2 = ""


# Get UPC function
def getupc(event=None):
  global upc
  upc = (upcbox.get(),)
  global upc2
  upc2 = (upcbox.get(),upcbox.get(),)
  cnx = mysql.connector.connect(**dbconfig)
  cursor = cnx.cursor()
  cursor.execute(selectcansquery, upc)
  if cursor.fetchall():
    cursor.execute(updatecansquery, upc)
    cnx.commit()
    cursor.execute(printcansquery, upc)
    canresult = cursor.fetchone()
    console.config(state='normal')
    console.delete('1.0','end')
    console.insert('1.0','-1 of: '+canresult[0])
    console.config(state='disabled')
    cursor.close()
    cnx.close()
    upcbox.delete('0','end')
  else:
    cursor.execute(selectboxesquery, upc)
    if cursor.fetchall():
      cursor.execute(updateboxesquery, upc2)
      cnx.commit()
      cursor.execute(printboxesquery, upc)
      boxresult = cursor.fetchall()
      console.config(state='normal')
      console.delete('1.0','end')
      console.insert('1.0','Added '+str(boxresult[0][1])+' To '+boxresult[0][0])
      console.config(state='disabled')
      cursor.close()
      cnx.close()
      upcbox.delete('0','end')
    else:
        console.config(state='normal')
        console.delete('1.0','end')
        console.insert('1.0','INVALID/NOT FOUND')
        console.config(state='disabled')
    upcbox.delete('0','end')
    cursor.close()
    cnx.close()

# App widgets
upcinput = tkinter.Label(app, text="UPC INPUT")
upcinput.grid(row=0,column=0,sticky="W",pady = "1")
consoleoutput = tkinter.Label(app, text="CONSOLE OUTPUT")
consoleoutput.grid(row=2,column=0,sticky="W",pady = "1")
upcbox = tkinter.Entry(app, relief="solid")
upcbox.grid(padx=5, pady=1, ipady=5, ipadx=77, row=1, column=0,sticky="W")
console = tkinter.Text(app, relief = "solid", width = "38", height = "6")
console.grid(padx=5, pady=1, ipady=5, ipadx=5, row=3, column=0,sticky="W")
console.config(state='disabled')

def startquery(event=None):
  threading.Thread(target = getupc).start()

# Enter bind
upcbox.bind('<Return>', startquery)

# Main GUI loop
app.mainloop()