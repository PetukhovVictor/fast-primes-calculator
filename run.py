# -*- coding: utf-8 -*-

import sys

from lib.primes_calculator import get_prime

prime_number = sys.stdin.readline()

prime = get_prime(int(prime_number))

sys.stdout.write(str(prime))
