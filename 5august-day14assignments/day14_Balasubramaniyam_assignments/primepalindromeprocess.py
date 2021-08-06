import time,multiprocessing,logging
logging.basicConfig(filename='multiprocess.log',level=logging.DEBUG)
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
        logging.info("plaindrome completed")
                
    if __name__ == "__main__":
        t1=multiprocessing.Process(target=prime)
        t2=multiprocessing.Process(target=palindrome)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
except:
    logging.error("please check the program")
