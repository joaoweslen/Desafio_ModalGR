# Função que remover os conectores do nome
def remove_conectores(nm):
    # Uma lista com os conectores que devem ser removidos
    conectores = [" de ", " da ", " das ", " do ", " dos ", " e "]
    
    # Para cada conector na lista de conectores
    for c in conectores:
        # Substitui o conector por um espaço
        nm = nm.replace(c, " ")
    return nm

# Input do nome, que é salvo já em maiúsculo e separado numa lista
nome = remove_conectores(input("Nome completo colaborador: ")).upper().split()

# Separa as iniciais do nome em uma lista, menos a inicial do ultimo nome
iniciais = [inicial[0] + '.' for inicial in nome[:-1]]

# Armazena o ultimo nome
ultimo_nome = nome[-1]

# Formata no nome que será colocado no crachá
nome_cracha = ultimo_nome + ', ' + ' '.join(iniciais)

print(f"Nome que deverá ser impresso no crachá: {nome_cracha}")