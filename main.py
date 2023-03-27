import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

def hello():
    print("hello")

# style
root.title("Java 319")
root.geometry("1000x800")
root.configure(bg="#2A2A2A")

# Fonction execute
def execute_code():
    code = input1.get("1.0", "end-1c")  # Récup input1
    try:
        result = eval(code)  # évalu le code
    except Exception as e:
        result = str(e)  # trouve l'erreur
    console.insert(tk.END, result + "\n")  # systeme erreure

# div
main_div = tk.Frame(root, width=100, height=300, bg="#2A2A2A")
main_div.pack(fill="both", expand=True, padx=20, pady=20)

# label input
label1 = tk.Label(main_div, text="CODE:", font=("Arial", 20), fg="#FFFFFF", bg="#2A2A2A")
label1.pack(pady=(0, 10))
input1 = tk.Text(main_div, width=50, height=10, font=("Arial", 20), bd=2, relief="groove", fg="#FFFFFF", bg="#3D3D3D")
input1.bind("<Shift-Return>", lambda event: input1.insert(tk.END, '\n')) # retour a la ligne
input1.pack(fill="x")

# label console
label2 = tk.Label(main_div, text="CONSOLE", font=("Arial", 20), fg="#FFFFFF", bg="#2A2A2A")
label2.pack(pady=(0, 10))
console = ScrolledText(main_div, width=50, height=0, font=("Arial", 20), bd=2, relief="groove", fg="#FFFFFF", bg="#3D3D3D")
console.pack(fill="both", expand=True)

# boutton execute
execute_button = tk.Button(main_div, text="Execute", font=("Arial", 20), bd=2, relief="groove", command=execute_code, fg="#FFFFFF", bg="#3D3D3D")
execute_button.pack(pady=(20,0))

# menu
menu1 = tk.Menu(root, fg="#FFFFFF", bg="#2A2A2A")
menu1.add_command(label="app 1", command=hello)
root.config(menu=menu1)

x = ('test')

root.mainloop()
