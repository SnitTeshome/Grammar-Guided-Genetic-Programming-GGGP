# src/complexity.py

def complexity(expression):
    """
    Compute complexity of a Boolean expression.
    
    Parameters
    ----------
    expression : str
        Fully expanded Boolean expression (phenotype)
        
    Returns
    -------
    int
        Complexity score (higher = more complex)
    """
    # Count spaces as a simple proxy for number of operators and terms
    return expression.count(" ")


def final_score(expression, variable_values, alpha=1.0):
    """
    Combine fitness and complexity to compute final score.

    Parameters
    ----------
    expression : str
        Phenotype expression
    variable_values : dict
        Mapping from variable names to 0/1 values for fitness evaluation
    alpha : float
        Weight for complexity penalty
    
    Returns
    -------
    float
        Final score: fitness - alpha * complexity
    """
    from src.fitness import evaluate_expression

    fitness = evaluate_expression(expression, variable_values)
    penalty = complexity(expression)

    return fitness - alpha * penalty
