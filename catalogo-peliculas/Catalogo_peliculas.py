import tkinter as tk
from client.gui_app import *

def main():
    root = tk.Tk()
    root.title("Catalogo de Peliculas")
    root.iconbitmap('img/Logo.ico')
    root.resizable(0,0)

    barra_menu(root)

    app = Frame(root = root )
   

    root.mainloop()

if __name__=='__main__':
    main()