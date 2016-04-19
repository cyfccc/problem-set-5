#! /usr/bin/env python

import pybedtools

filename = 'lamina.bed'
genes = pybedtools.BedTool(filename)

max_start = 0 
chrom = ''
for record in genes:
    if  max_start < record.start:
         max_start = record.start
         chrom = record.chrom
print "answer-1: ", chrom, max_start 

list = []
max_start = 0

for record in genes:
    list.append(record.start)
max_start = sorted(list, reverse=True)[0]

#for record in genes:
#   if record.start == max_start:
#        print record.chrom, record.start

max_end = 0
chrom = ''
start = 0
for record in genes:
    if  record.chrom == 'chrY' and max_end < record.end:
        max_end = record.end
        chrom = record.chrom
        start = record.start
print "answer-2: ", chrom,':',start,'-',max_end
