import re
import pandas as pd
def print_words(filename):   
    # count = 0 
    # print(filename)
    'Comment 0: Initializing dictionary for temporarily storing and comparing words to find frequencies'
    d={      
    }
    count = 0
    for line in filename:
        line = line[:-1:]
        line = re.sub(",","",line)
        line = line.split(",")
        sentence = line[0]
        
        'Comment 1: converting input to lower case for comparing all the values'
        sentence = sentence.lower()      
        'Comment 1(a): eliminating spaces and replace special character with space'
        sentence = sentence.strip()        
        'Comment 1(b): Replacing special characters with blank space'        
        sentence = re.sub("[,“.;”]","",sentence)
        sentence = re.sub("  ","",sentence)        
        # print("STEP 1: Sentence : ",sentence)         
        'Comment 2: Splitted csv file sentence into words'
        collection_words = sentence.split(" ")        
        # print("STEP 2: Words : ",collection_words) 
           
        'Comment 3: Read each word and comparing with whichever stored in dictionary'
        for eachword in collection_words:
            # print(eachword)
            if eachword in d:
                d[eachword]+=1
            else:
                d[eachword]=1
    # print("STEP 3 : ",d)
                          
    #Comment 4: assigning dictionary to DataFrame
    df=pd.DataFrame(d,index=['Final Computation of words and frequency'])
    print("--------------------------")
    print("Printing Data Frame Finally : ",df)              
    filename.close()
        
           

#invoking function
filehandler = open(r'C:\Users\Administrator\OneDrive\Desktop\UST Training\Milestone_Assessment1\The_Alchemist.csv', encoding="utf8")
print_words(filehandler)
