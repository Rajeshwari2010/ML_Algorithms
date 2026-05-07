#Multithreading with thread pool

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Numbers: {number}"

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,numbers)

for result in results:
    print(result)    

##multiproccessing with pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Numbers: {number}"

numbers=[1,2,3,4,5]

with ProcessPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,numbers)

for result in results:
    print(result)    

