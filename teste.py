from tkinter import *

# Função chamada quando o botão é clicado
def adicionar_tarefa():
    tarefa = Entry(janela, width=30)
    tarefa.pack(pady=10)
    listar_tarefas = tarefa.get()
    label = Label(janela, text=f"{listar_tarefas}")
    label.pack()

janela = Tk()

# Criação da janela principal

# Criação de um botão
botao = Button(janela, text="+", command=adicionar_tarefa)
botao.pack()

# Inicia o loop principal da aplicação
janela.mainloop()