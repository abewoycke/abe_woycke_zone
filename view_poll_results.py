from dbsetup import init_conn
import os
import pandas as pd

class view_poll_results:
    def __init__(self,group:str,month:int,year:int):
        self.group = group
        self.month = month
        self.year = year

    def view_poll_results(self):
        c = init_conn()

        # for a given sql file, run with connection c
        def view_records(file, *args):
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            sql_path = os.path.join(BASE_DIR, file)

            with open(sql_path) as sql:
                read = sql.read()

            c.execute(read, args)
            results = c.fetchall()
            return results

        # data manipulation on queries to return everything
        # in the form that is most useful to the viewer

        group = self.group
        month = self.month
        year = self.year
        top_poll_results_votes = view_records('top_poll_results_votes.sql', group, month, year)

        votes = top_poll_results_votes[0][1]

        df = pd.DataFrame(top_poll_results_votes, columns=['poll_option', 'votes', 'submitted_name'])

        # group by poll option
        df = df.groupby(['poll_option'])['submitted_name'].apply(', '.join).reset_index()

        # sort by day of month ascending
        df['day_of_month'] = df['poll_option'].str.extract(r'\/(\d\d)')
        df.sort_values(by='day_of_month', inplace=True)
        df.drop(columns=['day_of_month'], inplace=True)
        df = df.reset_index(drop=True)
        return votes, df.to_html