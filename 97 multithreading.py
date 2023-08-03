import time
import threading
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print(f"sleeping time is {seconds} seconds")
    time.sleep(seconds)
def main():
  # using normal method
  # func(3)
  # func(2)
  # func(1)

  #now function using threading

  t1=threading.Thread(target=func,args=[4])
  t2=threading.Thread(target=func,args=[2])
  t3=threading.Thread(target=func,args=[1])

  t1.start()
  t2.start()
  t3.start()


def poolingDemo():
   with ThreadPoolExecutor() as executor:
    #   future = executor.submit(func,3)
    #   print(future.result)
    #   future = executor.submit(func,2)
    #   print(future.result)
    #   future = executor.submit(func,4)
    #   print(future.result)
    l = [3,4,5,2,1,2]
    results = executor.map(func,l)
    for i in results:
       print(i)

poolingDemo()      