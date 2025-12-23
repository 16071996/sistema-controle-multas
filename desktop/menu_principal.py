from desktop.tela_cadastro import abrir_tela_cadastro
import tkinter as tk
from tkinter import messagebox


def abrir_menu_principal():
    def chamar_cadastro():
        abrir_tela_cadastro(janela)
    # -----------------------------
    # Funções internas
    # -----------------------------
    def abrir_cadastro():
        print("Abrir tela de cadastro de multa")

    def abrir_gerenciamento():
        print("Abrir tela de gerenciamento de multas")

    def abrir_relatorio():
        print("Abrir tela de relatório de multas")

    def sair_sistema():
        janela.destroy()

    # -----------------------------
    # Janela principal
    # -----------------------------
    janela = tk.Tk()
    janela.title("Sistema de Controle de Multas")
    janela.geometry("400x300")
    janela.resizable(False, False)

    # -----------------------------
    # Título
    # -----------------------------
    titulo = tk.Label(
        janela,
        text="Sistema de Controle de Multas",
        font=("Arial", 14, "bold")
    )
    titulo.pack(pady=20)

    # -----------------------------
    # Botões
    # -----------------------------
    tk.Button(
        janela,
        text="Cadastrar Multa",
        width=25,
        command=chamar_cadastro
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Gerenciar Multas",
        width=25,
        command=abrir_gerenciamento
    ).pack(pady=5)

    tk.Button(
        janela,
        text="Relatório de Multas",
        width=25,
        command=abrir_relatorio
    ).pack(pady=5)

    tk.Button(
        janela,
        text="Sair",
        width=25,
        command=sair_sistema
    ).pack(pady=20)

    # -----------------------------
    # Loop da aplicação
    # -----------------------------
    janela.mainloop()

