import mysql.connector as c

class DB:
    def __init__(self):
        # create a connection
        self.conn = c.connect(host='localhost', port=8484, user='root', passwd='Mansi@2701', database='conn', auth_plugin='mysql_native_password')
        print('Connection is successful')
       
   

# Instantiate the class and call the create method
c_d = DB()

