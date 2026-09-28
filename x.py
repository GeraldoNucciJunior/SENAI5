import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos.")


# Janela principal
janela = tk.Tk()
janela.title("Somar Números puxa vida")
janela.geometry("500x600")
janela.resizable(False, False)

# Campo 1
tk.Label(janela, text="Número 1:").pack(pady=(15, 0))
entrada1 = tk.Entry(janela)
entrada1.pack()

# Campo 2
tk.Label(janela, text="Número 2:").pack(pady=(10, 0))
entrada2 = tk.Entry(janela)
entrada2.pack()

# Botão OK
botao = tk.Button(janela, text="OK", command=calcular)
botao.pack(pady=15)

# Resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

janela.mainloop()