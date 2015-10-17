# Summary 
## (i) Reference : 
## Precise Interface Identification to Improve Testing and Analysis of Web Applications
William G.J. Halfond, Saswat Anand, and Alessandro Orso

Georgia Institute of Technology

{whalfond|saswat|orso} @ cc . gatech . edu

[Paper](http://dl.acm.org/citation.cfm?id=1572305)
[Download](http://www-bcf.usc.edu/~halfond/papers/halfond09issta.pdf)

## (ii) Keywords
  * (ii1)**Interface identification** : Identifying how components of a (web) application communicate extensively. To generate content for the end user, the components of a web application communicate by sending a certain type of HTTP request,
called an interface invocation, to the interfaces of other components. An interface invocation provides arguments in the form of name-value pairs (e.g., login=username).
  * (ii2)**Symbolic Execution** : Is a means of analyzing a program to determine what inputs cause each part of a program to execute
  * (ii3)**Domain-constraining operations** : Certain types of operations that we call domain-constraining operations, implicitly constrain the domain of an IP. Examples of these operations are functions that convert an IP value into a numeric value or comparisons of the IP value against a specific value.
  * (ii4)**Interface domain constraint (IDC)** : the set of constraints place on an accepted interface along a specific execution path an interface domain constraint (IDC). An accepted interface may have more than one IDC associated with it, if different domain-constraining operations are performed on its IPs along different paths.

## (iii) Artifacts
* (iii1) **Motivation** : As web applications become more widespread, sophisticated, and complex, automated quality assurance techniques for such applications have grown in importance. Accurate interface identification is fundamental for many of these techniques, as the components of a web application communicate extensively. Current techniques for identifying web application interfaces can be incomplete or imprecise. To address these limitations, paper present a new approach for identifying web application interfaces that is based on a specialized form of symbolic execution.
* (iii2) **2.	Tutorial materials** : Paper gives an example web application to illustrate the technique. approach works in three main steps. In the first step, technique performs a transformation of the web application so that IPs are represented as symbolic values and domain-constraining operations are modeled by symbolic operations. In the second step, technique symbolically executes the web application and generates a set of PCs for each component. In the third step, technique identifies the accepted interfaces and interface domain constraints of the web application by analyzing the PCs generated during symbolic execution.

Sample code in paper, on which testing was done:

![code](images/servlet.png)

* (iii3) **3.	Data** : Two reusable projects are discussed, which we have submitted  at http://openscience.us/repo/contribute/donate.

    a.	**Java PathFinder (JPF)** an explicit-state model checker for Java programs

    b.	**YICES** is an Satisfiability modulo theories (SMT) solver that decides the satisfiability of formulas containing uninterpreted function symbols with equality, linear real and integer arithmetic, bitvectors, scalar types, and tuples.

* (iii4) **Related Work** : Several techniques and a few tools have been presented in the literature to support testing of Web applications.

    i.	Model-based testing of Web applications:
    
        1.	F. Ricca and P. Tonella. Analysis and testing of Web applications. In Proc. of ICSE 2001, International Conference
on Software Engineering, Toronto, Ontario, Canada, May 12-19, pages 25–34, 2001.
      
        2.	A. Andrews, J. Offutt, and R. Alexander. Testing Web Applications by Modeling with FSMs. Software and System Modeling, Vol 4, n. 3, July 2005.

    ii.	State-based testing approach:
    
        1.	C. D. Turner and D. J. Robson. The state-based testing of object-oriented programs. IEEE Conference on Software Maintenance (ICSM), September 1993.
      
        2.	X. Yuan and A. M. Memon. Using GUI run-time state as feedback to generate test cases. In ICSE ’07: Proceedings of the 29th International Conference on Software Engineering, pages 396–405, Washington, DC, USA, May 23–25, 2007. IEEE Computer Society.

        3.	A.Marchetto, P. Tonella, and F. Ricca. State-based testing of ajax web applications. In Proc. of IEEE International Con-ference on Software Testing (ICST), Lillehammer, Norway, April 2008.

    iii. Web Application Testing: Previous work on web application testing has focused on static webpages and the loosely
    structured control flow between them: 
    
        1.	F. Ricca and P. Tonella. Analysis and testing of web applications. In Proceedings of the 23rd International Conference on Software Engineering (ICSE 2001), pages 25–34, 2001.
    
        2.	D. Kung, C. H. Liu, and P. Hsia. An object-oriented web test model for testing web applications. In 24th International Computer Software and Applications Conference (COMPSAC 2000), pages 537–542, 2000.

## (iv) Future work:
  * (iv1) Future work will be devoted to the improvement of the FSM algorithm.
  * (iv2) Experiment with alternative search based algorithms and we will apply them to a larger benchmark of Ajax applications.
  * (iv3) Investigate the role of input selection and infeasible paths in the FSM during test case generation.



