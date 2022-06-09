from menu.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Imprimir Zeresima', 'Iniciar Votacao', 'NULO'])
    if resposta == 1:
        print('ZERESIMA: ')
        cabecalho(f'\033[34mPREFEITOS\033[m')
        print(
            'PREFEITO JOSÉ DA SILVA    10 - TOTAL DE VOTOS = 0 \n'
            'PREFEITA MARIA DO JURUNAS 11 - TOTAL DE VOTOS = 0 \n'
            'PREFEITO JOÃO DO TAPANÃ   12 - TOTAL DE VOTOS = 0 \n'
        )
        cabecalho(f'\033[34mVEREADORES\033[m')
        print(
            'VEREADOR JADSON SILVA      12547  - TOTAL DE VOTOS = 0 \n'
            'VEREADORA MARCIA NINA      59874  - TOTAL DE VOTOS = 0 \n'
            'VEREADOR JOAO RIBEIRO      98454  - TOTAL DE VOTOS = 0 \n'
            'VEREADOR GUSTAVO GUANABARA 23598  - TOTAL DE VOTOS = 0 \n'
            'VEREADORA ANA SILVA        45782  - TOTAL DE VOTOS = 0 \n'
            'VEREADORA CARLOS RIBEIRO   98547  - TOTAL DE VOTOS = 0 \n'
            'VEREADORA ANTONIO ALVES    23458  - TOTAL DE VOTOS = 0 \n'
            'VEREADORA FELIPE SILVA     02147  - TOTAL DE VOTOS = 0 \n'
            'VEREADORA MARIA CONDE      32587  - TOTAL DE VOTOS = 0 \n'
            'VEREADORA RUI VENTURA      15985  - TOTAL DE VOTOS = 0 \n'
        )

    elif resposta == 2:
        print(f'\033[31mVotacao Iniciada\033[m')


        def votacao(candidato):  # fução para votação com a variavel candidato como argumento
            global prefeita_Maria_do_Jurunas, prefeito_Jose_da_Silva, prefeito_Joao_do_Tapana, vereador_Jadson_silva, \
                vereadora_Marcia_Nina, vareador_Joao_Ribeiro, vareador_Gustavo_Guanabara, vareadora_Ana_Silva, \
                vareador_Carlos_Ribeiro, vareador_Antonio_Alves, vareador_Felipe_Silva, vareador_Maria_Conde, \
                vareador_Rui_Ventura

            if candidato.isnumeric():  # checa se candidato e um caracter numerico
                if candidato == '10' or candidato == '11' or candidato == '12' or candidato == '12547' or \
                        candidato == '59874' or candidato == '98454' or candidato == '23598' or candidato == '45782' or \
                        candidato == '98547' or candidato == '23458' or candidato == '02147' or candidato == '32587' or \
                        candidato == '15985':
                    if candidato == '10':
                        prefeito_Jose_da_Silva += 1
                        print(f'\033[1;33mJOSE DA SILVA MDB\033[m')
                    elif candidato == '11':
                        prefeita_Maria_do_Jurunas += 1
                        print(f'\033[1;33mMARIA DO JURUNAS PRONA\033[m')
                    elif candidato == '12':
                        prefeito_Joao_do_Tapana += 1
                        print(f'\033[1;33mJOAO DO TAPANA PSDB\033[m')
                    elif candidato == '12547':
                        vereador_Jadson_silva += 1
                        print(f'\033[1;33mJADSON SILVA PRONA\033[m')
                    elif candidato == '59874':
                        vereadora_Marcia_Nina += 1
                        print(f'\033[1;33mMARCIA NINA PRONA\033[m')
                    elif candidato == '98454':
                        vareador_Joao_Ribeiro += 1
                        print(f'\033[1;33mJOAO RIBEIRO PT\033[m')
                    elif candidato == '23598':
                        vareador_Gustavo_Guanabara += 1
                        print(f'\033[1;33mGUSTAVO GUANBARA PTB\033[m')
                    elif candidato == '45782':
                        vareadora_Ana_Silva += 1
                        print(f'\033[1;33mANA SILVA AGIR\033[m')
                    elif candidato == '98547':
                        vareador_Carlos_Ribeiro += 1
                        print(f'\033[1;33mCARLOS RIBEIRO PCdoB\033[m')
                    elif candidato == '23458':
                        vareador_Antonio_Alves += 1
                        print(f'\033[1;33mANTONIO ALVES PSC\033[m')
                    elif candidato == '02147':
                        vareador_Felipe_Silva += 1
                        print(f'\033[1;33mFELIPE SILVA DC\033[m')
                    elif candidato == '32587':
                        vareador_Maria_Conde += 1
                        print(f'\033[1;33mMARIA CONDE MARVEL\033[m')
                    elif candidato == '15985':
                        vareador_Rui_Ventura += 1
                        print(f'\033[1;33mRUI VENTURA PRTB\033[m')
                else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
                    print(f'\033[31mNumero invalido o voto sera computado como NULO!\033[m')
                sleep(1)

            if candidato.isalpha():  # checa se candidato contem apenas letras
                if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
                    print()

                    resposta = menu(['Continuar Votacao', 'Finalizar Votacao'])

                    if resposta == 2:
                        print()
                        print_resultados()
                        print()


        def print_resultados():  # printa resultados e encerra programa
            global prefeita_Maria_do_Jurunas, prefeito_Jose_da_Silva, prefeito_Joao_do_Tapana, vereador_Jadson_silva, \
                vereadora_Marcia_Nina, vareador_Joao_Ribeiro, vareador_Gustavo_Guanabara, vareadora_Ana_Silva, \
                vareador_Carlos_Ribeiro, vareador_Antonio_Alves, vareador_Felipe_Silva, vareador_Maria_Conde, \
                vareador_Rui_Ventura

            print('QUANTIDADE DE VOTOS:\n')
            print('PREFEITO JOSÉ DA SILVA     - TOTAL DE VOTOS ' + str(prefeito_Jose_da_Silva))
            print('PREFEITA MARIA DO JURUNAS  - TOTAL DE VOTOS ' + str(prefeita_Maria_do_Jurunas))
            print('PREFEITO JOÃO DO TAPANÃ    - TOTAL DE VOTOS ' + str(prefeito_Joao_do_Tapana))
            print('VEREADOR JADSON SILVA      - TOTAL DE VOTOS ' + str(vereador_Jadson_silva))
            print('VEREADORA MARCIA NINA      - TOTAL DE VOTOS ' + str(vereadora_Marcia_Nina))
            print('VEREADOR JOAO RIBEIRO      - TOTAL DE VOTOS ' + str(vareador_Joao_Ribeiro))
            print('VEREADOR GUSTAVO GUANABARA - TOTAL DE VOTOS ' + str(vareador_Gustavo_Guanabara))
            print('VEREADORA ANA SILVA        - TOTAL DE VOTOS ' + str(vareadora_Ana_Silva))
            print('VEREADORA CARLOS RIBEIRO   - TOTAL DE VOTOS ' + str(vareador_Carlos_Ribeiro))
            print('VEREADORA ANTONIO ALVES    - TOTAL DE VOTOS ' + str(vareador_Antonio_Alves))
            print('VEREADORA FELIPE SILVA     - TOTAL DE VOTOS ' + str(vareador_Felipe_Silva))
            print('VEREADORA MARIA CONDE      - TOTAL DE VOTOS ' + str(vareador_Maria_Conde))
            print('VEREADORA RUI VENTURA      - TOTAL DE VOTOS ' + str(vareador_Rui_Ventura))

            exit()  # encerra prog


        if __name__ == '__main__':  # funcao main
            prefeita_Maria_do_Jurunas = 0
            prefeito_Jose_da_Silva = 0
            prefeito_Joao_do_Tapana = 0
            vereador_Jadson_silva = 0
            vereadora_Marcia_Nina = 0
            vareador_Joao_Ribeiro = 0
            vareador_Gustavo_Guanabara = 0
            vareadora_Ana_Silva = 0
            vareador_Carlos_Ribeiro = 0
            vareador_Antonio_Alves = 0
            vareador_Felipe_Silva = 0
            vareador_Maria_Conde = 0
            vareador_Rui_Ventura = 0

            while True:  # laço ocorre indefinidamente ate que ocorra o 'Fim'
                print()
                candidato = str(input('ELEIÇÃO ESPECIAL\nDigite o numero do seu candidato: '))
                print()
                votacao(candidato)


    elif resposta == 3:
        print('NULO', 'Votacao Encerrada!')
        break
    else:
        print('\033[31mERRO', 'Digite uma opcao valida!\033[m')
        sleep(2)
