# 📚 Sistema de Gerenciamento de Biblioteca

Um sistema simples de linha de comando (CLI) desenvolvido em Python para gerenciar o acervo de livros, registrar empréstimos, devoluções e gerar relatórios.

## 🌟 Funcionalidades Principais

* **Cadastro de Livros:** Adicione novos livros ao acervo com título, autor, ano e categoria.
* **Geração Automática de Código:** Cada livro recebe um código único.
* **Listagem e Busca:** Visualize o acervo completo ou pesquise livros por título, autor ou categoria.
* **Gestão de Empréstimos e Devoluções:**
    * Registre empréstimos, definindo uma data de devolução (7 dias após o empréstimo).
    * Registre devoluções e calcule multas automaticamente (R$ 0,50 por dia de atraso).
* **Relatórios:** Gere relatórios sobre o total de livros, a distribuição por categoria e a situação de empréstimo (disponíveis vs. emprestados).
* **Persistência de Dados:** Salva o acervo principal em um arquivo binário (`acervo.bin`) usando o módulo `struct` do Python.
* **Arquivos de Log:** Salva dados de empréstimos e usuários em arquivos de texto (`emprestimos.txt`, `usuarios.txt`).

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python** | Linguagem de programação principal. |
| **`datetime`** | Manipulação de datas e tempo para empréstimos e multas. |
| **`random`** | Geração de códigos de livro únicos. |
| **`struct`** | Empacotamento de dados para salvar o acervo em formato binário. |
| **Escapes ANSI** | Utilizado para colorir as mensagens no terminal (Verde para sucesso, Vermelho para erro). |

## ⚙️ Instalação e Execução

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### 🚀 Rodando o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github](https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
    cd [NOME DO SEU REPOSITÓRIO]
    ```

2.  **Execute o script:**
    ```bash
    python seu_arquivo.py 
    # Substitua 'seu_arquivo.py' pelo nome do seu arquivo, se for diferente.
    ```

## 📖 Como Usar (Menu Principal)

O sistema é operado através de um menu de texto simples.

=====Menu Principal=====
1 - Cadastrar livro
2 - Listar livros
3 - Buscar livros
4 - Registrar empréstimo
5 - Registrar devolução
6 - Gerar relatórios
7 - Salvar acervo
8 - Sair

### Exemplo de Uso

1.  **Cadastrar Livro (Opção 1):** O sistema pedirá o título, autor, ano (com validação) e categoria.
2.  **Registrar Empréstimo (Opção 4):**
    * Primeiro, lista os livros cadastrados.
    * Você informa o código ou título do livro e o nome do usuário.
    * O sistema calcula a data de devolução.
3.  **Registrar Devolução (Opção 5):**
    * Você informa o código/título do livro e o nome do usuário.
    * O sistema pedirá a **data de devolução real** (no formato `DD/MM/AAAA`).
    * Será calculado e exibido o valor da multa, se houver atraso.
4.  **Gerar Relatórios (Opção 6):** Cria um arquivo `relatorio.txt` com estatísticas e um `relatorio_rapido.txt` com a lista simples de títulos.
5.  **Salvar Acervo (Opção 7):** Salva o acervo atual no arquivo binário `acervo.bin`.

## 🤝 Contribuições

Sinta-se à vontade para abrir _issues_ ou enviar _pull requests_. Toda contribuição é bem-vinda!

---
Desenvolvido por MiguelPerino
