from tkinter import *
from tkinter import messagebox
from tkinter import font

def adicionar_tarefa():
    global afazeres
    afazeres = tarefa.get()
    if afazeres.strip() == "":
        messagebox.showerror("Erro","Digite um afazer")
    else: 
        check_var = IntVar()
        check = Checkbutton(janela, text=afazeres, variable=check_var)#command=atualizar_checklist)
        check.pack()
        variavel_checks.append((check, check_var))
        tarefa.delete(0, END)
    
variavel_checks = []    

janela =Tk()

tarefa = Entry(janela, width=30)
tarefa.pack(pady=10)

botao = Button(janela, text="+", command=adicionar_tarefa)
botao.pack()

janela.mainloop()