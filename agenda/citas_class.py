import tkinter as tk
from tkinter import ttk
from sql_class import Consultas
from tkinter import messagebox

class Citas:
    def __init__(self, notebook, select_citas):
        self.sqls = Consultas()
        self.table = None
        self.citas_frame = None
        self.form_insert = []
        self.form_edit = []
        self.encabezados = ["Fecha", "Hora", "Motivo", "Persona"]
        self.lista_citas = select_citas
        self.crear_seccion_citas(notebook)

    

    def crear_formulario(self, panel, labels):
        frame_formulario = ttk.Frame(panel)
        frame_formulario.pack(padx=20, pady=20)

        for i, label_text in enumerate(labels):
            label = tk.Label(frame_formulario, text=label_text + ":")
            label.grid(row=i, column=0)
            entry = tk.Entry(frame_formulario)
            entry.grid(row=i, column=1)
            self.form_insert.append(entry)

        boton_formulario = tk.Button(frame_formulario, text="Enviar")
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

        boton2_tabla = tk.Button(frame_botones_tabla, text="Eliminar", width=40)
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

        boton_actualizar = tk.Button(frame_editar, text="Actualizar")
        boton_actualizar.grid(row=len(self.encabezados) + 1, columnspan=2, padx=10, pady=10)


    def refrescar_tabla(self, tree, tabla_obj):
            for row in tabla_obj:
                tree.insert('', 'end', values=row)