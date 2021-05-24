# Opdracht 3: Productieklaar maken van een gedistribueerde data-analyse: Paxos-implementatie

## Input examples
Example #1
```
1 3 0 15
0 PROPOSE 1 42
0 END
```

Example #2
```
2 3 0 50
0 PROPOSE 1 42
8 FAIL PROPOSER 1
11 PROPOSE 2 37
26 RECOVER PROPOSER 1
0 END
```

Example #3
```
1 3 1 10000 
0 PROPOSE 1 nl: g
100 PROPOSE 1 nl:ga
200 PROPOSE 1 nl:af
300 PROPOSE 1 nl:f 
400 PROPOSE 1 en: g
500 PROPOSE 1 en:gr
600 PROPOSE 1 en:re
700 PROPOSE 1 en:ea
800 PROPOSE 1 en:at
900 PROPOSE 1 en:t 
0 END
```