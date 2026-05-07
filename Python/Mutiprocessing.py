#processes that run in parallel
#CPU-Bpund task
#parallel execution -Multiple cores of CPU

'''import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"square: {i**2}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i**3}")  

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t1 = time.time()

    p1.start()
    p2.start()

    # Wait for both processes
    # With join():
    # Main program waits until p1 and p2 finish
    p1.join()
    p2.join()

    finished = time.time() - t1
    print(finished)'''


#EXAMPLE

import multiprocessing
import time
import math  
import sys


''' Python 3.11+ has a default limit: 4,300 digits
If you try converting a bigger number:  int("9" * 5000)
You get:
ValueError: Exceeds the limit for integer string conversion...'''

#Increase max number of digits for integer conversion
sys.set_int_max_str_digits(100000)

def factorial(num):
    print(f"Computing factorial of {num}...")
    result = math.factorial(num)
    print(f"Number of digits in factorial of {num}: {len(str(result))}")
    return result

if __name__ == "__main__":
    numbers = [5000, 8000, 3000, 4000]
    start_time = time.time()  # Make sure this line is before you calculate end_time

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    end_time = time.time() - start_time  # Now start_time exists
    print("Factorials computed.")
    print(f"Time taken: {end_time:.2f} seconds")

