__author__ = "Axel Aviloff"

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from math import factorial
from datetime import date

def labelHover1(event):
    statusLabel.config(text = "Entre com a quantidade de tentativas")


def labelHoverLeave1(event):
    statusLabel.config(text = d)


def labelHover2(event):
    statusLabel.config(text = "Entre com a quantidade de sucessos")


def labelHoverLeave2(event):
    statusLabel.config(text = d)

def labelHover3(event):
    statusLabel.config(text = "Entre com a probabilidade de sucesso [0%, 100%]")

def labelHoverLeave3(event):
    statusLabel.config(text = d)

def comboHover1(event):
    statusLabel.config(text = "Escolha um valor ou intervalo de x")

def comboHoverLeave1(event):
    statusLabel.config(text = d)

def removePct(event):
    if entry_C.get() == "%":
        entry_C.delete(0, END)


def howToUse():
    #Criando e configurando janela segundária
    newWindow = Toplevel()
    newWindow.resizable(False, False)
    newWindow.geometry('350x200')
    newWindow.configure(background="white")

    #Criando e configurando os widgets
    label_title = Label(newWindow, text = "FÓRMULA DE DISTRIBUIÇÃO BINOMIAL", fg="red", background = "white", font=("comic-sans", 10, 'bold'))
    label_formula = Label(newWindow, text = 'P(x = ₓ) = Cₙ,ₓpˣ(p-1)ⁿ⁻ˣ', fg="black", background = "white", font=("arial", 20, 'bold'))
    lbl_A = Label(newWindow, text = 'P(x = ₓ): Probabilidade de x sucessos em n ensáios', background = "white", fg="black", font=("helvetica", 10, 'bold'))
    lbl_B = Label(newWindow, text = 'Cₙ,ₓ: Combinação de n valores tomados x a x', fg="black", background = "white", font=("helvetica", 10, 'bold'))
    lbl_C = Label(newWindow, text = 'p: Probabilidade de sucesso em cada ensáio', fg="black", background = "white", font=("helvetica", 10, 'bold'))
    lbl_D = Label(newWindow, text = '1-p = q: Probabilidade de fracasso em cada ensáio', fg="black", background = "white", font=("helvetica", 10, 'bold'))
    button = Button(newWindow, text = "Entendido", command = newWindow.destroy)
    
    #Colocando os widgets na janela
    label_title.place(x = 10, y = 10)
    label_formula.place(x = 10, y = 30)
    lbl_A.place(x = 10, y = 70)
    lbl_B.place(x = 10, y = 90)
    lbl_C.place(x = 10, y = 110)
    lbl_D.place(x = 10, y = 130)
    button.place(x = 130, y = 160)
    
    newWindow.mainloop


def delEntries():
    entry_A.delete(0, END)
    entry_B.delete(0, END)
    entry_C.delete(0, END)


def isNumber(x):
    try:
        float(x)
        return True
    
    except:
        return False


def combination(n,p):
   return factorial(n) / (factorial(n-p) * factorial(p))


def calculateProbability(A, B, C, D):
    if A == '' or B == '' or C == '':
        messagebox.showerror("Entrada Inválida", "Entre com os 3 valores")
    
    elif D == '':
        messagebox.showerror("Entrada Inválida", "Selecione um intervalo de x")
    
    elif not(isNumber(A) and isNumber(B) and isNumber(C)):
        messagebox.showerror("Entrada Inválida", "Entre apenas com números")
    
    elif ('.' in A or '.' in B):
        messagebox.showerror("Entrada Inválida", "n e x precisam ser inteiros")
    
    elif ('-' in A or '-' in B or "-" in C):
        messagebox.showerror("Entrada Inválida", "Entre apenas com números positivos")

    elif int(A) < int(B):
        messagebox.showerror("Entrada Inválida", "x deve ser menor ou igual a n")
    
    else:
        A = int(A)
        B = int(B)
        C = float(C)
        somaProbabilidade = 0
        if (D == '='):
            comb = combination(A, B)
            p = (C/100) ** B
            q = (1-(C/100)) ** (A-B)
            probabilidade = comb * p * q
            probabilidade *= 100
            labelPct.config(text = '')
            labelPct.config(text = "P(x = " + str(B) + ") = " + str(round(probabilidade, 4))+ "%")
        elif (D == '>='):
            for i in range(B, A+1):
                comb = combination(A, i)
                p = (C/100) ** i
                q = (1-(C/100)) ** (A-i)
                probabilidade = comb * p * q
                probabilidade *= 100
                somaProbabilidade += probabilidade
            labelPct.config(text = '')
            labelPct.config(text = "P(x >= " + str(B) + ") = " + str(round(somaProbabilidade, 4))+ "%")
        else:
            for i in range(0, B+1):
                comb = combination(A, i)
                p = (C/100) ** i
                q = (1-(C/100)) ** (A-i)
                probabilidade = comb * p * q
                probabilidade *= 100
                somaProbabilidade += probabilidade
            labelPct.config(text = '')
            labelPct.config(text = "P(x <= " + str(B) + ") = " + str(round(somaProbabilidade, 4))+ "%")

        window.geometry('330x190'+'+'+ str(window.winfo_x()) + "+" + str(window.winfo_y()))
        labelPct.place(x = 2, y = 140)


def showResult():
    calculateProbability(entry_A.get(), entry_B.get(), entry_C.get(), comboX.get())

#Criando e configurando janela principal
window = Tk()
window.resizable(False, False)
window.geometry('330x160')
window.title("Fórmula Binomial - UFFS 2020")
window.configure(background="black")
window.option_add('*TCombobox*Listbox.selectForeground', 'red')

#Definindo ícone do programa
ico = Image.open('includes/icon.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

#Menu principal
myMenu = Menu(window)
window.config(menu = myMenu)
OptionMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label='Opções', menu=OptionMenu)
OptionMenu.add_command(label = "Como Funciona?", command=howToUse)
OptionMenu.add_command(label = "Sair", command=window.quit)

#Barra de status
today = date.today()
d = today.strftime("%B %d, %Y")
statusLabel = Label(window, text = d, bd = 1, relief = SUNKEN, anchor = W)
statusLabel.pack(fill=X, side=BOTTOM, ipady=1)

#Criando e configurando os widgets
labelPct = Label(window, fg = "red", text= "", font=("helvetica", 14, "bold"))
labelPct.configure(background="black")
lbl_A = Label(window, text = "N (número de tentativas)", fg="white", font=("comic-sans", 10))
lbl_A.configure(background="black")
lbl_B = Label(window, text = "X (número de sucessos)", fg="white", font=("comic-sans", 10))
lbl_B.configure(background="black")
lbl_C = Label(window, text = "P (Probabilidade de sucesso)", fg="white", font=("comic-sans", 10))
lbl_C.configure(background="black")
entry_A = Entry(window, width=4, justify = "center", fg = 'black', cursor = 'hand1')
entry_A.configure(background="white")
comboX = ttk.Combobox(window, width = 3, cursor = 'hand1', justify = "center",state="readonly", values = ["=", ">=", "<="])
comboX.selection_clear()
comboX.configure(background="white")
entry_B = Entry(window,width=4, justify = "center", fg = 'black', cursor = 'hand1')
entry_B.configure(background="white")   
entry_C = Entry(window,width=4, justify = "center", fg = 'black', cursor = 'hand1')
entry_C.configure(background="white")
calculate_btn = Button(text = "CALCULAR", command = showResult, font = ("comic-sans", 10, 'bold'), relief = 'solid', cursor = 'hand1')

#Colocando os widgets na janela principal
lbl_A.place(x = 2, y = 10)
lbl_A.bind("<Enter>", labelHover1)
lbl_A.bind("<Leave>", labelHoverLeave1)
entry_A.place(x = 200, y = 10)
lbl_B.place(x = 2, y = 40)
lbl_B.bind("<Enter>", labelHover2)
lbl_B.bind("<Leave>", labelHoverLeave2)
comboX.place(x = 200, y = 40)
comboX.bind("<Enter>", comboHover1)
comboX.bind("<Leave>", comboHoverLeave1)
entry_B.place(x = 250, y = 40)
lbl_C.place(x = 2, y = 70)
lbl_C.bind("<Enter>", labelHover3)
lbl_C.bind("<Leave>", labelHoverLeave3)
entry_C.place(x = 200, y = 70)
entry_C.insert(0, "%")
entry_C.bind("<Button-1>", removePct)
calculate_btn.place(x = 2, y = 100)

window.mainloop()
