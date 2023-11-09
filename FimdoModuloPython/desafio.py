"""
DESAFIO FINAL DO MÓDULO PYTHON - CAMPINHO DIGITAL / AWS re/Start


Escreva um script Python para:

Exibir todos os números primos entre 1 e 250.
Armazenar os resultados em um arquivo results.txt.
Teste o script. Verifique se ele produziu os resultados esperados no arquivo results.txt.

Salve o script e anote sua localização (caminho absoluto) para referência futura.
"""

#Função para verificar se um número é um Número Primo.
def verificar_primo(numero):
    if numero <= 1:
        return False
    i = 2
    while i < numero:
        if numero % i == 0:   
            return False
        i += 1
    return True

numeros_primos = []

print("\nVamos lá: Digite um número inicial e final para que eu possa escrever um arquivo apenas com os números primos no range que você escolher.\n")
inicio = int(input("Número inicial: \n"))
fim = int(input("Número final: \n"))

# Loop que vai de inicial até final definido pelo usuario chamando a função para verificar se o número é primo e adicionando os números primos a um array.
for contador in range(inicio, fim):
    if verificar_primo(contador) == True:
        numeros_primos.append(contador)

print(numeros_primos)
print("\nGerando arquivo .TXT com os números primos descritos acima...\n")
      
with open("primos.txt", "w") as arquivo:
    arquivo.write(str(numeros_primos))

print("Arquivo 'primos.txt' criado com sucesso, até logo...")
