from dbsetup import init_conn

class poll_output:
    def __init__(self, group_name: str, month: int, year: int):
        self.group_name = group_name
        self.month = month
        self.year = year

    def query_poll(self):
        c = init_conn()
        def get_results(file,*args):
            with open(file) as sql:
                query = sql.read()
            c.execute(query, args)

        get_results('query_poll_results.sql',self.month, self.year, self.group_name)

test_poll_query = poll_output(group_name='comm_601',month=2,year=2023)
test_poll_query.query_poll()