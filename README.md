Contributors: Vaishali Sharma, Brenden McShanne

NBA Shot Log Analysis: MapReduce program for Fear Score and Comfortable Zone Identification

Objectives: 
The project has two goals: 

Goal1: Finding the “most unwanted defender” for each player based on the fear score

Goal2: Classify each player’s records into 4 comfortable zones and find which comfortable zone is best for players based on their hit rate

Prerequisites: 
This project requires the SSL, Hadoop, and an active Google Cloud Platform account/credit 

Installation: 
-	Hadoop installation, install.sh, test files (test.sh) for running mapper and reducer code files. 
-	Setting up 3-node cluster on Google Cloud Platform
-	Requires Python 3+

Dataset: 
NBA dataset contains 21 Columns (e.g., player_name, CLOSE_DEF_DIST etc.) and 128,069 rows (all players information) is used. The source of the data set is Kaggle: https://www.kaggle.com/dansbecker/nba-shot-logs%20

Code Structure: 

Goal 1: “Most Unwanted Defender” for each player
Step 1: Mapper.py : reads csv and passes player, defender, and outcome to reducer 
Step 2: reducer.py : aggregated the mapped data to retrieve each players lowest success rate against a defender

Goal 2: “Comfortable Zones” for each player
Step1: mapper1.py :  Read csv and send the output to the first reducer.
Step 2: reducer1.py : Centroids Initialization - outputs players id, average stat line and current centroid to mapper 2. 
Step 3: mapper2.py : Find closest centroid and group the players 
Step 4: reducer2.py : Centroids normalization
 


