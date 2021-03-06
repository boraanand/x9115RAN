Reference:
----------
1. Dynamic adaptive search based software engineering.
By Mark Harman, Edmund Burke, John Clark and Xin Yao, 2012.
IN ESEM '12 Proceedings of the ACM-IEEE international symposium on Empirical software engineering and measurement
[Link](http://www0.cs.ucl.ac.uk/staff/mharman/esem12.pdf)

ii: Keywords:
------------------
#### ii1: Search Based Software Engineering (SBSE): 
*"Search Based Software Engineering (SBSE) is the name given to a field of research and practice in which computational search (as well as optimization techniques more usually associated with Operations Research) are used to address problems in Software Engineering"*
#### ii2: Hyper-heuristic search: 
Normal heuristics operate on search space of potential solutions. Hyper Heuristics operate on search space of heuristics.
#### ii3: Self Adaptive software Systems: 
Software systems that have SBSE integrated within the systems that allows them to fix faults and cope with anomalies, provides on-line adaptivity to meet new challenges, environments and platforms. 
#### ii4: Automatic Programming: 
When software re writes of updates the part of software itself.

iii: Artifacts:
------------------
#### iii1: Motivational statements:
- The main motivation behind this paper is to present a proposal of applying Search based software engineering practices to create self adaptive software systems. The author starts by refereing many examples where SBSE is proved useful in the past : Requirements optimization, Predictive Modelling, search based testing for Non-Functional Properties, Program Comprehension, search–based software design and search based automated Testing. - The main challenge according author is following: Although SBSE has been successfully applied in isolation to the above mentioned phases of software development process, there is a need to develop holistic sbse approach which can allow all of these techniques to applied in co-ordination. The programmers will not need to devise the search algorithms for different phases.
- Instead of designing bespoke optimization algorithms for specific instances, we advocate the design of ‘reasonably good’ hyper heuristic optimizers that have the generality to be applied more readily ‘out of the box’.
- Self-adaptivity has been a goal of software and systems engineering research for some time and author beleives that SBSE will allow to add some value to this grand challenge.

#### iii2: Hypothesis: 
- The author believes that using Hyper heuristics search, we can directly optimize the engineering material: the programs themselves. This means that the software itself will re-balance, re-configure, and even to redevelop itself as it operates.
- Since we have achieved great results in tuning of parameters, re-design aspects of systems to fix bugs using genetic programming, migration to new platforms and languages and optimization of nonfunctional
properties, All this work is early indication of potential for Dynamic Adaptive SBSE.

#### iii3: Related Work:
The author provides a good introduction on the all the relevant work done so far in the field of SBSE that might help us to get the motivation for developing autonomous softwares in the future. Specifically, the most important work is in the field of genetic programming. Following work has shown good potential :

1. **Bug fixing:** The automated generation of Bug Fix patches is already successfully implemented. Currently, this is used for temporary fix in the program till developer fixes the actual bug. Recently evidences have found for the patches that can sustain long term in software.
2. **Migration:** Evidence have been found that indicates that it is possible to evolve new code for completely different architectures and languages than those for which the original code was designed.
A key insight in this work is that the original program can act as an oracle for the functional requirements of the system to be re-evolved in this way.
3. **Trading Functional and non-functional requirements:** Finding balance between functional and non functional requirements of software. How should we decide if we need to sacrifice the functional requirments for performance benefits. Author mentions the results achieved in pseudo random generator.

#### iii4: Patterns:

- The authors provides a great insight into the role of Experimentation vs Empirical results in relation to computer science. Experimentation is something that scientists do "under the laboratory conditions" in order to observe cause and effect of different quantities. On the other hand, epirical results are any statement about the world that is related to observation or experience.
- In order to make experimentations in software engineering, people often use synthetic data. Author makes a cautious note that such data should be used only for finding answers that are not clear from real data. It should not be a "substitute" , rather it should be "augmentation" to real data. In empirical software engineering we need both laboratory controlled data and data based on real world empirical experimentation, not one or the other.

We can clearly see that these insights can be used for other researches as well. Hence this falls under "pattern" section.

iv: Improvements:
-----------------
#### iv1:
No concrete examples present in paper to support the authors claims about Adaptive Automated Software Engineering. Although the purpose of the paper is to introduce this new idea that can be worked upon by other researchers in the future, it would have been nice to give some pointers on the required work done by the authors.

#### iv2:
Not clear how the author plans to achieve hypothesis. Author provides details about the work done so far, and related work.but there is no mention on techniques to consolidate that work into holistic system. This question is somewhat kept open ended by authors.

#### iv3:
No examples of synthetic data sets provided. The author has dedicated 2 sections of paper on the discussion of various properties of synthetic data sets for Experimentations in software engineering.But there are no example data sets provided for that. No supporting visuals would have been nice too.


v: connection to initial paper(s):
----------------------------------
This paper takes initial seed paper as one of its motivations. The seed paper (Automated Web Application Testing Using Search Based Software Engineering) talks about automated test generations using sbse. This paper pus forward an hypothesis about hollistic sbse for softwares that will allow the softwares to behave as autonomic entities. Author derives this motivation becasuse os the isolated use of sbse in test generation (seed paper) , re-design aspects of systems to fix bugs using genetic programming, migration to new platforms and languages and optimization of nonfunctional properties.



