import mysql.connector
def custom ():
        import random
        #getting user name and other needed things
        print("\n",end="")
        player_name=repr(input("Enter Youre Name : "))
        print("\n",end="")

        while True:
                #checking the user input num_of_question is an integer
                while True:
                        try:
                                num_question=int(input("Enter Number of Questions You Want : "))
                                break
                        except:
                                print("\nWhat you entered for 'Enter number of questions you want' is not an Integer.Please input an Integer value")
                                continue
                
                num_question=int(num_question)
            
                                
                #checking the user input questions is an integer
                while True:
                        try:
                                questions=int(input("Re-enter Number of Questions You Want : "))
                                break
                        except:
                                print("\nWhat you entered for 'Re-enter number of questions you want' is not an Integer.Please input an Integer value")
                                continue
                
                questions=int( questions) 
                                        
                #checking whether num_question==questions
                if num_question==questions:
                        break
                else:
                        print("\nERROR:Entered number of questions are not matching re-enter")
                        continue


        print("\n",end="")
        while True:
                level=(input("Enter Difficulty Level You Want (easy,medium,hard) : "))
                level_type=level.lower()

                if  level_type=="easy":
                        break
                elif  level_type=="medium":
                        break
                elif  level_type=="hard":
                        break
                else:
                         print("\nERROR:Entered key word is not valid re-enter")
        print("\n",end="")
        count=0
        list_1=[]
        if  level_type=="easy"  :
                for i in range(1,num_question+1):
                        list_2=[]
                        #getting random operands
                        num1=(random.randint(0,10))
                        list_2.append(num1)
                        opr=(random.choice("+"))
                        list_2.append(opr)
                        num2=(random.randint(0,10))
                        list_2.append(num2)
                        #displaying questions
                        print((str(i))+") ",num1,opr,num2,"=",end="")
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
                print("You played the game with Custom mode,easy",end="")
                print("\nYou answered "+str(len(list_1))+" questions\n")
        
                for i in range(len(list_1)):
                        print(str(i+1)+")",(list_1[i][0]),(list_1[i][1]),(list_1[i][2]),"=",(list_1[i][3]),end="")
                        ans = (list_1[i][0]) + (list_1[i][2])
                        if str(ans)==(list_1[i][3]):
                                print(" (Answer" + str(ans) +") [Correct]")
                                count+=1
                        else:
                                print(" (Answer" + str(ans) +") [Incorrect]")
                #printing the number of total answers       
                print("\nNumber of Correct Answers",count)
                #calculating score
                score=int((count/ num_question)*100)
                percentage=(str(score)+"%")
                print("Youre score is",percentage,"\n")
                print("**End of the game**")
                #sending the require data to a database
                mydb = mysql.connector.connect(
                          host="localhost",
                          user="root",
                          passwd="",
                          database="chamo_2019366"
                )

                mycursor = mydb.cursor()
                record="INSERT INTO result (Name,Game_Mode,Level,Num_of_questions,Correct,Marks) VALUES ({},'Custom','Easy',{},{},{})".format(player_name,num_question,count,repr(percentage))
                mycursor.execute(record)
                mydb.commit()
                mydb.close()
                return

                
        elif  level_type=="medium":
                for i in range(1,num_question+1):
                        list_2=[]
                        #getting random operands
                        num1=(random.randint(0,50))
                        list_2.append(num1)
                        opr=(random.choice("+-"))
                        list_2.append(opr)
                        num2=(random.randint(0,50))
                        list_2.append(num2)
                        ans=num1+num2
                        #displaying questions
                        print((str(i))+") ",num1,opr,num2,"=",end="")
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
                print("You played the game with Custom mode,medium",end="")
                print("\nYou answered "+str(len(list_1))+" questions\n")
        
                for i in range(len(list_1)):
                        if (list_1[i][1])=="+":
                                print(str(i+1)+")",(list_1[i][0]),(list_1[i][1]),(list_1[i][2]),"=",(list_1[i][3]),end="")
                                ans = (list_1[i][0]) + (list_1[i][2])
                                if str(ans)==(list_1[i][3]):
                                        print(" (Answer" + str(ans) +") [Correct]")
                                        count+=1
                                else:
                                        print(" (Answer" + str(ans) +") [Incorrect]")

                        else:
                                print(str(i+1)+")",str(list_1[i][0]),(list_1[i][1]),str(list_1[i][2]),"=",str(list_1[i][3]),end="")
                                ans = (list_1[i][0]) - (list_1[i][2])
                                if str(ans)==(list_1[i][3]):
                                        print(" (Answer" + str(ans) +") [Correct]")
                                        count+=1
                                else:
                                        print(" (Answer" + str(ans) +") [Incorrect]")

               #printing the number of total answers       
                print("\nNumber of Correct Answers",count)
                #calculating score
                score=int((count/ num_question)*100)
                percentage=(str(score)+"%")
                print("Youre score is",percentage,"\n")
                print("**End of the game**")
                #sending the require data to a database
                mydb = mysql.connector.connect(
                          host="localhost",
                          user="root",
                          passwd="",
                          database="chamo_2019366"
                )

                mycursor = mydb.cursor()
                record="INSERT INTO result (Name,Game_Mode,Level,Num_of_questions,Correct,Marks) VALUES ({},'Custom','Medium',{},{},{})".format(player_name,num_question,count,repr(percentage))
                mycursor.execute(record)
                mydb.commit()
                mydb.close()
                return


        elif  level_type=="hard":    
                for i in range(1,num_question+1):
                        list_2=[]
                        #getting random operands
                        num1=(random.randint(0,100))
                        list_2.append(num1)
                        opr=(random.choice("+-*"))
                        list_2.append(opr)
                        num2=(random.randint(0,100))
                        list_2.append(num2)
                        ans=num1+num2
                        #displaying questions
                        print((str(i))+") ",num1,opr,num2,"=",end="")
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
                print("You played the game with Custom mode,Hard",end="")
                print("\nYou answered "+str(len(list_1))+" questions\n")
        
                for i in range(len(list_1)):
                        if (list_1[i][1])=="+":
                                print(str(i+1)+")",(list_1[i][0]),(list_1[i][1]),(list_1[i][2]),"=",(list_1[i][3]),end="")
                                ans = (list_1[i][0]) +  (list_1[i][2])
                                if str(ans)==(list_1[i][3]):
                                        print(" (Answer" + str(ans) +") [Correct]")
                                        count+=1
                                else:
                                        print(" (Answer" + str(ans) +") [Incorrect]")

                        elif (list_1[i][1])=="-":
                                print(str(i+1)+")",(list_1[i][0]),(list_1[i][1]),(list_1[i][2]),"=",(list_1[i][3]),end="")
                                ans = (list_1[i][0]) -  (list_1[i][2])
                                if str(ans)==(list_1[i][3]):
                                        print(" (Answer" + str(ans) +") [Correct]")
                                        count+=1
                                else:
                                        print(" (Answer" + str(ans) +") [Incorrect]")

                        else:
                                print(str(i+1)+")",(list_1[i][0]),(list_1[i][1]),(list_1[i][2]),"=",(list_1[i][3]),end="")
                                ans = (list_1[i][0]) *  (list_1[i][2])
                                if str(ans)==(list_1[i][3]):
                                        print(" (Answer" + str(ans) +") [Correct]")
                                        count+=1
                                else:
                                        print(" (Answer" + str(ans) +") [Incorrect]")



              #printing the number of total answers       
                print("\nNumber of Correct Answers",count)
                #calculating score
                score=int((count/ num_question)*100)
                percentage=(str(score)+"%")
                print("Youre score is",percentage,"\n")
                print("**End of the game**")
                #sending the require data to a database
                mydb = mysql.connector.connect(
                          host="localhost",
                          user="root",
                          passwd="",
                          database="chamo_2019366"
                )

                mycursor = mydb.cursor()
                record="INSERT INTO result (Name,Game_Mode,Level,Num_of_questions,Correct,Marks) VALUES ({},'Custom','Hard',{},{},{})".format(player_name,num_question,count,repr(percentage))
                mycursor.execute(record)
                mydb.commit()
                mydb.close()
                return


