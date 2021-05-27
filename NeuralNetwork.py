#
#   `
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
import csv
from builtins import map
import random
from math import sqrt
#from neupy.layers import activations

trainTable1 = [[0 for x in range(10)] for y in range(177)] 
trainTable2 = [0 for x in range(177)]
c =  0;
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\neuralNetworkMainDatabase.csv','r',encoding="ISO-8859-1") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
            if(c == 0):
                c = c+1;
                continue;
            if(c >= 177):
                break;
            print(c)

            trainTable1[c][0] = float(row[11]);
            trainTable1[c][1] = float(row[2]);
            trainTable1[c][2] = float(row[3]);
            trainTable1[c][3] = float(row[4]);
            trainTable1[c][4] = float(row[5]);
            trainTable1[c][5] = float(row[6]);
            trainTable1[c][6] = float(row[7]);
            trainTable1[c][7] = float(row[8]);
            trainTable1[c][8] = float(row[9]);
            trainTable1[c][9] = float(row[10]);
            c = c+1; 
c = 0;            
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\ratingForNeuralNetwork.csv','r',encoding="ISO-8859-1") as inf6:
    reader6 = csv.reader(inf6, delimiter=',')
    for row in reader6:
            if(c == 0):
                c = c+1;
                continue;
            if(c > 176):
                break;
            trainTable2[c] = row[0];
            c = c+1;

print("trainTable1")
print(trainTable1)
print(len(trainTable1))
print("trainTable2")
print(trainTable2)
print(len(trainTable2))
 

vector = random.sample(range(177), 20)
print(vector)
testTable1 = [[0 for x in range(11)] for y in range(20)] 
testresult = [0 for x in range(20)];

c = 0;
d = 0;
for m in range(177):
    if(c == 0):
        c =  c +1;
        continue;
    if c in vector:
        testTable1[d] = trainTable1[c];
        testresult[d] = trainTable2[c];
        d = d+1; 
        trainTable1[c] = 0
        trainTable2[c] = 0
    c = c+1;   
    
d = 0;    
c = 0
print("trainTable1")
print(len(trainTable1))
print("trainTable2")
print(len(trainTable2))

while(c < 155):
    print(c)
    if(trainTable2[c] == 0):
        trainTable2 = trainTable2[:c] + trainTable2[c+1:]
        trainTable1 = trainTable1[:c] + trainTable1[c+1:]
        c = c -1;
        d = d+1;
    c = c + 1;
    


### we need evaluation. Done!logistic_tanh_relu_identity
### activation function change
### create a table for different activatio functions and hiden layer, input nodes. 
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6, 4), random_state=1, activation = 'logistic')
len(trainTable1)
len(trainTable2)
clf.fit(trainTable1, trainTable2)
result = clf.predict(testTable1)
print(testTable1)
print(result)
print(testresult)
sum = 0;
c= 0 ;
for i in result:
    sum = sum + sqrt((float(testresult[c])-float(result[c]))**2)
    c = c + 1
sum = sum / c;
print(sum)
print(len(result))
print(len(testresult))
print(clf)

#print(classification_report(result,testresult))