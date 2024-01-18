from tkinter import *
from tkinter import messagebox

def limparDisplay() -> None:
    display.delete(0,END) #END = len(display.get()-1)

def inserir(valor: str) -> None:
    display.insert(END,valor) #posição, valor

def calcular() -> None:
    textoDisplay = display.get()
    resultado = eval(textoDisplay)
    limparDisplay()
    inserir(resultado)


janela = Tk()
janela.title("Calculadora")
janela.iconbitmap("Calculator_30001.ico")

gray = "#333333"
green = "#03331c"
orange = "#FF9500"

display =Entry(janela, bg=green,fg="white",font="Tahoma 18", width=21)
display.pack()

# Frame: container, semelhante à div do HTML
frame = Frame(janela)
frame.pack()


#Botões
btn0 = Button(frame,text="0",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6, command= lambda:inserir("0"))
btn0.grid(row=3,column=1)

btn1 = Button(frame,text="1",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("1"))
btn1.grid(row=2,column=0)

btn2 = Button(frame,text="2",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("2"))
btn2.grid(row=2,column=1)

btn3 = Button(frame,text="3",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("3"))
btn3.grid(row=2,column=2)

btn4 = Button(frame,text="4",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("4"))
btn4.grid(row=1,column=0)

btn5 = Button(frame,text="5",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("5"))
btn5.grid(row=1,column=1)

btn6 = Button(frame,text="6",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("6"))
btn6.grid(row=1,column=2)

btn7 = Button(frame,text="7",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("7"))
btn7.grid(row=0,column=0)

btn8 = Button(frame,text="8",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("8"))
btn8.grid(row=0,column=1)

btn9 = Button(frame,text="9",font="Tahoma 12 bold",bg=gray,fg="white",
              height=3,width=6,command=lambda:inserir("9"))
btn9.grid(row=0,column=2)

btnSomar = Button(frame,text="+",font="Tahoma 12 bold",bg=orange,fg="white",
                  height=3,width=6,command=lambda:inserir("+"))
btnSomar.grid(row=0,column=3)

btnSubtrair = Button(frame,text="-",font="Tahoma 12 bold",bg=orange,fg="white",
                     height=3,width=6,command=lambda:inserir("-"))
btnSubtrair.grid(row=1,column=3)

btnMultiplicar = Button(frame,text="x",font="Tahoma 12 bold",bg=orange,fg="white",
                        height=3,width=6,command=lambda:inserir("*"))
btnMultiplicar.grid(row=2,column=3)

btnDividir = Button(frame,text="/",font="Tahoma 12 bold",bg=orange,fg="white",
                    height=3,width=6,command=lambda:inserir("/"))
btnDividir.grid(row=3,column=3)

# btnPonto = Button(frame,text=".",font="Tahoma 12 bold",bg=orange,fg="white",height=3,width=6)
# btnPonto.grid(row=3,column=0)

btnIgual = Button(frame,text="=",font="Tahoma 12 bold",bg=orange,fg="white",
                  height=3,width=6, command=calcular)
btnIgual.grid(row=3,column=2)

btnApagar = Button(frame,text="CE",font="Tahoma 12 bold",bg=orange,fg="white",
                   height=3,width=6, command= limparDisplay)
btnApagar.grid(row=3,column=0)





janela.mainloop()