# Creating Passwords with Python and Strength Check

## Summary
This project is a password generator and strength assessor that runs on Python. It generates random passwords with different lengths and levels of complexity, then assesses them according to security best practices, estimated crack times, and entropy.


## Features: - Create random passwords with a configurable level of difficulty
  Lowercase letters
  Capital letters
  - Numbers
  - Symbols
To determine the strength of a password, compute **entropy**.
Calculate **crack times** for varying attacker speeds.
For reference, save the results to a CSV file.

## Sample Output 
| password       | length | entropy_bits | strength | Low (1e3/sec) | Moderate (1e6/sec) | High (1e9/sec) | Massive (1e12/sec) |
|----------------|--------|--------------|----------|---------------|--------------------|----------------|--------------------|
| xagpdbsz       | 8      | 37.6         | Weak     | 5 days        | 7 minutes          | 0 seconds      | 0 seconds          |
| Kjeiopwd        | 8      | 45.6         | Moderate | 17 years      | 6 days             | 9 minutes      | 0 seconds          |
| aY4x9pQwR2      | 10     | 59.4         | Moderate | 19,000 years  | 19 years           | 7 days         | 10 minutes         |

*(The values above are examples; each run will produce a different output.)*

## How It Operates
To create a password, a random selection of characters (uppercase, lowercase, digits, and symbols) is made from predetermined sets.
2. **Strength Evaluation** Determines entropy bits and labels them as such:
   Extremely Weak, Weak, Moderate, Strong, and Very Strong
3. Estimating the Crack Time  
   calculates how long it would take to use brute force to crack the password at four different attacker speeds:
   - 1,000 guesses per second - 1,000,000 guesses per second - 1,000,000,000 guesses per second - 1,000,000,000,000 guesses per second
