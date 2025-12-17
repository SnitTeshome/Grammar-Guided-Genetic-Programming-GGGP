# src/fitness.py
def evaluate_expression(expr, variable_values):
    """
    Evaluate a Boolean expression (phenotype) given variable assignments.

    expr : str
        Boolean expression like "NOT (A AND B) OR C"
    variable_values : dict
        Mapping from variable names to 0/1 values, e.g., {"A":1, "B":0, "C":1}

    Returns
    -------
    int
        Result of expression (0 or 1)
    """
    # Replace variables with their values
    for var, val in variable_values.items():
        expr = expr.replace(var, str(val))

    # Evaluate expression using Python logic operators
    expr = expr.replace("AND", " and ").replace("OR", " or ").replace("NOT", " not ").replace("XOR", " != ")
    return int(eval(expr))
