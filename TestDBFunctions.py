from Backend.Postgres.DatabaseClasses import *
from Backend.Postgres.PostgresFlaskConnection import PostgresFlaskConnectionClass
from sqlalchemy import insert, select
import json


class TestingConnectionClass:
    def __init__(self):
        self.postgresConnectionClass = PostgresFlaskConnectionClass()

        self.selectReturn = None

    def __repr__(self):
        return f"""
        return from tbl_linekdinProfile >> {self.selectReturn}
        """
    
    def createSession(self):
        self.postgresConnectionClass.startConnection()
        return

    
    def testSelect(self):
        # Create session object
        self.postgresConnectionClass.startConnection()
        session = self.postgresConnectionClass.getSession()

        # Create select statement
        stmnt = select(LinkedInProfile)
        result = session.execute(stmnt)
        self.selectReturn = result
        session.close()
        return result # Optional to instead return the result here

    def testInsert(self):
        # insert from the json test file
        file = open('Backend/outputProxyCurlSimer.json', 'r')
        data = json.load(file)
        file.close()


        self.postgresConnectionClass.startConnection()
        session = self.postgresConnectionClass.getSession()
        
        stmnt = insert(LinkedInProfile).values(
                public_identifier = data["public_identifier"],
                profile_pic_url =  data["profile_pic_url"],
                background_cover_image_url = data["background_cover_image_url"],
                first_name =  data["first_name"],
                last_name =  data["last_name"],
                full_name =  data["full_name"],
                follower_count =  data["follower_count"],
                occupation =  data["occupation"],
                headline =  data["headline"],
                summary =  data["summary"],
                country =  data["country"],
                country_full_name =  data["country_full_name"],
                city =  data["city"],
                state =  data["state"]
        )
        session.execute(stmnt)
        session.commit()
        session.close()

        return

if __name__ =='__main__':
    testingObject = TestingConnectionClass()
    testingObject.testSelect()
    print(testingObject)
