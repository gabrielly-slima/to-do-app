import tkinter as tk
from data_utils import convert_date_to_pt

janela = tk.Tk()
janela.title("To do list")
janela.geometry("300x500")
janela.configure(bg="#86d8ff")

rotulo = tk.Label(janela, text= convert_date_to_pt(), font= ("Segoe UI Emoji", 10), bg= "#86d8ff")
rotulo.pack()

text_to_do = tk.Label(janela, text="\nTo do list", font= ("Segoe UI Semibold", 12), bg="#86d8ff")
text_to_do.pack()



janela.mainloop()
