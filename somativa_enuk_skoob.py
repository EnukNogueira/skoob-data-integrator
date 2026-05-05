from datetime import datetime
import json
import os

"""Projeto de Somativa 2 da PUCPR, foi utilizado a base da somativa 1, formativa 4,5,6 e cursos da ALURA para criar esse código. 
Antes ele criava um projeto porem como eu gosto batante de ler resolvi mudar para livros. 
Inspiração para o projeto: App skoob."""

def converter_para_bool(valor):
    return valor.strip().lower() in ("s", "sim", "true", "1", "t", "y", "yes")

def carregar_portfolio(nome_arquivo="biblioteca.json"):
    """Carrega a lista de livros de um arquivo do JSON."""
    try:
        if not os.path.exists(nome_arquivo):
            print("Primeira vez aqui! Criando sua biblioteca...")
            return []
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            if not isinstance(dados, list):
                print("AVISO: formato do JSON inválido. Iniciando com a biblioteca vazia.")
                return []
            return dados
    
    except json.JSONDecodeError:
        print("ERRO: arquivo JSON está com problemas ou vazio. Iniciando com a biblioteca vazia.")
        return []
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}. Iniciando com a biblioteca vazia.")
        return []


def salvar_portfolio(lista_de_livros, nome_arquivo="biblioteca.json"):
    """Salva a lista de livros em um arquivo JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(lista_de_livros, arquivo, indent=4, ensure_ascii=False)
        print(f"Biblioteca salva com sucesso em '{nome_arquivo}'!")
    except Exception as e:
        print(f"Erro ao salvar biblioteca: {e}")

def encontrar_livro(lista_de_livros, nome_procurado):
    for livro in lista_de_livros:
        if livro.get('titulo', '').lower() == nome_procurado.lower():
            return livro
    return None

def adicionar_livro(lista_de_livros):
    try:
        titulo = input('Título do livro: ').strip()
        if not titulo:
            print("Erro: Digite o título do livro.")
            return
        
        if encontrar_livro(lista_de_livros, titulo) is not None:
            print(f"Erro: livro '{titulo}' já existe no banco de dados do projeto.")
            return
        
        autor = input('Autor (opcional): ').strip()
        
        livro = {
            'titulo': titulo,
            'autor': autor,
            'lido': False,
            'historico': []
        }
        lista_de_livros.append(livro)
        print('Livro adicionado com sucesso!')
    
    except Exception as e:
        print(f"Erro ao adicionar livro: {e}")

def listar_livros(lista_de_livros, nome):
    if len(lista_de_livros) == 0:
        print('Não tem livros na lista')
    else:
        print(f"\nHistórico de livros de {nome}:")
        for contador, livro in enumerate(lista_de_livros, start=1):
            status = 'Lido' if livro.get('lido') else 'Não lido'
            titulo = livro.get('titulo', '<sem título>')
            autor = livro.get('autor', '')
            print(f"{contador}. Título: {titulo}")
            if autor:
                print(f"   Autor: {autor}")
            print(f"   Lido: {status}")
            if livro.get('historico'):
                print(f"Histórico: {livro['historico']}")
            else:
                print(f"Histórico: sem os dados")

def about():
    print('\nSobre o Código:')
    print('Este código cadastra, lista, atualiza e remove livros.') #Inspirado no app Skoob ao qual uso para anotar os livros que estou lendo ou que pretender ler no futuro.
    print('Os dados são persistidos em um arquivo JSON chamado "biblioteca.json".')

def atualizar_livro(lista_de_livros):
    try:
        titulo_atualizar = input('Qual livro você deseja alterar? ').strip()
        if not titulo_atualizar:
            print("Erro: título inválido.")
            return
        
        livro = encontrar_livro(lista_de_livros, titulo_atualizar)
        if livro is None:
            print('Livro não encontrado.')
            return

        novo_titulo = input(f'Novo título (Enter para alterar "{livro.get("titulo")}"): ').strip()
        if not novo_titulo:
            novo_titulo = livro.get('titulo')

        novo_autor = input(f'Novo autor (Enter para alterar "{livro.get("autor","")}"): ').strip()
        if not novo_autor:
            novo_autor = livro.get('autor', '')

        novo_status_texto = input('Você já leu esse livro? (s/n): ').strip()
        novo_status = converter_para_bool(novo_status_texto)
        data_da_mudanca = datetime.now().strftime('%d/%m/%Y %H:%M:%S') #Foi utilizado IA para aprender como usar essa biblioteca, pois não sabia como puxar a data e hora do computador do usuario, logo pedi uma explicacao de como fazer isso e descobri que era assim como podem ver no código.

        livro['titulo'] = novo_titulo
        livro['autor'] = novo_autor
        livro['lido'] = novo_status
        livro['historico'].append((data_da_mudanca, novo_status, novo_titulo))
        print('Livro atualizado com sucesso!')
    
    except Exception as e:
        print(f"Erro ao atualizar livro: {e}")

def deletar_livro(lista_de_livros):
    try:
        titulo_remover = input('Qual livro deseja deletar? ').strip()
        if not titulo_remover:
            print("Erro: título inválido.")
            return
        
        livro = encontrar_livro(lista_de_livros, titulo_remover)
        if livro is None:
            print('Livro não foi encontrado.')
            return

        lista_de_livros.remove(livro)
        print(f'Livro "{livro.get("titulo")}" deletado com sucesso!')
    
    except Exception as e:
        print(f"Erro ao deletar livro: {e}")

def exibir_stats(lista_de_livros):
    """Exibe os dados da biblioteca de livros."""
    if len(lista_de_livros) == 0:
        print("Nenhum livro para exibir os dados.")
        return
    
    concluidos = sum(1 for p in lista_de_livros if p.get('lido'))
    em_andamento = len(lista_de_livros) - concluidos
    
    print("\n=== DADOS DA BIBLIOTECA ===")
    print(f"Total de livros: {len(lista_de_livros)}")
    print(f"Livros lidos: {concluidos}")
    print(f"Livros em andamento: {em_andamento}")
    
    if concluidos > 0:
        ultima_conclusao = None
        for livro in lista_de_livros:
            if livro.get('lido') and livro.get('historico'):
                if ultima_conclusao is None or livro['historico'][-1][0] > ultima_conclusao:
                    ultima_conclusao = livro['historico'][-1][0]
        if ultima_conclusao:
            print(f"Última leitura concluída em: {ultima_conclusao}")

def buscar_livros(lista_de_livros):
    """Busca livros pelo título."""
    try:
        termo = input('Digite o termo de busca (título): ').strip().lower()
        if not termo:
            print("Erro: termo de busca não pode estar vazio.")
            return
        
        resultados = [p for p in lista_de_livros if termo in p.get('titulo','').lower()]
        
        if not resultados:
            print(f"Nenhum livro encontrado com o termo '{termo}'.")
        else:
            print(f"\n=== RESULTADOS DA BUSCA ({len(resultados)} encontrado(s)) ===")
            for contador, livro in enumerate(resultados, start=1):
                status = 'Lido' if livro.get('lido') else 'Em andamento'
                titulo = livro.get('titulo')
                autor = livro.get('autor','')
                linha = f"{contador}. {titulo} - {status}"
                if autor:
                    linha += f" (Autor: {autor})"
                print(linha)
    
    except Exception as e:
        print(f"Erro ao buscar: {e}")

nome = str(input('Escreva seu nome: ')).strip()
lista_de_livros = carregar_portfolio() 

while True:
    print("REGRAS")
    print("ADD(icionar), LIST(ar), UPDATE(ar), DELETE(ar), STATS, SEARCH, ABOUT ou N(sair)")

    comando = input('O que deseja fazer agora? ').upper()

    if comando == 'N':
        print(f'Finalizando sessão, {nome}...')
        salvar_portfolio(lista_de_livros)
        break

    elif comando == 'ADD':
        adicionar_livro(lista_de_livros)

    elif comando == 'LIST':
        listar_livros(lista_de_livros, nome)

    elif comando == 'UPDATE':
        atualizar_livro(lista_de_livros)

    elif comando == 'DELETE':
        deletar_livro(lista_de_livros)

    elif comando == 'ABOUT':
        about()
    
    elif comando == 'STATS':
        exibir_stats(lista_de_livros)
    
    elif comando == 'SEARCH':
        buscar_livros(lista_de_livros)

    else:
        print('Opção invalida por favor tente novamente.')

