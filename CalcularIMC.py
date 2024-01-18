from tkinter import *
from tkinter import messagebox


def clicou() -> None:
    try:
        peso = float(txtPeso.get())
    except:
        messagebox.showerror("Error","Digite o peso!")

    try:
        altura = float(txtAltura.get())
    except:
        messagebox.showerror("Error","Digite a altura!")

    imc = peso/altura**2
    messagebox.showinfo("IMC",f"Peso: {peso}\n"
                                            f"Altura; {altura}\n"
                                            f"IMC: {round(imc,1)}")

janela = Tk()
janela.geometry("300x100+600+100")
janela.title("Calculadora de IMC")
janela.iconbitmap("Calculator_30001.ico")

lbPeso = Label(janela,text="Peso:",font="Times 12")
lbPeso.grid(row=0,column=0,sticky=W)

txtPeso = Entry(janela,font="Times 10", fg= "#0D7A49")
txtPeso.grid(row=0,column=1)

lbAltura = Label(janela, text="Altura:",font="Times 12")
lbAltura.grid(row=1,column=0,sticky=W)

txtAltura = Entry(janela, font="Times 10", fg="#0D7A49")
txtAltura.grid(row=1,column=1)

btnCalcular = Button(janela, text="Calcular IMC",bg="#0D7A49",
                     fg="white",command= clicou)
btnCalcular.grid(row=2,column=1)



janela.mainloop()