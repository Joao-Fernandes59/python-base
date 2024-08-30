"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.

Exemplo:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""


words = []
while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word:    # condição de parada
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiouãâêéóóá":
            final_word += letter * 2
        else:
            final_word += letter
        # If ternário alternativo
        #final_word += letter * 2 if letter.lower() in "aeiouãâêéóóá" else letter 
        
    words.append(final_word)

"""
for word in words:
    print(word)
"""
print(*words, sep="\n") # utilizando o desempacotamento (*), para substituir o for