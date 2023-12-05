import tkinter as tk
from tkinter import ttk
from sql_class import Consultas
from tkinter import messagebox
from tkcalendar import DateEntry

class Citas:
    def __init__(self, notebook, select_citas):
        self.sqls = Consultas()
        self.table = None
        self.citas_frame = None
        self.form_insert = []
        self.form_edit = []
        self.fecha_edit = None
        self.fecha_insert = None
        self.encabezados = ["Fecha", "Hora", "Motivo", "Persona"]
        self.lista_citas = select_citas
        self.crear_seccion_citas(notebook)

    

    def crear_formulario(self, panel, labels):
        frame_formulario = ttk.Frame(panel)
        frame_formulario.pack(padx=20, pady=20)

        for i, label_text in enumerate(labels):
            label = tk.Label(frame_formulario, text=label_text + ":")
            label.grid(row=i, column=0)

            if i == 0: 
                self.fecha_edit = DateEntry(frame_formulario, selectmode='day', date_pattern='yyyy-mm-dd')
                self.fecha_edit.grid(row=i, column=1)
                self.form_insert.append(self.fecha_edit.get_date()) 
            else:
                entry = tk.Entry(frame_formulario)
                entry.grid(row=i, column=1)
                self.form_insert.append(entry)

        boton_formulario = tk.Button(frame_formulario, text="Agregar", command=self.insertar_cita)
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

        boton2_tabla = tk.Button(frame_botones_tabla, text="Eliminar", width=40, command=self.del_cita)
        boton2_tabla.pack(side=tk.LEFT, padx=10, pady=10)

    def crear_seccion_citas(self, notebook):
        self.citas_frame = ttk.Frame(notebook)
        notebook.add(self.citas_frame, text="Citas")

        self.crear_formulario(self.citas_frame, self.encabezados)
        self.crear_tabla(self.citas_frame, self.encabezados, self.lista_citas)

    def abrir_ventana_edicion(self):
        selected_item = self.table.focus()
        if selected_item:
            values = self.table.item(selected_item, 'values')
            self.crear_form_edit(values)
        else:
            messagebox.showinfo("Mensaje", "Seleccione un registro para editar")

    def crear_form_edit(self, values):
        self.form_edit.clear()
        edit_window = tk.Toplevel()
        edit_window.title("Editar cliente")

        frame_editar = ttk.Frame(edit_window)
        frame_editar.pack(padx=20, pady=20)

        for i, label_text in enumerate(self.encabezados):
            label = tk.Label(frame_editar, text=label_text + ":")
            label.grid(row=i, column=0)

            if i == 0:  # Check if it's the first entry
                self.fecha_edit = DateEntry(frame_editar,date_pattern='yyyy-mm-dd' )
                self.fecha_edit.set_date(values[0])
                self.fecha_edit.grid(row=i, column=1)
                #self.fecha_edit.insert(tk.END, values[i])
                self.form_edit.append(self.fecha_edit.get_date()) 
            else:
                entry = tk.Entry(frame_editar)
                entry.grid(row=i, column=1)
                entry.insert(tk.END, values[i]) 
                self.form_edit.append(entry)


        boton_actualizar = tk.Button(frame_editar, text="Actualizar", command=self.actualizar_cita)
        boton_actualizar.grid(row=len(self.encabezados) + 1, columnspan=2, padx=10, pady=10)


#inserta un nuevo registro en la tabla
    def insertar_cita(self):
        values = []
        for i, entry in enumerate(self.form_insert):
            if i == 0:
                value = self.fecha_edit.get_date()
                values.append(value)
            else:
                value = entry.get()
                value = value.strip()
                values.append(value)

        if self.isEmpty(self.form_insert):
            messagebox.showinfo("Mensaje", "No puede haber campos vacios")
        else:
            if self.sqls.registroExistente(self.sqls.table_citas, self.sqls.cita_cond, values[3] ):
                messagebox.showinfo("Importante", "registro existente!")
            else: 
                self.sqls.insertar(self.sqls.table_citas, self.sqls.cita_cols, values)
                self.refrescar_tabla(self.table, self.sqls.select(self.sqls.table_citas))
                messagebox.showinfo("Mensaje", "registro agregado!")
                self.limpiar_entradas(self.form_insert)


    def actualizar_cita(self):
        new_values = []
        for i, entry in enumerate(self.form_edit):
            if i == 0:
                value = self.fecha_edit.get_date()
                new_values.append(value)
            else:
                value = entry.get()
                value = value.strip()
                new_values.append(value)

        if self.sqls.registroExistente(self.sqls.table_citas, self.sqls.cita_cond, new_values[3]):
            if self.isEmpty(self.form_edit):
                messagebox.showinfo("Mensaje", "No puede haber campos vacios")
            else:
                self.sqls.update(self.sqls.table_citas, self.sqls.cita_cols, new_values, self.sqls.cita_cond, new_values[3])
                self.refrescar_tabla(self.table, self.sqls.select(self.sqls.table_citas))
                messagebox.showinfo("Mensaje", "Registro Actualizado!")
        else: messagebox.showinfo("Error", "Cita no encontrada en el sistema!") 

    def del_cita(self):
            selected_item = self.table.focus()
            if selected_item:
                values = self.table.item(selected_item, 'values')
                celda = values[3]
                self.sqls.eliminar(self.sqls.table_citas, self.sqls.cita_cond, celda)
                self.refrescar_tabla(self.table, self.sqls.select(self.sqls.table_citas))
                messagebox.showinfo("Mensaje", "Registro eliminado")
            else: messagebox.showinfo("Mensaje", "Seleccione el registro a eliminar")



    #actualiza la tabla con un select
    def refrescar_tabla(self, tree, tabla_retornada):
        tree.delete(*tree.get_children())
        for row in tabla_retornada:
            tree.insert('', 'end', values=row)

    def isEmpty(self, formulario):
        for i, entry in enumerate(formulario):
            if i == 0:
                pass
            else:
                value = entry.get()
                if not value or value.isspace():
                    return True  
        return False  

    def limpiar_entradas(self, entry_list):
        for i, entry in enumerate (entry_list):
            if i == 0:
                pass
            else:
                entry.delete(0, tk.END)