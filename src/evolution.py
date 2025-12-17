# src/evolution.py

"""
Evolutionary logic for Grammar-Guided Genetic Programming (GGGP).

This module handles:
- Population initialization
- Genotype → Phenotype mapping
- Fitness evaluation with complexity penalty
- Selection of best individuals
"""

import random
from src.genotype_mapping import map_genotype
from src.complexity import final_score


def initialize_population(pop_size, genotype_length):
    """
    Initialize a random population of genotypes.

    Parameters
    ----------
    pop_size : int
        Number of individuals in the population.
    genotype_length : int
        Length of each genotype (number of genes).

    Returns
    -------
    list of list of int
        Randomly generated genotypes.
    """
    return [
        [random.randint(0, 10) for _ in range(genotype_length)]
        for _ in range(pop_size)
    ]


def evaluate_population(population, grammar, variable_values, alpha=1.0):
    """
    Evaluate all individuals in the population.

    Maps each genotype to a phenotype using the grammar, 
    then computes a final score combining fitness and complexity.

    Parameters
    ----------
    population : list of list of int
        List of genotypes.
    grammar : Grammar
        Grammar object for mapping genotypes.
    variable_values : dict
        Variable assignments for fitness evaluation.
    alpha : float
        Weight for complexity penalty.

    Returns
    -------
    list of tuples
        Each tuple contains (genotype, phenotype, final_score)
    """
    results = []
    for genotype in population:
        # Map genotype to phenotype
        phenotype = map_genotype(genotype, grammar)
        # Compute final score with complexity penalty
        score = final_score(phenotype, variable_values, alpha)
        results.append((genotype, phenotype, score))
    return results


def select_best(evaluated_population, k=2):
    """
    Select the top k individuals based on their final scores.

    Parameters
    ----------
    evaluated_population : list of tuples
        Each tuple = (genotype, phenotype, final_score)
    k : int
        Number of individuals to select

    Returns
    -------
    list of tuples
        Top k individuals with highest scores.
    """
    # Sort descending by score
    evaluated_population.sort(key=lambda x: x[2], reverse=True)
    return evaluated_population[:k]