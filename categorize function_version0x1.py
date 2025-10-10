Library_1=['study','academic','book','scholarship','research','exam']
Library_2=['sports','sports','run','aikido','health','healthy','strong','play','basketball','tennis','swimming','football','Zumba','karate','yoga','waterpolo']
Original_text=input()
text_token=Original_text.split()
def categorized(tokens):
    score_1=0
    score_2=0
    for token in tokens:
        for words in Library_1:
            if token==words:
                score_1+=1
        for words in Library_2:
            if token==words:
                score_2+=1
    if score_1>score_2:
        return 'study'
    elif score_1<score_2:
        return 'sports'
    else:
        return 'unsure'

category=categorized(text_token)
            
print(text_token,category)