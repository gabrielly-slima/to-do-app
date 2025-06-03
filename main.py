import tkinter as tk
from datetime import datetime
from data_utils import convert_date_to_pt

janela = tk.Tk()
janela.title("To do list")

rotulo = tk.Label(janela, text= convert_date_to_pt())
rotulo.pack()

janela.mainloop()