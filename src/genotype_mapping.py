def map_genotype(genotype, grammar, start_symbol="<expr>", max_steps=100):
    """
    Deterministic and safe grammar-guided genotype → phenotype mapping.
    """

    expression = start_symbol
    gene_index = 0
    steps = 0

    while "<" in expression and steps < max_steps:
        start = expression.find("<")
        end = expression.find(">", start)
        if start == -1 or end == -1:
            break

        non_terminal = expression[start:end + 1]
        productions = grammar.get_productions(non_terminal)

        if gene_index < len(genotype):
            choice = genotype[gene_index] % len(productions)
            gene_index += 1
        else:
            # Force safest production when genes are exhausted
            if non_terminal == "<expr>":
                choice = productions.index("<term>")
            else:
                choice = 0

        expression = expression[:start] + productions[choice] + expression[end + 1:]
        steps += 1

    if "<" in expression:
        raise ValueError(f"Incomplete expansion: {expression}")

    return " ".join(expression.split())
