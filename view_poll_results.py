from dbsetup import init_conn
import os
import pandas as pd

class vpr:
    def __init__(self,crew:str,month:int,year:int):
        self.crew = crew
        self.month = month
        self.year = year

    def vpr_html(self):
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

        crew = self.crew
        month = self.month
        year = self.year
        top_poll_results_votes = view_records('view_results.sql', crew, month, year)

        df = pd.DataFrame(top_poll_results_votes, columns=['Month','Day','Time','Headcount','Folks Available (Submitted Name)'])

        # group by poll option
        df = df.groupby(['Month','Day','Time','Headcount'],group_keys=False)['Folks Available (Submitted Name)'].apply(', '.join).reset_index()

        # sort by headcount
        df = df.sort_values(by=['Day','Time']).sort_values(by=['Headcount'],ascending=False)

        # reset index
        df = df.reset_index(drop=True)

        # prettify output
        def make_pretty(styler):
            styler.set_caption("Top Five Date Results")
            styler.hide(axis="index")
            styler.set_table_styles([
                {"selector":"thead",
                 "props":[("background-color","dodgerblue"), ("color","white"),
                          ("font-size", "1em"), ('text-align', 'center')]
                },])
            styler.highlight_max(subset="Headcount",axis=0,color='green')
            styler.set_properties(**{'text-align': 'center'})
            styler.set_properties(**{'width': '12em'})
            return styler

        return df.style.pipe(make_pretty).to_html()
