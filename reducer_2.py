import sys

player_cent = {'player':[],'stat_matrix':[] , 'new_cent':[] ,'cent_group':[]}

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    try:
        player_cent['player'].append(line[0])
        player_cent['stat_matrix'].append(line[1:4])
        player_cent['cent_group'].append(line[4])
    except:
        pass


cent_dict = {'cent_0':[],'cent_1':[] , 'cent_2':[] ,'cent_3':[]}
for i in range(0,len(player_cent['stat_matrix'])):
	try:
		lst_name = 'cent_' + str(player_cent['cent_group'][i])
		cent_dict[lst_name].append(player_cent['stat_matrix'][i])
	except:
		pass

new_cent = []
for i in range(0,4):
    lst_name = 'cent_' + str(player_cent['cent_group'][i])
    sums = [0,0,0]
    length = len(cent_dict[lst_name])
    for j in cent_dict[lst_name]:
        for k in range(0,len(j)):
            j[k]= float(j[k])
            sums[k] += j[k]
    for l in range(0,len(sums)):
        sums[l] = sums[l]/length

    new_cent += sums

new_cent = [new_cent[0:3],new_cent[3:6],new_cent[6:9],new_cent[9:12]]


for i in range(0,len(player_cent['cent_group'])):
    player_cent['new_cent'].append(new_cent[int(player_cent['cent_group'][i])])



for i in range(0,len(player_cent['new_cent'])):
    try:
        print(player_cent['player'][i] + '\t' + str(player_cent['stat_matrix'][i][0])+ '\t' + str(player_cent['stat_matrix'][i][1])+ '\t' + str(player_cent['stat_matrix'][i][2])+ '\t' + str(player_cent['new_cent'][i][0])+ '\t' + str(player_cent['new_cent'][i][1])+ '\t' + str(player_cent['new_cent'][i][2]))
    except:
        pass
    