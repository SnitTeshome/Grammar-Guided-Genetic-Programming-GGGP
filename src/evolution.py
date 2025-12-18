# src/evolution.py

"""
Evolutionary logic for Grammar-Guided Genetic Programming (GGGP).

This module handles:
- Population initialization
- Genotype → Phenotype mapping
- Fitness evaluation with complexity penalty
- Selection of best individuals
- Multi-generation evolution (elitism + mutation)
"""

import random
from src.genotype_mapping import map_genotype
from src.complexity import final_score


def initialize_population(pop_size, genotype_length):
    """
    Initialize a random population of genotypes.
    """
    return [
        [random.randint(0, 10) for _ in range(genotype_length)]
        for _ in range(pop_size)
    ]


def evaluate_population(population, grammar, variable_values, alpha=1.0):
    """
    Evaluate all individuals in the population.
    """
    results = []
    for genotype in population:
        phenotype = map_genotype(genotype, grammar)
        score = final_score(phenotype, variable_values, alpha)
        results.append((genotype, phenotype, score))
    return results


def select_best(evaluated_population, k=2):
    """
    Select the top k individuals based on final score.
    """
    evaluated_population.sort(key=lambda x: x[2], reverse=True)
    return evaluated_population[:k]


def mutate(genotype, mutation_rate=0.1):
    """
    Mutate a genotype by randomly changing some genes.
    """
    new_genotype = genotype.copy()
    for i in range(len(new_genotype)):
        if random.random() < mutation_rate:
            new_genotype[i] = random.randint(0, 10)
    return new_genotype


def run_gggp(
    grammar,
    variable_values,
    pop_size=5,
    genotype_length=10,
    generations=10,
    elite_size=2,
    mutation_rate=0.1,
    alpha=1.0,
):
    """
    Run Grammar-Guided Genetic Programming for multiple generations.

    Parameters
    ----------
    grammar : Grammar
        Grammar object
    variable_values : dict
        Variable assignments for fitness evaluation
    pop_size : int
        Population size
    genotype_length : int
        Length of each genotype
    generations : int
        Number of generations to evolve
    elite_size : int
        Number of best individuals preserved each generation
    mutation_rate : float
        Probability of mutating each gene
    alpha : float
        Complexity penalty weight

    Returns
    -------
    list of tuples
        Best individuals from the final generation
    """
    # ----- Generation 0 -----
    population = initialize_population(pop_size, genotype_length)

    for gen in range(generations):
        print(f"\n=== Generation {gen} ===")

        evaluated = evaluate_population(
            population, grammar, variable_values, alpha
        )

        best = select_best(evaluated, k=elite_size)

        for g, e, s in best:
            print("Best phenotype:", e, "| Score:", s)

        # ----- Create next generation -----
        elites = [g for g, _, _ in best]
        new_population = elites.copy()

        while len(new_population) < pop_size:
            parent = random.choice(elites)
            child = mutate(parent, mutation_rate)
            new_population.append(child)

        population = new_population

    return best
