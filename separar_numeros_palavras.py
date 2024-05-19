# String que desejamos separa
string = "Ana,89,78,Maria,45.8,27,56,Paula Pereira,978,A,VIVA,35,125,8999"
print(f"String Original: {string}")

# Dividi a string numa lista
str_sep = string.split(',')

# Usando list comprehension para formar a lista só com numero e a com palavras
numeros = [itens for itens in str_sep if itens.replace('.', '', 1).isdigit()]
palavras = [itens for itens in str_sep if not itens.replace('.', '', 1).isdigit()]

print(f"Lista de Numeros: {numeros}")
print(f"Lista de Palavras: {palavras}")