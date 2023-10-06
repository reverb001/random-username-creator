#Many times, a unique needs to be generated. I don't like to use personally identifying info, like my name or email address. 
#This script combines two, random 4-6 long words to be used as a username.

import random

# Opening, reading and closing the dictionary file. 
my_file = open("words.txt", "r") 
all_words = my_file.readlines() 
my_file.close() 



# Strips and lowers all words. Adds them to good_words list if they are 4-6 letters and don't contain a . or -
good_words = []
for word in all_words:
    word = word.strip().lower()
    if len(word) >= 4 and len(word) <= 6 and '.' not in word and '-' not in word:
        good_words.append(word)

# prints out list of 5 different combinations of two words, concatinated. 
i = 0
while i < 5:
    print(good_words[random.randrange(0,len(good_words))] +  good_words[random.randrange(0,len(good_words))])
    i += 1

##for future 
## add switch to configure options, like copy to clipboard or number of results or change the length of the words.