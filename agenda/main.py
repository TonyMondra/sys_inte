from citas_class import Citas
from clientes_class import Clientes
from sql_class import Consultas
import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.geometry("1000x700")

    sq = Consultas()
    t_clientes = sq.table_clientes
    t_citas = sq.table_citas
    select_clientes = sq.select(t_clientes)
    select_citas = sq.select(t_citas)
    

    notebook = ttk.Notebook(root)

    Clientes(notebook, select_clientes)
    Citas(notebook, select_citas)

    notebook.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()
