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
![alt text](https://i.postimg.cc/htT2B1Dx/image.png)
![alt text](https://i.postimg.cc/Nj6kVGDk/image.png)
![alt text](https://i.postimg.cc/g04qzMfw/image.png)
![alt text](https://i.postimg.cc/DZMrsSfn/image.png)
![alt text](https://i.postimg.cc/0QFtvWwY/image.png)
![alt text](https://i.postimg.cc/qB6bwTPj/image.png)
![alt text](https://i.postimg.cc/7LQ91sXF/image.png)
![alt text](https://i.postimg.cc/1XDKQ9PS/image.png)
![alt text](https://i.postimg.cc/9QmY65k3/image.png)
![alt text](https://i.postimg.cc/qqc2FjXM/image.png)
![alt text](https://i.postimg.cc/SKz25gmF/image.png)







