import mysql.connector as c

class DB:
    def __init__(self):
        # create db
        # self.con = c.connect(host='localhost', port=8484, user='root', passwd='Mansi@2701', auth_plugin='mysql_native_password')
        # q ='create database student'
        # cur = self.con.cursor()
        # cur.execute(q)
        # print('database created')

        # create a connection
       
        self.con = c.connect(host='localhost', port=8484, user='root', passwd='Mansi@2701', database='student', auth_plugin='mysql_native_password')
        print('Connection is successful')
    
       
    def create(self):
        query = 'CREATE TABLE IF NOT EXISTS stud_49 (s_id INT, s_name VARCHAR(200),s_city VARCHAR(200),s_gender VARCHAR(20),s_contact INT(10))'
        self.cur =self.con.cursor()
        self.cur.execute(query)
        print('Table created')

    def insert(self,s_id, s_name,s_city,s_gender,s_contact):
        print('------insert---------------')
        query = 'INSERT INTO stud_49(s_id,s_name,s_city,s_gender,s_contact) VALUES ({},"{}","{}","{}",{})'.format(s_id, s_name,s_city,s_gender,s_contact)
     
        self.cur= self.con.cursor()
        self.cur.execute(query)
        self.con.commit()  

    def update(self,s_id,s_name,s_city,s_gender,s_contact):
        try:
                # print('-------update------------------')
              
                query='update stud_49 set s_name="{}",s_city="{}",s_gender="{}",s_contact={} where s_id={}'.format( s_name,s_city,s_gender,s_contact,s_id)
                self.cur=self.con.cursor()
                self.cur.execute(query)
                self.con.commit()
                print('row updated')
                
        except Exception as e:
            print('ERROR',e)

    def delete(self,s_id):
        print('----------delete-----------------')
       
        query='delete from stud_49 where id={}'.format(s_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()  
    def fetch(self):
        print('----------fetch-----------------')
       
        query='select * from stud_49'
        cur = self.con.cursor()
        cur.execute(query)
        for cu in cur:
            print(cu)
        self.con.commit()  

    def close(self):
        self.con.close()

        print('Connection closed')
print('-----------------------------------------------')
    




# Instantiate the class, create table, and insert data

print('-----------------------------------------------')

c_d = DB()
# c_d.create()
# c_d.insert(62,"abcd","baroda","male",454561223)

c_d.update(59,"tigers","than","male",454567689)
c_d.fetch()
# c_d.delete()
 # Close the connection

