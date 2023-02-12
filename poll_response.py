class poll_response:
    def __init__(self,group_name,submitted_name,month,year,submitted_dt,poll_option,response):
        self.group_name = group_name
        self.submitted_name = submitted_name
        self.month = month
        self.year = year
        self.submitted_dt = submitted_dt
        self.poll_option = poll_option
        self.response = response

    def record_records(self, file, *args):
        with open(file) as sql:
            update = sql.read()
        c.execute(update, args)

    def record_votes(self):
        record_records('insert_ignore_dim_group.sql',self.group_name)
        record_records('insert_ignore_dim_participant.sql',self.submitted_name)
        record_records('insert_ignore_dim_poll.sql',self.group_name,self.month,self.year)
        record_records(fact_response_sql_file,self.submitted_name,self.group_name,
                       self.month,self.year,self.group_name,self.submitted_dt,
                       self.poll_option,self.response)
        c.execute(query)