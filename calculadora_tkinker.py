import tkinter as tk

# Função para adicionar texto ao display
def adicionar_texto(texto):
    display.insert(tk.END, texto)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, resultado)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro")

# Função para limpar o display
def limpar():
    display.delete(0, tk.END)

# Configurando a janela principal
janela = tk.Tk()
janela.title("Calculadora Rosa")

# Cor de fundo rosa
janela.configure(bg='pink')

# Criando o display da calculadora
display = tk.Entry(janela, width=16, font=('Arial', 24), borderwidth=2, relief="solid", bg='white')
display.grid(row=0, column=0, columnspan=4, pady=10)

# Criando os botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), 
]

# Adicionando os botões na interface
for (texto, linha, coluna) in botoes:
    tk.Button(janela, text=texto, width=5, height=2, command=lambda t=texto: adicionar_texto(t), bg='lightpink').grid(row=linha, column=coluna, pady=5, padx=5)

# Botão de igual (=) para mostrar o resultado
tk.Button(janela, text='=', width=5, height=2, command=calcular, bg='deeppink').grid(row=4, column=3, pady=5, padx=5)

# Botão de limpar (C)
tk.Button(janela, text='C', width=5, height=2, command=limpar, bg='lightpink').grid(row=5, column=0, columnspan=4, pady=5, padx=5)

# Executando a interface gráfica
janela.mainloop()
