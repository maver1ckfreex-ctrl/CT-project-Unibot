import random
    
def fire(token, match):                 #we need consider verb/noun variations that's the first problem we meet
    letters=list(token)
    letters_m=list(match)
    print(letters)
    print(letters_m)
    match_times=0
    k=0
    for i in range(max(len(letters),len(letters_m))):
        if i<len(letters) and i-k<len(letters_m): 
            if (letters[i]>='a' and letters[i]<='z') or letters[i]==' ':
                if letters[i]==letters_m[i-k]:
                    match_times=match_times+1
            else:
                k=k+1
        else:
            if len(letters)>len(letters_m):
                if (letters[i]>='a' and letters[i]<='z') or letters[i]==' ':
                    k=k
                else:
                    k=k+1
            if len(letters)<len(letters_m):
                if (letters_m[i]>='a' and letters_m[i]<='z') or letters_m[i]==' ':
                    k=k
                else:
                    k=k+1
    print(k)
    fit_value=match_times/(max(len(token),len(match))-k)
    if fit_value>0.7:
        return 1
    else:
        return 0

"""only consider the suffix, fully solve with symbol like ". , ? / " now we can control the match accurcy above 70% 
(program can know says and say is same meaning, the longer the words is, the higher understanding the program can perfrom)"""
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
    print(score_1,score_2)   
    if score_1>score_2:
        print("No worries! there are lots of ways can help you, would you mind work on it with fellow students or not?")
        sub_2_categorized_study(text_dealing())
    else:
        print("Very interesting topic, maybe you can contact form of the Student Desk!")

def sub_2_categorized_study(tokens):
    Library_ax1=['do not',"dont",'not','hate','shy','no']
    score_1=0
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_ax1:
            if fire(token,words)==1:
                score_1=score_1+1  
    if score_1>0:
 
            print("I suggest you can seeking out a study group for what you are struggling now.")
    else:
            print("I suggest you can seeking out a student advisor for what you are struggling now.")


def sub_categorized_sports(tokens):
    score_1=0
    score_2=0
    Library_a_s=['aikido','basketball','tennis','swimming','football','zumba','karate','yoga','waterpolo','specific','play']
    Library_b=['try','new','explore','find','taste',"don't",'do not','no'] 
    for token in tokens:
        for words in Library_a_s:
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
        print("seems you want try new sport! our university offer ballgames, cardio and strengh training, which type you would want to try?") 
        sub_2_categorized_sports(text_dealing())
    else:
        print("seems our university don't offer this sport, do you want try a new one or have other things want tell me?" )
        sub_categorized_sports(text_dealing())

def sub_2_categorized_sports(tokens):
    Library_ballgame=['basketball','tennis','football','waterpolo']
    Library_cardio=['zumba','yoga']
    Library_strgenth=['aikido','karate','swimming']
    score_1=0
    score_2=0
    score_3=0
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_1:
            if fire(token,'strgenth'):
                print(token,words)
                score_1+=1
            if fire(token,'cardio')==1:
                print(token,words)
                score_2+=1
            if fire(token,'ballgames')==1:
                score_3+=1
    print(score_1,score_2,score_3)   
    if score_1>max(score_2,score_3):
        print('nice choice, I would like to recommend',random.choice(Library_strgenth))
    elif score_2>max(score_3,score_1):
        print('nice choice, I would like to recommend',random.choice(Library_cardio))
    elif score_3>max(score_1,score_2):
        print('nice choice, I would like to recommend',random.choice(Library_ballgame))
    else:
        print("seems I did'n understand your request, could you tell me agian?")
        sub_2_categorized_sports(text_dealing())

def sub_categorized_social(tokens):
    score_1=0
    score_2=0
    Library_a=['event','upcoming']
    Library_e=['association']
    Library_ex=["New Year's Party (13 Jan)","Valentine's Dinner (14 Feb)","Carnival Night (1 March)","Karaoke Night (18 April)","Kayaking Trip (5 May)","Seaside Picnic (15 Sep)","Halloween Party (31 Oct)","Thanksgiving Jamboree (26 Nov)","Christmas Dinner (18 Dec)"]
    for token in tokens:
        for words in Library_a:
            if fire(token,words)==1:
                print(token,words)
                score_1+=1
        for words in Library_e:
            if fire(token,words)==1:
                print(token,words)
                score_2+=1
    print(score_1,score_2)   
    if score_1>score_2:
        random.shuffle(Library_ex)
        print("I would like to recommand three up coming events:", Library_ex[0],Library_ex[1],Library_ex[2])
    elif score_2>score_1:
        print("seems you wish join an association! our university offer five types of association:artist, international, debate, Science&Society and Environment, which type you would want to try?") 
        sub_2_categorized_social(text_dealing())
    elif score_2==score_1:
        print("seems you answer is not clear, could you tell me more about the details you want?")
        sub_categorized_social(text_dealing())
    
def sub_2_categorized_social(tokens):
    score_1=0
    score_2=0
    Library_type1=['artist',['poetry pals','painting and pottery']]
    Library_type2=['international',['international students society','bunch of backpackers']]
    Library_type3=['debate',['debate club']]
    Library_type4=['science','society',['Science Society',' Language Club']]
    Library_type5=['environment',['Students for Sustainability','Animal Shelter Volunteers']]
    for token in tokens:
        if fire(token,Library_type1[0])==1:
            print(token,Library_type1[0])
            print("I would like to recommend",random.choice(Library_1[1]),'association.')
        if fire(token,Library_type2[0])==1:
            print(token)
            print("I would like to recommend",random.choice(Library_2[1]),'association.') 
        if fire(token,Library_type3[0])==1:
            print(token)
            print("I would like to recommend",Library_type3[1][0],'association.') 
        if fire(token,Library_type4[0])==1 or fire(token,Library_type4[1])==1 :
            print(token)
            print("I would like to recommend",random.choice(Library_type4[2]),'association.') 
        if fire(token,Library_type5[0])==1:
            print(token)
            print("I would like to recommend",random.choice(Library_type5[1]),'association.') 
        else:
            print("seems we don't have this type of association, please try to tell me another type which our university has ")
            sub_2_categorized_social(text_dealing())

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
    sub_categorized_study(text_dealing())
if category=='sports':
    print("Oh, I think it's about sports, do you have a specific sport in mind? Would you tell me its name?")
    sub_categorized_sports(text_dealing())
if category=='social':
    print("Oh, I think it's about Social activities, Our university have many interesting events and student association, which type you are interesting?")
    sub_categorized_social(text_dealing())
if category=='uncertain':
    print("Sorry, it seems I can't understand your problem or this problem of its field I can't help, try to ask me again, thank you")

    
    

