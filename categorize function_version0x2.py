def fire(token, match):                 #we need consider verb/noun variations that's the first problem we meet
    letters=list(token)
    letters_m=list(match)
    match_times=0
    k=0
    for i in range(max(len(letters),len(letters_m))):
        if i>=len(letters) or i-k>=len(letters_m):
            break   
        if (letters[i]>='a' and letters[i]<='z') or letters[i]==' ':
            if letters[i]==letters_m[i-k]:
                match_times=match_times+1
        else:
            k=k+1  
    fit_value=match_times/(len(token)-k)
    if fit_value>0.7:
        return 1
    else:
        return 0
"""only consider the suffix"""
""" in this Fire function we calculate the degree of similarity between the tokens and words in our dictionary. but this is not a perfect
 version, cause we can't just match and judge the letter one by one, we should consider the principle of word formation and give the weight
 of letters in the different sequence or position of a word like "event" ->"events"  the suffix give more weights for calculation """               
    
def categorized(tokens):
    score_1=0
    score_2=0
    score_3=0
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_1:
            if fire(token,words)==1:
                print(token,words)
                score_1+=1
        for words in Library_2:
            if fire(token,words)==1:
                print(token,words)
                score_2+=1
        for words in Library_3:
            if fire(token,words)==1:
                score_3+=1
    print(score_1,score_2,score_3)   
    if score_1>max(score_2,score_3):
        return 'study'
    elif score_2>max(score_3,score_1):
        return 'sports'
    elif score_3>max(score_1,score_2):
        return 'social'
    else:
        return 'uncertain'

def sub_categorized_study(tokens):
    Library_a=['struggle','difficult','difficulty','bad','help','anxiety','nervous']
    Library_ax1=['do not',"don't",'not','hate','shy']
    Library_b=['interesting','information','interest','practical']
    score_1=0
    score_2=0
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_a:
            if fire(token,words)==1:
                print(token,words)
                score_1+=1
        for words in Library_b:
            if fire(token,words)==1:
                print(token,words)
                score_2+=1
        for words in Library_ax1:
            if fire(token,words)==1:
                score_1=score_1*-1
    print(score_1,score_2)   
    if abs(score_1)>score_2:
        if score_1>=0:
            print("I suggest you can seeking out a study group for what you are struggling now.")
        else:
            print("I suggest you can seeking out a student advisor for what you are struggling now.")
    else:
        print("Very interesting topic, maybe you can contact form of the Student Desk!")

def sub_categorized_sports(tokens):
    score_1=0
    score_2=0
    Library_a=['aikido','basketball','tennis','swimming','football','zumba','karate','yoga','waterpolo']
    Library_b=['try','new','explore','find','taste',"don't",'do not'] 
    for token in tokens:
        for words in Library_a:
            if fire(token,words)==1:
                print(token,words)
                score_1+=1
        for words in Library_b:
            if fire(token,words)==1:
                print(token,words)
                score_2+=1
    print(score_1,score_2)   
    if score_1>score_2:
        print('you are lucky, this is sport is available in our university, you can find more information on University Sports Centre website!')
    elif score_1<score_2: 
        print("seems you want try new sport, what kind of sports you want ")

def sub_categorized_social(tokens):
    score_1=0
    score_2=0
    Library_a=['poetry pals','debate club','science society','painting and pottery','language club','international students society','students for sustainability','animal shelter volunteers','bunch of backpackers']
    Library_ax1=['try','new','explore','find','taste',"don't",'do not']
    Library_e=['upcomming','events','enjoy','activity','activities']
    for token in tokens:
        for words in Library_a:
            if fire(token,words)==1:
                print(token,words)
                score_1+=1
        for words in Library_b:
            if fire(token,words)==1:
                print(token,words)
                score_2+=1
    print(score_1,score_2,)   
    if score_1>max(score_2,score_3):
        return 'events'
    elif score_2>max(score_3,score_1):
        return 'association'

def text_dealing(): 
    Original_text=input()
    original_text=Original_text.lower()
    text_token=original_text.split()
    return text_token    


Library_1=['math','study','academic','book','scholarship','research','exam','learn','test','physics']
Library_2=['sports','run','aikido','health','strong','play','basketball','tennis','swimming','football','zumba','karate','yoga','waterpolo']
Library_3=['social','party','event','activity','association','club','friends','trip','night','picnic','festival','celebration']
print("Hi, I'm Unibot. What can I help you with?")

category=categorized(text_dealing())

if category=='study':
    print("Oh, I think it's about study, are you struggling with something or only interested in practical information?")
    sub_category=sub_categorized_study(text_dealing())
if category=='sports':
    print("Oh, I think it's about sports, Any thing I can help you on it? I'm glad to hear you to tell me more ")
if category=='social':
    print("Oh, I think it's about Social activities, Any thing I can help you on it? I'm glad to hear you to tell me more")
if category=='uncertain':
    print("Sorry, it seems I can't understand your problem or this problem of its field I can't help, try to ask me again, thank you")
    
    

