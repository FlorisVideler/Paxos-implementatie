# Opdracht 3: Productieklaar maken van een gedistribueerde data-analyse: Paxos-implementatie

## Input examples
Example #1
```
1 3 0 15
0 PROPOSE 1 42
0 END
```
![alt text](https://i.ibb.co/cYK3zrJ/example1.png)

Example #2
```
2 3 0 50
0 PROPOSE 1 42
8 FAIL PROPOSER 1
11 PROPOSE 2 37
26 RECOVER PROPOSER 1
0 END
```
![alt text](https://i.ibb.co/ZzGJqY6/example2.png)

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
![alt text](https://i.ibb.co/GRQdCgw/example3-1.png)
![alt text](https://i.ibb.co/5nWMQVz/example3-2.png)
![alt text](https://i.ibb.co/j48Bpyf/example3-3.png)
![alt text](https://i.ibb.co/FstPyzQ/example3-4.png)
![alt text](https://i.ibb.co/4R8DBGT/example3-5.png)
![alt text](https://i.ibb.co/47FfGPB/example3-6.png)
![alt text](https://i.ibb.co/PMyVC72/example3-7.png)
![alt text](https://i.ibb.co/FbmBL1D/example3-8.png)
![alt text](https://i.ibb.co/M6nV7Bp/example3-9.png)
![alt text](https://i.ibb.co/svDN1Cr/example3-9-1.png)





