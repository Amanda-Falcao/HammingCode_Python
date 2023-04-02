def gerador_Hamming(dadosOriginais):
    """
    Realiza a codificação da mensagem de entrada usando o código de Hamming.
    Retorna a sequência codificada.
    """
    # Calcula o número de bits de paridade necessários.
    m = len(dadosOriginais)
    k = 0
    while 2**k < m + k + 1:
        k += 1
    # Cria a mensagem codificada com bits de paridade inicializados em 0.
    bitsGerados = [0] * (m + k)
    # Preenche os bits de dados na mensagem codificada.
    j = 0
    for i in range(m + k):
        if i+1 == 2**j:
            j += 1
        else:
            bitsGerados[i] = dadosOriginais[i-j]

    # Calcula os bits de paridade e insere na mensagem codificada.
    for i in range(k):
        d = 1 << i  #Retorna "1" com os seus bits movidos "i" casas à esquerda, adicionando zeros aos bits "novos" da direita. Isso é a mesma coisa que multiplicar 1 por 2**i.
        paridade = 0
        for j in range(m + k):
            if (j+1) & d:  #Realiza um "E" binário.
                paridade ^= bitsGerados[j] #operação XOR bit a bit entre as variáveis e, em seguida, atribuiu o resultado à variável à esquerda.
        bitsGerados[2**i-1] = paridade

    return bitsGerados

def verificador_Hamming(bits):
        """
        Realiza a verificação de erro Hamming para uma sequência de bits.
        Retorna a sequência corrigida, caso haja erro. Caso contrário, retorna a sequência original.
        """
        # Calcula o número de bits de paridade (r) e cria uma cópia da lista original, uma lista auxiliar para manter os dados fornecidos.
        listAuxiliar  = bits.copy()
        r = 0
        while 2**r < len(bits) + r + 1:
            r += 1
        
        # Calcula os valores das posições de paridade.
        posicoes_paridade = []
        for i in range(r):
            posicoes_paridade.append(2**i - 1)
        
        # Calcula os valores das paridades para cada posição de paridade.
        posicao_paridades = []
        for p in posicoes_paridade:
            # Soma os valores dos bits nas posições correspondentes a esta paridade.
            paridade = sum([bits[i] for i in range(len(bits)) if ((i+1) & (p+1))])
            # Verifica se a paridade é ímpar.
            if paridade % 2 == 0:
                posicao_paridades.append(0)
            else:
                posicao_paridades.append(1)
        
        # Calcula o valor da posição do bit com erro, se houver erro.
        posicao_erro = 0
        for i in range(len(posicao_paridades)):
            posicao_erro += posicao_paridades[i] * (2**i)
        
        # Verifica se há erro na sequência de bits.
        if posicao_erro != 0:
            # Inverte o valor do bit com erro.
            bits[posicao_erro - 1] = 1 - bits[posicao_erro - 1]
            print('\n')
            print('Foi detectado um erro no bit nº {} do grupo: '.format(posicao_erro), end='')
            for a in range (0, len(bits)):
                print(listAuxiliar[a], end='')
            print('\n')
        # Retorna a sequência corrigida, se houver erro, ou a sequência original, se não houver erro.
        return bits

print('..::GERADOR E VERIFICADOR DE CODIGO DE HAMMING::..')
print('\n')
print('Digite o que você deseja fazer:')
print('1) Enviar um grupo de bits')
print('2) Verificar um grupo de bits recebido')
print('3) Sair')
while True:
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('Opção 1 selecionada!')
        print('#Caso 1')   
        numBits = int(input('Digite a quantidade de bits do grupo original:'))
        dadosOriginais = list(range(0, numBits))
        for c in range (0, numBits):
            dadosOriginais[c] = int(input('Digite o número {}:'.format(c+1)))
            while True:
                if  dadosOriginais[c] == 1 or dadosOriginais[c] == 0 :
                    break
                else:
                    print('Digite um/apenas um bit válido:')
                    dadosOriginais[c] = int(input('Digite o número {}:'.format(c+1)))
        print('\n')
        print('Dados Originais: ', end='')
        for a in range (0, numBits):
            print(dadosOriginais[a], end='')
        print('\n')
        dadosGerados = gerador_Hamming(dadosOriginais)
        print('Dados que serão enviados: ', end='')
        for a in range (0, len(dadosGerados)):
            print(dadosGerados[a], end='')
        break
    elif opcao == 2:
        print('Opção 2 selecionada!')
        print('#Caso 2')   
        numBits2 = int(input('Digite a quantidade de bits que foram recebidos:'))
        dadosRecebidos = list(range(0, numBits2))
        for b in range (0, numBits2):
            dadosRecebidos[b] = int(input('Digite o número {}:'.format(b+1)))
            while True:
                if  dadosRecebidos[b] == 1 or dadosRecebidos[b] == 0 :
                    break
                else:
                    print('Digite um/apenas um bit válido:')
                    dadosRecebidos[b] = int(input('Digite o número {}:'.format(b+1)))
        verificador_Hamming(dadosRecebidos)
        print('Grupo de bits com o bit corrigido: ', end='')
        for a in range (0, len(dadosRecebidos)):
            print(dadosRecebidos[a], end='')
        break
    elif opcao == 3:
        break
    else:
        print('Selecione uma opção válida')







