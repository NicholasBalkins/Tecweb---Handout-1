from utils import load_data, load_template, add_note, build_response

def index(request):
    # Carrega a lista de notas do arquivo JSON e gera o HTML correspondente
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    # Verifica se a requisição é POST
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        partes = request.split('\n\n')  # Separa cabeçalho e corpo da requisição
        corpo = partes[1]
        params = {}
        # Preenche o dicionário params com as informações do corpo da requisição
        for chave_valor in corpo.split('&'):
            adicionar = chave_valor.replace('+'," ")
            adicionar = adicionar.split("=")
            params[adicionar[0]] = adicionar[1]
        add_note(params)
        # Retorna uma resposta de redirecionamento com código 303 e cabeçalho 'Location: /'
        return build_response(code=303, reason='See Other', headers='Location: /')

    # Se não for uma requisição POST, retorna a página inicial normalmente
    return build_response(body=load_template('index.html').format(notes=notes))

