import mysql.connector

mydb = mysql.connector.connect(
        host="hypegenai.com",
        user="hypegena",
        password="aZ5xjXf133",
        database="hypegena_chain"
    )
   
email = 'halit@hotmail.com'
password = 'halit123'
mycursor = mydb.cursor()
mycursor.execute("select*from users2 where mail='" +
                    email+"' and password='"+password+"'")
myresult = mycursor.fetchall()
mycursor.close()

# print(myresult)
if myresult:
    for x in myresult:
        print(x)