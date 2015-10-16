# Summary 
## (i) Reference : 
## Search-Based Testing of AjaxWeb Applications
Alessandro Marchetto and Paolo Tonella
Fondazione Bruno Kessler - IRST
marchetto|tonella@fbk.eu

[Paper](https://scholar.google.com/scholar?q=Search-Based+Testing+of+AjaxWeb+Applications&btnG=&hl=en&as_sdt=0%2C34)

## (ii) Keywords
  * (ii1)**Ajax Applications** : Short for asynchronous JavaScript and XML. With Ajax, web applications can send data to and retrieve from a server asynchronously (in the background) without interfering with the display and behavior of the existing page. 
  * (ii2)**Finite State Machine (FSM)** : It is conceived as an abstract machine that can be in one of a finite number of states. The machine is in only one state at a time; the state it is in at any given time is called the current state. It can change from one state to another when initiated by a triggering event or condition; this is called a transition. A particular FSM is defined by a list of its states, and the triggering condition for each transition.
  * (ii3)**Hill-Climbing Algorithm** : It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by incrementally changing a single element of the solution. If the change produces a better solution, an incremental change is made to the new solution, repeating until no further improvements can be found.
  * (ii4)**Fitness function**  : A fitness function is a particular type of objective function that is used to summarise, as a single figure of merit, how close a given design solution is to achieving the set aims.

## (iii) Artifacts
* (iii1) **Motivation** : Manual testing requires extensive human effort, which comes at significant cost. Within the domain of automated web application testing, this paper focuses on automatic test case generation, automatic test input generation by modelling string operations, and checking string values against existing policies to prevent SQL injection attacks. Paper discusses techniques and coding examples for PHP applications.
* (iii2) **2.	Tutorial materials** : Paper has focused extensively on PHP web application, has covered several coding examples to help the reader get started upon their approach. The code takes a user ID, and attempts to authenticate the user to perform other actions. If the user’s ID does not appear in the database, the program exits with an error message.

Sample code in paper:

![code](images/code.png)

* (iii3) **3.	Data** : Several reusable projects are discussed, which we have submitted  at http://openscience.us/repo/contribute/donate.

    a.	**Mantis** 1.0.0rc2, is an open source bug tracking system, similar to Bugzilla

    b.	**Mambo** 4.5.3, is an open source content management system.

    c.	**Utopia News Pro** 1.3.0, is a news management system.

    d.	**PHC** is an open source PHP front-end compiler.
* (iii4) **Related Work** : 

    i.	Generate random values as inputs:
    
        1.	C. Cadar, V. Ganesh, P. M. Pawlowski, D. L. Dill, and D. R. Engler. Exe: automatically generating inputs of death. In Proceedings of the 13th ACM Conference on Computer and Communications Security (CCS 2006), pages 322–335, 2006.
      
        2.	Y. Lei and J. H. Andrews. Minimization of randomized unit test cases. In 16th International Symposium on Software Reliability Engineering (ISSRE 2005), pages 267–276, 2005.
      
        3.	C. Pacheco and M. D. Ernst. Eclat: Automatic generation and classification of test inputs. In Object-Oriented Programming, 19th European Conference (ECOOP 2005), pages 504–527, 2005.

    ii.	Test input generation that leverages runtime values:
    
        1.	C. Cadar and D. R. Engler. Execution generated test cases: How to make system code crash itself. In Model Checking Software, 12th International SPIN Workshop, pages 2–23, 2005.
      
        2.	C. Cadar, V. Ganesh, P. M. Pawlowski, D. L. Dill, and D. R. Engler. Exe: automatically generating inputs of death. In Proceedings of the 13th ACM Conference on Computer and Communications Security (CCS 2006), pages 322–335, 2006.

        3.	M. Costa, M. Castro, L. Zhou, L. Zhang, and M. Peinado. Bouncer: securing software by blocking bad input. In Proceedings of the 21st ACM Symposium on Operating Systems Principles 2007 (SOSP 2007), pages 117–130, 2007.

    iii. Web Application Testing: Previous work on web application testing has focused on static webpages and the loosely
    structured control flow between them: 
    
        1.	F. Ricca and P. Tonella. Analysis and testing of web applications. In Proceedings of the 23rd International Conference on Software Engineering (ICSE 2001), pages 25–34, 2001.
    
        2.	D. Kung, C. H. Liu, and P. Hsia. An object-oriented web test model for testing web applications. In 24th International Computer Software and Applications Conference (COMPSAC 2000), pages 537–542, 2000.

    iii. Previous work on PHP application testing:
    
        1.	N. Jovanovic, C. Kruegel, and E. Kirda. Pixy: A static analysis tool for detecting web application vulnerabilities (short paper). In 2006 IEEE Symposium on Security and Privacy (S&P 2006), pages 258–263, 2006.
    
        2.	Y. Xie and A. Aiken. Static detection of security vulnerabilities in scripting languages. In Proceedings of the USENIX Security Symposium, 2006.

        3.	M. Costa, M. Castro, L. Zhou, L. Zhang, and M. Peinado. Bouncer: securing software by blocking bad input. In Proceedings of the 21st ACM Symposium on Operating Systems Principles 2007 (SOSP 2007), pages 117–130, 2007.

## (iv) Improvizations:
  * (iv1) Constraint resolution algorithm discussed in the paper could be enhanced to include multivariate constraints in some cases.
  * (iv2) Current approach suggested in the paper is not fully automated. The web page must be manually loaded (e.g., by clicking “go”), the analyzer must be manually invoked, and analyzer writes the next inputs to a file, so they must be manually provided to the URL. An additional step of automation could be handy to overcome this drawback.



