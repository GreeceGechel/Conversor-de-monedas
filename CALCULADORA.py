from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
root=Tk()

global resultado
def sum():
 global resultado
 resultado=(int(num1.get())+int(num2.get()))

def rest(): 
      global resultado
 
      resultado=(int(num1.get())-int(num2.get()))
def div():
    global resultado
 
    resultado=(int(num1.get())/int(num2.get()))
def mul():
         global resultado
         resultado=(int(num1.get())*int(num2.get()))

def desplegar():
      textoNumeroB.config(text=f'{resultado}')

def reiniciar():
      global e1
      global e2
      global num1
      global num2
      e1=Entry(ventanaPrin,textvariable="",font=("Roboto",10)).grid(row=11,column=3,padx=5,pady=5)
      e2=Entry(ventanaPrin,textvariable="",font=("Roboto",10)).grid(row=12,column=3,padx=5,pady=5)
      textoNumeroB.config(text=f'{0}')

      
    
      


ventanaPrin=Frame(root)

root.geometry("400x500")

ventanaPrin.grid(row=1,column=1)


#variables

num1=IntVar()
num2=IntVar()
resultado=StringVar()



titulo=Label(ventanaPrin,text="CALCULADORA",font=("Roboto",20)).grid(row=2,column=3,padx=5,pady=5)

numA=Label(ventanaPrin,text="Numero A ",font=("Roboto",10)).grid(row=11,column=2,padx=5,pady=5)
e1=Entry(ventanaPrin,textvariable=num1,font=("Roboto",15)).grid(row=11,column=3,padx=5,pady=5)

numB=Label(ventanaPrin,text="Numero B:",font=("Roboto",10)).grid(row=12,column=2,padx=5,pady=5)
e2=Entry(ventanaPrin,textvariable=num2,font=("Roboto",15)).grid(row=12,column=3,padx=5,pady=5)

titulo3=Label(ventanaPrin,text="Resultado",font=("Roboto",10)).grid(row=13,column=2,padx=5,pady=5)

textoNumeroB = Label(ventanaPrin, text="", font=("Roboto",15))
textoNumeroB.grid(row=13,column=3,padx=5,pady=5)


Suma=Button(ventanaPrin,text="Suma",command=sum)
Suma.grid(row=16,column=2,pady=1)

Resta=Button(ventanaPrin,text="Resta",command=rest)
Resta.grid(row=17,column=2,pady=1)

Mult=Button(ventanaPrin,text="Mult",command=mul)
Mult.grid(row=16,column=3,pady=1,padx=5)

Division=Button(ventanaPrin,text="Division",command=div)
Division.grid(row=17,column=3,pady=1)

c=Button(ventanaPrin,text="C",command=reiniciar)
c.grid(row=16,column=4,pady=1)

igual=Button(ventanaPrin,text="=",command=desplegar)
igual.grid(row=17,column=4,pady=1)


root.mainloop()
