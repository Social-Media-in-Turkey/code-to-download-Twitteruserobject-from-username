'''
You should define your path as 
path = "/TrajectoryThatContainsJSONFiles/*.json"
so that it can detect all json files in the corresponding file.

'''
#Define your path name here. Example --> path = r'/content/gdrive/MyDrive/Social-Media-in-Turkey/Twitter'

import json
import glob
from google.colab import drive
drive.mount('/content/gdrive')

!ls "/content/gdrive/MyDrive/..." 

def merge_jsons(path):
    result = ''
    for f in glob.glob(path):
        with open(f, "r") as infile:
            result += infile.read()
     
    with open("merged_filename.json", "w") as outfile:    # Write the filename that you want to save your merged file in the place of "merged_filename.json" with .json at the end. 
        outfile.writelines(result)

merge_jsons(path)

id_set = set()

with open ("merged_filename_with_nonduplicates.json", "w") as outfile:           # Give your file a name which will contain user objects with unique user ids. 
    for line in open("merged_filename.json", "r"):                               # It should be the same file name that you created above. 
            if line.split(' ')[1][:-1] not in id_set:
                outfile.write(line)
                id_set.add(line.split(' ')[1][:-1])
                
                
