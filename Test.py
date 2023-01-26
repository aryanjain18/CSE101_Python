words = "Abuse Adult Agent Anger Apple Award Basis Beach Birth Block Blood Board Brain Bread Break Brown Buyer Cause Chain Chair Chest Chief Child China Claim Class Clock Coach Coast Court Cover Cream Crime Cross Crowd Crown Cycle Dance Death Depth Doubt Draft Drama Dream Dress Drink Drive Earth Enemy Entry Error Event Faith Fault Field Fight Final Floor Focus Force Frame Frank Front Fruit Glass Grant Grass Green Group Guide Heart Henry Horse Hotel House Image Index Input Issue Japan Jones Judge Knife Laura Layer Level Lewis Light Limit Lunch Major March Match Metal Model Money Month Motor Mouth Music Night Noise North Novel Nurse Offer Order Other Owner Panel Paper Party Peace Peter Phase Phone Piece Pilot"
#words = "Aryan Tisha"

words = words.lower()
list_words = words.split()

import random
r = random.randint(0,len(list_words)-1)
ques = [*list_words[r]]

lis_ans = ["-","-","-","-","-"]
i = 6
while i > 0:
    word = input("No. Of Guesses Left %s - Your Guess: " %i)
    import requests
    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    url = api_url+word
    resp = requests.get(url)
    if resp.status_code == 200:  #Word Exists
        temp_lis = [*word]
        print("Your Guess: ", *temp_lis)
        count = 0
        flag = 0
        extrachar = []
        for j in range(5):
            if temp_lis[j] == ques[j]:
                lis_ans[j] = ques[j]
                count+=1 
                flag = 1
            else:
                if temp_lis[j] in ques:
                    extrachar.append(temp_lis[j])
                continue
        if count == 5:
            print("You Won! \nYes %s is the correct word." %list_words[r].upper()) 
            break 
        else:
            extrachar = set(extrachar)
            print("The Correctly Placed Characters Are: ", *lis_ans)
            print("Other Characters Are: ", *extrachar)
            print()
        if flag == 0:
            i-=1
    else: #Word Does NOT Exist.
        print("Sorry, Please Enter A Valid English Language Word.")
