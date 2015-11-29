from __future__ import print_function, division
import random as r
import math
from copy import deepcopy
import sys
from math import sqrt, exp, sin
from models import *
from util import *

def ga(model):
    settings = O(
        gens = 1000,
        candidates = 100,
        better = lt,
        era = 100
    )
 
    global era_cur, era_prev, np

    

    # Generate random population in beginning
    population = [model.generate() for _ in range(settings.candidates)]
    
    sorted_population = sorted(population,  key=lambda x: model.energy(x))
    e_best = model.energy(sorted_population[0])
    print("\n Best Denormalized Energy Before optimization:" + str(e_best) )    
    
    for i in range(settings.gens):
        if i % settings.era == 0:
            print('\n')

        # Add top 20% of population by domination
        # Add 10% bad performing candidates to increase diversity
        # So 30% of the last population will act as parents.
        elites = elite_sampling(population, model)
        if len(elites) < 2: continue
        next_generation = elites[:]
        # print(len(elite_population))

        # Add all the elite parents to next generation

        for j in range(settings.candidates):
            papa, mama = select(elites)
            papa, mama = mutate(model, [papa, mama])
            new_can = crossover([papa, mama])
            next_generation.append(new_can)
            e_new = model.energy(new_can)

        population = sorted(next_generation,  key=lambda x: model.energy(x))
        e_new = model.energy(population[0])

        if e_new < e_best:
            e_best = e_new
            print('+', end='')          
        else:
            print('.', end='')

    print("\n Best Denormalized Energy:" + str(e_best) )


def elite_sampling(population, model):
    """ 
        population: ith population
        model: the instance of model we are using
        returns (can, # of domination) that dominate other candidates
    """
    pop_dominations = []
    
    #Apply all pair binary dominations
    for can_1 in population:
        count = 0  # Number of candidates that can_1 dominates
        for can_2 in population:
            if model.dominates(can_1, can_2):
                count += 1
        if count > 0: pop_dominations.append((can_1, count))
    
    pop_dominations.sort(key=lambda x: x[1])

    n = len(pop_dominations)
    #print(n)
    elites = pop_dominations[:int(0.2*n)]   #Top 20%
    elites += pop_dominations[-int(0.1*n):] # bottom 10%

    elites = [ x[0] for x in elites ]   # remove scores
    return elites

def select(elite_population):
    # TODO: How to select and how many to select?? Not clear about binary
    # domination thing
    a = r.randint(0, len(elite_population) - 1)
    while True:
        b = r.randint(0, len(elite_population) - 1)
        if b != a:
            break
    
    return (elite_population[a], elite_population[b])


def mutate(model, parents, mutate_prob=0.05):
    # TODO: Any specific mutation method ??
    result = []
    for individual in parents:
        individual = individual.clone()
        if r.random() < mutate_prob:
            pos = r.randint(0, len(individual.decs) - 1)
            individual.decs[pos] = r.randint(model.decs[pos].low, model.decs[pos].high)
        result.append(individual)
    return result


def crossover(parents, mutate_prob=0.05):
    # TODO: What if more than 2 parents ??
    pos = r.randint(0, len(parents[0].decs) - 1)
    can = parents[0].clone()
    can.decs[pos:] = parents[1].decs[pos:]
    return can


if __name__ == '__main__':
    for model in [DTLZ_7]:
        for optimizer in [ga]:
            optimizer(model())
        print ("\n\n")