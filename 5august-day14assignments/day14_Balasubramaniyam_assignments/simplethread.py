import threading,time,multiprocessing

# def printnumber():
#     for i in range(1,10):
#         time.sleep(5)
#         print(i)
# def sayhello():
#     for i in range(1,10):
#         time.sleep(3)
#         print("Hello")
# t1=threading.Thread(target=printnumber)
# t2=threading.Thread(target=sayhello)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("..............")


# def squarenumber(mylist):
#     for i in mylist:
#         time.sleep(1)
#         print(i*i)
# def cubenumber(mylist):
#     for i in mylist:
#         time.sleep(1)
#         print(i*i*i)

# mylist=[1,2,3,4]
# t1=threading.Thread(target=squarenumber,args=(mylist,))
# t2=threading.Thread(target=cubenumber,args=(mylist,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

def findeven(mylist):
    for i in mylist:
        if i%2==0:
            time.sleep(1)
            print(i)
def findodd(mylist):
    for i in mylist:
        if i%2!=0:
            time.sleep(1)
            print(i)

if __name__ == "__main__":
    mylist=[1,2,3,4,5,6,7,8]
    p1=multiprocessing.Process(target=findeven,args=(mylist,))
    p2=multiprocessing.Process(target=findodd,args=(mylist,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

'''write a program prime number between 2 and 500 and to palindrome numbers 2 and 500 using multitreading and multiprocessing'''
