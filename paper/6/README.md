# Summary 
## (i) Reference : 
## Search-Based Testing of AjaxWeb Applications
Alessandro Marchetto and Paolo Tonella

Fondazione Bruno Kessler - IRST

marchetto | tonella @ fbk . eu


[Paper](http://dl.acm.org/citation.cfm?id=1572305)
[Download](http://www-bcf.usc.edu/~halfond/papers/halfond09issta.pdf)

## (ii) Keywords
  * (ii1)**Ajax Applications** : Short for asynchronous JavaScript and XML. With Ajax, web applications can send data to and retrieve from a server asynchronously (in the background) without interfering with the display and behavior of the existing page. 
  * (ii2)**Finite State Machine (FSM)** : It is conceived as an abstract machine that can be in one of a finite number of states. The machine is in only one state at a time; the state it is in at any given time is called the current state. It can change from one state to another when initiated by a triggering event or condition; this is called a transition. A particular FSM is defined by a list of its states, and the triggering condition for each transition.
  * (ii3)**Hill-Climbing Algorithm** : It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by incrementally changing a single element of the solution. If the change produces a better solution, an incremental change is made to the new solution, repeating until no further improvements can be found.
  * (ii4)**Fitness function**  : A fitness function is a particular type of objective function that is used to summarise, as a single figure of merit, how close a given design solution is to achieving the set aims.

## (iii) Artifacts
* (iii1) **Motivation** : Author's previous work investigated a state-based testing approach, based on semantically interacting events. The main drawback of this approach is that exhaustive generation of semantically interacting event sequences limits quite severely the maximum achievable length, while longer sequences would have higher fault exposing capability. This paper investigates a search-based algorithm for the exploration of the huge space of long interaction sequences, in order to select those that are most promising, based on a measure of test case diversity, on the hill climbing algorithm. 
* (iii2) **2.	Tutorial materials** : Paper proposes a search-based test case derivation technique for Ajax (called HILL), based on the hill climbing algorithm. Paper provides pseudo-code of the algorithm used by HILL to generate the sequences of semantically interacting events composing the final testing suite. 

Pseudo-code in paper:

![code](images/hill.png)

* (iii3) **3.	Data** : Two reusable projects are discussed, which we have submitted  at http://openscience.us/repo/contribute/donate.

    a.	**Tudu Lists** is an Open Source, on-line application for managing todo lists

    b.	**Oryx3** is an academic Open Source project that allows you to add your prototypes to a powerful process modeling infrastructure.

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



