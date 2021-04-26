from tkinter import *

class Ventana(Frame):
    
    def __init__(self,parent = None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.init_window()
    
    def init_window(self):
        self.parent.title("Calculadora Básica")
        label = Label(self.parent,text= "       ",bg="white")
        label.pack()
        var1 = StringVar()
        entrada= Entry(root,width=90,textvariable=var1)
        entrada.pack()

        def executor():
            print("kkota")

        def nueve():
            entrada.insert(END,"9")
        
        def ocho():
            entrada.insert(END,"8")

        def siete():
            entrada.insert(END,"7")
            
        def seis():
            entrada.insert(END,"6")
            
        def cinco():
            entrada.insert(END,"5")
            
        def cuatro():
            entrada.insert(END,"4")
        
        def tres():
            entrada.insert(END,"3")

        def dos():
            entrada.insert(END,"2")

        def uno():
            entrada.insert(END,"1")
       
        def cero():
            entrada.insert(END,"0")
       
        def punto():
            entrada.insert(END,".")
        
        boton7 = Button(root,text="7",command = siete,width=5,height=2,bg="#222825",fg="white")
        boton7.place(x=25,y=50)

        boton8 = Button(root,text="8",command = ocho,width=5,height=2,bg="#222825",fg="white")
        boton8.place(x=125,y=50)

        boton9 = Button(root,text="9",command = nueve,width=5,height=2,bg="#222825",fg="white")
        boton9.place(x=225,y=50)

        boton4 = Button(root,text="4",command = cuatro,width=5,height=2,bg="#222825",fg="white")
        boton4.place(x=25,y=110)
        
        boton5 = Button(root,text="5",command = cinco,width=5,height=2,bg="#222825",fg="white")
        boton5.place(x=125,y=110)
        
        boton6 = Button(root,text="6",command = seis,width=5,height=2,bg="#222825",fg="white")
        boton6.place(x=225,y=110)

        boton1 = Button(root,text="1",command = uno,width=5,height=2,bg="#222825",fg="white")
        boton1.place(x=25,y=170)
        
        boton2 = Button(root,text="2",command = dos,width=5,height=2,bg="#222825",fg="white")
        boton2.place(x=125,y=170)
        
        boton3 = Button(root,text="3",command = tres,width=5,height=2,bg="#222825",fg="white")
        boton3.place(x=225,y=170)
        
        boton0 = Button(root,text="0",command = cero,width=5,height=2,bg="#222825",fg="white")
        boton0.place(x=25,y=230)
        
        botonpto = Button(root,text=".",command = punto,width=5,height=2,bg="#222825",fg="white")
        botonpto.place(x=125,y=230)
      
        def suma():
            entrada.insert(END,"+")
        
        def resta():
            entrada.insert(END,"-")
       
        def multiplicacion():
            entrada.insert(END, "*")
           
        def division():
            entrada.insert(END,"/")

        def igual():
            resultado = eval( var1.get())
            entrada.delete(0,END)
            entrada.insert(0,resultado)
        def borrar():
            tam=len(entrada.get())
            entrada.delete(tam-1)
       
        def parentesis1():
            entrada.insert(END,"(")

        def parentesis2():
            entrada.insert(END,")")
        
        def borrartodo():
            entrada.delete(0,END)

        botonigual = Button(root,text="=",command = igual,width=5,height=2,bg="#ef974a",fg="white")
        botonigual.place(x=225,y=230)

        botondiv = Button(root,text="/",command = division,width=5,height=2,bg="#ce4a53",fg="white")
        botondiv.place(x=325,y=50)

        botonmult = Button(root,text="*",command = multiplicacion,width=5,height=2,bg="#ce4a53",fg="white")
        botonmult.place(x=325,y=110)
        
        botonmenos = Button(root,text="-",command = resta,width=5,height=2,bg="#ce4a53",fg="white")
        botonmenos.place(x=325,y=170)
        
        botonmas = Button(root,text="+",command = suma,width=5,height=2,bg="#ce4a53",fg="white")
        botonmas.place(x=325,y=230)

        botondel = Button(root,text="<-",command=borrar,width=5,height=2,bg="#222825",fg="white")
        botondel.place(x=425,y=50)
        
        botonpar1= Button(root,text="(",command=parentesis1,width=5,height=2,bg="#222825",fg="white")
        botonpar1.place(x=425,y=110)

        botonpar2= Button(root,text=")",command=parentesis2,width=5,height=2,bg="#222825",fg="white")
        botonpar2.place(x=425,y=170)

        botonlimpiar= Button(root,text="C",command = borrartodo,width=5,height=2,bg="#222825",fg="white")
        botonlimpiar.place(x=425,y=230)




if __name__ == "__main__":
    root = Tk()
    root.geometry("520x300")
    root.configure(bg="white")
    app = Ventana(parent = root)
    root.iconphoto(False,PhotoImage(file='calculator.png'))
    app.mainloop()
