def reduce_3sat_to_cryptarithm(cnf_formula):
    """
    Reduz uma fórmula 3-SAT em CNF para uma instância de cryptarithm.
    
    Args:
        cnf_formula (list of list of tuples): Fórmula 3-CNF, onde cada cláusula é uma lista de literais.
            Um literal é representado como (var, is_negated), onde:
                - var é o índice da variável (int).
                - is_negated é True se o literal é negado, False caso contrário.

    Returns:
        dict: Um dicionário representando o cryptarithm, com:
            - "columns": Colunas do cryptarithm (list of tuples).
            - "letters": Conjunto de letras usadas.
            - "base": A base mínima necessária.
    """
    letters = set()
    columns = []
    lines = [[], [], []]
    n_vars = max(var for clause in cnf_formula for var, _ in clause)
    base = 3072 * (n_vars ** 3)

    # Definir letras de controle 0 e 1
    letters.update(['0', '1'])

    # Adicionar colunas para variáveis e seus complementos

    # Adicionar colunas para cada cláusula
    for i, clause in enumerate(cnf_formula):
        clause_vars = [f'v{var}' if not negated else f'v{var}\''
                       for var, negated in clause]
        clause_columns = [
            (f'a{i}', clause_vars[0], f'b{i}'),
            (f'c{i}', clause_vars[1], f'd{i}'),
            (f'e{i}', clause_vars[2], f'f{i}')
        ]
        columns.extend(clause_columns)
        letters.update([f'a{i}', f'b{i}', f'c{i}', f'd{i}', f'e{i}', f'f{i}'])
        soma = f'u{clause_vars[0][1:]}{clause_vars[1][1:]}'

        # Adicionar linhas para cada cláusula
        lines[0].extend([soma, '0', f'{clause_vars[0]}', '0', '1', f'r{i}', '0', f'g{i}', f'w{i}', '0', f'f{i}', '0'])
        lines[1].extend([f'{clause_vars[2]}', '0', f'{clause_vars[1]}', '0', f'h{i}', f'r{i}', '0', f'g{i}', f'w{i}', '0', f'f{i}', '0'])
        lines[2].extend([f't{i}', '0', soma, '0', f't{i}', f's{i}', '0', f'h{i}', f'x{i}', '0', f'g{i}', '0'])

    #Agora, para cada variável, adicionaremos as colunas correspondentes
    for var in range(1, n_vars + 1):
        v = f'V{var}'
        not_v = f'V{var}\''
        letters.update([v, not_v])
        # # Adicionar colunas conforme o padrão descrito no artigo
        lines[0].extend([f'd{var}', '0', '1', f'y{var}', '0', f'c{var}', f'y{var}', '0', f'b{var}', f'y{var}', '0', f'a{var}', '0'])
        lines[1].extend([f'e{var}', '0', f'd{var}', f'y{var}', '0', f'c{var}', f'y{var}', '0', f'b{var}', f'y{var}', '0', f'a{var}', '0'])
        lines[2].extend([not_v, '0', f'e{var}', f'z{var}', '0', f'd{var}', f'z{var}', '0', v, f'z{var}', '0', f'b{var}', '0'])

    #Por fim, adicionamos as 3 colunas da direita, para controle
    lines[0].extend(['0', 'p', '0'])
    lines[1].extend(['0', 'p', '0'])
    lines[2].extend(['1', 'q', '0'])

    print("Lines:")
    for line in lines:
        print(" ".join(f"{term:>3}" for term in line))

    return {
        "columns": columns,
        "letters": letters,
        "base": base
    }

# Exemplo de uso:
# Fórmula: (x1 OR NOT x2 OR x3) AND (NOT x1 OR x2 OR x3)
cnf_formula = [
    [(1, False), (2, True), (3, False)]#,  # x1 OR NOT x2 OR x3
    #[(1, True), (2, False), (3, False)]  # NOT x1 OR x2 OR x3
]

cryptarithm_instance = reduce_3sat_to_cryptarithm(cnf_formula)
print("Cryptarithm Instance:")
print("Columns:", cryptarithm_instance["columns"])
print("Letters:", cryptarithm_instance["letters"])
print("Base:", cryptarithm_instance["base"])
