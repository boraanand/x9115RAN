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
    population = [model.generate() for _ in range(settings.candidates)]
    sorted_population = sorted(population,  key=lambda x: model.energy(x))
    
    e_best = model.energy(sorted_population[0])

    frontier = sorted_population # Needs to be changed

    for i in range(settings.gens):
        if i % settings.era == 0:
            print('\n')

        papa, mama = select(frontier, model)
        
        #papa = frontier[papa_pos]
        #mama = frontier[mama_pos]
        
        mutate(model, [papa, mama])
        
        new_can = crossover([papa, mama])

        e_new = model.energy(new_can)
        e_papa = model.energy(papa)
        e_mama = model.energy(mama)

        if model.dominates(new_can, papa) and model.dominates(new_can, mama):
            frontier.append(new_can)

        if e_new < e_best:
            e_best = e_new
            print('+', end='')          
        else:
            print('.', end='')

        """
        # TODO : should we replace the parents??
        # frontier.append(new_can)
        energies = [(e_new, np), (e_papa, papa_pos), (e_mama, mama_pos)]

        if e_new < e_papa and e_new < e_mama:
            if e_papa > e_mama:
                frontier[papa_pos] = new_can
            else:
                frontier[mama_pos] = new_can
        elif e_new < e_papa:
            frontier[papa_pos] = new_can
        elif e_new < e_mama:
            frontier[mama_pos] = new_can
        """

    print("\n Best Denormalized Energy:" + str(e_best) )


def select(population, model):
    # TODO: How to select and how many to select?? Not clear about binary
    # domination thing
    """

    """
    elite_population = []

    for can_1 in population:
        for can_2 in population:
            if(model.dominates(can_1, can_2)):
                elite_population.append(can_1)


    a = r.randint(0, len(elite_population) - 1)
    while True:
        b = r.randint(0, len(elite_population) - 1)
        if b != a:
            break
    
    return (elite_population[a], elite_population[b])


def mutate(model, parents, mutate_prob=0.05):
    # TODO: Any specific mutation method ??
    for individual in parents:
        if r.random() < mutate_prob:
            pos = r.randint(0, len(individual.decs) - 1)
            individual.decs[pos] = r.randint(model.decs[pos].low, model.decs[pos].high)


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