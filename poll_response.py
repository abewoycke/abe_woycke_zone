from dbsetup import init_conn
import os

class poll_response:
    def __init__(self, crew: str, participant: str, month: int, day: int, year: int, time_description: str, response: int, submitted_dt: str):
        self.crew = crew
        self.participant = participant
        self.month = month
        self.day = day
        self.year = year
        self.time_description = time_description
        self.response = response
        self.submitted_dt = submitted_dt

    def insert_responses(self):
        c = init_conn()
        # for a given sql file, run with connection c
        def record_records(file, *args):
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            sql_path = os.path.join(BASE_DIR, file)
            with open(sql_path) as sql:
                update = sql.read()
            c.execute(update, args)

        record_records('insert_response.sql',self.crew,self.participant,
                       self.month,self.day,self.year,
                       self.time_description,self.response,
                       self.submitted_dt)