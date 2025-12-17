# src/grammar.py      → language definition
class Grammar:
    """
    Boolean Grammar for Grammar-Guided Genetic Programming (GGGP)

    <expr>  -> <expr> <bin_op> <expr>
             | <un_op> <expr>
             | <term>

    <bin_op> -> AND | OR | XOR
    <un_op>  -> NOT
    <term>   -> A | B | C | ...
    """
    def __init__(self, variables, binary_operators=None, unary_operators=None):

        if binary_operators is None:
            binary_operators = ["AND", "OR", "XOR"]

        if unary_operators is None:
            unary_operators = ["NOT"]

        self.rules = {
            "<expr>": [
                "( <expr> <bin_op> <expr> )",
                "( <un_op> <expr> )",
                "<term>"
            ],
            "<bin_op>": binary_operators,
            "<un_op>": unary_operators,
            "<term>": variables
        }

    def get_productions(self, non_terminal):
        return self.rules[non_terminal]
