#standards & hyperparameters
import random
import numpy as np
import math

cat=[1,1,1,1,0,0,0,0]
dog=[0,0,0,0,1,1,1,1]

L=2
I=8
O=2
alpha=0.5
error=0.07

#training set
input=np.array([1,1,1,1,0,0,0,0])
cat=1
dog=0

def ran_num():
    return random.randint(0,1)/1.0

w1=np.array([[ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num()],
              [ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num()],
              [ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num()],
              [ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num(),ran_num()]])
b1=np.array([ran_num(),ran_num(),ran_num(),ran_num()])
w2=np.array([[ran_num(),ran_num(),ran_num(),ran_num()],
              [ran_num(),ran_num(),ran_num(),ran_num()]])
b2=np.array([ran_num(),ran_num()])

def tanh(x):
    return (math.exp(x)-math.exp(-x))/(math.exp(x)+math.exp(-x))

def forward_prop(input):
    s1=np.matmul(input,np.transpose(w1))+b1
    for i in range(len(s1)):
        s1[i]=tanh(s1[i])
    s2=np.matmul(s1,np.transpose(w2))+b2
    for j in range(len(s2)):
        s2[j]=tanh(s2[j])
    pcat=math.exp(s2[0])/(math.exp(s2[0])+math.exp(s2[1]))
    pdog=math.exp(s2[1])/(math.exp(s2[0])+math.exp(s2[1]))
    return pcat,pdog

def cost_func_cat(cat,dog,pcat,pdog):
    cost=-(cat*math.log(pcat)+dog*math.log(pdog))/2.0
    cost_grad=np.array([pcat-cat,pdog-dog])
    return cost,cost_grad

pcat=forward_prop(input)[0]
pdog=forward_prop(input)[1]
cost=cost_func_cat(cat,dog,pcat,pdog)[0]
cost_grad=cost_func_cat(cat,dog,pcat,pdog)[1]
print(pcat,pdog)
while cost>error:
    w=np.matmul(np.transpose(cost_grad),w2)
    for i in range(len(w)):
        for j in range(len(w1[i])):
            w1[i][j]=w1[i][j]-alpha*w[i]*w1[i][j]
            b1[i]=b1[i]-alpha*(cost_grad[0]+cost_grad[1])/2
    for m in range(len(cost_grad)):
        for n in range(len(w2[m])):
            w2[m][n]=w2[m][n]-alpha*cost_grad[m]*w2[m][n]
            b2[m]=b2[m]-alpha*cost_grad[m]
    pcat=forward_prop(input)[0]
    pdog=forward_prop(input)[1]
    cost=cost_func_cat(cat,dog,pcat,pdog)[0]
    cost_grad=cost_func_cat(cat,dog,pcat,pdog)[1]
if cost<=error:
    print(pcat,pdog)