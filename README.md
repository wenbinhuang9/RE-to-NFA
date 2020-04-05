# RE-to-NFA
This project is to parse the regular expression to NFA(non-determinism finite automaton), as the two are equivalent. 

# Overveiw of Project Flow
The basic idea as follows
1. parse the regular expressiont to an abstract syntax tree
2. using the AST(abstract syntax tree) to generate NFA
3. Finally, compute the NFA layout and draw the NFA. 

![image](https://github.com/wenbinhuang9/RE-to-NFA/blob/master/flow.png)


# How to use
```
from  engine import convertREtoNFA

input = "(0|1)*111"
convertREtoNFA(input)
```

# Pictures of NFA
NFA of 'cd|eff|ab'

![image](https://github.com/wenbinhuang9/RE-to-NFA/blob/master/new_nfa_draw.jpg)

# Issues to fix

1. drawing line for star transition
2. adding a drawing arrow function, which can flexibly adjust the arrow angle.

