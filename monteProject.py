#Siddharth Vadgama
#UTA ID-1001397508
import numpy as np

def estDuration(runs) :
    # put student code here
    A=np.random.uniform(0,100,size=(runs,1))
    B=np.random.uniform(0,100,size=(runs,1))
    C=np.random.uniform(0,100,size=(runs,1))
    D=np.random.uniform(0,100,size=(runs,1))

    A[(A>=0)&(A<10)]=2
    A[(A>=10)&(A<30)]=4
    A[(A>=30)&(A<=100)]=3
    
    B[(B>=0)&(B<50)]=1
    B[(B>=50)&(B<=100)]=2
    
    C[(C>=0)&(C<20)]=5
    C[(C>=20)&(C<40)]=8
    C[(C>=40)&(C<=100)]=6
    
    D[(D>=0)&(D<5)]=2
    D[(D>=5)&(D<10)]=3
    D[(D>=10)&(D<20)]=5
    D[(D>=20)&(D<=100)]=4
    
    Total_days=A+B+C+D
    MIN=min(Total_days)
    MAX=max(Total_days)
    avg=sum(Total_days)/runs
    return MIN,MAX,avg

########################  main  ########################
if __name__ == "__main__" :
    runs = 1000

    minDays, maxDays, avg = estDuration(runs)

    print("min = %d, max = %d, average = %.1f" % (minDays, maxDays, avg))

