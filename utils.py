import json
from pathlib import Path


def extract_route(string):
    return string.split()[1][1:]

def read_file(path):
    with open(path, mode='rb') as file:
        conteudo = file.read()
    return conteudo


def load_data(arquivo):
    file_path = Path("data") / arquivo
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def load_template(nome):
    file_path = Path("templates") / nome
    with open(file_path, 'r') as file:
        conteudo1 = file.read()
    return conteudo1

def add_note(nova):
    notes_file = Path("data") / "notes.json"
    if notes_file.exists():
        with open(notes_file, 'r') as file:
            notes_data = json.load(file)
    else:
        notes_data = []

    notes_data.append(nova)

    with open(notes_file, 'w') as file:
        json.dump(notes_data, file)

def build_response(body='', code=200, reason='OK', headers=''):
    resposta = f'HTTP/1.1 {code} {reason}'
    if headers != '':
        resposta += f'\n{headers}'
    resposta += f'\n\n{body}'
    return resposta.encode()