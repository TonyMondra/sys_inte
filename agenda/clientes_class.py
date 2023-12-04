import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sql_class import Consultas

class Clientes:
    def __init__(self, notebook):
        self.sqls = Consultas()
        self.table = None
        self.clientes_frame = None
        self.form_insert = []
        self.form_edit = []
        self.encabezados = ["Clave", "Nombre", "Teléfono", "Correo", "Direccion"]
        self.lista_clientes = self.sqls.select(self.sqls.table_clientes)
        self.crear_seccion_clientes(notebook)


    def crear_formulario(self, panel, labels):
        frame_formulario = ttk.Frame(panel)
        frame_formulario.pack(padx=20, pady=20)

        for i, label_text in enumerate(labels):
            label = tk.Label(frame_formulario, text=label_text + ":")
            label.grid(row=i, column=0)
            entry = tk.Entry(frame_formulario)
            entry.grid(row=i, column=1)
            self.form_insert.append(entry) 

        boton_formulario = tk.Button(frame_formulario, text="Agregar", command=self.insertar_cliente)
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

        boton1_tabla = tk.Button(frame_botones_tabla, text="Editar", width=40, command=self.abrir_ventana_edicion)
        boton1_tabla.pack(side=tk.LEFT, padx=10, pady=10)

        boton2_tabla = tk.Button(frame_botones_tabla, text="Eliminar", width=40, command=self.del_persona)
        boton2_tabla.pack(side=tk.LEFT, padx=10, pady=10)

    def crear_seccion_clientes(self, notebook):
        self.clientes_frame = ttk.Frame(notebook)
        notebook.add(self.clientes_frame, text="Clientes")

        self.crear_formulario(self.clientes_frame, self.encabezados)
        self.crear_tabla(self.clientes_frame, self.encabezados, self.lista_clientes)

    def abrir_ventana_edicion(self):
            selected_item = self.table.focus()
            if selected_item:
                values = self.table.item(selected_item, 'values')
                self.editar_cliente(values)
            else:
                messagebox.showinfo("Mensaje", "Seleccione un registro para editar")
    
    def editar_cliente(self, values):
        self.form_edit.clear()
        edit_window = tk.Toplevel()
        edit_window.title("Editar cliente")

        frame_editar = ttk.Frame(edit_window)
        frame_editar.pack(padx=20, pady=20)

        for i, label_text in enumerate(self.encabezados):
            label = tk.Label(frame_editar, text=label_text + ":")
            label.grid(row=i, column=0)
            entry = tk.Entry(frame_editar)
            entry.grid(row=i, column=1)
            entry.insert(tk.END, values[i])  
            self.form_edit.append(entry)

        boton_actualizar = tk.Button(frame_editar, text="Actualizar", command=self.actualizar_cliente)
        boton_actualizar.grid(row=len(self.encabezados) + 1, columnspan=2, padx=10, pady=10)


    #inserta un nuevo registro en la tabla
    def insertar_cliente(self):
        values = []
        for entry in self.form_insert:
            value = entry.get()
            value = value.strip()
            values.append(value)

        if self.isEmpty(self.form_insert):
            messagebox.showinfo("Mensaje", "No puede haber campos vacios")
        else:
            if self.sqls.registroExistente(self.sqls.table_clientes, self.sqls.pers_cond, values[0] ):
                messagebox.showinfo("Importante", "registro existente!")
                self.limpiar_entradas(self.form_insert)
            else: 
                self.sqls.insertar(self.sqls.table_clientes, self.sqls.pers_cols, values)
                self.refrescar_tabla(self.table, self.sqls.select('gente'))
                messagebox.showinfo("Mensaje", "registro agregado!")

    def actualizar_cliente(self):
        new_values = []
        for entry in self.form_edit:
            value = entry.get()
            value = value.strip()
            new_values.append(value)

        if self.sqls.registroExistente(self.sqls.table_clientes, self.sqls.pers_cond, new_values[0]):
            if self.isEmpty(self.form_edit):
                messagebox.showinfo("Mensaje", "No puede haber campos vacios")
            else:
                self.sqls.update(self.sqls.table_clientes, self.sqls.pers_cols, new_values, self.sqls.pers_cond, new_values[0] )
                self.refrescar_tabla(self.table, self.sqls.select(self.sqls.table_clientes))
                messagebox.showinfo("Mensaje", "registro Actualizado!")
        else: messagebox.showinfo("Error", "Persona no encontrada en el sistema!")            

    #elimina el registro seleccionado
    def del_persona(self):
        selected_item = self.table.focus()
        if selected_item:
            values = self.table.item(selected_item, 'values')
            celda = values[0]
            self.sqls.eliminar(self.sqls.table_clientes, self.sqls.pers_cond, celda)
            self.refrescar_tabla(self.table, self.sqls.select(self.sqls.table_clientes))
            messagebox.showinfo("Mensaje", "Registro eliminado")
        else: messagebox.showinfo("Mensaje", "Seleccione el registro a eliminar")

    #actualiza la tabla con un select
    def refrescar_tabla(self, tree, tabla_obj):
        tree.delete(*tree.get_children())
        for row in tabla_obj:
            tree.insert('', 'end', values=row)

    #valida si el algun input esta vacio
    def isEmpty(self, formulario):
        for entry in formulario:
            value = entry.get()
            if not value or value.isspace():
                return True  
        return False  

    def limpiar_entradas(self, entry_list):
        for entry in entry_list:
            entry.delete(0, tk.END)
