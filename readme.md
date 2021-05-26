# Opdracht 3: Productieklaar maken van een gedistribueerde data-analyse: Paxos-implementatie
Niels Bijl 1754339 <br>
Floris Videler 1758374

## Validation
(For all the input examples from fase 1 we added a 0, for the amount of learners needed.)<br>
Example #1
```
1 3 0 15
0 PROPOSE 1 42
0 END
```
![alt text](https://i.postimg.cc/W1tXr6Qg/image.png)

Example #2
```
2 3 0 50
0 PROPOSE 1 42
8 FAIL PROPOSER 1
11 PROPOSE 2 37
26 RECOVER PROPOSER 1
0 END
```
![alt text](https://i.postimg.cc/sfwYcGPc/image.png)

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
![alt text](https://i.postimg.cc/xd3J1BtR/image.png)
![alt text](https://i.postimg.cc/QCwVzDdX/image.png)
![alt text](https://i.postimg.cc/bNSZtZmd/image.png)
![alt text](https://i.postimg.cc/V65fPhT5/image.png)
![alt text](https://i.postimg.cc/sDCM5Vqc/image.png)
![alt text](https://i.postimg.cc/xTQdc6Np/image.png)
![alt text](https://i.postimg.cc/xCr2BdKp/image.png)
![alt text](https://i.postimg.cc/MpcgxSZC/image.png)
![alt text](https://i.postimg.cc/vTB3zrcJ/image.png)
![alt text](https://i.postimg.cc/vB8zYrL4/image.png)







