import re


def evaluate_expression(expr, variable_values):
    """
    Evaluate Boolean expression safely.
    """
    if "<" in expr or ">" in expr:
        raise ValueError(f"Unexpanded non-terminals remain in expression: {expr}")

    # Replace variable names only when they appear as whole tokens
    for var, val in variable_values.items():
        expr = re.sub(rf"\\b{re.escape(var)}\\b", str(val), expr)

    # Normalize operators to Python equivalents (use spaces to ensure separation)
    expr = expr.replace("AND", " and ").replace("OR", " or ") \
               .replace("NOT", " not ").replace("XOR", " != ")

    expr = " ".join(expr.split())
    return int(eval(expr))
