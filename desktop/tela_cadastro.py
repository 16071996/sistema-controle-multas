import tkinter as tk
from tkinter import messagebox


def abrir_tela_cadastro(janela_pai):
    # Janela filha
    cadastro = tk.Toplevel(janela_pai)
    cadastro.title("Cadastro de Multa")
    cadastro.geometry("400x350")
    cadastro.resizable(False, False)

    # Título
    tk.Label(
        cadastro,
        text="Cadastro de Multa",
        font=("Arial", 14, "bold")
    ).pack(pady=15)

    # Campo Placa
    tk.Label(cadastro, text="Placa do veículo:").pack(anchor="w", padx=20)
    entry_placa = tk.Entry(cadastro)
    entry_placa.pack(fill="x", padx=20, pady=5)

    # Campo Data
    tk.Label(cadastro, text="Data da multa:").pack(anchor="w", padx=20)
    entry_data = tk.Entry(cadastro)
    entry_data.pack(fill="x", padx=20, pady=5)

    # Campo Valor
    tk.Label(cadastro, text="Valor da multa (R$):").pack(anchor="w", padx=20)
    entry_valor = tk.Entry(cadastro)
    entry_valor.pack(fill="x", padx=20, pady=5)

    # Campo Descrição
    tk.Label(cadastro, text="Descrição:").pack(anchor="w", padx=20)
    entry_descricao = tk.Entry(cadastro)
    entry_descricao.pack(fill="x", padx=20, pady=5)

    # Função salvar (temporária)
    def salvar_multa():
        messagebox.showinfo(
            "Teste",
            "Tela de cadastro criada com sucesso!"
        )

    # Botão salvar
    tk.Button(
        cadastro,
        text="Salvar Multa",
        command=salvar_multa
    ).pack(pady=20)

