import re

def evaluate_expression(expr, variable_values):
    if "<" in expr or ">" in expr:
        raise ValueError(f"Unexpanded non-terminals remain in expression: {expr}")

    for var, val in variable_values.items():
        expr = re.sub(rf"\b{re.escape(var)}\b", str(val), expr)

    expr = expr.replace("AND", " and ").replace("OR", " or ") \
               .replace("NOT", " not ").replace("XOR", " != ")

    expr = " ".join(expr.split())
    return int(eval(expr))
