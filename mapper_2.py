import sys
import math

player_cent = {'player':[],'stat_matrix':[] , 'current_cent':[] ,'dist_matrix':[],'min_index_group':[]}

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    try:
        player_cent['player'].append(line[0])
        player_cent['stat_matrix'].append(line[1:4])
        player_cent['current_cent'].append(line[4:7])
    except:
        pass

cent_list = []
for i in player_cent['current_cent']:
	if not i in cent_list:
		cent_list.append(i)

def e_dist(stat_matrix,cent_list):
	mat_dist = []
	for i in range(0,len(cent_list)):
		dist_sqrd = 0
		for j in range(0,len(cent_list[i])):
			dist_sqrd += (float(stat_matrix[j]) - float(cent_list[i][j]))**2

		dist = math.sqrt(dist_sqrd)
		mat_dist.append(dist)

	player_cent['dist_matrix'].append(mat_dist)

for k in range(0,len(player_cent['stat_matrix'])):
	e_dist(player_cent['stat_matrix'][k],cent_list)

for i in player_cent['dist_matrix']:
    player_cent['min_index_group'].append(i.index(min(i)))

print(player_cent['dist_matrix'])

for i in range(0,len(player_cent['stat_matrix'])):
	print(player_cent['player'][i] + '\t' + str(player_cent['stat_matrix'][i][0])+ '\t' + str(player_cent['stat_matrix'][i][1])+ '\t' + str(player_cent['stat_matrix'][i][2]) + '\t' + str(player_cent['min_index_group'][i]))