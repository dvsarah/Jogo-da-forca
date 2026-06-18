import os.path
import random
import time

dicasExibidas = []
letrasAcertadas = []
contadorErros = 0
contadorTentativas = 0
tempoLimite = 60000

if not os.path.exists("Jogo.txt"):
    print("O arquivo 'Jogo.txt' não existe.")
    exit()

def CarregarPalavra():
    matriz = []
    with open("Jogo.txt", "r", encoding="utf-8") as rank:
        for linha in rank:
            linha = linha.strip()
            if not linha:
                continue
            if linha[0] == "P":
                palavra = linha.split(":", 1)[1].strip()
                matriz.append([palavra])
            elif linha[0] == "D":
                if not matriz:
                    continue
                dica_conteudo = linha.split(":", 1)[1].strip()
                matriz[-1].append(f"Dica: {dica_conteudo}")
    return matriz

def AleatorizarPalavra():
    matriz = CarregarPalavra()
    totalLinhas = len(matriz) 
    indiceLinha = random.randint(0, totalLinhas - 1) 
    palavraSorteada = matriz[indiceLinha][0]
    return palavraSorteada, indiceLinha

def AleatorizarDicas(linha):
    global dicasExibidas
    matriz = CarregarPalavra()
    totalColunas = len(matriz[linha])
    
    indiceColuna = random.randint(1, totalColunas - 1)
    
    tentativas = 0
    while indiceColuna in dicasExibidas and tentativas < 30:
        indiceColuna = random.randint(1, totalColunas - 1)
        tentativas += 1 
        
    if indiceColuna not in dicasExibidas:
        dicasExibidas.append(indiceColuna)
        
    return matriz[linha][indiceColuna]

palavra, linha = AleatorizarPalavra()

def ExibirPalavra(tentativa, contadorErros, letrasAcertadas, palavra):
    acertouPalavra = False

    if len(tentativa) == 1:
        if tentativa in palavra.lower():
            if tentativa not in letrasAcertadas:
                letrasAcertadas.append(tentativa)
        else:
            contadorErros += 1

    elif tentativa == palavra.lower():
        acertouPalavra = True
    else:
        contadorErros += 1

    if contadorErros > 0:
        Erros(contadorErros)

    letras_descobertas = 0
    print("     ", end="")
    for letra in palavra.lower():
        if letra in letrasAcertadas:
            print(letra.upper(), end=" ")
            letras_descobertas += 1
        else:
            print("_", end=" ")
    print("")

    if letras_descobertas == len(palavra):
        acertouPalavra = True

    return contadorErros, acertouPalavra

def InicioDeJogo(palavra):
    print("\n     ", end="")
    for letra in palavra.lower():
        print("_", end=" ")
    print("")

def Erros(contadorErros):
    if contadorErros == 0:
        print("""                 ______
                /      \\
               /        \\
               \\        /
                \\______/""")
    elif contadorErros == 1:
        print("""                 ______
                / O  O \\
               /        \\
               \\        /
                \\______/""")
    elif contadorErros == 2:
        print("""                 ______
                / O  O \\
               /    ^   \\
               \\        /
                \\______/""")
    elif contadorErros == 3:
        print("""                 ______
                / O  O \\
               /    ^   \\
               \\ \\____/ /
                \\______/""")
    elif contadorErros == 4:
        print("""                 ______
                / O  O \\
               /    ^   \\
               \\ \\____/ /
                \\______/
                    |
                    |
                    |
                    |""")
    elif contadorErros == 5:
        print("""                 ______
                / O  O \\
               /    ^   \\
               \\ \\____/ /
                \\______/
                    |
                    |
                    |
                    |
                     \\
                      \\
                       \\""")
    elif contadorErros == 6:
        print("""                 ______
                / O  O \\
               /    ^   \\
               \\ \\____/ /
                \\______/
                    |
                    |
                    |
                    |
                   / \\
                  /   \\
                 /     \\""")
    elif contadorErros == 7:
        print("""                 ______
                / O  O \\
               /    ^   \\
               \\ \\____/ /
                \\______/
                    |
                    |_______
                    |
                    |
                   / \\
                  /   \\
                 /     \\""")
    elif contadorErros == 8:
        print("""                 ______
                / O  O \\
               /    ^   \\
               \\ \\____/ /
                \\______/
                    |
             _______|_______
                    |
                    |
                   / \\
                  /   \\
                 /     \\""")
        
def FimDeJogo():    
    print("""                 ______
                / X  X \\
               /  ____  \\
               \\ /    \\ /
                \\___X__/
                   /|\\
                  /_|_\\
                    |
                    |
                   / \\
                  /   \\
                 /     \\    """)

def DesejaJogarNovamente():
    while True:
        pergunta = input("Deseja jogar novamente? (S/N): ").lower().strip()
        if pergunta == "s":
            return True
        elif pergunta == "n":
            return False
        print("Resposta inválida! Digite 'S' para Sim ou 'N' para Não.")

def ReiniciarJogo():
    global dicasExibidas
    dicasExibidas = []
    
    palavra, linha = AleatorizarPalavra()
    return palavra, linha, [], [], 0, 0, False
    
def Main():
    os.system('cls')
    print("\nMariana Coronado Teixera; RA: 1680972611016")
    print("Pedro Henrique Rodrigues Pimenta; RA: 1680972611015")
    print("Sarah Dias Viana; RA: 1680972611011\n")

    print("JOGO [X] | DICAS [x] | CONTROLE DE TEMPO [X]\n")

    print("- JOGO DA FORCA - | - TEMA: Comidas -")
    print("Você tem 10 tentativas e 1 minuto. Boa sorte!")

    palavra, linha, letrasAcertadas, letrasTentadas, contadorErros, contadorTentativas, acertouPalavra = ReiniciarJogo()
    dica_atual = AleatorizarDicas(linha)
    tempoInicial = int(time.perf_counter() * 1000)
    tempoDeJogo = 0

    InicioDeJogo(palavra)

    while tempoDeJogo < tempoLimite:
        tempoAtual = int(time.perf_counter() * 1000)
        tempoDeJogo = tempoAtual - tempoInicial

        time.sleep(0.1)

        print(dica_atual)
        tentativa = input("Digite uma letra (ou 'dica' para ajuda): ").lower().strip()

        if tentativa == "dica":
            if contadorTentativas == 9:
                print("\nVocê pediu dica restando apenas 1 vida! GAME OVER automático!")
                Erros(10)
                FimDeJogo()
                return

            print("\n--- Nova Dica Solicitada! ---")
            dica_atual = AleatorizarDicas(linha)

            contadorErros += 1
            contadorTentativas += 1

            if contadorTentativas >= 10:
                print("\n           VOCÊ PERDEU!")
                FimDeJogo()
                print(f"A palavra era: {palavra.upper()}\n")
                return

            Erros(contadorErros)
            continue

        if len(tentativa) == 1:
            if tentativa in letrasTentadas:
                print("\nVocê já tentou essa letra! Tente outra.")
                continue
            else:
                letrasTentadas.append(tentativa)

        contadorErros, acertouPalavra = ExibirPalavra(tentativa, contadorErros, letrasAcertadas, palavra)     
        contadorTentativas += 1
        
        if acertouPalavra:
            print(f"\nPARABÉNS! A palavra era: {palavra.upper()}")
            print("FIM DE JOGO! VOCÊ VENCEU! \n")
            return

        if contadorTentativas >= 10:
            print("- FIM DAS TENTATIVAS -")
            print("\n               VOCÊ PERDEU!")
            FimDeJogo()
            print(f"A palavra era: {palavra.upper()}\n")
            return

        dica_atual = AleatorizarDicas(linha)

    print("Tempo limite atingido!")
    print("\n           VOCÊ PERDEU!")
    FimDeJogo()
    print(f"A palavra era: {palavra.upper()}\n")
    
while True:
    Main()
    if not DesejaJogarNovamente():
        print("\nObrigado por jogar! Até a próxima. ")
        break