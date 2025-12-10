import datetime
import random
from time import sleep
import struct
red = '\033[91m'
green = '\033[92m'
reset = '\033[0m'
current_year = datetime.datetime.now().year

def showMenu():
    print('''
=====Menu Principal=====
1 - Cadastrar livro
2 - Listar livros
3 - Buscar livros
4 - Registrar empréstimo
5 - Registrar devolução
6 - Gerar relatórios
7 - Salvar acervo
8 - Sair
========================'''
)

def generateCode(title):
    first_letter = title[0].upper()
    middle = random.randint(1000, 9999)
    last = datetime.datetime.now().year % 100   #pega os dois ultimos digitos

    code = f'{first_letter}{middle}-{last}'
    return code


acervo = []
def registerBook():
    while True:
        title = input('Informe o título do livro: ').lower()

        author = input('Informe o nome do autor: ').lower()
        
        while True:
            try:
                year = int(input('Informe o ano do livro: '))
                if year > current_year:
                    raise ValueError
                break

            except ValueError:
                print(f'{red}Ano inválido, tente novamnete!{reset}')

        category = input('Informe a categoria do livro: ').lower()

        code = generateCode(title)

        acervo.append((code, title, author, year, category))
        print(f'\n{green}Livro cadastrado com sucesso!{reset}')


        again = input('\nDeseja cadastrar outro livro? (s/n): ').lower()
        if again not in ['sim', 's', 'si']:
            print('\nVoltando para o menu principal!')
            sleep(0.3)
            break


def showBooks(books):       #ajeitar as  colunas
    ordered = sorted(books, key=lambda x: x[1])

    print('\n=====LIVROS CADASTRADOS======')
    for code, title, author, year, category in ordered:
        print(f"{code} | {title.title()} | {author.title()} | {year} | {category.title()}")


def search(books):
    found = False

    to_search = input('Digite o que deseja buscar (autor | título | categoria):  ').lower()
    print()
    for code, title, author, year, category in books:
        if to_search in title or to_search in author or to_search in category:
            print(f'{code};{title};{author};{year};{category}')
            found = True

    if not found:
        print('Nenhum livro encontrado')

    input('\nPressione Enter para voltar ao menu principal!')


loans = []
loaned = set()
def loan(books):
    showBooks(books)
    print()
    to_loan = input('Informe o nome ou o código do livro que quer emprestar: ').lower()
    username = input('Informe o nome do usuário que deseja fazer o empréstimo: ').lower()
    for code, title, _, _, _ in books:
        if to_loan == code.lower() or to_loan == title.lower():

            if code in loaned:
                print(f'\n{red}Livro ja emprestado{reset}')
                return
            
            date_loan = datetime.datetime.today()
            date_dev = date_loan + datetime.timedelta(days=7)

            loans.append((code, username, date_loan, date_dev))
            loaned.add(code)


            saveLoan(code, username, date_loan.strftime('%d/%m/%Y'), date_dev.strftime('%d/%m/%Y'))
            saveUsername(username)


            print(f'\n{green}Empréstimo registrado{reset}')
            print(f'Livro: {title.title()}')
            print(f'Usuário: {username.title()}')
            print(f'Devolver até: {date_dev.strftime('%d/%m/%Y')}')
            return

    print(f'\n{red}Livro não encontrado!{reset}')


def saveLoan(code, username, date_loan, date_dev):
    with open('emprestimos.txt', 'a', encoding='utf-8') as f:
        f.write(f'{code};{username};{date_loan};{date_dev}\n')
        
def saveUsername(username):
    with open('usuarios.txt', 'a', encoding='utf-8') as f:
        f.write(username + '\n')


def registerDev(books):
    to_dev = input('\nInforme o nome ou o código do livro para devolução: ').lower()
    username = input('Informe o nome do usuário que fez o empréstimo do livro: ').lower()
    exist = False
    for code, title, _, _, _ in books:
        if to_dev == code.lower() or to_dev == title.lower():
            exist = True

            for loan in loans:
                loan_code, loan_user, date_loan, date_expected = loan

                if loan_code == code and loan_user == username:
                    #Pega data real de devolução
                    real_date_str = input('Informe a data de devolução: ')  #para teste, para mostrar que ta funcionando o cálculo
                    try:
                        real_date = datetime.datetime.strptime(real_date_str, '%d/%m/%Y')
                    except ValueError:
                        print(f'{red}Formato de data inválido{reset}.')
                        return
                        
                    #Calcula o tempo de atraso
                    delay = (real_date - date_expected).days

                    if delay > 0:
                        fine = delay * 0.50
                    else:
                        fine = 0

                    #imprimir resultado
                    print(f"\n{green}Devolução registrada!{reset}")
                    print(f"Livro: {title.title()}")
                    print(f"Usuário: {username.title()}")
                    print(f"Data prevista: {date_expected.strftime('%d/%m/%Y')}")
                    print(f"Data devolvida: {real_date.strftime('%d/%m/%Y')}")
                    print(f"Atraso: {delay} dia(s)")
                    print(f"Multa: R$ {fine:.2f}")            
                    
                    if code in loaned:  #remove o livro do conjunto
                        loaned.remove(code)
                    
                    return
            
            print(f"\n{red}Este livro existe, mas não está registrado como emprestado para este usuário.{reset}")
            return
        
    if not exist:
        print(f'\n{red}Livro não registrado no sistema!{reset}')


def saveReport(books, loan):
    group_category = {}
    total_books = 0
    for _, _, _, _, category in books:
        if category not in group_category:
            group_category[category] = 0

        group_category[category] += 1

        total_books += 1

    loaned_books = len(loan)
    books_available = total_books - loaned_books

    with open('relatorio.txt', 'w', encoding='utf-8') as f:
        f.write('RELATÓRIO GERAL DA BIBLIOTECA\n\n')
        f.write(f'1. Total de livros cadastrados: {total_books}\n\n')

        f.write('2. Livros por categoria:\n')
        for category, qtd in group_category.items():
            f.write(f'- {category.title()}: {qtd}\n')

        f.write('\n3. Situação dos livros:\n')
        f.write(f'-Livros emprestados: {loaned_books}\n')
        f.write(f'Livros disponíveis: {books_available}')

    with open('relatorio_rapido.txt', 'w', encoding='utf-8') as f:
        for book in books:
            f.write(f'{book[1]}\n')

def saveBooks(books):
    fmt = "10s50s50si20s"

    with open('acervo.bin', 'wb') as f:

        for code, title, author, year, category in books:
            code_b = code.encode('utf-8')[:10].ljust(10, b' ')  #ajuste para cada campo com tamanho fixo
            title_b = title.encode('utf-8')[:50].ljust(50, b' ')#tem o truncamento se passar do limite
            author_b = author.encode('utf-8')[:50].ljust(50, b' ')
            category_b = category.encode('utf-8')[:20].ljust(20, b' ')

            record = struct.pack(fmt, code_b, title_b, author_b, year, category_b)
            f.write(record)
        
        print(f'\n{green}Acervo salvo no arquivo binário "acervo.bin" com sucesso!')

if __name__ == '__main__':
    while True:
        showMenu()

        while True:
            try:
                op = int(input('Informe a opção desejada: '))
                if op < 1 or op > 8:
                    raise ValueError
                break
            except ValueError:
                print(f'\n{red}Entrada inválida para esta opção{reset}\n')
        
        match op:
            case 1:
                registerBook()
            case 2:
                showBooks(acervo)
                input('\nPressione Enter para voltar ao menu principal!')
            case 3:
                search(acervo)
            case 4:
                loan(acervo)
                input('\nPressione Enter para voltar ao menu principal!')
            case 5:
                registerDev(acervo)
                input('\nPressione Enter para voltar ao menu principal!')
            case 6:
                saveReport(acervo, loaned)
                print(f'\n{green}Relatório salvo com sucesso{reset}')
            case 7:
                saveBooks(acervo)
                print(f'\n{green}Relatório salvo com sucesso{reset}')
            case 8:
                print('Saindo do sistema... até logo!')
                sleep(0.6)
                break

