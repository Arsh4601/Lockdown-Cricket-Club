import random as rd
def get_teams(choice1):#Assigning teams to both players

    team_choice=choice1
    team=["India","Pakistan","Bangladesh","Australia","Sri Lanka","England","West Indies","New Zealand"]
    team_assign=[ind,pak,ban,aus,sri,eng,wi,nz]

    if(team_choice==1):#default team names displayed

        print("We have 8 teams for you namely:-")
        for i in range(0,8):

            print(i+1," ",team[i])

        print("\n")
        print("To choose your team")

        while True:#team1 assigning

            try:
                t1=input("Enter nummber according to the team like 1 for India and so on: ")
                t1=int(t1)
                if(t1>=1 and t1<=8):

                    break
                else:
                    print("Sorry wrong choice,please renter")

            except:

                print("Sorry wrong choice,please renter")

        team1=team_assign[t1-1] #team 1 assigned
        name1=team[t1-1]
        print("Player 1 has choosen",name1)


        while True:#team 2 assigning

            try:
                t2=input("Player 2 please make your choice: ")
                t2=int(t2)
                if(t2==t1):

                    print("Sorry this team is already choosen,please change your choice")

                elif (t1>=1 and t1<=8):

                    break

                else:
                    print("Sorry wrong choice,please renter")

            except:

                print("Sorry wrong choice,please renter")

        team2=team_assign[t2-1] #team 2 assigned
        name2=team[t2-1]
        print("Player 2 has choosen",name2)

        if(t1==1):

            wiki1=ind[2]

        if(t1==2):

            wiki1=pak[2]

        if(t1==3):

            wiki1=ban[2]

        if(t1==4):

            wiki1=aus[2]

        if(t1==5):

            wiki1=sri[2]

        if(t1==6):

            wiki1=eng[2]

        if(t1==7):

            wiki1=wi[2]

        elif(t1==8):
            wiki1=nz[2]

        if(t2==1):

            wiki2=ind[2]

        if(t2==2):

            wiki2=pak[2]

        if(t2==3):

            wiki2=ban[2]

        if(t2==4):

            wiki2=aus[2]

        if(t2==5):

            wiki2=sri[2]

        if(t2==6):

            wiki2=eng[2]

        if(t2==7):

            wiki2=wi[2]

        elif(t2==8):
            wiki2=nz[2]


    else:
        t1=[]

        t2=[]

        print("\n")

        while True:#team1 name assigning
            try:
                name1=input("Player 1 enter name of your team: ") #team 1 assigned
                name1=int(name1)
                print("The name of the team can't be numbers: ")
            except:

                break

        print("Please add players to ",name1)
        print("Remember the team should have only 5 players")
        print("Enter the players in batting order i.e the first batsman will be named first")
        for i in range(1,6):#team 1 players assigning

            while True:#team 1 players assigned
                n1=0
                try:
                    n1=input("Enter name of player: ")
                    n1=int(n1)
                    print("The name of the team player cant be numbers")

                except:
                    t1.append(n1)
                    break

        while True:
            try:
                wiki1=input("Who will be your Wicket-Keeper: ")
                wiki1=int(wiki1)
                print("The name of wicket-Keeper cant be a number")
            except:
                try:
                    wiki1=float(wiki1)
                    print("The name of the team player cant be numbers")

                except:
                    for item in t1:
                        if(item==wiki1):
                            c=1
                            break

                        else:
                            c=2

                    if(c==1):
                        break

                    else:
                        print("The Wicket-Keeper must be the part of the team")



        print("\n")

        while True:#team 2 name assigning
            try:
                name2=input("Player 2 enter name of your team: ")#team 2 name assigned
                name2=int(name2)
                print("The name of the team can't be numbers: ")
            except:

                break

        print("Please add players to ",name2)
        print("Remember the team should have only 5 players")
        print("Enter the players in batting order i.e the first batsman will be named first")
        for i in range(1,6):#team 2  players assigning

            while True:#team 2 players assigned
                n2=" "
                try:
                    n2=input("Enter name of player: ")
                    n2=int(n2)
                    print("The name of the team player cant be numbers")

                except:

                    try:
                        n2=float(n2)
                        print("The name of the team player cant be numbers")

                    except:
                        t2.append(n2)
                        break

        while True:#team 2 wicki assigned

            try:
                wiki2=input("Who will be your Wicket-Keeper: ")
                wiki2=int(wiki2)
                print("The name of wicket-Keeper cant be a number")

            except:
                try:

                    wiki2=float(wiki2)
                    print("The name of the team player cant be numbers")
                except:

                    for item in t2:

                        if(item==wiki2):

                            c=1

                            break

                        else:
                            c=2

                    if(c==1):

                        break

                    else:

                        print("The Wicket-Keeper must be the part of the team")

        team1=t1
        team2=t2
        c=0
        print("\n")

    reference=list(toss(name1,name2))
    in_game(name1,name2,team1,team2,reference,wiki1,wiki2)

def toss(nameA,nameB):#Toss time

    coin=["heads","tails","tails","heads","heads","heads","tails","tails","tails","heads"]
    team_call=[nameA,nameB,nameA,nameB,nameA,nameA,nameB,nameB,nameB,nameA]
    x=rd.randint(1,10)

    print("\n")

    print("Its time for the toss,and now we have both the captains in the centre")

    print("The coin is tossed and its",team_call[x-1],"'s call")

    coin_status = coin[x-1]



    while True:#check for toss call(heads/tails)

        choice_call=input("Enter your call(heads/tails): ")

        try:
            choice_call=int(choice_call)

            print("Please enter either heads or tails only")

        except:

            try:

                choice_call=float(choice_call)
                print("Please enter either heads or tails only")

            except:

                if(choice_call=="heads" or choice_call=="tails"):

                    break

                else:
                    print("Please enter either heads or tails only")


    if(choice_call==coin_status):

        print(team_call[x-1],"has won the toss")
        team_won=team_call[x-1]

    else:

        if(team_call[x-1]==nameA):

            print(nameB,"has won the toss")
            team_won=nameB

        else:

            print(nameA,"has won the toss")
            team_won=nameA

    while True:#check for choice of toss winning team(bat/bowl)

        elect=input("What you like to choose(bat/bowl): ")

        try:
            elect=int(elect)

            print("Please enter either bat or bowl only")

        except:

            try:

                elect=float(elect)
                print("Please enter either bat or bowl only")

            except:

                if(elect=="bat" or elect=="bowl"):

                    break

                else:
                    print("Please enter either bat or bowl only")


    print("and elects to ",elect,"first")
    print("\n")
    return team_won,elect


def in_game(nameA,nameB,teamA,teamB,reference1,wikiA,wikiB):

    ref=reference1
    team_won=ref[0]
    elect=ref[1]

    print("This will be a 5 over match")
    print("Every bowler has a limit of 3 overs")
    print("\n")

    if(team_won==nameA and elect=="bat"):

        bat_first=teamA
        bowl_first=teamB
        bat_first_name=nameA
        bowl_first_name=nameB
        wiki_index=bowl_first.index(wikiB)
        wiki_next_index=wiki_index+1
        bowl_first.remove(wikiB)



    elif(team_won==nameA and elect=="bowl"):

        bat_first=teamB
        bowl_first=teamA
        bat_first_name=nameB
        bowl_first_name=nameA
        wiki_index=bowl_first.index(wikiA)
        wiki_next_index=wiki_index+1
        bowl_first.remove(wikiA)



    elif(team_won==nameB and elect=="bat"):

        bat_first=teamB
        bowl_first=teamA
        bat_first_name=nameB
        bowl_first_name=nameA
        wiki_index=bowl_first.index(wikiA)
        wiki_next_index=wiki_index+1
        bowl_first.remove(wikiA)


    elif(team_won==nameB and elect=="bowl"):

        bat_first=teamA
        bowl_first=teamB
        bat_first_name=nameA
        bowl_first_name=nameB
        wiki_index=bowl_first.index(wikiB)
        wiki_next_index=wiki_index+1
        bowl_first.remove(wikiB)


    print("\n")


    for m in range(1,3):

        score=0
        a=0
        wicket=0
        over_bowled=[0,0,0,0]
        bowler_status=["Available","Available","Available","Available"]
        bowler_select=[]
        wick_bowler=[0,0,0,0]
        run_bowler=[0,0,0,0]
        run_bat=[0,0,0,0,0]
        n=2
        striker=0
        non_striker=0
        b1=bat_first[0]
        b2=bat_first[1]
        bat_status=["Not Out","Not Out","Not Out","Not Out","Not Out"]
        print("\nBatting line up of ",bat_first_name,"is:-")
        print("\n")

        print("Batsman             ",end='')
        print("runs      ",end='')
        print("Status      ")

        for l in range(0,5):
            print(l+1,bat_first[l],"         " ,end='')
            print(run_bat[l],"      " ,end='')
            print(bat_status[l],"      " )

        print("\n")

        while True:

            ans=input("Do you want to continue if yes press y: ")

            if(ans=="yes" or ans=="y" or ans=="Y"):

                break

            else:

                print("ok,well wait for you")

        for i in range(1,6):

            c=0


            c=a
            if(c==1):
                break

            over_ball=0
            print("\n",bowl_first_name)

            print("\n")
            print("Bowler             ",end='')
            print("Over        ",end='')
            print("Status          ",end='')
            print("Runs          ",end='')
            print("Wickets          ")

            for j in range(0,4):
                print(j+1,bowl_first[j],"     " ,end='')
                print(over_bowled[j],"         " ,end='')
                print(bowler_status[j],"             ",end='' )
                print(run_bowler[j],"             ",end='' )
                print(wick_bowler[j],"             " )

            print("\n")

            while True:
                print("Choose your bowler according to the numbers given in the Line-Up i.e 1 to 4")
                bname=input("Enter: ")

                bname=int(bname)

                b=0

                if(bname>=1 and bname<=4 ):

                    chk=over_bowled[bname-1]+1
                    bowler_select.append(bowl_first[bname-1])
                    if(chk>=3):

                        bowler_status[bname-1]="Unavailable"

                    if(i>1):

                        if(bowler_select[i-1]==bowler_select[i-2]):

                            print("Bowlers cant bowl consecutive overs")
                            bowler_select.remove(bowler_select[i-1])


                        else:

                            b=1
                            over_bowled[bname-1]= over_bowled[bname-1]+1


                    else:

                            b=1
                            over_bowled[bname-1]= over_bowled[bname-1]+1



                else:

                    print("Number entered must be between 1 and 4")

                if(b==1):

                    c=1
                    break

                else:

                    c=2

                if(c==1):

                    break

                else:

                    print("Sorry bowler is not in your team")




            for K in range(1,7):
               r1=rd.randint(0,6)
               r=runs[r1]
               bname_index=bname-1


               if(r==1):

                   score=score+1
                   print("\nBall",K)
                   print("\nIts an easy single")
                   print(score,"-",wicket)
                   striker=striker+1
                   temp=striker
                   striker=non_striker
                   non_striker=temp
                   temp=b1
                   b1=b2
                   b2=temp
                   run_bowler[bname_index]=run_bowler[bname_index]+1
                   over_ball=over_ball+1

                   while True:

                       ans=input("Do you want to continue if yes press y: ")

                       if(ans=="yes" or ans=="y" or ans=="Y"):

                           break

                       else:

                           print("Okay we'll wait for you")

                   if(m==2):

                       if(score>=target):

                           a=1
                           w=1
                           break

                       else:

                           w=0
                           a=0

                   if(m==2 and w==1):

                       break

               if(r==2):

                   score=score+2
                   print("\nBall",K)
                   print("\nThey'll run for the second...and its easily taken")
                   print(score,"-",wicket)
                   striker=striker+2
                   run_bowler[bname_index]=run_bowler[bname_index]+2
                   over_ball=over_ball+1

                   while True:

                       ans=input("Do you want to continue if yes press y: ")

                       if(ans=="yes" or ans=="y" or ans=="Y"):

                           break

                       else:

                           print("Okay we'll wait for you")

                   if(m==2):

                       if(score>=target):

                           a=1
                           w=1
                           break

                       else:

                           w=0
                           a=0

                   if(m==2 and w==1):

                       break


               if(r==3):

                   score=score+3
                   print("\nBall",K)
                   print("\nBrilliant work by the fielder to stop the boundary,but batsmen ran 3 runs")
                   print(score,"-",wicket)
                   striker=striker+3
                   temp=striker
                   striker=non_striker
                   non_striker=temp
                   temp=b1
                   b1=b2
                   b2=temp
                   run_bowler[bname_index]=run_bowler[bname_index]+3
                   over_ball=over_ball+1

                   while True:

                       ans=input("Do you want to continue if yes press y: ")

                       if(ans=="yes" or ans=="y" or ans=="Y"):

                           break

                       else:

                           print("Okay we'll wait for you")

                   if(m==2):

                       if(score>=target):

                           a=1
                           w=1
                           break

                       else:

                          a=0
                          w=0

                   if(m==2 and w==1):

                       break



               if(r==4):

                   score=score+4
                   print("\nBall",K)
                   print("\nThe ball races away to the boundary for four!!!")
                   print(score,"-",wicket)
                   striker=striker+4
                   run_bowler[bname_index]=run_bowler[bname_index]+4
                   over_ball=over_ball+1

                   while True:

                       ans=input("Do you want to continue if yes press y: ")

                       if(ans=="yes" or ans=="y" or ans=="Y"):

                           break

                       else:

                           print("Okay we'll wait for you")

                   if(m==2):

                       if(score>=target):

                           a=1
                           w=1
                           break

                       else:

                           w=0
                           a=0

                   if(m==2 and w==1):

                       break


               if(r==6):

                   score=score+6
                   print("\nBall",K)
                   print("The ball flies up in the air... and in the crowd for six!!!")
                   print(score,"-",wicket)
                   striker=striker+6
                   run_bowler[bname_index]=run_bowler[bname_index]+6
                   over_ball=over_ball+1

                   while True:

                       ans=input("Do you want to continue if yes press y: ")

                       if(ans=="yes" or ans=="y" or ans=="Y"):

                           break

                       else:

                           print("Okay we'll wait for you")

                   if(m==2):

                       if(score>=target):

                           w=1
                           a=1
                           break

                       else:

                           w=0
                           a=0

                   if(m==2 and w==1):

                       break


               if(r=="out"):

                   wicket=wicket+1
                   print("\nBall",K)
                   print("\n",score,"-",wicket)
                   w=rd.randint(0,4)
                   over_ball=over_ball+1
                   if(w==2 or w==4):

                       print("\n Alas! ",b1,"is out by",out_types[w])
                       run_bat[bat_first.index(b1)]=striker
                       bat_status[bat_first.index(b1)]="Out"

                   else:

                       print("\n Alas! ",b1,"is",out_types[w])
                       print(score,"-",wicket)
                       run_bat[bat_first.index(b1)]=striker
                       bat_status[bat_first.index(b1)]="Out"


                   if(out_types[w]!="Run out"):

                       wick_bowler[bname_index]=wick_bowler[bname_index]+1

                   while True:

                       ans=input("Do you want to continue if yes press y: ")

                       if(ans=="yes" or ans=="y" or ans=="Y"):

                           break

                       else:

                           print("Okay we'll wait for you")



                   if (wicket==4):

                       print("\n",bat_first_name,"is  All-Out")

                       a=1

                       if(m==2):

                           w=0

                       break

                   else:

                       b1=bat_first[n]
                       striker=0
                       n=n+1
                       a=0

                   if(m==2):

                       if(score>=target):

                           w=1
                           a=1
                           break

                       elif(wicket==4):

                           a=1
                           w=0
                           break

                       else:

                           a=0
                           w=0


               if(r=="Dot Ball"):

                   print("\nBall",K)
                   print("\nIts a Brilliant ball bowled by ",bowl_first[bname-1],"its a dot ball")
                   print(score,"-",wicket)
                   over_ball=over_ball+1

                   while True:

                       ans=input("Do you want to continue if yes press y: ")

                       if(ans=="yes" or ans=="y" or ans=="Y"):

                           break

                       else:

                           print("Okay we'll wait for you")

                   if(m==2):

                       if(score>=target):

                           w=1
                           a=1
                           break


                       else:

                           w=0
                           a=0

                   if(m==2 and w==1):

                       break
            temp=striker
            striker=non_striker
            non_striker=temp
            temp=b1
            b1=b2
            b2=temp
            b1_index=bat_first.index(b1)
            b2_index=bat_first.index(b2)
            run_bat[b1_index]=striker
            run_bat[b2_index]=non_striker

            print("\n",bat_first_name)
            print("\n")

            print("Batsman             ",end='')
            print("runs      ",end='')
            print("Status      ")

            for l in range(0,5):

                print(l+1,bat_first[l],"         " ,end='')
                print(run_bat[l],"      " ,end='')
                print(bat_status[l],"      " )



            print("\nAfter over ",i,"score is: ",score,"-",wicket)

            if(wicket<4):

                print("Current run rate is: ",round((score/i),2))

            if(m==2):

                if(wicket<4 and score<target):

                    x=30-(i*6)
                    if(x>0):

                        print(bat_first_name,"need",target-score,"runs in",x,"balls")

            while True:

                ans=input("Do you want to continue if yes press y: ")
                if(ans=="yes" or ans=="y" or ans=="Y"):

                    break

                else:

                    print("Okay we'll wait for you")
     
                    
        if(m==1):

            print("\n",bat_first_name,"'s final score is ",score,"-",wicket,end='')
            print(", Run Rate : ",score/5)
            print(bowl_first_name," needs ",score+1,"runs to win from 30 balls",end='')
            print(", Required Run Rate : ",round(((score+1)/5),2))

            while True:

                ans=input("Do you want to continue if yes press y: ")
                if(ans=="yes" or ans=="y" or ans=="Y"):

                    break

                else:

                    print("Okay we'll wait for you")



            
        print("\n",bat_first_name)
        print("\n")

        print("Batsman             ",end='')
        print("runs      ",end='')
        print("Status      ")

        for l in range(0,5):

            print(l+1,bat_first[l],"         " ,end='')
            print(run_bat[l],"      " ,end='')
            print(bat_status[l],"      " )


        print("\n",bowl_first_name)
        print("\n")
        print("Bowler             ",end='')
        print("Over        ",end='')
        print("Status          ",end='')
        print("Runs          ",end='')
        print("Wickets          ")

        for j in range(0,4):

            print(j+1,bowl_first[j],"     " ,end='')
            print(over_bowled[j],"         " ,end='')
            print(bowler_status[j],"             ",end='' )
            print(run_bowler[j],"             ",end='' )
            print(wick_bowler[j],"             " )


        if(m==1):

           target=score+1
           temp=bat_first_name
           bat_first_name= bowl_first_name
           bowl_first_name=temp
           temp=bat_first
           bat_first=bowl_first
           
           try:

               temp.remove(wikiA)
           
           except:

               temp.remove(wikiB)

           bowl_first=temp

           if(bat_first_name==nameA):

               bat_first.append(wikiA)

           elif(bat_first_name==nameB):

               bat_first.append(wikiB)

           temp=bat_first[4]
           bat_first[4]=bat_first[wiki_index]
           bat_first[wiki_index]=temp
           temp=bat_first[4]
           bat_first[4]=bat_first[wiki_next_index]
           bat_first[wiki_next_index]=temp
         
            



    if(w==1):

        x1=30-over_ball

        if(x1==0):

            print("\n",bat_first_name,"wins by ",5-wicket," wickets")
        elif(x1>0):

            print("\n",bat_first_name,"wins by ",5-wicket," wickets with",x1,"balls to spare")

    elif(w==0):

        print("\n",bowl_first_name,"wins by ",target - score," runs")

    print("\n GAME OVER")



print("Welcome to lockdown Cricket Club")
print("\n")
print("You can choose amoungst the teams we have for you ")
print("or you can make your own team")

ind=["Shekhar Dhawan","Virat Kohli(c)","M Singh Dhoni","Jasprit Bumrah","Ravindra Jadeja"]
pak=["Babar Azam","Mohd Hafeez","S. Ahmed(c)","Mohd Amir","Wahab Riaz"]
ban=["Tamim Iqbal","Mossadak Hossain","Liton Das","S Al Hasan(c)","Abu Jayed"]
aus=["David Warner","Steve Smith(c)","Peter Handscamp","Mitchell Stark","N Coulter-Nile"]
sri=["Dimuth Karunaratne","Angelo Mathews(c)","Kausal Mendis","L Malinga","S Lakmal"]
eng=["Joe Root","Eoin Morgan","Jos Butler","Ben Strokes(c)","Jofra Archer"]
wi=["Chris Gayle","C Brathwaite(c)","Nicolas Pooran","Sheldon Cortlell","Shanon Gabriel"]
nz=["K Williamson(c)","Martin Guptill","Tom Latham","Tim Southee","Matt Henry"]
runs=[1,2,3,4,6,"out","Dot Ball"]
out_types=["Caught","Bowled","Lbw","Run out","Stumping"]


print("\n")
print("Press 1 for choose teams and")
print("Press 2 to to make your own team")
while True:

    try:
        choice=input("Enter your choice:")
        choice=int(choice)
        if(choice==1 or choice==2):
            break

        else:
            print("Sorry wrong choice,please renter")
    except:

        print("Sorry wrong choice,please renter")

get_teams(choice)
