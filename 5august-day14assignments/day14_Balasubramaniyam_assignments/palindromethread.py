import time,threading,logging
logging.basicConfig(filename='thread1.log',level=logging.DEBUG)
try:
    
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
        logging.info("prime is completed")
    def palindrome():
        for i in range(2,500):
            a=str(i)
            if a==a[::-1]:
                print("palindrome",i)
                
        logging.info("palindrome is completed")
    if __name__ == "__main__":
        t1=threading.Thread(target=prime)
        t2=threading.Thread(target=palindrome)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
except:
    logging.error("error is occured")