from mariadb import Error
import mariadb

# user,pw and db variable storing username, password and database name for sql connection
pwd = "qRuF4e5MLqxyQc"
user="root"
db = "bysonicg_misimu"

# Function to connect to server
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mariadb.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

# Function to read query
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# Function to read from database
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# Function to pass all queries to get users from different tables
def retrieve_users(query, arr):
    global results

    # Reading users from the db
    results = read_query(connection, query)

    # Reading all the data contained in table
    for result in results:
        user_info(result,arr)
    # print(arr)

# Function to get user information and store it in an 2d array
def user_info(users,arr):
    global results
    for i in range(len(results)):
        for user in users: # Useful to loop through 2d array incase of multiple DB entries
            # id = users[0]
            fName = users[1]
            lName = users[2]
            phone = users[4]
            email = users[3]
            telegram = users[5]
            location = users[6]
            # password = users[7]
    arr.insert(i,[fName,lName,phone,email,location,telegram])
         
def org_info(org,arr):
    global results
    for i in range(len(results)):
        # id = org[0]
        oname = org[1]
        email = org[2]
        phone = org[3]
        location = org[4]
        # password = org[5]
    arr.insert(i,[oname,email,phone,location])

# Main function 
#    
# Query used to get all users in regular table
q1 = "SELECT * FROM regular;"

# Query used to get all users in farmer table
q2 = "SELECT * FROM farmer;"

# Query used to get all users in organization table
q3 = "SELECT * FROM organization;"

# Creating the connection to the server
connection = create_server_connection("localhost","root", pwd, db)

# Array to store all users retrieved in lists 
reg_users = []
farmers = []
org = []

retrieve_users(q1,reg_users)
retrieve_users(q2,farmers)
results = read_query(connection, q3)

# Reading all the data contained in organization table statically
for result in results:
    org_info(result,org)
    # print(org)




    



