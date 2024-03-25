import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import *

# Getting the current day
currentyear = datetime.datetime.today().year
currentday = datetime.datetime.today().day
currentmonth = datetime.datetime.today().month


# Storage Cost in Days
storagecosta = 0.10
storagecostb = 0.16
storagecostc = 0.12

# Cost for delivery
deliverycost = 0.04

# Distances to the Cities in Miles
s = [125, 246, 232]
lc = [100, 80, 97]
laf = [89, 56, 20]
br = [124, 2, 68]
no = [203, 75, 133]

# Starts the application
root = Tk()
root.geometry("500x400")
root.configure(background="#CF9FFF")

# Get the selected date when the user closes the calendar
def pick_date(event):
    global cal, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title('Chose Date for Delivery')
    date_window.geometry('250x220+590+370')
    cal = Calendar(date_window, selectmode="day", date_pattern='mm/dd/y')
    cal.place(x=0, y=0)

    submit_btn = Button(date_window, text="Submit", command=grab_date)
    submit_btn.place(x=80, y=190)

def grab_date():
    date_entry.delete(0, END)
    date_entry.insert(0, cal.get_date())
    date_window.destroy()

def date_changed():
    global date
    date = date_entry.get()
    date = date.split('/')
    global deliverymonth
    deliverymonth = int(date[0])
    global deliveryday
    deliveryday = int(date[1])
    global deliveryyear
    deliveryyear = int(date[2])
def hour_changed():
    global hour
    hour = int(hour_entry.get())

def minute_change():
    global minute
    minute = int(minute_entry.get())

def TOD_change():
    global TOD
    TOD = TOD_entry.get()

def location_change():
    global location
    location = location_entry.get()

def amount_change():
    global amount
    amount = int(amount_entry.get())

def order_submission():
    date_changed()
    hour_changed()
    minute_change()
    location_change()
    TOD_change()
    amount_change()
    print(f"The date is {date}, the time is {hour}:{minute} {TOD} for {amount} material")


    monthdifference = abs(deliverymonth - currentmonth) * 30.4167
    daydifference = abs(deliveryday - currentday)
    yeardifference = abs(deliveryyear - currentyear) * 365
    timedifference = monthdifference + daydifference + yeardifference

    if "S" == location:
        estimatea = s[0] * deliverycost + timedifference * storagecosta
        print(f"The cost of storage a is {estimatea}")
        estimateb = s[1] * deliverycost + timedifference * storagecostb
        print(f"The cost of storage b is {estimateb}")
        estimatec = s[2] * deliverycost + timedifference * storagecostc
        print(f"The cost of storage c is {estimatec}")
        estimates = [estimatea, estimateb, estimatec]
        estimates = sorted(estimates)
        print(f"The cost is going to be {estimates[0]}")

    if "LC" == location:
        estimatea = lc[0] * deliverycost + timedifference * storagecosta
        print(f"The cost of storage a is {estimatea}")
        estimateb = lc[1] * deliverycost + timedifference * storagecostb
        print(f"The cost of storage b is {estimateb}")
        estimatec = lc[2] * deliverycost + timedifference * storagecostc
        print(f"The cost of storage c is {estimatec}")
        estimates = [estimatea, estimateb, estimatec]
        estimates = sorted(estimates)
        print(f"The cost is going to be {estimates[0]}")

    if "LAF" == location:
        estimatea = laf[0] * deliverycost + timedifference * storagecosta
        print(f"The cost of storage a is {estimatea}")
        estimateb = laf[1] * deliverycost + timedifference * storagecostb
        print(f"The cost of storage b is {estimateb}")
        estimatec = laf[2] * deliverycost + timedifference * storagecostc
        print(f"The cost of storage c is {estimatec}")
        estimates = [estimatea, estimateb, estimatec]
        estimates = sorted(estimates)
        print(f"The cost is going to be {estimates[0]}")

    if "BR" == location:
        estimatea = br[0] * deliverycost + timedifference * storagecosta
        print(f"The cost of storage a is {estimatea}")
        estimateb = br[1] * deliverycost + timedifference * storagecostb
        print(f"The cost of storage b is {estimateb}")
        estimatec = br[2] * deliverycost + timedifference * storagecostc
        print(f"The cost of storage c is {estimatec}")
        estimates = [estimatea, estimateb, estimatec]
        estimates = sorted(estimates)
        print(f"The cost is going to be {estimates[0]}")

    if "NO" == location:
        estimatea = no[0] * deliverycost + timedifference * storagecosta
        print(f"The cost of storage a is {estimatea}")
        estimateb = no[1] * deliverycost + timedifference * storagecostb
        print(f"The cost of storage b is {estimateb}")
        estimatec = no[2] * deliverycost + timedifference * storagecostc
        print(f"The cost of storage c is {estimatec}")
        estimates = [estimatea, estimateb, estimatec]
        estimates = sorted(estimates)
        print(f"The cost is going to be {estimates[0]}")


# Create Entry that will accept date of birth after clicking on submit
date_label = Label(root, text="Date of Delivery: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
date_label.place(x=10, y=158)

hour_label = Label(root, text="Time of Delivery: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
hour_label.place(x=10, y=198)

location_label = Label(root, text="Location of Delivery: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
location_label.place(x=10, y=238)

amount_label = Label(root, text="Amount of Material: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
amount_label.place(x=10, y=278)

date_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui", 12, "bold"))
date_entry.place(x=160, y=160, width=200)
date_entry.insert(0, "dd/mm/yyy")
date_entry.bind("<1>", pick_date)

hour_entry = ttk.Combobox(state="readonly", value=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
hour_entry.place(x=160, y=205, width=50)

minute_entry = ttk.Combobox(state="readonly", value=["00", "15", "30", "45"])
minute_entry.place(x=220, y=205, width=50)

TOD_entry = ttk.Combobox(state="readonly", values=["am", "pm"])
TOD_entry.place(x=280, y=205, width=50)

location_entry = ttk.Combobox(state="readonly", value=["S", "LC", "LAF", "BR", "NO"])
location_entry.place(x=185, y=245, width=50)

amount_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui", 12, "bold"))
amount_entry.place(x=185, y=280, width=50)

ttk.order_sub_bttn = Button(root, command=order_submission, text="Order Submission", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
ttk.order_sub_bttn.place(x=150, y=318)

root.mainloop()

