Reference:
-----------

By Kiran Lakhotia , Phil McMinn , Mark Harman, 2009. Automated Test Data Generation for Coverage: Haven't We Solved This Problem Yet?, Proceedings of the 2009 Testing: Academic and Industrial Conference - Practice and Research Techniques, p.95-104, September 04-06, 2009 [Link](http://ieeexplore.ieee.org.prox.lib.ncsu.edu/stamp/stamp.jsp?tp=&arnumber=5381642&tag=1)

ii: Keywords:
------------------
#### ii1: Concolic testing:
It formulates the test data generation problem as one of finding a solution to a constraint satisfaction problem, the constraints of which are produced by concolic execution of the program under test. Concolic execution combines symbolic  and concrete execution.

#### ii2: Search Based Testing: 
Search based testing formulates the test data adequacy criteria as objective functions, which can be optimized using Search Based Software Engineering.

#### ii3: AUSTIN: 
A search based tool to generate test data.

#### ii4: CUTE: 
A concolic tool to generate test data.

iii: Artifacts:
---------------
#### iii1. Motivational statements:
Little work had been done (at the time of writing that paper) to realize the effectiveness of concolic testing and search based testing with complete real world software applications. 
Research questions:
i) How effective are concolic and search based tools when applied to real world software applications?
ii) How long does it take for concolic and search based tools to achieve certain levels of coverage?

#### iii2. Related Work: 
Authors have mentioned some of the tools based on random testing, concolic testing and search based testing. DART (by Godefroid et al.) , a random testing tool, is  different from CUTE as DART does not attempt to solve constraints involving memory locations.
CREST tool is also mentioned by authors. It is a recent open-source successor to CUTE. It has  a more sophisticated, CFG based, path exploration strategy in comparison to CUTE.
ET-S (developed by Daimler) uses evolutionary algorithms to achieve various coverage types, including path,branch and data flow coverage.
Burnim and Sen  considered different search strategies to explore program paths in concolic testing and evaluated their findings on large open source applications including the Siemens benchmark suite, grep, a search utility based on regular expressions, and vim, a common text editor.
Concolic testing has also been used to search for security vulnerabilities in large Microsoft applications as part of the SAGE tool.

#### iii3: Patterns:
 While comparing two approaches, one of the best practices to be followed is the comparison should be fair.
Authors have given the importance to that and mentioned how they have tried to avoid any threats to validity of their findings. To address internal validity threats to the experiments, they have used default settings and if not possible, then reasonable values have been used.To address external validity threats, the authors have used a variety of programming styles and sources.

#### iii4. Results: 
The results show that there are many challenges remaining in making automatic test data generation tools robust and of a standard that could be considered ‘industrial strength’.
This is because with the exception of one of the test subjects chosen, neither tool managed to generate test data for over 50% of the branches in each application’s code.
Two main challenges pointed by authors are -  the tools need to be able to prevent or recover from segmentation faults, so that they may continue the test data generation process to any effect. Secondly, test data generation tools need to become much more heterogeneous in nature.

iv: Improvements:
-------------
It was a very well written research paper, so its really difficult to find any improvements.

#### iv1: 
Authors have not given the reason behind choosing CUTE or AUSTIN instead of other concolic tools or search based tools. Like checking effectiveness of concolic testing could be tested with CREST instead of CUTE which could have given better results.

#### iv2: 
There were number of functions which were not tested because of compilation error. Those things could have impacted the results observed. The authors could have given the reason of choosing the particular real world applications or could have argued that those errors are really not because of the application.

#### iv3:
The authors selected random 12 functions from the 4 test objects  to test the effectiveness of two approaches. It could have been better if apart from random 12 functions, they could have tested on some known functions on which both approaches were expected to perform better. It would have given additional evidences of the effectiveness of search based and concolic testing to generate input test data.

##### Connection to the initital paper(s):
The paper has discussed two techniques to generate test data - concolic testing and search based testing. The paper1”Automated Web Application Testing Using Search Based Software Engineering”  also discussed search based testing. Even both papers discussed AVM(Alternating Variable Method).
Paper 2 ”Dynamic test input generation for web applications” discussed concolic testing which is one of the technique whose effectiveness was measured in this paper. 

