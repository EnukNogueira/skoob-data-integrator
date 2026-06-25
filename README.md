# Skoob Data Integrator

Aplicação de linha de comando em Python para gerenciamento de biblioteca pessoal de livros, com persistência local em JSON e rastreamento de histórico de alterações.

---

## Sobre o projeto

O Skoob Data Integrator é um sistema CRUD completo para organização de leituras pessoais, desenvolvido inteiramente com bibliotecas nativas do Python. A aplicação roda no terminal, persiste os dados em um arquivo JSON local e registra o histórico de modificações de cada livro.

O projeto foi desenvolvido como trabalho acadêmico na PUCPR (Análise e Desenvolvimento de Sistemas), com foco na manipulação estruturada de dados, lógica de algoritmos e operações sobre coleções dinâmicas.

---

## Funcionalidades

- Adicionar livros com título e autor
- Listar todos os livros cadastrados
- Atualizar dados (título, autor, status de leitura) com registro automático de histórico
- Remover livros da biblioteca
- Buscar livros por termo no título
- Exibir estatísticas gerais (total, lidos, em andamento)
- Persistência automática dos dados em `biblioteca.json`

---

## Tecnologias utilizadas

- **Python 3** — linguagem principal
- **json** — serialização e persistência dos dados
- **os** — manipulação do sistema de arquivos
- **datetime** — registro de timestamps no histórico de alterações

Sem dependências externas. Roda em qualquer ambiente com Python 3 instalado.

---

## Como executar

```bash
# Clone o repositório
git clone https://github.com/EnukNogueira/skoob-data-integrator.git
cd skoob-data-integrator

# Execute a aplicação
python somativa_enuk_skoob.py
```

Informe seu nome ao iniciar. O menu de comandos será exibido automaticamente.

---

## Comandos disponíveis

| Comando   | Descrição                                      |
|-----------|------------------------------------------------|
| `ADD`     | Adiciona um novo livro à biblioteca            |
| `LIST`    | Lista todos os livros cadastrados              |
| `UPDATE`  | Atualiza dados de um livro e registra histórico|
| `DELETE`  | Remove um livro da lista                       |
| `SEARCH`  | Busca livros por termo no título               |
| `STATS`   | Exibe estatísticas gerais da biblioteca        |
| `ABOUT`   | Exibe uma descrição rápida do projeto          |
| `N`       | Salva os dados e encerra a sessão              |

---

## Estrutura de dados

Cada livro é armazenado no arquivo `biblioteca.json` com a seguinte estrutura:

```json
{
  "titulo": "Fundacao",
  "autor": "Asimov",
  "lido": false,
  "historico": []
}
```

O campo `historico` é populado automaticamente a cada atualização via comando `UPDATE`, registrando o que foi alterado e quando.

---

## Observações

- Na primeira execução, o arquivo `biblioteca.json` é criado automaticamente ao salvar
- Se o arquivo JSON estiver vazio ou corrompido, a aplicação inicia com biblioteca vazia para evitar falhas de execução

---

## Autores

**Enuk Nogueira** — desenvolvimento e implementação

**Guilherme Biassi** — ideias e concepção

---

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/enuknogueira/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/EnukNogueira)


## Autor

- Enuk dos Santos Alves Nogueira(Programador)
- Guilherme Biassi(Ideias)
