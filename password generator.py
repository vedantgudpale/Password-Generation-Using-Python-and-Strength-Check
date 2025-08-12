import random
import math
import pandas as pd
from datetime import timedelta

# Character sets
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Function to generate password
def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    charset = LOWER
    if use_upper:
        charset += UPPER
    if use_digits:
        charset += DIGITS
    if use_symbols:
        charset += SYMBOLS
    return ''.join(random.choice(charset) for _ in range(length))

# Estimate charset size
def charset_size(pwd):
    size = 0
    if any(c.islower() for c in pwd):
        size += 26
    if any(c.isupper() for c in pwd):
        size += 26
    if any(c.isdigit() for c in pwd):
        size += 10
    if any(c in SYMBOLS for c in pwd):
        size += len(SYMBOLS)
    return size

# Calculate entropy
def entropy_bits(pwd):
    s = charset_size(pwd)
    return len(pwd) * math.log2(s) if s > 1 else 0

# Convert seconds to readable format
def human_time(seconds):
    if seconds > 1e40:
        return "practically infinite"
    years = seconds / (3600 * 24 * 365)
    if years >= 1:
        return f"{int(years)} years"
    days = seconds / (3600 * 24)
    if days >= 1:
        return f"{int(days)} days"
    hours = seconds / 3600
    if hours >= 1:
        return f"{int(hours)} hours"
    minutes = seconds / 60
    if minutes >= 1:
        return f"{int(minutes)} minutes"
    return f"{int(seconds)} seconds"

# Strength label
def strength_label(bits):
    if bits < 28:
        return "Very Weak"
    if bits < 36:
        return "Weak"
    if bits < 60:
        return "Moderate"
    if bits < 80:
        return "Strong"
    return "Very Strong"

# Main program
if __name__ == "__main__":
    guess_rates = {
        "Low (1e3/sec)": 1e3,
        "Moderate (1e6/sec)": 1e6,
        "High (1e9/sec)": 1e9,
        "Massive (1e12/sec)": 1e12
    }

    results = []

    # Generate 10 passwords of varying complexity
    complexities = [
        (8, False, False, False),  # only lowercase
        (8, True, False, False),   # lower + upper
        (10, True, True, False),   # lower + upper + digits
        (12, True, True, True),    # full set
        (16, True, True, True),    # long strong
    ]

    for length, upper, digits, symbols in complexities:
        pwd = generate_password(length, upper, digits, symbols)
        bits = entropy_bits(pwd)
        entry = {
            "password": pwd,
            "length": length,
            "entropy_bits": round(bits, 2),
            "strength": strength_label(bits)
        }
        for label, rate in guess_rates.items():
            guesses_needed = 2 ** bits / 2
            crack_time = guesses_needed / rate
            entry[label] = human_time(crack_time)
        results.append(entry)

    # Save results
    df = pd.DataFrame(results)
    df.to_csv("password_strength_results.csv", index=False)
    print(df)
    print("\nResults saved to password_strength_results.csv")
