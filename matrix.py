import random

def random_number():
    return random.randint(-1,1)/1.0

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

def create_b(L,M):
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

def create_xy(L):
    i=0
    list=[]
    while i<=L:
        list.append([])
        i=i+1
    if i>L:
        return list

