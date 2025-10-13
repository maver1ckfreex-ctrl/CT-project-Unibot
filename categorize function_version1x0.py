import random
import datetime

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
    score_study=0
    score_sports=0
    score_social=0
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_1:
            if fire(token,words)==1:
                print(token,words)
                score_study+=1
        for words in Library_2:
            if fire(token,words)==1:
                print(token,words)
                score_sports+=1
        for words in Library_3:
            if fire(token,words)==1:
                score_social+=1
    print(score_study,score_sports,score_social)   
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
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_a:
            if fire(token,words)==1:
                print(token,words)
                score_study+=1
        for words in Library_b:
            if fire(token,words)==1:
                print(token,words)
                score_sports+=1
    print(score_study,score_sports)   
    if score_study>score_sports:
        print("No worries! There are lots of ways we can help you, would you mind working on it with fellow students or not?")
        sub_2_categorized_study(text_dealing())
    else:
        print("Very interesting topic, maybe you can see the contact form of the Student Desk!")

def sub_2_categorized_study(tokens):
    Library_ax1=['do not',"dont",'not','hate','shy','no']
    score_study=0
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_ax1:
            if fire(token,words)==1:
                score_study=score_study+1  
    if score_study>0:
            print("I suggest you can seek out a study group for what you are struggling with now.")
    else:
            print("I suggest you can seek out a student advisor for what you are struggling with now.")


def sub_categorized_sports(tokens):
    score_study=0
    score_sports=0
    Library_a_s=['aikido','basketball','tennis','swimming','football','zumba','karate','yoga','waterpolo','specific','play']
    Library_b=['try','new','explore','find','taste',"don't",'do not','no'] 
    for token in tokens:
        for words in Library_a_s:
            if fire(token,words)==1:
                print(token,words)
                score_study+=1
        for words in Library_b:
            if fire(token,words)==1:
                print(token,words)
                score_sports+=1
    print(score_study,score_sports)   
    if score_study>score_sports:
        print('you are lucky, this is sport is available in our university, you can find more information on University Sports Centre website!')
    elif score_study<score_sports: 
        print("seems you want try new sport! our university offer ballgames, cardio and strengh training, which type you would want to try?") 
        sub_2_categorized_sports(text_dealing())
    else:
        print("seems our university don't offer this sport, do you want try a new one or have other things want tell me?" )
        sub_categorized_sports(text_dealing())

def sub_2_categorized_sports(tokens):
    Library_ballgame=['basketball','tennis','football','waterpolo']
    Library_cardio=['zumba','yoga']
    Library_strgenth=['aikido','karate','swimming']
    score_study=0
    score_sports=0
    score_social=0
    for token in tokens:                    #we need find a more effiency search/match algorithm that's the second problem we meet
        for words in Library_1:
            if fire(token,'strgenth'):
                print(token,words)
                score_study+=1
            if fire(token,'cardio')==1:
                print(token,words)
                score_sports+=1
            if fire(token,'ballgames')==1:
                score_social+=1
    print(score_study,score_sports,score_social)   
    if score_study>max(score_sports,score_social):
        print('nice choice, I would like to recommend',random.choice(Library_strgenth))
    elif score_sports>max(score_social,score_study):
        print('nice choice, I would like to recommend',random.choice(Library_cardio))
    elif score_social>max(score_study,score_sports):
        print('nice choice, I would like to recommend',random.choice(Library_ballgame))
    else:
        print("seems I did'n understand your request, could you tell me agian?")
        sub_2_categorized_sports(text_dealing())

def sub_categorized_social(tokens):
    score_study=0
    score_sports=0
    Library_a=['event','upcoming']
    Library_e=['association']
    Dictionary_months={"New Year's Party":1, "Valentine's Dinner":2, "Carnival Night":3, "Karaoke Night":4, "Kayaking Trip":5, "Seaside Picnic":9, "Halloween Party":10, "Thanksgiving Jamboree":11, "Christmas Dinner":12}
    Dictionary_days={"New Year's Party":1, "Valentine's Dinner":14, "Carnival Night":1, "Karaoke Night":18, "Kayaking Trip":5, "Seaside Picnic":15, "Halloween Party":31, "Thanksgiving Jamboree":26, "Christmas Dinner":18}

   score_event = 0
    score_assoc = 0
    for token in tokens:
        for w in Library_a:
            if fire(token, w) == 1:
                score_event += 1
        for w in Library_e:
            if fire(token, w) == 1:
                score_assoc += 1
    if score_event >= score_assoc:
        today = datetime.date.today()
        upcoming = []
        for name, month in Dictionary_months.items():
            if name not in Dictionary_days:
                continue
            day = Dictionary_days[name]
            candidate = datetime.date(today.year, month, day)
            if candidate < today:
                candidate = datetime.date(today.year + 1, month, day)
            upcoming.append((candidate, name))
        upcoming.sort(key=lambda x: x[0])
        top3 = [name for _, name in upcoming[:3]]
        if top3:
            print("I would like to recommend three upcoming events:", ", ".join(top3))
        else:
            print("No upcoming events found at the moment.")
    else:
        print("Seems an association is of interest! Our university offers artist, international, debate, Science&Society, and Environment—which type would be interesting?")
        sub_2_categorized_social(text_dealing())

    # DISREGARD FOR NOW
        # print("I would like to recommand three up coming events:", Library_ex[0],Library_ex[1],Library_ex[2])
    # elif score_sports>score_study:
        # print("seems you wish join an association! our university offer five types of association:artist, international, debate, Science&Society and Environment, which type you would want to try?") 
        # sub_2_categorized_social(text_dealing())
    # elif score_sports==score_study:
        # print("seems you answer is not clear, could you tell me more about the details you want?")
        # sub_categorized_social(text_dealing())
    
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


def main():
    Library_1=['math','study','academic','book','scholarship','research','exam','learn','test','physics'] # STUDYING KEYWORDS
    Library_2=['sports','run','aikido','health','strong','play','basketball','tennis','swimming','football','zumba','karate','yoga','waterpolo'] # SPORTS KEYWORDS
    Library_3=['social','party','event','activity','association','club','friends','trip','night','picnic','festival','celebration'] # STUDY LIFE KEYWORDS

    print("Hi, I'm Unibot. What can I help you with?")

    category=categorized(text_dealing())

    if category=='study':
        print("Oh, I think it's about study, are you struggling with something or only interested in practical information?")
        sub_categorized_study(text_dealing())
    elif category=='sports':
        print("Oh, I think it's about sports, do you have a specific sport in mind? Would you tell me its name?")
        sub_categorized_sports(text_dealing())
    elif category=='social':
        print("Oh, I think it's about Social activities, Our university have many interesting events and student association, which type you are interesting?")
        sub_categorized_social(text_dealing())
    elif category=='uncertain':
        print("Sorry, it seems I can't understand your problem or this problem of its field I can't help, try to ask me again, thank you")
        category=categorized(text_dealing())

main()
    

    
    

