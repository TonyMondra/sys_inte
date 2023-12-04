import tkinter as tk
from tkinter import ttk
from sql_class import Consultas

class Citas:
    def __init__(self, notebook, select_citas):
        self.select_citas = select_citas
        self.crear_seccion_citas(notebook)

    def refrescar_tabla(self, tree, tabla_obj):
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

        boton_formulario = tk.Button(frame_formulario, text="Enviar")
        boton_formulario.grid(row=len(labels) + 1, columnspan=2, padx=10, pady=10)

    def crear_tabla(self, panel, labels, t_fuente):
        frame_tabla = ttk.Frame(panel)
        frame_tabla.pack(padx=20, pady=20)

        table = ttk.Treeview(frame_tabla, columns=labels, show="headings")
        for label in labels:
            table.heading(label, text=label)
        table.pack()

        self.refrescar_tabla(table, t_fuente)

        frame_botones_tabla = ttk.Frame(frame_tabla)
        frame_botones_tabla.pack(padx=20, pady=20)

        boton1_tabla = tk.Button(frame_botones_tabla, text="Editar", width=40)
        boton1_tabla.pack(side=tk.LEFT, padx=10, pady=10)

        boton2_tabla = tk.Button(frame_botones_tabla, text="Eliminar", width=40)
        boton2_tabla.pack(side=tk.LEFT, padx=10, pady=10)

    def crear_seccion_citas(self, notebook):
        citas_frame = ttk.Frame(notebook)
        notebook.add(citas_frame, text="Citas")

        etiquetas_citas = ["Fecha", "Hora", "Motivo", "Persona"]
        self.crear_formulario(citas_frame, etiquetas_citas)
        self.crear_tabla(citas_frame, etiquetas_citas, self.select_citas)

        boton_citas = tk.Button(citas_frame, text="Citas", command=lambda: self.cambiar_seccion(notebook, "Citas"))
        boton_citas.pack()

    def cambiar_seccion(self, notebook, seccion):
        for index, tab in enumerate(notebook.tabs()):
            if notebook.tab(tab, "text") == seccion:
                notebook.select(index)


