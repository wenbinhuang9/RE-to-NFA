# RE-to-NFA
This project is to parse the regular expression to NFA(non-determinism finite automaton), as the two are equivalent. 

# Overveiw of Model


```flow
st=>start: Start:>https://www.markdown-syntax.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end
st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```
