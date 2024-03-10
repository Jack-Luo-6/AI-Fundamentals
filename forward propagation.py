import math
import random

L=int(input('Layers: '))
M=int(input('Inputs: '))

def random_number():
    return random.randint(-1,1)/1.0

def random_input():
    return random.randint(-10,10)

def create_w(L,M):
    n=0
    a=0 
    b=0
    matrix=[]
    while n<=L:
        matrix.append([])
        if n>0:
                while a<L-n+1:
                    matrix[n].append([])
                    if n==1:
                        while b<M-n+1:
                            matrix[n][a].append(random_number())
                            b=b+1
                        if b>=M-n+1:
                            b=0
                            a=a+1
                    else:
                        while b<L-n+2:
                            matrix[n][a].append(random_number())
                            b=b+1
                        if b>=L-n+2:
                            b=0
                            a=a+1
                if a>=L-n+1:
                    b=0
                    a=0
                    n=n+1
        else:
            n=n+1
    if n>L:
        return matrix

def create_b(L):
    n=0
    b=0
    matrix=[]
    while n<=L:
        matrix.append([])
        if n>0:
            while b<L-n+1:
                matrix[n].append(random_number())
                b=b+1
            if b>=L-n+1:
                b=0
                n=n+1
        else:
            n=n+1
    if n>L:
        return matrix

w=create_w(L,M)
b=create_b(L)

def create_input(M):
    i=0
    list=[]
    while i<=M-1:
        list.append(random_input())
        i=i+1
    if i>M-1:
        return list

test={
    'input':create_input(M),
    'expected':100
}

def create_xy(L):
    i=0
    list=[]
    while i<=L:
        list.append([])
        i=i+1
    if i>L:
        return list

y=create_xy(L)
x=create_xy(L)
x[1].append(test['input'])

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

count=1 

def node_result(count,list):
    i=0
    j=0
    l=0 
    result=0
    if count<=len(x)-1:
        while l<=len(w[count])-1:
            if j>len(w[count][l])-1:
                list[count].append(sigmoid(result+b[count][l]))
                l=l+1
                i=0
                j=0
                result=0
            if l>len(w[count])-1:
                l=0
                return list
            while j<=len(w[count][l])-1:
                result=result+w[count][l][j]*x[count][0][i]
                i=i+1
                j=j+1
    else:
        exit()
    
while count<=len(x)-1:
    y=node_result(count,y)
    if count==len(x)-1:
        print(y[count])
        count=count+1
    else: 
        x[count+1].append(y[count])
        count=count+1

if count>=len(x)-1:
    exit()