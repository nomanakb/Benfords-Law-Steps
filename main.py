#!/usr/bin/env python3

"""
# Author: Noman Akbar
# Data: 13 August 2020
"""

import csv
import collections
import matplotlib.pyplot as plt

# Read the CVS file, only load the column containing steps
steps = []
with open('Step Data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        steps.append(row[2])  # Third row contains the step data

# Find the first digit of each number
FirstDigits = map(lambda n: str(n)[0], steps[1:])
# Find the total number of occurances for digits 0-9
CountDigits = collections.Counter(FirstDigits)
# Extract the frequency of each digits 0-9
DigitFrequency = []
for n in range(0, 10):
    DigitFrequency.append(CountDigits[str(n)])
# Find the total number of values that are not zero
num = sum(DigitFrequency) - DigitFrequency[0]
# Find the percentage for each digit
PercentageDigits = [(i / num)*100 for i in DigitFrequency]
# Freqeuncy for an ideal Benford curve
Benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
# Printout the values
print(PercentageDigits)
# Plot the curve and compare with ideal Benford curve
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], PercentageDigits[1:])
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], Benford, linestyle='--')
plt.legend(["Number of Steps in an Hour", "Benfords Law"])
plt.xlabel('First Digit')
plt.ylabel('$P_d$ (%)')
plt.show()
