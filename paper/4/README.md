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
GI is methodology where we directly apply sbse techniques on the source code. It treats software code as gentic material and tries to mutate it to improve the program for a given objective.

#### ii3: Genetic Programming (GP):

#### ii4: Abstract Syntax Tree (AST):

#### ii5: Genetic Algorithm (GA):

iii: Artifacts:
------------------
#### Motivational statements:
The main motivation behind the paper is to compare and contrast the ADA and GI. Both of these techniques have been used to design the new algorithms automatically using sbse. Although these techniques have some overlap, there are few fundamental difference in the approaches. The author wants to give us more insight for both of these techniques so that it will clear things out for future research.

#### pattern:
- The authors proide a good pattern for Altering and adjusting the algorithms to solve new problems. These techniques can be used as general pattern for automatic design ofAlgorithms.
    + replacing: Replace the components of existing algorithm by the component from some fixed set.
    + reordering: Depending on the restrictions, algorithms can be reorderd for initializing,return statements.
    + Parameter tuning: Changing the amount of any or each componnt. This should be used in association with the above two techniques, so that newly generated algorithm is tested against tuned parameters.
- When the algorithm being designed is a search or an optimization algorithm the main objective of the fitness function is typically to improve a functional property that is evaluated as the fitness of the best solution found by the evolved algorithm

#### 
  


iv: Improvements:
-----------------
#### iv1:
#### iv2:
#### iv3:
