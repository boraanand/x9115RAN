from __future__ import print_function, division
from util import *
import random as r
from copy import deepcopy
import sys
from math import sqrt, exp, sin
import time
from sk import *
import matplotlib.pyplot as plt
plt.ion()
from mpl_toolkits.mplot3d import Axes3D

class ga():
    def __init__(self):
        self.settings = O(
        gens = 1000,
        candidates = 100,
        better = lt,
        era = 100,
        retain = 0.2, #retain 20% of parents to next generation
        mutate_prob = 0.05
        )


    def optimize(self, model):
        # Generate random population in beginning
        population = [model.generate() for _ in range(self.settings.candidates)]    
        sorted_population = sorted(population,  key=lambda x: model.energy(x))
        e_best = model.energy(sorted_population[0])
        print(model)
        print("Settings: ")
        print(self.settings)
        print("Best Denormalized Energy Before optimization:" + str(e_best) )    

        current_era = []
        prev_era = [-1] * self.settings.era

        for i in range(self.settings.gens):
            
            # For the entire population, calculate its fitness score.
            # Fitness score is number of other can that a point dominates
            # After fitness calculation, retain x% of population as parents into next gen
            parents_with_score = self.elite_sampling(population, model, self.settings.retain)

            # Add all the elite parents to next generation
            next_generation = [can for can, score in parents_with_score]
            
            num_of_children = self.settings.candidates - len(next_generation)

            for j in range(num_of_children):
                papa, mama = self.select(parents_with_score)
                new_can = self.crossover([papa, mama])
                new_can = self.mutate(new_can, model, self.settings.mutate_prob)
                next_generation.append(new_can)
                e_new = model.energy(new_can)
            

            population = sorted(next_generation,  key=lambda x: model.energy(x))
            e_new = model.energy(population[0])
            current_era.append(e_new)

            if e_new < e_best:
                e_best = e_new
                print('+', end='')          
            else:
                print('.', end='')

            # Check for early termination
            if i % self.settings.era == 0 and i != 0:
                print('\n')
                if different(prev_era, current_era):
                   prev_era = current_era[:]
                   current_era = []
                else:
                   print ('Early Termination in era : ', i/self.settings.era)
                   break;

        # TODO: Plot the pareto frontier
        # TODO: Is the final population the final frontier??
        epoch_time = int(time.time())
        final_frontier = [ model.eval(can) for can in population ]
        if model.m == 3:
            # Plot results
            f1 = [x[0] for x in final_frontier]
            f2 = [x[1] for x in final_frontier]
            f3 = [x[2] for x in final_frontier]
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(f1, f2, f3)
            ax.set_xlabel('f1')
            ax.set_ylabel('f2')
            ax.set_zlabel('f3')
            plt.show()
        print("\nBest Denormalized Energy:" + str(e_best) )

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
                if model.dominates(can_1, can_2):
                    count += 1
            pop_dominations.append((can_1, count))

        pop_dominations.sort(key=lambda (can, score): score, reverse=True)
        n = len(pop_dominations) 
        elites = pop_dominations[:int(retain*n)]   
        return elites

    @staticmethod
    def select(elite_population):
        # Create a weighted roulette 
        # Each candidate will be added number of times its score
        roulette = []
        for can, score in elite_population:
            roulette += [can] * score

        papa = r.choice(roulette)

        while True:
            mama = r.choice(roulette)
            if mama != papa: break
        
        return (papa, mama)

    @staticmethod
    def mutate(new_can, model, mutate_prob):
        # TODO: Any specific mutation method ??
        if r.random() > mutate_prob:
            return new_can

        pos = r.randint(0, len(new_can.decs) - 1)
        new_can.decs[pos] = r.uniform(model.decs[pos].low, model.decs[pos].high)
        return new_can

    @staticmethod
    def crossover(parents):
        pos = r.randint(0, len(parents[0].decs) - 1)
        can = parents[0].clone()
        can.decs[pos:] = parents[1].decs[pos:]
        return can
