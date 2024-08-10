import numpy as np
import pandas as pd
import random
class Match():
    def _init_(self,start):
        print("choose 1 for quickmatch")
        choose=int(input("Enter your number : "))
        if choose==1:
            start.main()
        else:
            print("Wrong input, try again : ")

class Start(Match):
    def _init_(self):
        self.team1_data={}
        self.team2_data={}
        self.Team_1="" 
        self.Team_2="" 
        self.inning=1
    def get_player_data(self,num_players):
     player_data = {"Name": [], "Category": [], "Runs": [], "Balls": [],"Status":[]}
     for i in range(num_players):
        name = input(f"Enter name of player {i+1}: ")
        category = input(f"Enter category of player {i+1}: ")
        # runs = int(input(f"Enter runs scored by player {i+1}: "))
        # balls = int(input(f"Enter balls faced by player {i+1}: "))
        runs=0
        balls=0
        status=""
        player_data["Name"].append(name)
        player_data["Category"].append(category)
        player_data["Runs"].append(runs)
        player_data["Balls"].append(balls)
        player_data["Status"].append(status)
     return player_data

    def main(self):
     num_players = int(input("Enter the number of players for match: "))
     num_overs=int(input("Enter the number of over for match: "))
   

     print("Enter player data for Team 1:")
     self.Team_1=input("enter name of Team 1: ")
     team1_data = self.get_player_data(num_players)
     print(team1_data)
    

     print("\nEnter player data for Team 2:")
     self.Team_2=input("enter name of Team 2: ")
     team2_data = self.get_player_data(num_players)
     print(team2_data)

     outcome = self.coin_toss()
     toss=input("enter your choice team 1 heads or tails : ")
     match=self.Team_1+"vs"+self.Team_2+".xlsx"
     c=True
     tosswin=""
     r=0
     for i in range(2):
       if outcome == toss.capitalize():
        while c:
         choices=input("enter your choice team1 bat or ball : ")
         if choices=='bat':
          c=False
          tosswin+="t1bat"
          a,run=self.play(num_players,num_overs,team1_data,team2_data,r,tosswin)
          b,run=self.play(num_players,num_overs,team2_data,team1_data,run,tosswin) 

         if choices=='ball':
          c=False
          tosswin+="t1ball"
          a,run=self.play(num_players,num_overs,team2_data,team1_data,r,tosswin) 
          b,run=self.play(num_players,num_overs,team1_data,team2_data,run,tosswin)

         else:
           print("enter valid choice ")  
       else:
         while c: 
          choices=input("enter your choice team2 bat or ball : ")
          if choices=='bat':
           c=False
           tosswin+="t2bat"
           a,run=self.play(num_players,num_overs,team2_data,team1_data,r,tosswin)
           b,run=self.play(num_players,num_overs,team1_data,team2_data,run,tosswin)  
          if choices=='ball':
           c=False
           tosswin+="t2ball"
           a,run=self.play(num_players,num_overs,team1_data,team2_data,r,tosswin)
           b,run=self.play(num_players,num_overs,team2_data,team1_data,run,tosswin)  
          else:
             print("enter valid choice")
    # Convert data to DataFrames
     team1_df = pd.DataFrame(team1_data)
     team2_df = pd.DataFrame(team2_data)
     if tosswin=="t2ball" or tosswin=="t1ball":
       temp=a
       a=b
       b=temp

    # Write data to Excel file
     with pd.ExcelWriter(match, engine='openpyxl') as writer:
        team1_df.to_excel(writer, sheet_name="Team1", index=False)
        team2_df.to_excel(writer, sheet_name="Team2", index=False)
        a.to_excel(writer, sheet_name="Team1", startcol=10, startrow=1, header=True, index=False)
        b.to_excel(writer, sheet_name="Team2", startcol=10, startrow=1, header=True, index=False) 
   
    
    def play(self,num_players,num_overs,team1_data,team2_data,target,tosswin):
       t1run=t2run=0
 
       if tosswin=="t1bat" or tosswin=="t2ball":
          team1=self.Team_1
          team2=self.Team_2
       else:
           team1=self.Team_2
           team2=self.Team_1
             
       run = wide = noball = wicket = 0
       aa=bb=True
       while aa:
        striker=input("enter striker player name: ")
        a=self.verify_player_name(striker,team1_data)
        if a==True:
           aa=False
        else:print("enter valid name of player: ")   
       while bb: 
        nonstriker=input("enter nonstriker player name: ")
        b= self.verify_player_name(nonstriker,team1_data)
        if b==True:
           bb=False
        else:print("enter valid name of player: ")   
       strikerrun=strikerball=nonstrikerrun=nonstrikerball=0
       baller={"Baller":[],"Balls":[]}
       baller_name=""
       j=1
       i=0
       l=0
       strikerrun=strikerball=0
       nonstrikerball=nonstrikerrun=0
       if a:
         if b:
            while i<=num_overs:
                ballers=[]
                cc=True
                while cc:
                          baller_name = input("Enter baller name: ")
                          c=self.verify_bowler_name(baller_name,team2_data)
                          if c:
                            cc=False
                            break
                          else:
                              print("enter valid name of baller ")     
                ballers.append(baller_name)
                balls = []
                # strikerrun=strikerball=0
                # nonstrikerball=nonstrikerrun=0
                j=1
# Input baller n
# ames and balls
                
                while j<=6:
                    ballrun = input("Enter balls for separated by space: ")
                    if ballrun=="noball":
                      r=input("enter run in noball : ")
                      strikerrun=int(r)+strikerrun
                      if int(r)%2==1:
                            striker, nonstriker = nonstriker, striker
                            tempball = strikerball
                            temprun = strikerrun
                            strikerball = nonstrikerball
                            strikerrun = nonstrikerrun
                            nonstrikerrun = temprun
                            nonstrikerball = tempball
                            run=int(r)+run+1
                            r=r+"nb"
                            balls.append(r)
                      else:
                            run=int(r)+run+1
                            r=r+"nb"
                            balls.append(r)       
                      print(f"{run}/{wicket}")


                    elif ballrun=="wide":
                       run=run+1
                       balls.append(ballrun+"1")

                    elif ballrun=="w":
                         type_out=input("enter type of out : ")
                         balls.append(ballrun)
                         j=j+1
                         wicket=wicket+1
                         strikerball=strikerball+1
                         if type_out=="runout":
                           who=input("enter which player out striker or nonstriker : ")
                           if who=="striker":
                             team1_data["Runs"][team1_data["Name"].index(striker)] =strikerrun
                             team1_data["Balls"][team1_data["Name"].index(striker)] =strikerball 
                             team1_data["Status"][team1_data["Name"].index(striker)] = "out"
                             npp=True
                             if wicket==(num_players-1):
                              print(" innings end")
                              baller["Baller"].append(ballers)
                              baller["Balls"].append(balls)
                              break    
                             while npp:
                              newplayer=input("enter new player name : ")
                              np=self.verify_player_name(newplayer,team1_data)
                              if np:
                                 npp=False
                             striker=newplayer
                             strikerrun=strikerball=0
                           elif who=="nonstriker":
                              team1_data["Balls"][team1_data["Name"].index(nonstriker)] =nonstrikerball
                              team1_data["Runs"][team1_data["Name"].index(nonstriker)] =nonstrikerrun
                              team1_data["Status"][team1_data["Name"].index(striker)] = "out"
                              npp=True
                              if wicket==(num_players-1):
                               print(" innings end")
                               baller["Baller"].append(ballers)
                               baller["Balls"].append(balls)
                               break
                              while npp:
                               newplayer=input("enter new player name ")
                               np=self.verify_player_name(newplayer,team1_data)
                               if np:
                                 npp=False
                              nonstriker=newplayer
                              nonstrikerrun=nonstrikerball=0

                         else:
                             team1_data["Runs"][team1_data["Name"].index(striker)] =strikerrun
                             team1_data["Balls"][team1_data["Name"].index(striker)] =strikerball 
                             team1_data["Status"][team1_data["Name"].index(striker)] = "out"
                             if wicket==(num_players-1):
                              print(" innings end")
                              baller["Baller"].append(ballers)
                              baller["Balls"].append(balls)
                              break
                             npp=True
                             while npp:
                               newplayer=input("enter new player name")
                               np=self.verify_player_name(newplayer,team1_data)
                               if np:
                                 npp=False
                               striker=newplayer                    
                               strikerrun=strikerball=0
                        #  if wicket==(num_players-1):
                        #       print(" innings end")
                        #       break
                        #  else:
                        #       npp=True
                        #       while npp:
                        #        newplayer=input("enter new player name")
                        #        np=self.verify_player_name(newplayer)
                        #        if np:
                        #          npp=False
                        #       striker=newplayer                    
                        #       strikerrun=strikerball=0
                    
                   
                    elif 0 <= int(ballrun) <=6:
                       run=int(ballrun)+run
                       balls.append(ballrun)
                       j=j+1
                       strikerrun=int(ballrun)+strikerrun
                       strikerball=strikerball+1
                       print(f"{run}/{wicket}")
                       if int(ballrun)%2==1:
                            striker,nonstriker=nonstriker,striker
                            tempball=strikerball
                            temprun=strikerrun
                            strikerball=nonstrikerball
                            strikerrun=nonstrikerrun
                            nonstrikerrun=temprun
                            nonstrikerball=tempball 
                    else:
                      print("enter valid choice") 

                    if j>6:
                     print("over compleated")
                     baller["Baller"].append(ballers)
                     baller["Balls"].append(balls)
                     i=i+1

                    if self.inning==2:
                        if run>target:
                          print(f"Team {team2} won the match ")
                          break

               #      if (i == num_overs and j == 7) or wicket == (num_players - 1) or self.inning==2:
               #         if run<target:
               #            print(f"Team {team1} won the match ")
               #            break
               #         if run==target:
               #            print(f"Match Tied") 
               #            break
                       
               #  if (i == num_overs and j == 7) or wicket == (num_players - 1):
               #     print(" innings end")
               #     st=1
               #     team1_data["Runs"][team1_data["Name"].index(striker)] =strikerrun
               #     team1_data["Balls"][team1_data["Name"].index(striker)] =strikerball    
               #     team1_data["Balls"][team1_data["Name"].index(nonstriker)]=nonstrikerball
               #     team1_data["Runs"][team1_data["Name"].index(nonstriker)] =nonstrikerrun
               #     l=l+1
               #     df2=pd.DataFrame(baller)
               #     self.inning=self.inning+1
               #     return df2,run

                if (i == num_overs and j == 7) or wicket == (num_players - 1) or self.inning==2:
                       if run<target:
                          print(f"Team {team1} won the match ")
                        
                       if run==target:
                          print(f"Match Tied")   
                        
                if (i == num_overs and j == 7) or wicket == (num_players - 1):
                   print(" innings end")
                   st=1
                   team1_data["Runs"][team1_data["Name"].index(striker)] =strikerrun
                   team1_data["Balls"][team1_data["Name"].index(striker)] =strikerball    
                   team1_data["Balls"][team1_data["Name"].index(nonstriker)]=nonstrikerball
                   team1_data["Runs"][team1_data["Name"].index(nonstriker)] =nonstrikerrun
                   l=l+1
                   df2=pd.DataFrame(baller)
                   self.inning=self.inning+1
                   return df2,run
         else:
            print("The player's name does not exist in the dictionary.")
       else:
            print("The player's name does not exist in the dictionary.")

    def verify_player_name(self,player_name,team_data):
      if player_name in team_data['Name']:
        if team_data["Status"][team_data["Name"].index(player_name)] == "":
         return True
        else:
          return False
      else:
        return False 
    def verify_bowler_name(self,player_name,team_data):
      if player_name in team_data['Name']:
         return True
      else:
        return False 
    def coin_toss(self):
     result = random.choice(['Heads', 'Tails'])
     return result 


s=Start()
m=Match(s)