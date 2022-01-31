from flask import Flask, render_template
from mysql.connector import connect, Error
import os
app = Flask(__name__)

try:
    mydb = connect(
      host="db",
      user="root",
      password=os.environ["db_password"],
      database=os.environ["db_name"]
    )

except Error as e:
    print(e)

cursor = mydb.cursor()
cursor.execute('''SELECT id, name, lastname, age FROM register
              {% if PEOPLE_AGE is defined  %}  where age<={{ PEOPLE_AGE }} {% endif %}  ''')
result = cursor.fetchall()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
