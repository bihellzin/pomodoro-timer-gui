from tkinter import *
from time import sleep

class App:

  def __init__(self):
    app = Tk()
    # Concentration
    concentration_text = StringVar()
    concentration_label = Label(app, text='Minutes of concentation', font=('bold', 10), pady=10, padx=10)
    concentration_label.grid(row=0, column=0, sticky=W)
    concentration_entry = Entry(app, textvariable=concentration_text)
    concentration_entry.grid(row=0, column=1)

    # Short break
    short_break_text = StringVar()
    short_break_label = Label(app, text='Minutes of short break', font=('bold', 10), pady=10, padx=10)
    short_break_label.grid(row=1, column=0, sticky=W)
    short_break_entry = Entry(app, textvariable=short_break_text)
    short_break_entry.grid(row=1, column=1)

    # Long break
    long_break_text = StringVar()
    long_break_label = Label(app, text='Minutes of long break', font=('bold', 10), pady=10, padx=10)
    long_break_label.grid(row=2, column=0, sticky=W)
    long_break_entry = Entry(app, textvariable=long_break_text)
    long_break_entry.grid(row=2, column=1)

    # Long break
    cycles_text = StringVar()
    cycles_label = Label(app, text='Total cycles', font=('bold', 10), pady=10, padx=10)
    cycles_label.grid(row=3, column=0, sticky=W)
    cycles_entry = Entry(app, textvariable=cycles_text)
    cycles_entry.grid(row=3, column=1)

    start_btn = Button(app, text='click here', command=self.other_window)
    start_btn.grid(row=4, column=1, sticky=W)
  
    app.title('Pomodoro Timer')
    app.geometry('400x350')
    app.mainloop()
  

  def other_window(self):
    new_app = Tk()
    new_app.geometry('200x200')


if __name__ == "__main__":
  app = App()