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

        return mydb

    def execute(self):
        cursor=self.MySQLConnect().cursor()
        cursor.execute(self.sql,self.values)
        self.MySQLConnect().commit() #to tutaj trzeba poprawic
        print(mycursor.rowcount, "record inserted.")


class insert_values2():

    def __init__(self,columns,values,database):
        self.columns=columns
        self.values=values
        self.database=database

    @staticmethod
    def MySQLConnect():
        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user="mateusz",
                                   pw=os.environ["mysql_password"],
                                   db="python"))

        return engine

    def execute(self):
        df = pd.DataFrame(self.values, columns=self.columns)
        # sql.write_frame(df, con=mydb, name='python.mail',
        #                 if_exists='append', flavor='mysql')
        df.to_sql(con=MySQLConnect(), name=self.database, if_exists='append',index=False,index_label=self.columns)

sql = "INSERT INTO python.mail (imie,nazwisko,email,kraj,us_id,wynik) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("chrum", "Highway",'j.hidsadasghway@gmail','en',123523,200)
insert_values(sql,val).execute()

column=["imie",'nazwisko','email','kraj','us_id','wynik']
list=[["John", "Highway",'j.highway@gmail','en',123523,110],["Johnw", "Highwdsay",'j.highwaysda@gmail','en',123223,10]]
database='mail'
insert_values2(column,list,database).execute()