import pymysql
import db_config
from tkinter import *
from tkinter import messagebox

def mysqlconnect():
  #to connect MySql database
  conn = pymysql.connect(
        host = 'localhost',
        user='root',
        password='',
        db='pawnblock')

  return conn