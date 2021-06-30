import sqlite3

def create_tables():
    conn = sqlite3.connect('covid_tracker.db')
    
    

class Users:
    def __init__(self):
        conn = sqlite3.connect('covid_tracker.db')
        conn.execute("""CREATE TABLE IF NOT EXISTS users
            ( user_id INTEGER PRIMARY KEY AUTOINCREMENT,
              NAME VARCHAR(50) NOT NULL,
              pin NUMBER NOT NULL,
              mobile_number NUMBER NOT NULL,
              ROLE VARCHAR(5) NOT NULL
              );
             """)

    def register_user(self, pin, name, mobile_number, role):
        self.pin = pin
        self.name = name
        self.mobile_number = mobile_number
        self.role = role 
        conn = sqlite3.connect('covid_tracker.db')
        query = f"insert into users(NAME, pin, mobile_number, ROLE) values({self.name},{self.pin}, {self.mobile_number}, {self.role})"
        print(query)
        conn.execute(query)

# class Details:
#         def __init__(self):
#             conn.execute("""CREATE TABLE users
#                 ( user_id INTEGER FOREIGN KEY AUTOINCREMENT,
#                 NAME VARCHAR(50) NOT NULL,
#                 pin NUMBER NOT NULL,
#                 mobile_number NUMBER NOT NULL,
#                 ROLE VARCHAR(5) NOT NULL
#                 );
#         def register_user(self):
#             self.pin = pin
#             self.name = name
#             self.mobile_number = mobile_number
#             conn = db.connect('covid_tracker.db')
#             conn.execute("""
#                 insert into admins(pin, mobile_number) values({self.pin}, {self.mobile_number});
#             """)


        
        

