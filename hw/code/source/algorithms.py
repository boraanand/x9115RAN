from __future__ import print_function, division
from util import *
import random as r
from copy import deepcopy
import sys
from math import sqrt, exp, sin
import time
from sk import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import multiprocessing as mp

class ga():
    def __init__(self):
        self.settings = O(
        gens = 500,
        candidates = 100,
        better = lt,
        era = 100,
        retain = 0.33, #retain 33% of parents to next generation
        mutate_prob = 0.05
        )


    def optimize(self, model):
        ##### -- Generate random population in beginning --  #####
        population = [model.generate() for _ in range(self.settings.candidates * 5)]    
        frontier = []

        for can_1 in population:
            count = 1  # Number of candidates that can_1 dominates
            for can_2 in population:
                if model.cdom(can_1, can_2):
                    count += 1
            frontier.append((can_1, count))

        frontier = sorted(frontier, key = lambda (can, score): score)
        frontier = [can for can, score in frontier]
        population = frontier[:self.settings.candidates]

        
        sorted_population = sorted(population,  key=lambda x: model.energy(x))
        e_best = model.energy(sorted_population[0])

        #### Log initial settings
        print(model)
        print("Settings: ")
        print(self.settings)
        print("Best Denormalized Energy Before optimization:" + str(e_best) )    



        ######  Now the Evolution Begins    ###############
        for i in range(self.settings.gens):            
            # For the entire population, calculate its fitness score.
            # Fitness score is number of other can that a point dominates
            # After fitness calculation, retain x% of population as parents into next gen
            parents_with_score = self.elite_sampling(population, model, self.settings.retain)

            # Add all the elite parents to next generation
            next_generation = [can for can, score in parents_with_score]
            
            num_of_children = self.settings.candidates - len(next_generation)

          
            for _ in range(num_of_children ):
                papa, mama = ga.select(parents_with_score)
                new_can = ga.crossover(papa, mama)
                new_can = ga.mutate(new_can, model, self.settings.mutate_prob)
                next_generation.append(new_can)
        
            population = next_generation[:]
        
        ####### Sort the frontier according to Energy
        population.sort(key=lambda can: model.energy(can))
        e_best = model.energy(population[0])
        print("\nBest Denormalized Energy:" + str(e_best) )


        ###### Plot the Frontier
        ga.graph_it(population, model)
  

    @staticmethod
    def elite_sampling(population, model, retain):
        """ 
            population: ith population
            model: the instance of model we are using
            retain: '%' of population to retain in next generation

            returns list of (can, score) of elite population
        """
        pop_dominations = []
        
        #Apply all pair binary dominations
        for can_1 in population:
            count = 1  # Number of candidates that can_1 dominates
            for can_2 in population:
                if model.cdom(can_1, can_2):
                    count += 1
            pop_dominations.append((can_1, count))

        pop_dominations.sort(key=lambda (can, score): score, reverse=True)
        n = len(pop_dominations) 
        elites = pop_dominations[:int(retain*n)]   
        elites += pop_dominations[-int(retain*n):]      
        return elites

    @staticmethod
    def select(elite_population):
        # Create a weighted roulette 
        # Each candidate will be added number of times its score
        roulette = []
        for can, score in elite_population:
            roulette.append(can)

        #for can, score in elite_population:
        #    roulette += [can] * score

        papa = r.choice(roulette)

        while True:
            mama = r.choice(roulette)
            if mama != papa: break
        
        return (papa, mama)

    @staticmethod
    def crossover(papa, mama):
        pos = r.randint(0, len(papa.decs) - 1)
        can = papa.clone()
        can.decs[pos:] = mama.decs[pos:]
        return can

    @staticmethod
    def mutate(new_can, model, mutate_prob):
        # TODO: Any specific mutation method ??
        if r.random() > mutate_prob:
            return new_can

        for _ in range(int(len(new_can.decs)/4)):
            pos = r.randint(0, len(new_can.decs) - 1)
            new_can.decs[pos] = r.uniform(model.decs[pos].low, model.decs[pos].high)
        return new_can

    @staticmethod
    def graph_it(population, model):
        final_frontier = [ model.eval(can) for can in population ]

        # Plot results only if 2 or 3 dimensional
        if model.m == 2:
            # Plot results
            f1 = np.array([x[0] for x in final_frontier])
            f2 = np.array([x[1] for x in final_frontier])
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(f1, f2)
            ax.set_xlabel('f1')
            ax.set_ylabel('f2')
            fig.savefig(model.__class__.__name__)
        elif model.m == 3:
            # Plot results
            f1 = np.array([x[0] for x in final_frontier])
            f2 = np.array([x[1] for x in final_frontier])
            f3 = np.array([x[2] for x in final_frontier])
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(f1, f2, f3)
            ax.set_xlabel('f1')
            ax.set_ylabel('f2')
            ax.set_zlabel('f3')
            fig.savefig(model.__class__.__name__)


