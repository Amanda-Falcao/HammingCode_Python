
# HammingCode_Python

O Código de Hamming é um método de detecção e correção de erros em transmissões digitais. Foi criado por Richard Hamming em 1950 e é amplamente utilizado em sistemas de comunicação digital. 

O código de Hamming adiciona bits de verificação de paridade aos dados originais, permitindo que os erros sejam detectados e corrigidos. O código é baseado em operações binárias, como XOR e AND, e usa matemática modular para identificar e corrigir erros. 

Ele é frequentemente usado em sistemas de armazenamento de dados, como discos rígidos e memórias flash, bem como em sistemas de comunicação de dados, como redes de computadores e satélites. O código de Hamming é uma técnica importante para garantir a integridade dos dados em transmissões digitais e tem sido fundamental para o desenvolvimento de tecnologias modernas de comunicação.

O Código seguirá um escopo pré-estabelecido, que apresenta as seguintes características:

..:: GERADOR E VERIFICADOR DE CÓDIGO DE HAMMING ::..

Digite o que você deseja fazer:

1- Enviar um grupo de bits

2- Verificar um grupo de bits recebido

3- Sair

Opção:
#### Caso 1:
Digite a quantidade de bits do grupo original: 7

Digite o número 1: 0

Digite o número 2: 0

Digite o número 3: 0

Digite o número 4: 1

Digite o número 5: 0

Digite o número 6: 0

Digite o número 7: 1

Dados Originais: 0001001

Dados que serão enviados: 00010011001

+++++++++++++++++++++++++++++++++++
#### Caso 2:
Digite a quantidade de bits que foram recebidos: 11

Digite o número 1: 0

Digite o número 2: 0

Digite o número 3: 0

Digite o número 4: 1

Digite o número 5: 0

Digite o número 6: 0

Digite o número 7: 1

Digite o número 8: 1

Digite o número 9: 0

Digite o número 10: 1

Digite o número 11: 1

Foi detectado um erro no bit no 10 do grupo: 00010011011

Grupo de bits finais com o bit corrigido: 0001001

+++++++++++++++++++++++++++++++++++
#### Caso 3:
Encerrar
