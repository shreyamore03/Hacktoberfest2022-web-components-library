import smtplib
from email.message import EmailMessage
EMAIL_ADDRESS = "pollingsystem7@gmail.com"
EMAIL_PASSWORD = "Pollingsystem@"
import pandas as pd
from goto import with_goto
import numpy as np
expath="C:\\Users\\smoot\\Downloads\\Database.xlsx"

@with_goto
def main():

     n = int(input("Enter number of students: "))
     
     result = {}
     votes={}
     
     for i in range(n):
     
     
         print("Enter Details of student No.", i+1)
         name = input("Name: ")
         regno = int(input("Reg no: "))
     
         GPA = int(input("GPA: "))
         if(GPA<7):
             print("Not elligble for participation.")
             continue
     
         
         result[i+1] = [name, regno,GPA]
     print("The information of candidates who are eligible for participating int the elections are: ")    
     print(result) 
     for i in range(n):
         votes[i+1]=0
    
     exdata=pd.read_excel(expath)
     voterid=list(exdata.columns)
     enrollment=list(exdata.loc[:]["REG. NO"])
     #voterid=[101,102,103]
     voted=[]
     while True:
          if enrollment==[]:
               print("Voting is Over")
               max_key = max(votes, key=votes.get)
               print(f"The Candidate {max_key} won the elections.")
               break
          else:
               flag=0
              
               #label.this
               voter=int(input("Enter your voter id :"))
               if voter not in enrollment:
                    print("enter correct enrollment")                    
               
               if voter in voted:
                    print("You are already voted !")
               else:
                    if voter in enrollment:
                         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                              
                              smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                              msg = EmailMessage()
                              msg['Subject'] = "OTP verification for CR voting"
                              msg['From'] = EMAIL_ADDRESS
                              msg['To'] = EMAIL_ADDRESS
                              label.l
                              a = np.random.randint(100000,999999)
                              msg.set_content("Your OTP for Verfication is "+str(a))
                              smtp.send_message(msg)

                              otp=int(input("Enter the OTP: "))
                              if(otp==a):
                                   choice=int(input("Choose your candidate by the index number of candidate  :"))  
                                   
                                   
                                   if choice in votes:
                                        votes[choice]+=1
                                        print(f"You voted candidate {choice}")
                                        enrollment.remove(voter)
                                        voted.append(voter)
                                   else:
                                        print("You already voted!")
                              else:
                                   print("Wrong OTP, new OTP sent")
                                   goto.l





if __name__ =="__main__":
    main()
