"""
    This file consists of the script for performing brute force attack on SDES
"""
from sdes.sdes_cipher import main as main_sdes

import numpy
import itertools
import time

def keysFormation(key_size=10):
    """
        Forms all possible keys of given key size
        returns a genrative iterater where each element is a tuple consisting a string
    """
    all_keys =  numpy.array([''.join(seq) for seq in itertools.product("01", repeat=key_size)])

    key_genrator = itertools.product(all_keys)

    return key_genrator

def calculateCost(given_text, actual_text):
    """
        Calculates the cost for the % correctness of the calculated text and the correct text
        return is a in less than 100
        100 means perfect match
    """
    total_correct = 0

    for bit in range(len(given_text)):
        if given_text[bit] == actual_text[bit]:
            total_correct += 1

    return int((float(total_correct)/len(given_text))*100)

def runExaustiveSearch(plain_text, cipher_text):
    """
        Run the exaustive search using the above keys
    """
    max_cost        = 0
    presumed_keys   = []

    for key in keysFormation():
        sdes_obj = main_sdes(plain_text, key[0], encrypt=True)
        cipher   = sdes_obj.cipher_text

        cost = calculateCost(cipher, cipher_text)

        if cost > max_cost:
            presumed_keys = [key[0]]
            max_cost = cost
        elif cost == max_cost:
            presumed_keys.append(key[0])

    return (presumed_keys, max_cost)

if __name__ == "__main__":
    plain_text  = '11001001'
    key         = '1010101011'
    cipher_text = main_sdes(plain_text, key, True).cipher_text

    start = time.time()
    search, cost = runExaustiveSearch(plain_text, cipher_text)
    stop  = time.time()

    total_time = stop - start

    print 'Cipher -> ', cipher_text
    print 'Time taken -> ', total_time
    print 'Key present in sol -> ', key in search
    print 'Presumed Cost -> ', cost
    print 'All matching keys -> ', search
