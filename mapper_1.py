import sys
import string
import csv


for line in sys.stdin:
    line = line.strip()
    row = csv.reader([line], delimiter = ',')
    row = list(row)[0]

    key = row[19]
    shot_clock = row[8]
    shot_dist = row[11]
    close_def = row[16]
    outcome = row[13]
    if outcome == 'made':
    	print(key + '\t' + '1' + '\t' + shot_clock + '\t' + shot_dist + '\t' + close_def)