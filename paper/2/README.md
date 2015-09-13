# Summary 
## (i) Reference : 
## Dynamic Test Input Generation for Web Applications
Gary Wassermann
University of California, Davis
wassermg@cs.ucdavis.edu

Dachuan Yu
DoCoMo USA Labs
yu@docomolabs-usa.com

Ajay Chander
DoCoMo USA Labs
chander@docomolabs-usa.com

Dinakar Dhurjati
DoCoMo USA Labs
dhurjati@docomolabs-usa.com

Hiroshi Inamura
DoCoMo USA Labs
inamura@docomolabs-usa.com

Zhendong Su
University of California, Davis
su@cs.ucdavis.edu

## (ii) Keywords
  * (ii1)**Automatic test generation** : It the process of programmatically creating a set of data for testing the adequacy of new or revised software applications.
  * (ii2)**Concolic testing** : It is a software verification technique that performs symbolic execution, a classical technique that treats program variables as symbolic variables, along a concrete execution (testing on particular inputs) path. 
  * (ii3)**Symbolic execution** : It is a means of analyzing a program to determine what inputs cause each part of a program to execute.
  * (ii4)**Directed random testing**  : It is a black-box software testing technique where programs are tested by generating random, independent inputs. Results of the output are compared against software specifications to verify that the test output is pass or fail. In case of absence of specifications the exceptions of the language are used which means if an exception arises during test execution then it means there is a fault in the program.

## (iii) Artifacts
* (iii1) **Motivation** : Manual testing requires extensive human effort, which comes at significant cost. Within the domain of automated web application testing, this paper focuses on automatic test case generation, automatic test input generation by modelling string operations, and checking string values against existing policies to prevent SQL injection attacks. Paper discusses techniques and coding examples for PHP applications.
* (iii2) **2.	Tutorial materials** : Paper has focused extensively on PHP web application, has covered several coding examples to help the reader get started upon their approach. The code takes a user ID, and attempts to authenticate the user to perform other actions. If the user’s ID does not appear in the database, the program exits with an error message.
* (iii3) **3.	Data** : Several reusable projects are discussed, which we have submitted  at http://openscience.us/repo/contribute/donate.
    a.	**Mantis** 1.0.0rc2, is an open source bug tracking system, similar to Bugzilla

    b.	**Mambo** 4.5.3, is an open source content management system.

    c.	**Utopia News Pro** 1.3.0, is a news management system.

    d.	**PHC** is an open source PHP front-end compiler.
* (iii4) **Related Work** : 
   * a.	**Test Input Generation**: 
     i.	Generate random values as inputs:
        1.	C. Cadar, V. Ganesh, P. M. Pawlowski, D. L. Dill, and D. R. Engler. Exe: automatically generating inputs of death. In Proceedings of the 13th ACM Conference on Computer and Communications Security (CCS 2006), pages 322–335, 2006.

        2.	Y. Lei and J. H. Andrews. Minimization of randomized unit test cases. In 16th International Symposium on Software Reliability Engineering (ISSRE 2005), pages 267–276, 2005.

        3.	C. Pacheco and M. D. Ernst. Eclat: Automatic generation and classification of test inputs. In Object-Oriented Programming, 19th European Conference (ECOOP 2005), pages 504–527, 2005.

    ii.	Test input generation that leverages runtime values:
        1.	C. Cadar and D. R. Engler. Execution generated test cases: How to make system code crash itself. In Model Checking Software, 12th International SPIN Workshop, pages 2–23, 2005.
      
        2.	C. Cadar, V. Ganesh, P. M. Pawlowski, D. L. Dill, and D. R. Engler. Exe: automatically generating inputs of death. In Proceedings of the 13th ACM Conference on Computer and Communications Security (CCS 2006), pages 322–335, 2006.

        3.	M. Costa, M. Castro, L. Zhou, L. Zhang, and M. Peinado. Bouncer: securing software by blocking bad input. In Proceedings of the 21st ACM Symposium on Operating Systems Principles 2007 (SOSP 2007), pages 117–130, 2007.

   * b.	Web Application Testing: Previous work on web application testing has focused on static webpages and the loosely structured control flow between them: 

    i.	F. Ricca and P. Tonella. Analysis and testing of web applications. In Proceedings of the 23rd International Conference on Software Engineering (ICSE 2001), pages 25–34, 2001.

   ii.	D. Kung, C. H. Liu, and P. Hsia. An object-oriented web test model for testing web applications. In 24th International Computer Software and Applications Conference (COMPSAC 2000), pages 537–542, 2000.

   * c.	Previous work on PHP application testing:
   
   i.	N. Jovanovic, C. Kruegel, and E. Kirda. Pixy: A static analysis tool for detecting web application vulnerabilities (short paper). In 2006 IEEE Symposium on Security and Privacy (S&P 2006), pages 258–263, 2006.

   ii.	Y. Xie and A. Aiken. Static detection of security vulnerabilities in scripting languages. In Proceedings of the USENIX Security Symposium, 2006.




