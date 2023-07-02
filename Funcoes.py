# Gabriel Ache de Souza - ADS11
def cadastro(): # função de cadastro de atletas
    try: # Função usada para tratar os casos de exceções durante a execução do script
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
    except Exception as e: # indicação do caso de erro de exceção 
        print ("Ocorreu um erro! Não foi possivel cadastrar os dados do atleta.",str(e))

def listar_dados(): # função de listar dados dos atletas
    try: # Função usada para o caso de exceção
        with open ("Dados.txt", "r") as arquivo: # # A função with abre o arquivo "Dados.txt" em modo de leitura por causa do 'r'
            linhas = arquivo.readlines() # A função .readlines que lê todas as linhas do arquivo (dados.txt) e as armazena em uma lista armazenada na variável linhas
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

def alterar_dados(): #função que altera dados do atleta 
    try: # Função usada para o caso de exceção
        with open ("Dados.txt", "r") as arquivo: # A função with abre o arquivo "Dados.txt" em modo de leitura por causa do 'r'
            linhas = arquivo.readlines() # A função .readlines que lê todas as linhas do arquivo e as armazena em uma lista armazenada na variável linhas

        if not linhas: # Verifica se tem elementos a lista linhas e se está vazia retorna o print
            print ("Este atleta não foi cadastrado.")
            return #termina a função 
            
        matricula = input("Digite a matrícula do atleta que desejas alterar: ") # A variável matricula solicita pelo input a matrícula do atleta a ser alterado
        encontrado = False # Variável encontrado começa com o valor booleano em False

        with open("Dados.txt", "w") as arquivo: # A função with abre o arquivo "Dados.txt" escrita (irá substituir o conteúdo por causa do "w")
            for linha in linhas: # o for percorre toda linha da lista linhas
                dados = linha.strip().split(',') # A função .strip() remove espaços em branco no início e final da linha e a função .split()separa os dados pela vírgula
                if dados[0] == matricula: # Verifica se o valor da variável matricula que está armazenado no índice [0] em dados está na linha da lista, corresponde à matrícula digitada
                    nova_matricula = input ("Confirme a sua matricula: ") # inputs para alteração
                    novo_nome = input ("Digite o nome e sobrenome do atleta: ")
                    nova_data_nascimento = (input ("Digite a data de nascimento do atleta: "))
                    novo_sexo = (input ("Digite o sexo do atleta: "))
                    novo_endereco = (input ("Digite o endereço do atleta: "))
                    novo_telefone = (input ("Digite o telefone do atleta: "))

                    nova_linha = f"{matricula},{novo_nome}, {nova_data_nascimento}, {novo_sexo}, {novo_endereco}, {novo_telefone}" #criar um dicionario com o mesmo número de elementos da lista
                    arquivo.write((nova_linha) + '\n') # pular a linha para não bugar a alteração do arquivo dados.txt
                    encontrado = True #muda a para true e com isso realiza o bloco de comandos 
                    print("Os dados do atleta foram alterados com sucesso!")
                else:
                    arquivo.write(linha) # escreve na linha do arquivo  
                           
        if not encontrado:
             print("Nenhum atleta foi encontrado com este identificador de matrícula.")
    except FileNotFoundError: # caso de erro de exceção FileNotFoundError
         print("O arquivo de dados selecionado não foi encontrado.")
    except Exception as e: # caso de erro de exceção 
            print("Ocorreu um erro ao alterar os dados:", str(e))

def excluir_dados(): # função que excluir os dados do atleta
    try:
          with open ("Dados.txt", "r") as arquivo: # Abre o arquivo "Dados.txt" em modo de leitura por causa do "r"
            linhas = arquivo.readlines() # A função .readlines que lê todas as linhas do arquivo e as armazena em uma lista armazenada na variável linhas

            if not linhas: # faz a verificação dos elementos da lista linhas 
                print ("Este atleta não foi cadastrado.")
                return
            
            matricula = input("Digite a matrícula do atleta que desejas excluir: ") # pede a matrícula do atleta
            encontrado = False # Variável encontrado começa com o valor booleano em False

            with open("Dados.txt", "w") as arquivo: # A função with abre o arquivo "Dados.txt" escrita (irá substituir o conteúdo por causa do "w")
                 for linha in linhas: # o for percorre cada linha da lista linhas
                      dados = linha.strip().split(",") # A função .strip() remove espaços em branco no início e final da linha e a função .split()separa os dados pela vírgula
                      if dados[0] == matricula: # o if faz a verificação se a matrícula armazenada no arquivo dados.txt é igual a matrícula digitada
                            encontrado = True #muda a para true e com isso realiza o bloco de comandos
                            print ("Os dados do atleta foram excluídos com sucesso!")
                      else:
                           arquivo.write(linha) # escreve na linha do arquivo  

            if not encontrado: # se a condição booleana do encontrado se manter em False vai retornar o print 
             print("Nenhum atleta foi encontrado com este identificador de matrícula.")
    except FileNotFoundError:  # caso de erro de exceção FileNotFoundError
        print("O arquivo de dados selecionado não foi encontrado.")
    except Exception as e:# caso de erro de exceção 
        print("Ocorreu um erro ao alterar os dados:", str(e))

def backup(): # Função que realiza o backup dos dados alteta 
    try:
        with open("Dados.txt", "r") as arquivo_origem: # Abre o arquivo "Dados.txt" em modo de leitura por causa do "r"
               with open ("Backup_Dados.txt", "w") as arquivo_backup: # A função with abre o arquivo "Dados.txt" escrita (irá substituir o conteúdo por causa do "w")
                    conteudo = arquivo_origem.read() #faz a leitura dos dados armazenados no arquivo de origem
                    arquivo_backup.write(conteudo) #escreve os dados armazenados no arquivo de backup
        print("O backup do arquivo selecionado foi realizado com sucesso!")
    except FileNotFoundError: # caso de erro de exceção FileNotFoundError
        print("O arquivo de dados selecionado não foi encontrado.")
    except Exception as e:# caso de erro de exceção 
        print("Ocorreu um erro ao realizar o backup dos dados:", str(e))

def cria_linha(): # Função para criar linhas
    print("|", "-" * 60, "|") # quantidades de caracteres para separar as linhas

def menu(): #função do menu
     while True:
            cria_linha() #função cria_linha
            cria_linha()
            print ("+++++++++++++++++++   ESCOLINHA DO GRÊMIO   ++++++++++++++++++++")
            print ("                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print ("                ⣿⣿⣿⣿⣿⣿⣿⡿⢛⣉⣥⣶⡖⠚⠛⠛⠛⠛⢲⣶⢬⣍⡛⢿⣿⣿⣿⣿⣿⣿⣿")
            print ("                ⣿⣿⣿⣿⣿⠟⣡⡶⠏⠁⠄⠄⢉⣷⣶⣶⣶⣾⡉⠄⠄⠈⠙⢷⣌⠻⣿⣿⣿⣿⣿")
            print ("                ⣿⣿⣿⡟⣡⣾⠋⠄⠄⠄⠄⢰⣾⣿⠿⠿⡿⣿⣿⣆⠄⠄⠄⠄⠈⣳⣎⠻⣿⣿⣿")
            print ("                ⣿⣿⠟⣴⠋⠄⠙⠲⢄⣀⠄⣿⣿⣭⣧⣴⣥⣥⣿⣿⡄⢀⣠⠔⠊⠁⠘⣧⠙⣿⣿") 
            print ("                ⣿⡟⣰⡏⠄⠄⠄⠄⠄⠉⠙⠛⠻⠿⠿⠿⠿⠿⠿⠛⠛⠉⠁⠄⠄⠄⠄⠸⣦⢹⣿") 
            print ("                ⣿⠃⣿⠄⣠⡤⣄⡀⢠⣤⣤⣄⢠⣬⣭⣤⣤⣤⠄⢀⣤⠄⡄⢀⣠⢤⣄⠄⣿⡌⣿") 
            print ("                ⣿⠄⣿⢸⡇⠄⣈⣁⢸⣀⣀⡟⢸⣧⣤⡄⣿⣿⡄⣸⢹⠄⡇⣿⠁⠄⢸⡇⢸⡇⣿") 
            print ("                ⣿⡄⣿⠈⠷⢤⠴⠻⠸⠄⠄⠿⠸⠧⠤⠤⠿⠇⠷⠇⠸⠄⠇⠹⠧⡤⠼⠃⣿⢃⣿") 
            print ("                ⣿⣧⠹⣇⠄⠄⠄⠄⢀⣀⣤⣴⣶⣶⣶⣶⣶⣶⣶⣦⣤⣀⡀⠄⠄⠄⠄⢰⠟⣸⣿") 
            print ("                ⣿⣿⣦⠻⣄⢀⣠⠴⠋⠉⠄⣿⣿⠿⠻⡛⠛⠟⣿⣿⠃⠈⠙⠲⢤⡀⢠⡟⣠⣿⣿") 
            print ("                ⣿⣿⣿⣧⡙⢿⣄⠄⠄⠄⠄⠸⢿⣿⣾⣶⣿⣶⣿⠏⠄⠄⠄⠄⢀⡽⢏⣼⣿⣿⣿") 
            print ("                ⣿⣿⣿⣿⣿⣦⡙⠷⣆⡀⠄⠄⣈⡿⠿⠿⠿⢿⣁⠄⠄⢀⣠⡾⢋⣴⣿⣿⣿⣿⣿") 
            print ("                ⣿⣿⣿⣿⣿⣿⣿⣷⣮⣉⡛⠿⠧⢤⣤⣤⣤⣤⠼⠿⢚⣋⣥⣾⣿⣿⣿⣿⣿⣿⣿") 
            print ("                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
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
            
            #seleção das opções que chama cada uma das funções por IF, elifs e else
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
            elif (opcao == 0): #condição que vai encerrar o programa
                cria_linha()
                print ("--------------- ENCERRANDO O PROGRAMA... ------------------  ")
                cria_linha()
                print ("------------------ Programa encerado com sucesso. ---------  ")
                cria_linha()
                break #encerra o programa
            else:
                print("Opção invalida. Digite uma opção válida.")