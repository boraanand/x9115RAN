#Report

Team Members:  
  Anand Bora (abora)  
  Nirmesh Khandelwal (nbkhande)  
  Ravi Singh (rpsingh3)  

##Abstract:
------------------
Today, there are many well known optimization algorithms which are used to solve a wide randge of optimization problems.  
Each algorithm is different in the approach and can be better from each other for different models. Our main goal was to show the process of deciding which algorithm performs better for a given model.  
We implemented three types of comparisons- a) between candidate pairs, b) between sets of candidates from the same optimizer,  c) between sets of candidates from different optimizers.   
Then, we applied three optimization algorithms - Differential Evolution (DE) , MaxWalkSat (MWS) and Simulated Annealing (SA) on model DTLZ7( with 2 objectives and 10 decisions) to decide which one is the best for that model.

Keywords: DE, Simualted Anealing, MWS, Type1, Type2, Type3

##I. Introduction:
-------------------
There are two types of comparisons which are used in optimization algorithms and another type of comparison used to compare and decide which one is better among them for a given model.
For the paper, we have used DTLZ7 model to compare three different optimzation algorithm - DE, SA, MWS. 
Simulated Annealing is an optimzation algorithm which uses an probablistic technique to find a good solution(approximate global optimum) for a given model (or a function).  Differential evolution is a stochastic, population-based optimization algorithm which optimzes a problem by iteratively trying to improve candidate solution with regard to given measure of quality.
MaxWalkSat is a non-parametric stochastic method for sampling the landscape of the local region.
All these three uses different apporach to optimize a problem. 



