import os
import tkinter as tk
from tkinter import ttk

import ui.conf_importer

top = tk.Tk()
top.style = ttk.Style()
top.style.theme_use("classic")
root_path = os.path.dirname(os.path.abspath(__file__))
f = ui.conf_importer.conf_importer_win_local("/conf/macro_click.conf", root_path)
f.create_gui(top)
top.mainloop()
