# src/genotype_mapping.py

def map_genotype(genotype, grammar, start_symbol="<expr>"):
    """
    Maps an integer genotype to a Boolean expression (phenotype)
    using the grammar-guided expansion.
    """

    expression = start_symbol
    gene_index = 0

    # Continue until no non-terminals or genes exhausted
    while "<" in expression and gene_index < len(genotype):
        for non_terminal in grammar.rules:
            if non_terminal in expression:
                productions = grammar.get_productions(non_terminal)
                choice = genotype[gene_index] % len(productions)
                
                expression = expression.replace(
                    non_terminal, productions[choice], 1
                )
                
                gene_index += 1
                break

    return expression
