import mysql.connector
import pymysql
import os
from pandas.io import sql
import pandas as pd
# import MySQLdb
from sqlalchemy import create_engine

class insert_values():

    def __init__(self,sql,values):
        self.sql=sql
        self.values=values

    @staticmethod
    def MySQLConnect():
        mydb = mysql.connector.connect(
                user='mateusz'
                , password=os.environ["mysql_password"]
                , host='localhost'
                , database='python'
        )
        mycursor = mydb.cursor()
        return mycursor

    def execute(self):
        cursor=self.MySQLConnect()
        cursor.execute(self.sql,self.values)
        mydb.commit() #to tutaj trzeba poprawic
        print(mycursor.rowcount, "record inserted.")


class insert_values2():

    def __init__(self,database,columns,values):
        self.database=database
        self.columns=columns
        self.values=values

    @staticmethod
    def MySQLConnect():
        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user="mateusz",
                                   pw="oliverzamek7",
                                   db="python"))

        return engine

    def execute(self):
        df = pd.DataFrame(self.values, columns=self.columns)
        # sql.write_frame(df, con=mydb, name='python.mail',
        #                 if_exists='append', flavor='mysql')
        df.to_sql(con=MySQLConnect(), name=self.database, if_exists='append',index=False,index_label=self.columns)


column=["imie",'nazwisko','email','kraj','us_id','wynik']
list2=[["John", "Highway",'j.highway@gmail','en',123523,110],["Johnw", "Highwdsay",'j.highwaysda@gmail','en',123223,10]]
databasee='mail'