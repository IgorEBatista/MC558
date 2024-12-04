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
    n_vars = max(var for clause in cnf_formula for var, _ in clause)
    base = 3072 * (n_vars ** 3)

    # Definir letras de controle 0 e 1
    letters.update(['0', '1'])

    # Adicionar colunas para variáveis e seus complementos
    for var in range(1, n_vars + 1):
        v = f'v{var}'
        not_v = f'v{var}\''
        letters.update([v, not_v])
        # Adicionar colunas conforme o padrão descrito no artigo
        columns.append((f'd{var}', f'e{var}', f'{v}', f'{not_v}'))

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

    return {
        "columns": columns,
        "letters": letters,
        "base": base
    }

# Exemplo de uso:
# Fórmula: (x1 OR NOT x2 OR x3) AND (NOT x1 OR x2 OR x3)
cnf_formula = [
    [(1, False), (2, True), (3, False)],  # x1 OR NOT x2 OR x3
    [(1, True), (2, False), (3, False)]  # NOT x1 OR x2 OR x3
]

cryptarithm_instance = reduce_3sat_to_cryptarithm(cnf_formula)
print("Cryptarithm Instance:")
print("Columns:", cryptarithm_instance["columns"])
print("Letters:", cryptarithm_instance["letters"])
print("Base:", cryptarithm_instance["base"])
