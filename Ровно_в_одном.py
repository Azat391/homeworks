# Ровно в одном 1️⃣
def is_one_away(word1, word2):
    count=0
    i=0
    while i<(max(len(word1),len(word2))-1):
        
        if word1[i]!=word2[i]:
            count+=1
        i+=1
    if count<=1:
        return True
    else:
        return False
word1=input()
word2=input()
print(is_one_away(word1, word2))