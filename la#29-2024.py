import tkinter as tk

windows_ko = tk.Tk()
user = "ACE & RIVAII"
section = "BSIT - 2B"
windows_ko.title(f"OOP")
windows_ko.geometry("500x300")
windows_ko.configure(bg = "gray")

text_disp = tk.Label(windows_ko, text= f"OOP LA#29 {user},{section}")
text_disp.grid(row = 0, column = 0, padx = 150, pady = 50)

windows_ko.mainloop()