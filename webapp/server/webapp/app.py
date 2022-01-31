from flask import Flask, render_template
from mysql.connector import connect, Error
import os
app = Flask(__name__)

try:
    mydb = connect(
      host="db",
      user="root",
      password="password",
      database="people"
    )

except Error as e:
    print(e)

cursor = mydb.cursor()
age = 20
cursor.execute('''SELECT id, name, lastname, age FROM register
                where age=(%s)''', (age,))
result = cursor.fetchall()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
