import mysql.connector

def database():
        mydb = mysql.connector.connect(
                          host="localhost",
                          user="root",
                          passwd=""
                )

        mycursor = mydb.cursor()
        mycursor.execute("show databases")
        databases=mycursor.fetchall()
        #checking if the database is available
        if ('chamo_2019366',) in databases:
                 print("\nDo you really want to the Database",end="")
                 print("\n1. Yes\n2. No\n",end="")
                 print("\n",end="")
                 while True:
                         option=input("Enter your option: ")
                         if option=="1":
                                 mycursor.execute("drop database chamo_2019366;")
                                 mydb.commit()
                                 mydb.close()
                                 print("\n",end="")
                                 print("Past Player Results deleted")
                                 break

                         elif option=="2":
                                 break

                         else:
                                 print("\nPlease enter a valid keyword")
                                 continue

        else:
                print("\nPast player results is already deleted\n",end="")

        return
                                 
                                 
         




        
         



