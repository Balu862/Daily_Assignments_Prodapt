import time,threading
def prime():
    for i in range(2,500):
        t=0
        for j in range(2,i):
            if i%j==0:
                t=1
                #time.sleep(1)
        if t==0:
            print("prime",i)
            #time.sleep(1)
def palindrome():
    for i in range(2,500):
        a=str(i)
        if a==a[::-1]:
            print("palindrome",i)
            

t1=threading.Thread(target=prime)
t2=threading.Thread(target=palindrome)
t1.start()
t2.start()
t1.join()
t2.join()