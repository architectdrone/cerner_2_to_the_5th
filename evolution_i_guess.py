import random
import sys
iterations = int(sys.argv[1])
population_count = int(sys.argv[2])
sequence_length = int(sys.argv[3])
sequence_choices = int(sys.argv[4])
mutation_chance = float(sys.argv[5])
population = [[random.randrange(0,sequence_choices) for i in range(sequence_length)] for i in range(population_count+1)]
optimal = population[0] 
population = population[1:]
def y_combinator(a, b):
    return [(a_i if random.randrange(0, 2) else b_i) for a_i, b_i in zip(a, b)]
def mutate_individual(individual):
    return [(i if random.random() > mutation_chance else random.randrange(0,sequence_choices)) for i in individual]
def random_baby(parent_list):
    return mutate_individual(y_combinator(random.choice(parent_list), random.choice(parent_list)))
print(f"{optimal} <- OPTIMAL")
for i in range(iterations):
    ranked_population = []
    for individual in population:
        ranked_population.append((sum([(1 if a ==b else 0) for a, b in zip(individual, optimal)])/sequence_length, individual))
    ranked_population.sort(key=(lambda a: a[0]), reverse=True)
    population = [random_baby([i[1] for i in ranked_population[0:5]]) for i in range(population_count)]
    print(f"{ranked_population[0][1]} Fitness: {ranked_population[0][0]}")
    if (ranked_population[0][0] == 1):
        print(f"Converged in {i} iterations")
        break

'''
Does a really bad simulation of evolution.
"Organisms" in the world are a list of elements. They evolve to match the optimal.
The five of each population that are the closest to the optimal breed to create the next generation. Both parents are fed into a Y-Combinator and there is a small chance of mutation. 
USAGE: python evolution_i_guess.py <iterations> <population size> <sequence length> <sequence choices> <mutation chance>

EXAMPLE:
PS C:\dev\personal> python .\evolution_i_guess.py 20 20 10 5 0.1
[2, 1, 4, 3, 3, 0, 3, 1, 2, 1] <- OPTIMAL
[2, 4, 0, 3, 2, 4, 3, 1, 4, 1] Fitness: 0.5
[0, 1, 1, 3, 4, 0, 4, 3, 2, 1] Fitness: 0.5
[4, 1, 1, 3, 4, 0, 3, 3, 2, 1] Fitness: 0.6
[2, 1, 2, 3, 4, 0, 4, 3, 2, 1] Fitness: 0.6
[2, 1, 1, 3, 4, 0, 3, 4, 2, 1] Fitness: 0.7
[2, 1, 1, 3, 2, 0, 3, 1, 2, 1] Fitness: 0.8
[2, 1, 1, 3, 3, 0, 3, 1, 2, 1] Fitness: 0.9
[2, 1, 1, 3, 3, 0, 3, 1, 2, 1] Fitness: 0.9
[2, 1, 1, 3, 3, 0, 3, 1, 2, 1] Fitness: 0.9
[2, 1, 1, 3, 3, 0, 3, 1, 2, 1] Fitness: 0.9
[2, 1, 1, 3, 3, 0, 3, 1, 2, 1] Fitness: 0.9
[2, 1, 1, 3, 3, 0, 3, 1, 2, 1] Fitness: 0.9
[2, 1, 1, 3, 3, 0, 3, 1, 2, 1] Fitness: 0.9
[2, 1, 4, 3, 3, 0, 3, 1, 2, 1] Fitness: 1.0
Converged in 13 iterations
'''