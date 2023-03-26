import tkinter as tk

def hello():
    print("hello")

root = tk.Tk()

root.title("Java 319")
root.geometry("400x300")
root.configure(bg="#01192E")

# menu
menu1 = tk.Menu(root)
menu1.add_command(label="app 1", command=hello)
root.config(menu=menu1)

root.mainloop()
