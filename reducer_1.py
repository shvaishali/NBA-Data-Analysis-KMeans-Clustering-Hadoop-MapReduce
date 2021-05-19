#!/usr/bin/python
#!/usr/bin/python
from operator import itemgetter
from collections import defaultdict
import sys

player_prev = ''
player_mat = []
player_totals = [0,0,0,0]
counter = 0
cent_1 = [5,5,5]
cent_2 = [18,18,4]
cent_3 = [15,6,5]
cent_4 = [7,14,3]
cent_list = [cent_1,cent_2,cent_3,cent_4]

for line in sys.stdin:
    line = line.strip()

    #print(line)
    player, num, shot_clock, shot_dist, close_def = line.split('\t')

    try:
        shot_clock = float(shot_clock)
    except:
        shot_clock = float(0)

    if player == player_prev:
        player_mat = [int(num),shot_clock,float(shot_dist),float(close_def)]
        for i in range(4):
            player_totals[i] += player_mat[i]
        player_prev = player
    else:
        for i in range(1,4):
            if player_totals[0]!=0:
                player_totals[i] = player_totals[i]/player_totals[0]
        player_totals = player_totals[1:4]
        counter += 1
        r_l = cent_list[counter%4]
        if player_totals[0] != 0:
            print(player_prev + '\t' + str(player_totals[0])+ '\t' + str(player_totals[1])+ '\t' + str(player_totals[2]) + '\t'+ str(r_l[0]) + '\t' + str(r_l[1]) + '\t' + str(r_l[2]))
        player_totals = [0,0,0,0]
        player_totals += player_mat
        player_prev = player
	