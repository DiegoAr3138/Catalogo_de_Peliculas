import tkinter as tk
from tkinter import ttk
from model.pelicula_dao import crear_tabla, borar_tabla
from model.pelicula_dao import Pelicula, guardar , listar, editar, eliminar
from tkinter import messagebox

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu,tearoff=0)

    barra_menu.add_cascade(label="Inicio",menu=menu_inicio)
    menu_inicio.add_command(label="Crear un registro en DB", command=crear_tabla)
    menu_inicio.add_command(label="Eliminar registro en DB",command= borar_tabla)
    menu_inicio.add_command(label="Salir",command=root.destroy)

    barra_menu.add_cascade(label="Consultas")
    barra_menu.add_cascade(label="Configuracion")
    barra_menu.add_cascade(label="Ayuda")


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480, height=320)
        self.root = root
        self.pack()
        #self.config( bg="green" )
        self.id_pelicula=None
        self.campos_pelicula()
        self.desabilitar_campos()
        self.tabla_peliculas()

    def campos_pelicula(self):
        ##esto va a estar separado por columnas
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.config(font=("Arial",12,"bold"))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_genero = tk.Label(self, text="Genero:")
        self.label_genero.config(font=("Arial",12,"bold"))
        self.label_genero.grid(row=1,column=0,padx=10,pady=10)

        self.label_calificacion = tk.Label(self, text="Calificaion:")
        self.label_calificacion.config(font=("Arial",12,"bold"))
        self.label_calificacion.grid(row=2,column=0,padx=10,pady=10)
        #----------------------------------------------------------------------------------------
        
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width=50, font=("ariel",12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self , textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=("ariel",12))
        self.entry_genero.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_calificacion = tk.StringVar()
        self.entry_calificacion = tk.Entry(self, textvariable=self.mi_calificacion)
        self.entry_calificacion.config(width=50, font=("ariel",12))
        self.entry_calificacion.grid(row=2,column=1,padx=10,pady=10,columnspan=2)
        # Creacion de botone

        self.boton_nuevo =tk.Button(self,text="Nuevo")
        self.boton_nuevo.config(width=20,font=("Arial",12,"bold"), fg="white",bg="Green",
                                cursor="hand2", activebackground="#35BD6F", command=self.habilitar_campos)
        self.boton_nuevo.grid(row=3,column=0,padx=10,pady=10)


        self.boton_guardar = tk.Button(self,text="Guardar")
        self.boton_guardar.config(width=20,font=("Arial",12,"bold"), fg="#DAD5D6",bg="#1658A2",
                                cursor="hand2", activebackground="#3586DF", command= self.guardar_datos)
        self.boton_guardar.grid(row=3,column=1,padx=10,pady=10)


        self.boton_cancelar = tk.Button(self,text="Cancelar")
        self.boton_cancelar.config(width=20,font=("Arial",12,"bold"), fg="white",bg="red",
                                cursor="hand2", activebackground="#E15370", command=self.desabilitar_campos)
        self.boton_cancelar.grid(row=3,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_calificacion.set("")
        self.mi_genero.set("")
        self.mi_nombre.set("")
        self.entry_nombre.config(state="normal")
        self.entry_calificacion.config(state="normal")
        self.entry_genero.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def desabilitar_campos(self):
        self.id_pelicula=None
        self.mi_calificacion.set("")
        self.mi_genero.set("")
        self.mi_nombre.set("")
        self.entry_nombre.config(state="disabled")
        self.entry_calificacion.config(state="disabled")
        self.entry_genero.config(state="disabled")
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        pelicula =Pelicula(
            self.mi_nombre.get() , 
            self.mi_genero.get(),
            self.mi_calificacion.get()
        )
        if self.id_pelicula == None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id_pelicula)

        self.tabla_peliculas()
        self.desabilitar_campos()
    

    def tabla_peliculas(self):
        #recupera la lista de peliculas
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()

        self.tabla = ttk.Treeview(self, columns=("Nombre","Genero","Calificacion"))
        self.tabla.grid(row=4, column=0,columnspan=4,sticky="nse")
        
        #Scrollbar para la tabla si exde 10 registros
        self.scrol = ttk.Scrollbar(self, 
                                   orient="vertical", command= self.tabla.yview)
        self.scrol.grid(row=4,column=4,sticky="nse")
        self.tabla.config(yscrollcommand= self.scrol.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Genero")
        self.tabla.heading("#3", text="Calificacion")
        

        #iterar la lista de peliculas
        for p in self.lista_peliculas:
            self.tabla.insert("",0,text=p[0],values=(p[1],p[2],p[3]))

        #boton de editar
        self.boton_editar =tk.Button(self,text="Editar")
        self.boton_editar.config(width=20,font=("Arial",12,"bold"), fg="white",bg="Green",
                                cursor="hand2", activebackground="#35BD6F", command=self.editar_datos)
        self.boton_editar.grid(row=5,column=0,padx=10,pady=10)

        #boton de eliminar
        self.boton_eliminar =tk.Button(self,text="Eliminar")
        self.boton_eliminar.config(width=20,font=("Arial",12,"bold"), fg="white",bg="red",
                                cursor="hand2", activebackground="#E15370",command=self.eliminar_datos)
        self.boton_eliminar.grid(row=5,column=1,padx=10,pady=10)
        
    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())["text"]
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())["values"][0]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())["values"][1]
            self.calificacion_pelicula = self.tabla.item(self.tabla.selection())["values"][2]

            self.habilitar_campos()

            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_genero.insert(0,self.genero_pelicula)
            self.entry_calificacion.insert(0,self.calificacion_pelicula)
        except:
            titulo="Edicion de datos"
            mensaje ="No ha selecionado ningun registro"
            messagebox.showerror(titulo,mensaje)
    
    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())["text"]
            eliminar(self.id_pelicula)
            self.tabla_peliculas()
            self.id_pelicula = None
        except:
            titulo="Eliminar un registro"
            mensaje ="No a seleccionado ningun registro registro"
            messagebox.showerror(titulo,mensaje)