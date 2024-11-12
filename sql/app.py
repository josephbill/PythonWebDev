# import sqlite3
import sqlite3
## connect/create to the sqlite3 database
conn = sqlite3.connect("example.db")
## cursor object : this object will help us to execute SQL queries to our db engine
cursor = conn.cursor()
'''
1. create the table 
2. run the python file 
3. connect to the database sources.
'''
### create the table : users : id , name , age and email
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NULL,
                email TEXT)''')
conn.commit()

# method is to insert records to the db using SQL statements
# To insert we use the SQL insert into.
def insert_users(name,age,email):
    # writing sql using prepared statements : preventing SQLinjections.
    cursor.execute("INSERT INTO users(name,age,email) VALUES(?,?,?)",(name,age,email))
    conn.commit()

## to select data we use the SQL SELECT statement
def get_users():
    # to get all records from the table
    # cursor.execute("SELECT * FROM users")

    # to specify columns
    # cursor.execute("SELECT name,age FROM users")

    # add a filter to add a condition based on the column  :: WHERE keyword
      cursor.execute("SELECT * FROM users WHERE email=(?)", ("alice@gmail.com",))
    ## the cursor method fetch all returns a list of tuples
      return cursor.fetchall()



def update_user(user_id, name=None, age=None, email=None):
    query = "UPDATE users SET "
    # collections of fields to add
    fields = []
    # collections of values to edit with
    values = []
    if name:
        fields.append("name=?")
        values.append(name)
    if age:
        fields.append("age=?")
        values.append(age)
    if email:
        fields.append("email=?")
        values.append(email)
    values.append(user_id)
    # append values and fields info to build up query
    query += ", ".join(fields) + " WHERE id=?"
    cursor.execute(query,values)
    conn.commit()

## delete
def delete_user(user_id):
    # to delete everything
    cursor.execute("DELETE FROM users")
    # to delete on selection
    # cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
    conn.commit()

#usage
# insert_users("Alice",23,"a@gmail.com")
# insert_users("Bob",23,"b@gmail.com")
# insert_users("Joseph",23,"c@gmail.com")
print(get_users())
update_user(18,"Joseph Doe","20","joseph@gmail.com")
# delete_user(2)
conn.close()









