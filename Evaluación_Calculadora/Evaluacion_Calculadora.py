import tkinter as tk

class Calculadora:
    def init(self):
        self.valor1 = 0
        self.valor2 = 0

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 == 0:
            return "No se puede dividir por cero"
        return self.valor1 / self.valor2

def calcular(operacion):
    resultado = 0
    if operacion == "Suma":
        resultado = calculadora.suma()
    elif operacion == "Resta":
        resultado = calculadora.resta()
    elif operacion == "Multiplicación":
        resultado = calculadora.multiplicacion()
    elif operacion == "División":
        resultado = calculadora.division()
    resultado_label.config(text=f"Resultado: {resultado}")

def actualizar_valores():
    calculadora.valor1 = float(valor1_entry.get())
    calculadora.valor2 = float(valor2_entry.get())

app = tk.Tk()
app.title("Calculadora")

calculadora = Calculadora()

valor1_label = tk.Label(app, text="Valor 1:")
valor1_label.pack()

valor1_entry = tk.Entry(app)
valor1_entry.pack()

valor2_label = tk.Label(app, text="Valor 2:")
valor2_label.pack()

valor2_entry = tk.Entry(app)
valor2_entry.pack()

operaciones = ["Suma", "Resta", "Multiplicación", "División"]

for operacion in operaciones:
    tk.Button(app, text=operacion, command=lambda op=operacion: [actualizar_valores(), calcular(op)]).pack()

resultado_label = tk.Label(app, text="Resultado:")
resultado_label.pack()

app.mainloop()