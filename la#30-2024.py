import tkinter as tk 

root = tk.Tk()
root.title("basic tkinter widgets") 
root.geometry("500x300")
root.configure(bg= "light blue")
anime ="ONE PUNCH MAN"
frame = tk.Frame(root)
frame.pack(pady=20)

def display_text():
    print(f" My favorite anime is {anime}")

button = tk.Button(root, text="Run", command=display_text)
button.pack(pady=10)

root.mainloop()