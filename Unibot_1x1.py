import random
from datetime import date


def fire(token, match):                 
    letters=list(token)
    letters_m=list(match)
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
    score_study=0
    score_sports=0
    score_social=0
    for token in tokens:                    
        for words in Library_1:
            if fire(token,words)==1:
                score_study+=1
        for words in Library_2:
            if fire(token,words)==1:
                score_sports+=1
        for words in Library_3:
            if fire(token,words)==1:
                score_social+=1
    if score_study>max(score_sports,score_social):
        return 'study'
    elif score_sports>max(score_social,score_study):
        return 'sports'
    elif score_social>max(score_study,score_sports):
        return 'social'
    else:
        return 'uncertain'


def sub_categorized_study(tokens):
    Library_a=['struggle','difficult','difficulty','bad','help','anxiety','nervous']
    Library_b=['interesting','information','interest','practical']
    score_study=0
    score_sports=0
    for token in tokens:                    
        for words in Library_a:
            if fire(token,words)==1:
                score_study+=1
        for words in Library_b:
            if fire(token,words)==1:
                score_sports+=1
    if score_study>score_sports:
        print("No worries! There are lots of ways we can help you, would you mind working on it with fellow students or not?")
        sub_2_categorized_study(text_dealing())
    else:
        print("Very interesting topic, maybe you can see the contact form of the Student Desk!")

def sub_2_categorized_study(tokens):
    Library_ax1=['do not',"dont",'not','hate','shy','no']
    score_study=0
    for token in tokens:                    
        for words in Library_ax1:
            if fire(token,words)==1:
                score_study=score_study+1  
    if score_study>0:
            print("I suggest you can seek out a student advisor for what you are struggling with now.")
    else:
            print("I suggest you can seek out a study group for what you are struggling with now.")


def sub_categorized_sports(tokens):
    score_study=0
    score_sports=0
    Library_a_s=['aikido','basketball','tennis','swimming','football','zumba','karate','yoga','waterpolo','specific','play']
    Library_b=['try','new','explore','find','taste',"don't",'do not','no'] 
    for token in tokens:
        for words in Library_a_s:
            if fire(token,words)==1:
                score_study+=1
        for words in Library_b:
            if fire(token,words)==1:
                score_sports+=1
    print(score_study,score_sports)   
    if score_study>score_sports:
        print("You are lucky, this is sport is available at our university, you can find more information on University Sports Centre website!")
    elif score_study<score_sports: 
        print("Seems you want try out a new sport! Our university offers ballgames, cardio and strength training, which type you would want to try?") 
        sub_2_categorized_sports(text_dealing())
    else:
        print("It seems that our university doesn't offer this sport. Do you want to try asking me if another sports exists at our university? Or would you like to try a new sport?")
        sub_categorized_sports(text_dealing())

def sub_2_categorized_sports(tokens):
    Library_ballgame=['basketball','tennis','football','waterpolo']
    Library_cardio=['zumba','swimming']
    Library_strength=['aikido','karate','yoga']
    score_study=0
    score_sports=0
    score_social=0
    for token in tokens:                    
        for words in Library_1:
            if fire(token,'strength'):
                score_study+=1
            if fire(token,'cardio')==1:
                score_sports+=1
            if fire(token,'ballgames')==1:
                score_social+=1
    print(score_study,score_sports,score_social)   
    if score_study>max(score_sports,score_social):
        print('nice choice, I would like to recommend',random.choice(Library_strength))
    elif score_sports>max(score_social,score_study):
        print('nice choice, I would like to recommend',random.choice(Library_cardio))
    elif score_social>max(score_study,score_sports):
        print('nice choice, I would like to recommend',random.choice(Library_ballgame))
    else:
        print("seems I did'n understand your request, could you tell me agian?")
        sub_2_categorized_sports(text_dealing())


def sub_categorized_social(tokens):
    Library_a=['event','upcoming']
    Library_e=['association']
    score_event = 0
    for t in tokens:
        for w in Library_a:
            if fire(t, w) == 1:
                score_event += 1
    score_assoc = 0
    for t in tokens:
        for w in Library_e:
            if fire(t, w) == 1:
                score_assoc += 1
    if score_event >= score_assoc:
        t = date.today()
        day=t.day
        Library_ex=["New Year's Party ","Valentine's Dinner","Carnival Night","Karaoke Night ","Kayaking Trip ","Seaside Picnic","Halloween Party","Thanksgiving Jamboree ","Christmas Dinner","New Year's Party ","Valentine's Dinner","Carnival Night"]
        List_m=[1,2,3,4,5,9,10,11,12,1,2,3]
        List_d=[13,14,1,18,5,15,31,26,18]
        month=t.month
        day=t.day
        i=0
        while i>=0:
            if month>List_m[i]:
                i=i+1
            else:
                break
        if month > List_m[i]:
            print("I would recommend", Library_ex[i],Library_ex[i+1],Library_ex[i+2])
        else:
            if day>=List_d[i]:
                print("I would recommend", Library_ex[i+1],Library_ex[i+2],Library_ex[i+3])
            else:
                print("I would recommend", Library_ex[i], Library_ex[i+1], Library_ex[i+2])    
    else:
        print("Seems an association is of interest! Our university offers interesting areas of associations - artists, international, debate, Science&Society, and environment. Which of these areas would you be interested in?")
        sub_2_categorized_social(text_dealing())
    
def sub_2_categorized_social(tokens):
    Library_type1=['artist',['poetry pals','painting and pottery']]
    Library_type2=['international',['international students society','bunch of backpackers']]
    Library_type3=['debate',['debate club']]
    Library_type4=['science','society',['Science Society',' Language Club']]
    Library_type5=['environment',['Students for Sustainability','Animal Shelter Volunteers']]
    for token in tokens:
        if fire(token,Library_type1[0])==1:
            print(token,Library_type1[0])
            print("I would like to recommend",random.choice(Library_1[1]),'association.')
        elif fire(token,Library_type2[0])==1:
            print(token)
            print("I would like to recommend",random.choice(Library_2[1]),'association.') 
        elif fire(token,Library_type3[0])==1:
            print(token)
            print("I would like to recommend",Library_type3[1][0],'association.') 
        elif fire(token,Library_type4[0])==1 or fire(token,Library_type4[1])==1 :
            print(token)
            print("I would like to recommend",random.choice(Library_type4[2]),'association.') 
        elif fire(token,Library_type5[0])==1:
            print(token)
            print("I would like to recommend",random.choice(Library_type5[1]),'association.') 
        else:
            print("Seems we don't have this type of association, please try to tell me another type which our university has ")
            sub_2_categorized_social(text_dealing())


def text_dealing(): 
    Original_text=input()
    original_text=Original_text.lower()
    text_token=original_text.split()
    return text_token    

Library_1=['math','study','academic','book','scholarship','research','exam','learn','test','physics','studies']
Library_2=['sports','run','aikido','health','strong','play','basketball','tennis','swimming','football','zumba','karate','yoga','waterpolo']
Library_3=['social','party','event','activity','association','club','friends','trip','night','picnic','festival','celebration']

def main():

    print("Hi, I'm Unibot. What can I help you with?")

    category=categorized(text_dealing())

    if category=='study':
        print("Oh, I think it's about studying, are you struggling with something or only interested in practical information?")
        sub_categorized_study(text_dealing())
    elif category=='sports':
        print("Oh, I think it's about sports, do you have a specific sport in mind? Would you tell me its name?")
        sub_categorized_sports(text_dealing())
    elif category=='social':
        print("Oh, I think it's about Social activities, Our university has many interesting events and student association. Are you interested in upcoming events or in some interesting associations?")
        sub_categorized_social(text_dealing())
    elif category=='uncertain':
        print("Sorry, it seems I can't understand your problem or this problem is in a field I can't help with. Try asking me again.")
        category=categorized(text_dealing())

main()
