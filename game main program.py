import sys
import game.quick
import game.custom
import game.database
import game.delete
import mysql.connector
from prettytable import PrettyTable


if sys.argv[1]=="start":
        while True:
                print("\nGame Menu")
                print("\n1. Quick Game\n2. Custom Game\n3. Past Player Results\n4. Delete Past Player Results\n5. End\n6. Game Instuctions")
                choice=input("\nEnter your option: ")

               
                if choice=="1":
                        
                        #creating database
                        game.database.creating_database()

                        #calling the quick mode
                        game.quick.quick()

                        #creating list
                        list_1=[]
      
                        #displaying past player results
                        mydb = mysql.connector.connect(
                          host="localhost",
                          user="root",
                          passwd="",
                          database="chamo_2019366"
                        )

                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT * FROM `result`")
                        data=mycursor.fetchall()
                        print("---------------------------------------------------------------------------------\n\nPast Player Results")
                        for i in data:
                                list_1.append(i)
                        mydb.close()
                                
                        #displaying past player results in a pretty table
                        table=PrettyTable(['num','player name','game mode','level','num of questions','correct','percentage'])
                       

                        for i in range(len(list_1)):
                                table.add_row([list_1[i][0],list_1[i][1],list_1[i][2],list_1[i][3],(list_1[i][4]),list_1[i][5],list_1[i][6]])
                        print(table)   


                        print("\ntotal number of players",len(list_1))
              

       
                elif choice=="2":

                        #creating database
                        game.database.creating_database()

                        #calling the custom mode
                        game.custom.custom()

                        #creating list
                        list_1=[]

                        #displaying past player results
                        mydb = mysql.connector.connect(
                          host="localhost",
                          user="root",
                          passwd="",
                          database="chamo_2019366"
                        )

                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT * FROM `result`")
                        data=mycursor.fetchall()
                        print("---------------------------------------------------------------------------------\n\nPast Player Results")
                        for i in data:
                                list_1.append(i)
                        mydb.close()
                                
                        #displaying past player results in a pretty table
                        table=PrettyTable(['num','player name','game mode','level','num of questions','correct','percentage'])
                       

                        for i in range(len(list_1)):
                                table.add_row([list_1[i][0],list_1[i][1],list_1[i][2],list_1[i][3],(list_1[i][4]),list_1[i][5],list_1[i][6]])
                        print(table)   


                        print("\ntotal number of players",len(list_1))
              

                elif choice=="3":

                        #creating list
                        list_1=[]

                        #displaying past player results
                        mydb = mysql.connector.connect(
                          host="localhost",
                          user="root",
                          passwd=""
                        )

                        mycursor = mydb.cursor()
                        mycursor.execute("show databases")
                        databases=mycursor.fetchall()

                        if ('chamo_2019366',) in databases:
                                mycursor.execute("use chamo_2019366")
                                mycursor.execute("show tables;")
                                data=mycursor.fetchall()
                                if ('result',) in data:
                                        mycursor.execute("SELECT * FROM `result`")
                                        data=mycursor.fetchall()
                                        mydb.close()
                                        if len(data)>=1:
                                                print("---------------------------------------------------------------------------------\n\nPast Player Results")
                                                for i in data:
                                                        list_1.append(i)

                                                #displaying past player results in a pretty table
                                                table=PrettyTable(['num','player name','game mode','level','num of questions','correct','percentage'])
                       

                                                for i in range(len(list_1)):
                                                        table.add_row([list_1[i][0],list_1[i][1],list_1[i][2],list_1[i][3],(list_1[i][4]),list_1[i][5],list_1[i][6]])
                                                print(table)   
                                                print("\ntotal number of players",len(list_1))
                                        else:
                                                print("\nCurrenty no players available in past player results")
                                else:
                                      print("\nCurrenty no players available in past player results")
   

                        else:
                                print("\nCurrenty no players available in past player results")


                #delete option
                elif choice=="4":
                        game.delete.database()
                              

                elif choice=="5":
                        print("\n**end of the game**")
                        break

                elif choice=="6":
                        print("""\n~Instuctions~\n\nFirstly its highly recommended to delete if there is a database as game existing MySQL.\nSelect the game mode you wanted from the game menu and enter the number of the option you wanted.\nPlayer name should not be more than 10 characters\nYou can skip any difficult question you wanted both in Quick Mode and Custom Mode by just typing 'skip' instead of answer.\nAlso can easily leave the game by typing 'end' at any stage while answering questions.\nIn Custom Mode you have to give the relevant key words. Otherwise the program will ask again to input correct keywords.\nEach game results will automatically store in a database and you cansee it if you wanted.\nEnjoy the game.""")

                else:
                        print("\nYou have entered a wrong input. Please enter a valid input")
            
                              
       
