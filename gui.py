import tkinter as tk
import tkinter.ttk as ttk


def initialize():
    top = tk.Tk()
    nb = ttk.Notebook(top)
    nb.grid(row=0, column=0)
    return top, nb


def get_button(parent, text, col, row, command, bg="white", fg="black", ):
    btn = tk.Button(parent, text=text, command=command, bg=bg, fg=fg, padx=5, pady=5, width=20)
    btn.grid(row=row, column=col, padx=20, pady=3)
    return btn


def get_textarea(parent, text, col, row):
    txt = tk.Text(parent, padx=1, pady=1, width=20, height=2)
    txt.grid(row=row, column=col, padx=20, pady=3)
    return txt


def create_tabs(parent, tabs_list_with_frame):
    # tabs_list_with_frame should contain list of dict contain tab name and frame
    frames_list = []
    nb = ttk.Notebook(parent)
    nb.grid(row=0, column=0)
    for element in tabs_list_with_frame:
        frame = tk.Frame()
        nb.add(frame, text=element)
        frames_list.append(frame)
    return frames_list


def add_tab(notebook, tab_name):
    nb = notebook
    frame = tk.Frame()
    nb.add(frame, text=tab_name)
    return frame


def add_frame(tab, frame_name, column):
    frame = tk.Frame(tab)
    frame.grid(row=0, column=column)
    return frame
