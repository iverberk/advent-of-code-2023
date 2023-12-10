"""
Advent-of-Code 2023: Day 9 / Part 2
"""

from itertools import pairwise

reports = []
with open("input", "r", encoding="UTF8") as file:
    for report in file:
        reports.append([int(reading) for reading in report.strip().split()])

sum = 0
for report in reports:
    report = report[::-1]
    report_sum = report[-1]
    while set(report) != {0}:
        report = [pair[1] - pair[0] for pair in pairwise(report)]
        report_sum += report[-1]
    sum += report_sum

print(sum)
