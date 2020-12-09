# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:39:22 2020

@author: hites
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import collections 
from scipy.stats import entropy

# function for calulation of entropy
# This function takes bytes of file as input and return the entropy of the file 
# bases keeps track of number of bytes in file and dist is the normalization of bases
# entropy value is calculated by entropy() method which takes dist and base as arguments
# entropy value is returned

def calculate_entropy(data):
    bases = collections.Counter(data)  
    # define distribution using divide every value of bases with total values of bases
    dist = [x/sum(bases.values()) for x in bases.values()]
    # from scipy library use entropy method to calculate entropy with base 2
    entropy_value = entropy(dist, base=2,axis=0)
    return entropy_value

# open file from directory. If not in directory then give full path to file.
file_name = r"488303.png"
input_file = open(file_name,"rb")
#key is selected here randomly of 16 bytes length
key = get_random_bytes(16)
# buffer size is here defined as 64 kb
buffer_size = 65536 
#open outputfile as encrypted.bin in write mode
output_file = open("encrypted.txt", 'wb')

# using CFB mode to create cipher takes argument as key and cipher mode
cipher = AES.new(key, AES.MODE_CFB)
# add bytes into buffer from input file and size of buffer
buffer = input_file.read(buffer_size)


# encrypt data and write into the output file until the end of input file 
# and close the files
while len(buffer) > 0:
    ciphered_bytes = cipher.encrypt(buffer)
    output_file.write(ciphered_bytes)
    buffer = input_file.read(buffer_size)
input_file.close()
output_file.close()

# open file in read mode for finding entropy and read as bytes
input_file = open(file_name,"rb")
output_file = open("encrypted.txt","rb")
i_f = input_file.read()
o_f = output_file.read()
# call calculate_entropy method and print entropy
print(f'entropy is {calculate_entropy(i_f)}')
print(f'entropy is {calculate_entropy(o_f)}')

