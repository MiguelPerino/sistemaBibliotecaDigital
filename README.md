📚 Sistema de Gerenciamento de Biblioteca (Python)

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido em Python, permitindo cadastrar livros, registrar empréstimos, devoluções, gerar relatórios e salvar o acervo em arquivo binário com tamanho fixo utilizando struct.

O projeto funciona inteiramente pelo terminal e pode ser usado como base para estudos de:

Manipulação de arquivos (texto e binário)

Estruturas de dados (listas, tuplas, conjuntos)

Datas e prazos (datetime)

Formatação com struct e tamanhos fixos

Organização de um sistema completo em Python

🚀 Funcionalidades
1. Cadastrar Livro

O usuário informa:

título

autor

ano

categoria

O sistema gera automaticamente um código no formato:

LetraInicial + número aleatório de 4 dícios + "-" + anoAtual2D
Ex: P1234-25


O livro é armazenado em memória no formato:

(code, title, author, year, category)

2. Listar Livros

Mostra todos os livros cadastrados ordenados por título, com a formatação:

Código | Título | Autor | Ano | Categoria

3. Buscar Livros

Busca por:

título

autor

categoria

A busca não diferencia maiúsculas de minúsculas.

4. Registrar Empréstimo

Encontra o livro pelo título ou código

Verifica se já está emprestado

Registra:

data do empréstimo

data de devolução programada (7 dias após)

Salva em emprestimos.txt

Salva o nome do usuário em usuarios.txt

Controle de empréstimos é feito com:

lista loans

conjunto loaned (evita duplicações)

5. Registrar Devolução

Verifica livro e usuário

Solicita data real da devolução

Calcula atraso em dias

Calcula multa (R$ 0,50 por dia de atraso)

Remove o livro do conjunto loaned

Mostra um resumo completo ao final.

6. Gerar Relatórios

Gera 2 arquivos:

relatorio.txt

Contém:

total de livros

livros por categoria

quantidade de livros emprestados e disponíveis

relatorio_rapido.txt

Lista somente os títulos, um por linha.

7. Salvar Acervo em Arquivo Binário

O arquivo é salvo como acervo.bin usando o formato fixo:

"10s50s50si20s"


Ou seja:

Campo	Tipo	Tamanho
código	string	10 bytes
título	string	50 bytes
autor	string	50 bytes
ano	int	4 bytes
categoria	string	20 bytes

Strings são:

truncadas se excederem o tamanho

preenchidas com espaços caso menores (ljust)

Cada registro ocupa 134 bytes.

📦 Estrutura do Projeto
biblioteca.py
emprestimos.txt
usuarios.txt
relatorio.txt
relatorio_rapido.txt
acervo.bin

🛠 Tecnologias Utilizadas

Python 3.x

datetime

struct

Manipulação de arquivos texto e binários

Controle de fluxo (loops, match-case)


🛠️ Tecnologias Utilizadas

Python 3

datetime

struct

Manipulação de arquivos (texto e binário)

Estruturas: listas, tuplas, conjuntos

match-case para controle de fluxo

📌 Observações Importantes

O acervo fica na memória até ser salvo em binário.

Os arquivos .txt são atualizados a cada operação.

As datas devem sempre estar no formato dd/mm/aaaa.

O arquivo binário sobrescreve o acervo anterior.

🤝 Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests!
Feedbacks são sempre bem-vindos.
