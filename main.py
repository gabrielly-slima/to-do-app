import tkinter as tk
from data_utils import convert_date_to_pt

janela = tk.Tk()
janela.title("To do list")
janela.geometry("300x500")

rotulo = tk.Label(janela, text= convert_date_to_pt(), font= ("Segoe UI Semibold", 15), )
rotulo.pack()

janela.mainloop()