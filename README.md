# DES_cryptanalysis
Implementation of various techniques for cryptanalysis of different versions of DES

## SDES Implementation
The self implementation of SDES is done according to http://mercury.webster.edu/aleshunas/COSC%205130/G-SDES.pdf
Performance   -> 5 to 10 micro seconds

## Brute Force
The implementation of Brute Force in which we create all possible keys and run the code to genrate cipher than compare it with calculated cipher

Performance   -> 20 miliseconds to run a exaustive search for a plain cipher text pair<br>
Acuracy       -> About 5 to 10 possible keys for a single pair
