from tkinter import *
from tkinter import ttk

import z_test
import t_test

window = Tk()
window.title('Statistical Calculator')
window.geometry('900x600')

tabs = ttk.Notebook(window)
tabs.grid(column=0, row=0)

z_tab = z_test.create_tab(tabs)
tabs.add(z_tab, text = 'Z-test')

t_tab = t_test.create_tab(tabs)
tabs.add(t_tab, text = 'T-test')


tabs.columnconfigure([i for i in range(1,50)], weight=1, uniform='')
tabs.rowconfigure([i for i in range(1,50)], weight=1, uniform='')
window.mainloop()