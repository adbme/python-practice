import tkinter as tk

def hello():
    print("hello")

root = tk.Tk()

root.title("Java 319")
root.geometry("1000x800")
root.configure(bg="#01192E")

# Création de la div principale avec une couleur de fond
main_div = tk.Frame(root, width=400, height=300, bg="#353535")
main_div.pack(fill="both", expand=True, padx=40, pady=40)

# menu
menu1 = tk.Menu(root)
menu1.add_command(label="app 1", command=hello)
root.config(menu=menu1)

root.mainloop()





