import tkinter as tk
import funcoes_calculadora as fc

valor_1 = 0
valor_2 = 0
resultado = 0
 
def calcular_operacao(operacao):

    valor_1 = float(entry_valor_1.get())
    valor_2 = float(entry_valor_2.get())

    match operacao:
        case "+":
            resultado = fc.adicao(valor_1, valor_2)           
        case "-":
            resultado = fc.subtracao(valor_1, valor_2)
        case "*":
            resultado = fc.multiplicacao(valor_1, valor_2)
        case "/":
            resultado = fc.divisao(valor_1, valor_2)

    entry_resultado.insert(0,resultado)

def zerar():

    entry_valor_1.delete(0, tk.END)       
    entry_valor_2.delete(0, tk.END)       
    entry_resultado.delete(0, tk.END)       
 
root = tk.Tk()
root.title("Calculadora")
root.geometry("450x550")

tk.Label(root, text="Valor 1:").grid(row=0, column=0, sticky="w", pady=10)
entry_valor_1 = tk.Entry(root, width=30)
entry_valor_1.grid(row=0, column=1, pady=5)
 
tk.Label(root, text="Valor 2:").grid(row=1, column=0, sticky="w", pady=10)
entry_valor_2 = tk.Entry(root, width=30)
entry_valor_2.grid(row=1, column=1, pady=5)

tk.Label(root, text="Resultado:").grid(row=2, column=0, sticky="w", pady=10)
entry_resultado = tk.Entry(root, width=30)
entry_resultado.grid(row=2, column=1, pady=5)

btn_salvar1 = tk.Button(root, text="+", width=4, height=2, command=lambda:(calcular_operacao("+")))
btn_salvar1.grid(row=3, column=0, padx=12, pady=(20, 10))

btn_salvar2 = tk.Button(root, text="-", width=4, height=2, command=lambda:(calcular_operacao("-")))
btn_salvar2.grid(row=3, column=1, padx=12, pady=(20, 10))

btn_salvar3 = tk.Button(root, text="*", width=4, height=2, command=lambda:(calcular_operacao("*")))
btn_salvar3.grid(row=4, column=0, padx=12, pady=10)

btn_salvar4 = tk.Button(root, text="/", width=4, height=2, command=lambda:(calcular_operacao("/")))
btn_salvar4.grid(row=4, column=1, padx=12, pady=10)

btn_zerar = tk.Button(root, text="C\nE", width=3, height=7, command=zerar)
btn_zerar.grid(row=3, column=2, rowspan=2, padx=12, pady=(20, 10))
 
root.mainloop()