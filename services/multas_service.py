import json
import os

CAMINHO_ARQUIVO = os.path.join("data", "multas.json")


def carregar_multas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_multas(multas):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(multas, arquivo, indent=4, ensure_ascii=False)


def cadastrar_multa(placa, data, valor, descricao):
    # -----------------------------
    # Validações básicas
    # -----------------------------
    if not placa or not data or not valor:
        raise ValueError("Placa, data e valor são obrigatórios.")

    # Padronização
    placa = placa.upper()

    # -----------------------------
    # Carrega multas existentes
    # -----------------------------
    multas = carregar_multas()

    # -----------------------------
    # Nova multa
    # -----------------------------
    nova_multa = {
        "placa": placa,
        "data": data,
        "valor": float(valor),
        "descricao": descricao
    }

    multas.append(nova_multa)

    # -----------------------------
    # Salva no arquivo
    # -----------------------------
    salvar_multas(multas)

    return nova_multa

