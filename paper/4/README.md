Reference:
----------
Automated design of algorithms and genetic improvement: contrast and commonalities
By Saemundur O. Haraldsson, John R. Woodward.
In GECCO Comp '14 Proceedings of the Companion Publication of the 2014 Annual Conference on Genetic and Evolutionary Computation. [Link](http://www.cs.stir.ac.uk/~jrw/publications/2014/AutomatedDesignAlgorithmsGeneticImprovementContrastCommonalities/AutomatedDesignAlgorithmsGeneticImprovementContrastCommonalities.pdf)

ii: Keywords:
--------------

#### ii1: Automated Design of Algorithms:
A methodology for using sbse for discovering and updating the algorithms for computational problems.

#### ii2: Genetic Improvement(GI):
GI is methodology where we directly apply sbse techniques on the source code. It treats software code as gentic material and tries to mutate it to improve the program for a given objective. These operations may for example
consist of copying, deleting and swapping lines of code.

#### ii5: Genetic Algorithm (GA): 
These are evolutionary algorithms used to solve optimization problems. Below are the two main steps:
1. Initial generation of candidate solutions at random (tested against the objective function)
2. Subsequent generations evolve from the 1st through selection, crossover and mutation.

#### ii3: Genetic Programming (GP): 
Specialization of genetic algorithms where each individual is a computer program. Computer programs are represented as Abstract Syntax trees and these tree are mutated to generate new programs.



iii: Artifacts:
------------------
#### ii1. Motivational statements:
The main motivation behind the paper is to compare and contrast the ADA and GI. Both of these techniques have been used to design the new algorithms automatically using sbse. Although these techniques have some overlap, there are few fundamental difference in the approaches. The author wants to give us more insight for both of these techniques so that it will clear things out for future research.

#### ii2. pattern:
- The authors proide a good pattern for Altering and adjusting the algorithms to solve new problems. These techniques can be used as general pattern for automatic design ofAlgorithms.
    + replacing: Replace the components of existing algorithm by the component from some fixed set.
    + reordering: Depending on the restrictions, algorithms can be reorderd for initializing,return statements.
    + Parameter tuning: Changing the amount of any or each componnt. This should be used in association with the above two techniques, so that newly generated algorithm is tested against tuned parameters.
- When the algorithm being designed is a search or an optimization algorithm the main objective of the fitness function is typically to improve a functional property that is evaluated as the fitness of the best solution found by the evolved algorithm

#### ii3. Tutorial materials:
- Author provides a comprehensive guide to ADA and GI in the paper. 
- One particular instance is guide to GI, its Application comparison with ADA. Author specifies how to choose fitness functions for GI - *The correctness of an improvement is found either by comparing the output with the output of the original software as an oracle [34, 2] or by evaluating its performance on a suite of test cases that has already been run on the original code*
- Applications of GI: 
    + Bug Fixing
    + Increasing Speed of program
    + Migration and transplantation
    + Dynamic adaptive approach- Ability of sofftware to improve itself while its running.

#### ii4: Future Work:
- In the last section of paper, author provides a compare and contrast between ADA and GI. The author mainly describes the types of problem that both algorithm tries to solve, and which one to choose for a gives typeof problem. This can act as a base for the fuure work in the domain.
- The most notable difference is that GI is applied in-situ or directly to the source code while ADA works ex-situ, i.e. evolves a function that is injected into the original code.
-  GI makes small changes, sometimes many small changes that do not have to be constrained to a small region of the source code. ADA’s improvement of an existing program on the other hand is a replacement of a certain call or statement in the source and is thus limited to the places where that call is made.

  
iv: Improvements:
-----------------
#### iv1: 
No example presen on how these techniques have been applied to improve softwares. Eventhough references of other papers explaining that is present, it would have been nice to get 1 example of each.
#### iv2: 
Some informative visualizations woulf have been nice.Comparison of applying both ADA and GI on a particular algorithm and comparing improvements in functional and non functional requirements.
#### iv3: 
Since both ADA and GI use GP as their search method, a small tutorial on DP would have been nice.
