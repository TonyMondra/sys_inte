import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sql_class import Consultas

class Clientes:
    def __init__(self, notebook, select_clientes):
        self.sqls = Consultas()
        self.table = None
        self.clientes_frame = None
        self.entry_values = []
        self.tabla_encabezados = ["Clave", "Nombre", "Teléfono", "Correo", "Direccion"]
        self.select_clientes = select_clientes
        self.crear_seccion_clientes(notebook)


    #elimina el registro seleccionado
    def delPersona(self):
        selected_item = self.table.focus()
        if selected_item:
            values = self.table.item(selected_item, 'values')
            celda = values[0]
            print (celda)
    
    #valida si el algun input esta vacio
    def isEmpty(self):
        for entry in self.entry_values:
            value = entry.get()
            if not value or value.isspace():
                return True  
        return False  

    #inserta un nuevo registro en la tabla
    def insert(self):
        values = []
        for entry in self.entry_values:
            value = entry.get()
            value = value.strip()
            values.append(value)

        if self.isEmpty():
            messagebox.showinfo("Mensaje", "No puede haber campos vacios")
        else:
            if self.sqls.registroExistente(self.sqls.table_clientes, self.sqls.pers_cond, values[0] ):
                messagebox.showinfo("Importante", "registro existente!")
            else: 
                self.sqls.insertar_persona(values)
                self.refrescar_tabla(self.table, self.sqls.select('gente'))
                messagebox.showinfo("Mensaje", "registro agregado!") 
            

    #actualiza la tabla con un select
    def refrescar_tabla(self, tree, tabla_obj):
        tree.delete(*tree.get_children())
        for row in tabla_obj:
            tree.insert('', 'end', values=row)

    
    def crear_formulario(self, panel, labels):
        frame_formulario = ttk.Frame(panel)
        frame_formulario.pack(padx=20, pady=20)

        for i, label_text in enumerate(labels):
            label = tk.Label(frame_formulario, text=label_text + ":")
            label.grid(row=i, column=0)
            entry = tk.Entry(frame_formulario)
            entry.grid(row=i, column=1)
            self.entry_values.append(entry) 

        boton_formulario = tk.Button(frame_formulario, text="Agregar", command=self.insert)
        boton_formulario.grid(row=len(labels) + 1, columnspan=2, padx=10, pady=10)
    

    def crear_tabla(self, panel, labels, t_fuente):
        frame_tabla = ttk.Frame(panel)
        frame_tabla.pack(padx=20, pady=20)

        self.table = ttk.Treeview(frame_tabla, columns=labels, show="headings")
        for label in labels:
            self.table.heading(label, text=label)
        self.table.pack()

        self.refrescar_tabla(self.table, t_fuente)

        frame_botones_tabla = ttk.Frame(frame_tabla)
        frame_botones_tabla.pack(padx=20, pady=20)

        boton1_tabla = tk.Button(frame_botones_tabla, text="Editar", width=40)
        boton1_tabla.pack(side=tk.LEFT, padx=10, pady=10)

        boton2_tabla = tk.Button(frame_botones_tabla, text="Eliminar", width=40, command=self.delPersona)
        boton2_tabla.pack(side=tk.LEFT, padx=10, pady=10)

    def crear_seccion_clientes(self, notebook):
        self.clientes_frame = ttk.Frame(notebook)
        notebook.add(self.clientes_frame, text="Clientes")

        self.crear_formulario(self.clientes_frame, self.tabla_encabezados)
        self.crear_tabla(self.clientes_frame, self.tabla_encabezados, self.select_clientes)

        #boton_clientes = tk.Button(self.clientes_frame, text="Clientes", command=lambda: self.cambiar_seccion(notebook, "Clientes"))
        #boton_clientes.pack()

    def cambiar_seccion(self, notebook, seccion):
        for index, tab in enumerate(notebook.tabs()):
            if notebook.tab(tab, "text") == seccion:
                notebook.select(index)
