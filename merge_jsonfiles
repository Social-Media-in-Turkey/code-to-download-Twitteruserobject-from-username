'''
You should define your path as 
path = "C:/TrajectoryThatContainsJSONFiles/*.json"
so that it can detect all json files in the corresponding file.

'''

path = "C:/Users/HP/Desktop/Özgem/Koç/Twitter Data/*.json"

def merge_jsons(path):
    result = ''
    for f in glob.glob(path):
        with open(f, "r") as infile:
            result += infile.read()
    
    with open("merged_file_FG.json", "w") as outfile:
        outfile.writelines(result)

merge_jsons(path)
