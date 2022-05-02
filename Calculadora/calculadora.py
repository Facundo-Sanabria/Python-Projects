import tkinter as tk
class Calculadora:
    def __init__(self):
        self.calcu = tk.Tk()
        self.calcu.title("Calculadora")
        self.calcu.config(bg="#252536")
        self.calcu.geometry("260x460")
        self.calcu.resizable(0,0)

        self.text = tk.StringVar()
        self.text.set("")
        self.espacio = tk.Label(self.calcu, bg="#252536", textvariable=self.text, width= 30,justify="right",fg="white")
        self.espacio.grid(column=0,row=0)
        self.num = tk.StringVar()
        self.display = tk.Entry(self.calcu, width= 14 ,textvariable = self.num)
        self.display.config(justify="right",bg="#252536", bd="0", fg="white", font=("Poppins", 25))
        self.display.grid(column=0,row=1)
        self.espacio2 = tk.Label(self.calcu, bg="#252536", text="", width= 30)
        self.espacio2.grid(column=0,row=2)

        self.botones = tk.Frame(self.calcu, height=450, width=340, bg="#262637")
        self.botones.grid(column=0,row=3)
        
        self.porcentaje = tk.Button(self.botones, text="%",height=2, width= 5,command=self.porcentajef)
        self.porcentaje.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.porcentaje.grid(column=0,row=0, padx=2, pady=2)
        self.ce = tk.Button(self.botones, text="CE",height=2, width= 5, command=self.cef)
        self.ce.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.ce.grid(column=1,row=0, padx=2, pady=2)
        self.c = tk.Button(self.botones, text="C",height=2, width= 5,command=self.cf)
        self.c.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.c.grid(column=2,row=0, padx=2, pady=2)
        self.borrarulti = tk.Button(self.botones, text="<<<",height=2, width= 5)
        self.borrarulti.config(bg="#1A1A26", font=("Time New Roman", 15), fg="white", bd="0",command=self.buf)
        self.borrarulti.grid(column=3,row=0, padx=2, pady=2)

        self.fraccion = tk.Button(self.botones, text="1/x",height=2, width= 5,command=self.fraf)
        self.fraccion.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.fraccion.grid(column=0,row=1, padx=2, pady=2)
        self.cuadrado = tk.Button(self.botones, text="x^2",height=2, width= 5,command=self.cuadradof)
        self.cuadrado.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.cuadrado.grid(column=1,row=1, padx=2, pady=2)
        self.raiz = tk.Button(self.botones, text="Raiz",height=2, width= 5,command=self.raizf)
        self.raiz.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.raiz.grid(column=2,row=1, padx=2, pady=2)
        self.division = tk.Button(self.botones, text="/",height=2, width= 5,command=self.divisionf)
        self.division.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.division.grid(column=3,row=1, padx=2, pady=2)

        self.n7 = tk.Button(self.botones, text="7",height=2, width= 5,command=self.n7f)
        self.n7.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n7.grid(column=0,row=2, padx=2, pady=2)
        self.n8 = tk.Button(self.botones, text="8",height=2, width= 5,command=self.n8f)
        self.n8.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n8.grid(column=1,row=2, padx=2, pady=2)
        self.n9 = tk.Button(self.botones, text="9",height=2, width= 5,command=self.n9f)
        self.n9.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n9.grid(column=2,row=2, padx=2, pady=2)
        self.x = tk.Button(self.botones, text="x",height=2, width= 5,command=self.xf)
        self.x.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.x.grid(column=3,row=2, padx=2, pady=2)

        self.n4 = tk.Button(self.botones, text="4",height=2, width= 5,command=self.n4f)
        self.n4.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n4.grid(column=0,row=3, padx=2, pady=2)
        self.n5 = tk.Button(self.botones, text="5",height=2, width= 5,command=self.n5f)
        self.n5.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n5.grid(column=1,row=3, padx=2, pady=2)
        self.n6 = tk.Button(self.botones, text="6",height=2, width= 5,command=self.n6f)
        self.n6.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n6.grid(column=2,row=3, padx=2, pady=2)
        self.restas = tk.Button(self.botones, text="-",height=2, width= 5,command=self.restasf)
        self.restas.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.restas.grid(column=3,row=3, padx=2, pady=2)

        self.n1 = tk.Button(self.botones, text="1",height=2, width= 5,command=self.n1f)
        self.n1.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n1.grid(column=0,row=4, padx=2, pady=2)
        self.n2 = tk.Button(self.botones, text="2",height=2, width= 5,command=self.n2f)
        self.n2.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n2.grid(column=1,row=4, padx=2, pady=2)
        self.n3 = tk.Button(self.botones, text="3",height=2, width= 5,command=self.n3f)
        self.n3.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n3.grid(column=2,row=4, padx=2, pady=2)
        self.sumas = tk.Button(self.botones, text="+",height=2, width= 5,command=self.sumasf)
        self.sumas.config(bg="#1A1A26", font=("Poppins", 15), fg="white", bd="0")
        self.sumas.grid(column=3,row=4, padx=2, pady=2)

        self.signo = tk.Button(self.botones, text="+/-",height=2, width= 5,command=self.signof)
        self.signo.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.signo.grid(column=0,row=5, padx=2, pady=2)
        self.n0 = tk.Button(self.botones, text="0",height=2, width= 5,command=self.n0f)
        self.n0.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.n0.grid(column=1,row=5, padx=2, pady=2)
        self.punto = tk.Button(self.botones, text=".",height=2, width= 5,command=self.puntof)
        self.punto.config(bg="#0E0E14", font=("Poppins", 15), fg="white", bd="0")
        self.punto.grid(column=2,row=5, padx=2, pady=2)
        self.igual = tk.Button(self.botones, text="=",height=2, width= 5,command=self.igualf)
        self.igual.config(bg="#175B90", font=("Poppins", 15), fg="white", bd="0")
        self.igual.grid(column=3,row=5, padx=2, pady=2)

        self.calcu.mainloop()
    def porcentajef(self):
        dato = float(self.num.get())
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,str(dato/100))
    def cef(self):
        dato = len(self.num.get())
        self.display.delete(0,(dato))
    def cf(self):
        self.text.set("")
        dato = len(self.num.get())
        self.display.delete(0,(dato))
    def buf(self):
        dato = len(self.num.get())
        if dato >= 1:
            self.display.delete(dato-1)
    def fraf(self):
        dato = float(self.num.get())
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,str(1/dato))
    def cuadradof(self):
        dato = float(self.num.get())
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,str(dato**2))
    def raizf(self):
        dato = float(self.num.get())
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,str(dato**(1/2)))
    def signof(self):
        dato = float(self.num.get())
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,str(dato*(-1)))
    def n0f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"0"))
    def n1f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"1"))
    def n2f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"2"))
    def n3f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"3"))
    def n4f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"4"))
    def n5f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"5"))
    def n6f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"6"))
    def n7f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"7"))
    def n8f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"8"))
    def n9f(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"9"))
    def puntof(self):
        dato = self.num.get()
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.display.insert(0,(dato+"."))
    def divisionf(self):
        dato = (self.num.get()) + "/"
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.text.set(dato)
    def xf(self):
        dato = (self.num.get()) + "*"
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.text.set(dato)
    def restasf(self):
        dato = (self.num.get()) + "-"
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.text.set(dato)
    def sumasf(self):
        dato = (self.num.get()) + "+"
        dato2 = len(self.num.get())
        self.display.delete(0,dato2)
        self.text.set(dato)
    def igualf(self):
        nom = self.text.get()
        nom += self.num.get()
        num1 = ""
        sig = None
        oper = None
        num2 = ""
        for n in range(len(nom)):
            if nom[n] == "/" or nom[n] == "*" or nom[n] == "+":
                sig=n
                oper = nom[n]
                break
            if nom[n] == "-" and n != 0:
                sig=n
                oper = nom[n]
                break           
            num1 += nom[n]        
        for n in range(sig+1,len(nom)):
            num2 += nom[n]
        if oper == "/":
            try:
                r = float(num1)/float(num2)
                dato2 = len(self.num.get())
                self.display.delete(0,dato2)
                self.text.set("")
                self.display.insert(0,str(r))
            except ZeroDivisionError:
                dato2 = len(self.num.get())
                self.display.delete(0,dato2)
                self.text.set("")
                self.display.insert(0,"Math Error")
        elif oper == "*":
            r = float(num1)*float(num2)
            dato2 = len(self.num.get())
            self.display.delete(0,dato2)
            self.text.set("")
            self.display.insert(0,str(r))
        elif oper == "+":
            r = float(num1)+float(num2)
            dato2 = len(self.num.get())
            self.display.delete(0,dato2)
            self.text.set("")
            self.display.insert(0,str(r))
        elif oper == "-":
            r = float(num1)-float(num2)
            dato2 = len(self.num.get())
            self.display.delete(0,dato2)
            self.text.set("")
            self.display.insert(0,str(r))

cl = Calculadora()
