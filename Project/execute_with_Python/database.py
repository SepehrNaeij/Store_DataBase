import psycopg2
c = None
cur=None
try:
    c = psycopg2.connect(
        host="localhost",
        database="Database_Connection",
        user="postgres",
        password="2220166058Ss")
    cur = c.cursor()

    cur.execute('DROP TABLE IF EXISTS Customer')
    
    #Create table
    create_table=''' Create table if Not exists Customer(
                        ID serial primary key ,
                        first_name varchar (200) ,
                        last_name varchar (200) ,
                        phone_number text,
                        validity integer
                        )'''
    cur.execute(create_table)

    #insert table
    def insert(id,f_name,l_name,phone,validity):
        insert_tabel='INSERT INTO Customer (ID, first_name , last_name , phone_number, validity ) VALUES(%s,%s,%s,%s,%s)'
        insert_values=(id,f_name,l_name,phone,validity)
        cur.execute(insert_tabel,insert_values)
        print("data inserted")
    
    #delete records
    def delete(Id):
        delete_record= 'DELETE FROM Customer WHERE ID=' + str(Id)
        cur.execute(delete_record)
        print("data deleted")
    

    #update records
    def update(id , entity , new_entity):
        update_table='UPDATE Customer SET ' + entity +' = %s WHERE ID = %s'
        update_values=(new_entity,id)
        cur.execute(update_table,update_values)
        print("data updated")

    

    #read table
    def read(ID):
        cur.execute('select * from Customer')
        for record in cur.fetchall():
            if record[0]==ID :
                print ("ID : ",record[0])
                print ("first name : ",record[1])
                print ("last name : ",record[2])
                print ("phone number : ",record[3])
                print ("validity : ",record[4])
    #Test
    #insert(1,'sepehr','naeij','09331984840',200)
    #insert(2,'amirhossein','najafi','09117771991',250)
    #insert(3,'sadegh','vahedi','09336491946',300)
    #delete(1)
    #update(2,  'last_name' , "rahmati")
    #read(1)


    c.commit()
except Exception as eror:
    print(eror)
finally:
    if cur is not None:
        cur.close
    if c is not None:
        c.close
    