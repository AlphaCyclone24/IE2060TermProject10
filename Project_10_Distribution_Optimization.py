import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import *
#import pandas as pd

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
order_screen = Tk()
order_screen.geometry("500x400")
order_screen.configure(background="#CF9FFF")

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
    global text_location
    text_location = location

def amount_change():
    global amount
    amount = int(amount_entry.get())

    monthdifference = abs(deliverymonth - currentmonth) * 30.4167
    daydifference = abs(deliveryday - currentday)
    yeardifference = abs(deliveryyear - currentyear) * 365
    timedifference = monthdifference + daydifference + yeardifference

    def estimates():
        global estimates
        estimates = [estimatea, estimateb, estimatec]
        estimates = sorted(estimates)
        print(f"The cost is going to be {estimates[0]}")
        global final_estimate
        final_estimate = estimates[0]

    if "S" == location:
        global estimatea
        estimatea = s[0] * deliverycost + timedifference * storagecosta
        estimatea = round(estimatea, 2)
        print(f"The cost of storage a is {estimatea}")
        global estimateb
        estimateb = s[1] * deliverycost + timedifference * storagecostb
        estimateb = round(estimateb, 2)
        print(f"The cost of storage b is {estimateb}")
        global estimatec
        estimatec = s[2] * deliverycost + timedifference * storagecostc
        estimatec = round(estimatec, 2)
        print(f"The cost of storage c is {estimatec}")
        estimates()


    if "LC" == location:
        estimatea = lc[0] * deliverycost + timedifference * storagecosta
        estimatea = round(estimatea, 2)
        print(f"The cost of storage a is {estimatea}")
        estimateb = lc[1] * deliverycost + timedifference * storagecostb
        estimateb = round(estimateb, 2)
        print(f"The cost of storage b is {estimateb}")
        estimatec = lc[2] * deliverycost + timedifference * storagecostc
        estimatec = round(estimatec, 2)
        print(f"The cost of storage c is {estimatec}")
        estimates()

    if "LAF" == location:
        estimatea = laf[0] * deliverycost + timedifference * storagecosta
        estimatea = round(estimatea, 2)
        print(f"The cost of storage a is {estimatea}")
        estimateb = laf[1] * deliverycost + timedifference * storagecostb
        estimateb = round(estimateb, 2)
        print(f"The cost of storage b is {estimateb}")
        estimatec = laf[2] * deliverycost + timedifference * storagecostc
        estimatec = round(estimatec, 2)
        print(f"The cost of storage c is {estimatec}")
        estimates()

    if "BR" == location:
        estimatea = br[0] * deliverycost + timedifference * storagecosta
        estimatea = round(estimatea, 2)
        print(f"The cost of storage a is {estimatea}")
        estimateb = br[1] * deliverycost + timedifference * storagecostb
        estimateb = round(estimateb, 2)
        print(f"The cost of storage b is {estimateb}")
        estimatec = br[2] * deliverycost + timedifference * storagecostc
        estimatec = round(estimatec, 2)
        print(f"The cost of storage c is {estimatec}")
        estimates()

    if "NO" == location:
        estimatea = no[0] * deliverycost + timedifference * storagecosta
        estimatea = round(estimatea, 2)
        print(f"The cost of storage a is {estimatea}")
        estimateb = no[1] * deliverycost + timedifference * storagecostb
        estimateb = round(estimateb, 2)
        print(f"The cost of storage b is {estimateb}")
        estimatec = no[2] * deliverycost + timedifference * storagecostc
        estimatec = round(estimatec, 2)
        print(f"The cost of storage c is {estimatec}")
        estimates()

    def yes_button(event):
        print("Successfully Submitted")

    def no_button(event):
        order_screen.window = Toplevel()

def confirmation_screen():
    confirmation_window = Toplevel()
    confirmation_window.geometry("500x400")
    confirmation_window.configure(background="#CF9FFF")

    confirmation_date_label = Label(confirmation_window, text=f"The date is for delivery is {deliverymonth}/{deliveryday}/{deliveryyear}", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    confirmation_date_label.place(x=10, y=50)

    confirmation_time_label = Label(confirmation_window, text=f"The time for the delivery is {hour}:{minute} {TOD}", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    confirmation_time_label.place(x=10, y=100)

    confirmation_material_amount_label = Label(confirmation_window, text=f"The location to be delivered to is {text_location}", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    confirmation_material_amount_label.place(x=10, y=150)

    confirmation_material_amount_label = Label(confirmation_window, text=f"The amount of material to be delivered is {amount}", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    confirmation_material_amount_label.place(x=10, y=200)

    confirmation_price_amount_label = Label(confirmation_window, text=f"The estimated cost is ${final_estimate}", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    confirmation_price_amount_label.place(x=10, y=250)

    confirmation_label = Label(confirmation_window, text=f"Is this information correct?", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    confirmation_label.place(x=10, y=300)

    ttk.order_yes_submission_bttn = Button(confirmation_window, text="Yes", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    ttk.order_yes_submission_bttn.place(x=150, y=350)

    ttk.order_no_submission_bttn = Button(confirmation_window, text="No", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
    ttk.order_no_submission_bttn.place(x=200, y=350)

def order_submission():
    date_changed()
    hour_changed()
    minute_change()
    location_change()
    TOD_change()
    amount_change()
    print(f"The date is {date}, the time is {hour}:{minute} {TOD} for {amount} material")
    print(f"The cost is going to be {final_estimate}")
    confirmation_screen()

# Create Entry that will accept date of birth after clicking on submit
date_label = Label(order_screen, text="Date of Delivery: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
date_label.place(x=10, y=158)

# Set up for hour label on order screen
hour_label = Label(order_screen, text="Time of Delivery: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
hour_label.place(x=10, y=198)

# Set up for location label on order screen
location_label = Label(order_screen, text="Location of Delivery: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
location_label.place(x=10, y=238)

# Set up for amount label on order screen
amount_label = Label(order_screen, text="Amount of Material: ", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
amount_label.place(x=10, y=278)

# Set up for date entry
date_entry = Entry(order_screen, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui", 12, "bold"))
date_entry.place(x=160, y=160, width=200)
date_entry.insert(0, "dd/mm/yyy")
date_entry.bind("<1>", pick_date)

# Creates a dropdown menu for hour of deliver
hour_entry = ttk.Combobox(state="readonly", value=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
hour_entry.place(x=160, y=205, width=50)

# Creates a dropdown menu for minute of deliver
minute_entry = ttk.Combobox(state="readonly", value=["00", "15", "30", "45"])
minute_entry.place(x=220, y=205, width=50)

# Creates dropdown menu for if the delivery is in the am or pm
TOD_entry = ttk.Combobox(state="readonly", values=["am", "pm"])
TOD_entry.place(x=280, y=205, width=50)

# Creates a dropdown menu for location of deliver
location_entry = ttk.Combobox(state="readonly", value=["S", "LC", "LAF", "BR", "NO"])
location_entry.place(x=185, y=245, width=50)

# Creates a number input for amount of materials
amount_entry = Entry(order_screen, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui", 12, "bold"))
amount_entry.place(x=185, y=280, width=50)

ttk.order_confirmation_bttn = Button(order_screen, command=order_submission, text="Order Confirmation", bg="#CF9FFF", fg="white", font=("yu gothic ui", 13, "bold"))
ttk.order_confirmation_bttn.place(x=150, y=318)

order_screen.mainloop()

