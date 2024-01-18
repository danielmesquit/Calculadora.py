from tkinter import *
from tkinter import messagebox

def clicou() -> None:
    # Como pegar o que foi digitado nos campos?
    nome = txtNome.get()
    salario = float(txtSalario.get())

    # Como criar uma messagebox(caixa de alerta)
    messagebox.showwarning("Clicou",f"{nome} clicou no botão!\n"
                                    f"Salário: R${salario}")

# Como criar uma janela?
janela = Tk()   # cria janelas

# Alterar o tamanho e posicionamento
janela.geometry("400x300+1200+300") # alturaxlargura+eixo X+eixo Y em px

# Titulo da janela
janela.title("Hello world")

# #----------------------- Componentes ----------------------#
# 1- informar onde será adicionado
# 2- parametros
# 3- forma de indexar: 3 opções (pack, place ou grid)

# Criando um label
labelNome = Label(janela, text="Nome:", font="Tahoma 16", fg="navy")
lblSalario = Label(janela, text="Salário:", font="Arial 14", fg="#3D1108")

#Como adicionar com pack, place ou grid
# labelNome.pack()
# labelNome.place(x=150,y=150)
labelNome.grid(row=0,column=0, sticky= W)
lblSalario.grid(row=1, column=0)

# Criando uma caixa de texto
txtNome = Entry(janela, font="Tahoma 16", width=15)
txtNome.grid(row=0,column=1)

txtSalario = Entry(janela, font="Arial 14", width=15)
txtSalario.grid(row=1,column=1)

# Criando um botão
btnEnviar = Button(janela, text="Enviar",font="Tahoma 8",bg="red", fg="white",
                   width=6, command= clicou)
btnEnviar.grid(row=2,column=1)




# Como rodar o programa no S.O.
janela.mainloop() # deve ser sempre a última

