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
![alt text](https://i.postimg.cc/mk7jqT1q/image.png)

Example #2
```
2 3 0 50
0 PROPOSE 1 42
8 FAIL PROPOSER 1
11 PROPOSE 2 37
26 RECOVER PROPOSER 1
0 END
```
![alt text](https://i.postimg.cc/K8GfqSGq/image.png)
![alt text](https://i.postimg.cc/zBgFbq7B/image.png)

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
![alt text](https://i.postimg.cc/3Rm2rnr0/image.png)
![alt text](https://i.postimg.cc/QCjK8Dnv/image.png)
![alt text](https://i.postimg.cc/xTxN2WGF/image.png)
![alt text](https://i.postimg.cc/sgbBB7NY/image.png)
![alt text](https://i.postimg.cc/3NLN3vGD/image.png)
![alt text](https://i.postimg.cc/m25kq7Rv/image.png)
![alt text](https://i.postimg.cc/k5r4M92w/image.png)
![alt text](https://i.postimg.cc/wvgjJVcm/image.png)
![alt text](https://i.postimg.cc/2yXksfpQ/image.png)
![alt text](https://i.postimg.cc/dtLt8Dd4/image.png)
![alt text](https://i.postimg.cc/y8R1b5LR/image.png)







