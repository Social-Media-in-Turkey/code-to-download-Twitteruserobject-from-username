# Instructions
The first part of this python code, follower_tweepy.py, is about getting user objects by using twitter API and write them as json files. 
The second part, merge_jsonfiles.py, deals with converting all json files into one with unique user ids.

The codes are written in Google Colab, but by changing trajectory, you can use any IDE you want.

### follower_tweepy.py

* Configparser is used to keep Twitter API access tokens and keys secret. After you save your keys as a txt file, you can change filenames in line 20 and run the code.
* From line 34 to 39, you should change the screen name that you want to get followers from in line 34 and the file name that you want to give the user oject collection of that user's followers as json file in line 36. Then it will write the user objects line by line.

### merge_jsonfiles.py

* merge_jsons() takes the path name that your json files are located then writes them all in a single json file called "merged_filename.json".
  * You can change the name of the file as you wish.
* From line 20 to 26, the code creates a new json file as "merged_filename_with_nonduplicates.json" at the end of the iteration, it will write each user objects once and eliminates the duplicates from the file. 
  * You can change the name of the file as you wish in line 22. 
* In line 20, it keeps an empty id set in the beginning and then in each iteration, it adds the user ids that are not written to the json file yet.




