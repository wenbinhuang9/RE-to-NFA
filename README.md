# RE-to-NFA
This project is to parse the regular expression to NFA(non-determinism finite automaton), as the two are equivalent. 

# Overveiw of Project Flow
The basic idea as follows
1. parse the regular expressiont to an abstract syntax tree
2. using the AST(abstract syntax tree) to generate NFA
3. Finally, compute the NFA layout and draw the NFA. 

![image](https://github.com/wenbinhuang9/RE-to-NFA/blob/master/flow.png)

# Easy start 
```
from  engine import drawNFA

re= "(0|1)*111"
drawNFA(re)
```

# Pictures of NFA
NFA of '(0|1)*010'

![image](https://github.com/wenbinhuang9/RE-to-NFA/blob/master/test_combination1.svg)

# BNF desing

```

    <re> ::=  <term> '|' <re> | <term>
    <term> ::= { <factor> }
    <factor> ::= <base> {'*'}
    <base> ::= <char> | '(' <re> ')'
  
```
