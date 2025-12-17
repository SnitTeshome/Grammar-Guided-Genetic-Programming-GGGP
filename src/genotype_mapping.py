# src/genotype_mapping.py

def map_genotype(genotype, grammar, start_symbol="<expr>"):
    """
    Optimized mapping of an integer genotype to a Boolean expression (phenotype)
    using grammar-guided expansion.

    Parameters
    ----------
    genotype : list of int
        Sequence of genes guiding production choice.
    grammar : Grammar
        Grammar object containing production rules.
    start_symbol : str, optional
        Starting non-terminal symbol (default is "<expr>").

    Returns
    -------
    str
        Fully expanded Boolean expression (phenotype).
    """

    expression = start_symbol  # Initialize expression with root
    gene_index = 0             # Start from the first gene

    # Continue expanding until no non-terminals remain or genes exhausted
    while "<" in expression and gene_index < len(genotype):

        # Find the first non-terminal (string enclosed in '<' and '>')
        start = expression.find("<")
        end = expression.find(">", start)
        if start == -1 or end == -1:
            break  # No more non-terminals

        non_terminal = expression[start:end + 1]  # Extract non-terminal

        # Get possible productions for this non-terminal
        productions = grammar.get_productions(non_terminal)

        # Choose production using current gene (wrap around if necessary)
        choice = genotype[gene_index] % len(productions)

        # Replace the first occurrence of this non-terminal
        expression = expression[:start] + productions[choice] + expression[end + 1:]

        gene_index += 1  # Move to next gene

    return expression
