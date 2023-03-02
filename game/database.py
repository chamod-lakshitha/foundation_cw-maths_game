import mysql.connector

def creating_database():
        list_1=[]
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd=""
        )
        mycursor = mydb.cursor()

        mycursor.execute("show databases")
        databases=mycursor.fetchall()

        #checking if the data base is available
        if ('chamo_2019366',) in databases:
                mycursor.execute("use chamo_2019366")
                mycursor.execute("show tables;")
                data=mycursor.fetchall()
                if ('result',) in data:
                        pass
                else:
                        mycursor.execute("use chamo_2019366")
                        mycursor.execute("""CREATE TABLE result (num int(11) NOT NULL AUTO_INCREMENT,
                             Name varchar(10),
                             Game_Mode char(10),
                             Level varchar(10),
                             Num_of_questions int(5),
                             Correct int(5),
                             Marks varchar(10),
                             PRIMARY KEY (num));""")
                        mydb.close()
                        return

        else:
                mycursor.execute("CREATE DATABASE chamo_2019366;")
                mycursor.execute("use chamo_2019366")
                mycursor.execute("""CREATE TABLE result (num int(11) NOT NULL AUTO_INCREMENT,
                             Name varchar(10),
                             Game_Mode char(10),
                             Level varchar(10),
                             Num_of_questions int(5),
                             Correct int(5),
                             Marks varchar(10),
                             PRIMARY KEY (num));""")
                mydb.close()
                return




                     
