import time
from primePy import primes

t1 = time.time()
primzahlen = primes.upto(100000)
t2 = time.time()
print("primePy:", t2-t1)
