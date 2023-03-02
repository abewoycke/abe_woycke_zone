from dbsetup import init_conn
import os

class poll_response:
    def __init__(self, group_name: str, submitted_name: str, month: int, year: int, poll_option: str, response: int):
        self.group_name = group_name
        self.submitted_name = submitted_name
        self.month = month
        self.year = year
        self.poll_option = poll_option
        self.response = response

    def record_votes(self):
        c = init_conn()
        # for a given sql file, run with connection c
        def record_records(file, *args):
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            sql_path = os.path.join(BASE_DIR, file)
            with open(sql_path) as sql:
                update = sql.read()
            c.execute(update, args)

        record_records('insert_ignore_dim_group.sql',self.group_name)
        record_records('insert_ignore_dim_participant.sql',self.submitted_name)
        record_records('insert_ignore_dim_poll.sql',self.group_name,self.month,self.year)
        record_records('insert_fact_response.sql',self.submitted_name,self.group_name,
                       self.month,self.year,self.group_name,
                       self.poll_option,self.response)