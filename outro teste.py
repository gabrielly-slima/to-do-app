from tkinter import *

def atualizar_label():
    estado_check = check_var.get()
    if estado_check == 1:
        label_resultado.config(text="Checkbutton selecionado")
    else:
        label_resultado.config(text="Checkbutton deselecionado")

# Criando a janela principal
janela = Tk()
janela.title("Exemplo de Checkbutton")

# Variável IntVar para armazenar o estado do Checkbutton
check_var = IntVar()

# Criando o Checkbutton
checkbutton = Checkbutton(janela, text="Selecionar", variable=check_var, command=atualizar_label)
checkbutton.pack(pady=10)

# Rótulo para exibir o resultado
label_resultado = Label(janela, text="")
label_resultado.pack(pady=10)

# Iniciando o loop principal da aplicação
janela.mainloop()