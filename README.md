# RE-to-NFA
This project is to parse the regular expression to NFA(non-determinism finite automaton), as the two are equivalent. 

# Overveiw of Model
The basic idea is parse the regular expressiont to an abstract syntax tree. And then using the AST(abstract syntax tree) to generate NFA. Finally, comput the NFA layout and draw the NFA. 

![image](https://github.com/wenbinhuang9/RE-to-NFA/blob/master/flow.png)


# How to use
```
from  engine import convertREtoNFA

input = "(0|1)*111"
convertREtoNFA(input)
```

# Pictures of NFA
NFA as follows is from 'cd|eff|ab'
![image](https://github.com/wenbinhuang9/RE-to-NFA/blob/master/new_nfa_draw.jpg)

# Issues to fix

1. drawing line for star transition
2. adding a drawing arrow function, which can flexibly adjust the arrow angle.

