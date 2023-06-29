def cadastro(): # classe de cadastro
    try: # Função usada para o caso de exceção
        with open ("Dados.txt", "a") as arquivo: # A função with que cria o arquivo Dados.TXT em modo para acrescentar novos dados sem apagar os dados anteriores por causa do 'a'
            matricula = input ("Digite o número de matrícula do atleta: ") # Variável que identifica o atleta
            nome = input ("Digite o nome e sobrenome do atleta: ") # declaração das variáveis 
            data_nascimento = input ("Digite a data de nascimento do atleta: ")
            sexo = input ("Digite o sexo do atleta: ")
            endereco = input ("Digite o endereço do atleta: ")
            telefone = input ("Digite o telefone do atleta: ")

            atleta = f"{matricula}, {nome}, {data_nascimento}, {sexo}, {endereco}, {telefone},\n" # dicionario armazenado na variável. O \n serve para pular a linha
            arquivo.write(atleta) # função que escreve a variável atleta no arquivo txt
            print ("Os dados do atleta foram cadastrados com sucesso!")
    except Exception as e: # caso de erro de exceção 
        print ("Ocorreu um erro! Não foi possivel cadastrar os dados do atleta.",str(e))

def listar_dados(): # classe de listar dados 
    try: # Função usada para o caso de exceção
        with open ("Dados.txt", "r") as arquivo: # # A função with abre o arquivo "Dados.txt" em modo de leitura por causa do 'r'
            linhas = arquivo.readlines() # A função .readlines que lê todas as linhas do arquivo e as armazena em uma lista armazenada na variável linhas
            if not linhas: # Verifica se tem elementos a lista linhas e se está vazia retorna o print
                print ("Nenhum atleta foi cadastrado ainda.")
            else: #se não printa
                print ("Dados dos atletas cadastrados:")
                for linha in linhas: # O for percorre todas as linhas da minha lista armazenada na variável linhas
                    dados = linha.strip().split(",") # A função .strip() remove espaços em branco no início e final da linha e a função .split()separa os dados pela vírgula
                    print ("Matrícula:", dados[0]) # O print é orientado pelo dado (que está armazenado na linha que está armazenada na lista linhas) pelo índice dos elementos, começando pela posição [0]
                    print ("Nome:", dados[1])
                    print ("Data de nascimento:", dados[2])
                    print ("Sexo:", dados[3])
                    print ("Endereço:", dados[4])
                    print ("Telefone:", dados[5])
                    print ("============+++++++++++++============++++++++++++===========")
    except FileNotFoundError: # caso de erro de exceção FileNotFoundError
        print("O arquivo de dados selecionado não foi encontrado.")
    except Exception as e: # caso de erro de exceção 
        print("Ocorreu um erro ao listar os dados:", str(e))

def alterar_dados(): #Classe que altera dados
    try: # Função usada para o caso de exceção
        with open ("Dados.txt", "r") as arquivo: # A função with abre o arquivo "Dados.txt" em modo de leitura por causa do 'r'
            linhas = arquivo.readlines() # A função .readlines que lê todas as linhas do arquivo e as armazena em uma lista armazenada na variável linhas

        if not linhas: # Verifica se tem elementos a lista linhas e se está vazia retorna o print
            print ("Este atleta não foi cadastrado.")
            return
            
        matricula = input("Digite a matrícula do atleta que desejas alterar: ") # A variável matricula solicita pelo input a matrícula do atleta a ser alterado
        encontrado = False # Variável encontrado começa com o valor booleano em False

        with open("Dados.txt", "w") as arquivo: # A função with abre o arquivo "Dados.txt" escrita (irá substituir o conteúdo por causa do "w")
            for linha in linhas:
                dados = linha.strip().split(',')
                if dados[0] == matricula: # Verifica se o valor da variável matricula que está armazenado no índice [0] em dados está na linha da lista, corresponde à matrícula digitada
                    nova_matricula = input ("Confirme a sua matricula: ")
                    novo_nome = input ("Digite o nome e sobrenome do atleta: ")
                    nova_data_nascimento = (input ("Digite a data de nascimento do atleta: "))
                    novo_sexo = (input ("Digite o sexo do atleta: "))
                    novo_endereco = (input ("Digite o endereço do atleta: "))
                    novo_telefone = (input ("Digite o telefone do atleta: "))

                    nova_linha = f"{matricula},{novo_nome}, {nova_data_nascimento}, {novo_sexo}, {novo_endereco}, {novo_telefone}" #criar um dicionario com o mesmo número de elementos da lista
                    arquivo.write((nova_linha) + '\n') # pular a linha para não bugar a alteração do arquivo dados.txt
                    encontrado = True
                    print("Os dados do atleta foram alterados com sucesso!")
                else:
                    arquivo.write(linha)
                           
        if not encontrado:
             print("Nenhum atleta foi encontrado com este identificador de matrícula.")
    except FileNotFoundError:
         print("O arquivo de dados selecionado não foi encontrado.")
    except Exception as e:
            print("Ocorreu um erro ao alterar os dados:", str(e))

def excluir_dados():
    try:
          with open ("Dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print ("Este atleta não foi cadastrado.")
                return
            
            matricula = input("Digite a matrícula do atleta que desejas excluir: ")
            encontrado = False

            with open("Dados.txt", "w") as arquivo:
                 for linha in linhas:
                      dados = linha.strip().split(",")
                      if dados[0] == matricula:
                            encontrado = True
                            print ("Os dados do atleta foram excluídos com sucesso!")
                      else:
                           arquivo.write(linha)

            if not encontrado:
             print("Nenhum atleta foi encontrado com este identificador de matrícula.")
    except FileNotFoundError:
        print("O arquivo de dados selecionado não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao alterar os dados:", str(e))

def backup():
    try:
        with open("Dados.txt", "r") as arquivo_origem:
               with open ("Backup_Dados.txt", "w") as arquivo_backup:
                    conteudo = arquivo_origem.read()
                    arquivo_backup.write(conteudo)
        print("O backup do arquivo selecionado foi realizado com sucesso!")
    except FileNotFoundError:
        print("O arquivo de dados selecionado não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao realizar o backup dos dados:", str(e))

def cria_linha():
    print("|", "-" * 60, "|")

def menu():
     while True:
            cria_linha()
            print ("     ------------------  MENU DE OPÇÕES  ------------------")
            cria_linha()
            print("       1- Cadastrar dados:")
            cria_linha()
            print("       2- Listar dados:")
            cria_linha()
            print("       3- Alterar dados:")
            cria_linha()
            print("       4- Excluir dados:")
            cria_linha()
            print("       5- Fazer Backup dos dados:")
            cria_linha()
            print("       0- Sair:")
            cria_linha()
            opcao = int(input("    Digite uma opção válida: "))
            cria_linha()
            
            
            if opcao == 1:
                print("             Opção de cadastrar dados selecionada")
                cria_linha()
                cadastro()
            elif opcao == 2:
                print("             Opção de listar dados selecionada")
                cria_linha()
                listar_dados()
            elif opcao == 3:
                print("             Opção de alterar dados selecionada")
                cria_linha()
                alterar_dados()
            elif opcao == 4:
                print("             Opção de excluir dados selecionada")
                cria_linha()
                excluir_dados()
            elif opcao == 5:
                print("             Opção de backup dados selecionada")
                cria_linha()
                backup()
            elif (opcao == 0):
                cria_linha()
                print ("Encerrando...")
                print ("Programa encerado com sucesso.")
                break
            else:
                print("Opção invalida. Digite uma opção válida.")