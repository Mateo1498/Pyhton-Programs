from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S %p")
    timeLabel.config(text=time_string)

    day_string = strftime("%A")
    dayLabel.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    dateLabel.config(text=date_string)

    window.after(1000, update)


window = Tk()

timeLabel = Label(window,font=("Arial",50))
timeLabel.pack()

dayLabel = Label(window,font=("Helvatica",25))
dayLabel.pack()

dateLabel = Label(window,font=("Helvatica",30))
dateLabel.pack()
update()

window.mainloop()
