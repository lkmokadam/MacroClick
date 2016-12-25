import tkinter as tk
from tkinter import ttk

from conf_importer import *

top = tk.Tk()
top.style = ttk.Style()
top.style.theme_use("classic")
f = conf_importer()
f.create_gui(top)
top.mainloop()
