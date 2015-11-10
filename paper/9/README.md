Reference:
-----------

By Gordon Fraser, Andrea Arcuri, "The Seed is Strong: Seeding Strategies in Search-Based Software Testing", IEEE Fifth International Conference on Software Testing, Verification and Validation, 2012 [Link](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6200103)

ii: Keywords:
------------------
#### ii1: Genetic Algorithm(GA):
It is an evolutionary algorithm (EA), which generate solutions to optimization problems using techniques inspired by natural evolution, such as inheritance, mutation, selection and crossover.

#### ii2: Seeding: 
Seeding refers to any technique that exploits previous related knowledge to help solve the testing problem at hand.

#### ii3: EVOSUITE:
An advanced tool based on Genetic Algorithm, featuring for example the whole test suite optimization approach to test data generation, bloat control techniques and effective assertion generation through mutation testing.

#### ii4: Search-based Software Testing: 
Search-based Software Testing is the use of a meta-heuristic optimizing search technique, such as a GA, to automate or partially automate a testing task, for example the automatic generation of test data.

iii: Artifacts:
---------------
#### iii1. Motivational statements: 
Authors of the paper mentioned that search-based techniques had been showm to be a promising approach to tackle many kinds of software engineering tasks, particularly software testing. 
They claimed that those techniques were not adopted by practitioners because of limitations like efficiency and applicability. So, investigating those techniques was of practical value.

#### iii2. Hypothesis:  
The efficiency is heavily dependent on many different factors; seeding is one such factor that may strongly influence this efficiency. Even for a testing tool that is already able to achieve high coverage, the use of appropriate seeding strategies can further improve performance.

#### iii3: Related Work: 
The authors discussed few papers on seeding strategies to improve the search. Some of the papers/work they mentioned were: 
a) angdon and Nordin studied a seeding strategy in order to improve the ability of a classifier/regressor to generalize. 
b) In the context of testing real-time systems to find worst case execution times, Tlili et al. applied seeding strategies.  
They also discussed some of the work related to GA. Like, 
a) Miraz et al. created the initial population by selecting the best individuals out of a larger pool of randomly generated individuals. 

#### iii4. Future Work:  
Authors considered several seeding strategies, and applied them to the context of testing object oriented code in terms of the EVOSUITE tool. 
Authors mentioned that further seeding strategies are possible, and these as well as investigations of how individual seeding strategies interact will be part of their future work. 

iv: Improvements:
-------------
Though it is a very well written paper, I think below points could be area of improvement.

#### iv1: 
In this paper, the length of test suite generated is given secondary priority with prime focus on coverage. But, it could have been better if they could have run the experiments with equal focus on coverage as well as length. Those results would have given better understanding of feasibility and usability of the test suites.

#### iv2: 
Authors mentioned that it is well known that testing alone cannot prove the absence of defects. Also, randomized algorithms are affected by chance. So, to cope with this problem, they ran each experiment 30 times, and followed rigorous statistical procedures to evaluate their results. 
But they have not mentioned the reason coming up with 30. It could have been better if they would have explained the reason behind choosing the count as 30 for which the experiments need to be repeated.

#### iv3:
The paper claims that seeding strategies help EVOSUITE to achieve higher code coverage. But, it is possible that there exists parameter combinations for seeding strategies and search budget, that can perform better. So different parameter settings should be tried.

##### Connection to the initital paper(s):
This paper is on seeding strategies and the initial paper too has mentioned one if the seeding strategy named "Dynamically Mined Value".
