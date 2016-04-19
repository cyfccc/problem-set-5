#! /usr/bin/env python

from collections import Counter

filename = 'SP1.fq'
line_num = 0
name = ''
seq = ''
counts = {}

max_c = 0
max_name = ''

for line in open(filename):
    line_num += 1
    if line_num < 41:
        line_type = line_num % 4 
        if line_type == 1:
            name = line.strip()
        elif line_type == 2:
            seq = line.strip()
            counts = Counter(seq)
            if counts['C'] > max_c:
                max_c = counts['C']
                max_name = name
                max_seq = seq
print "answer-3: ", max_name

qual_sum = 0
max = 0
def sum_quals(qual):
    sum = 0
    for char in qual:
        sum += ord(char)
    return sum
for line in open(filename):
    line_num += 1
    line_type = line_num % 4
    if line_type == 0:
        qual = line.strip()
        qual_sum = sum_quals(qual)
        if qual_sum > max:
            max = qual_sum
print "answer-4: ", max

def reverse_compliment(seq):
    comps = []
    empty = ''
    for char in seq:
        if char == 'A':
            comps.append ('T')
        if char == 'T':
            comps.append ('A')
        if char == 'G':
            comps.append ('C')
        if char == 'C':
            comps.append ('G')
    for char in reversed(comps):
        empty += char
    return empty

line_num = 0
print"answer-5: "
for line in open(filename):
    line_num += 1
    if line_num < 41:
        line_type = line_num % 4
        if line_type == 1:
            name = line.strip()
        elif line_type == 2:
            seq = line.strip()
            print reverse_compliment(seq)
