import mysql.connector
def quick():
        import random
        #getting user name
        print("\n",end="")
        player_name=repr(input("Enter Your Name : "))
        print("\n",end="")
        count=0
        list_1=[]
        for i in range(1,6):
                list_2=[]
                #getting random operands
                num1=(random.randint(0,10))
                list_2.append(num1)
                num2=(random.randint(0,10))
                list_2.append(num2)
                #displaying questions
                print((str(i))+") ",num1,"+",num2,"=",end="")
                #getting user's answer
                x=(input(" "))
                if x=="end":
                        break
                elif x=="skip":
                        list_2.append("_")
                        list_1.append(list_2)
                        continue
                list_2.append(x)
                list_1.append(list_2)

        print("\nGame Results\n")
        print("Your name is",player_name)
        print("You played the game with Quick mode",end="")
        print("\nYou answered "+str(len(list_1))+" questions\n")
        
        for i in range(len(list_1)):
                print(str(i+1)+")",str(list_1[i][0]),"+",str(list_1[i][1]),"=",str(list_1[i][2]),end="")
                ans = (list_1[i][0]) + (list_1[i][1])
                if str(ans)==(list_1[i][2]):
                        print(" (Answer" + str(ans) +") [Correct]")
                        count+=1
                else:
                        print(" (Answer" + str(ans) +") [Incorrect]")
               
        #printing the number of total answers       
        print("\nNumber of correct answers",count)
        #calculating score
        score=int((count/5)*100)
        percentage=(str(score)+"%")
        print("Youre score is",percentage,"\n")
        print("**End of the game**")
        #sending the require data to the database
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
          database="chamo_2019366"
        )

        mycursor = mydb.cursor()
        record="INSERT INTO result (Name,Game_Mode,Level,Num_of_questions,Correct,Marks) VALUES ({},'Quick','-',5,{},{})".format(player_name,count,repr(percentage))
        mycursor.execute(record)
        mydb.commit()
        mydb.close()
        return





        



