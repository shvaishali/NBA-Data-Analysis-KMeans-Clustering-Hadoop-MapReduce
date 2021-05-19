#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /pro_1/part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /pro_1/part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /pro_1/part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/part2/shot_logs.csv /pro_1/part2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/pro_1/part2/mapper_1.py -mapper ../../mapreduce-test-python/pro_1/part2/mapper_1.py \
-file ../../mapreduce-test-python/pro_1/part2/reducer_1.py -reducer ../../mapreduce-test-python/pro_1/part2/reducer_1.py \
-input /pro_1/part2/input/* -output /pro_1/part2/output/
for i in {0..5}
do
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/pro_1/part2/mapper_2.py -mapper ../../mapreduce-test-python/pro_1/part2/mapper_2.py \
-file ../../mapreduce-test-python/pro_1/part2/reducer_2.py -reducer ../../mapreduce-test-python/pro_1/part2/reducer_2.py \
-input /pro_1/part2/input/* -output /pro_1/part2/output/
done
/usr/local/hadoop/bin/hdfs dfs -cat /pro-1/part2/output/
../../stop.sh