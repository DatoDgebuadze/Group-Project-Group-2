from flask import Flask, render_template
import pandas as pd
import sqlite3
import os



current_directory = os.getcwd()
print("Current Directory:", current_directory)


app = Flask(__name__)

# Initialize SQLite database connection
# con = sqlite3.connect('./database/pd_data.db')


@app.route('/')
def index():
    return render_template('index.html', app_name='Our ML Group project')


@app.route('/about')
def about():
    return render_template('about.html', app_name='Our ML Group project')


@app.route("/data")
def data():
    con = sqlite3.connect('../database/pd_data.db')
    # Query SQLite database to read data
    result_1 = pd.read_sql_query("SELECT * FROM pd_euros", con)
    # result_2 = pd.read_sql_query("SELECT * FROM pd_fuel", con)

    # Convert DataFrames to HTML tables
    table_html1 = result_1.to_html(index=False)
    # table_html2 = result_2.to_html(index=False)

    # Close the database connection
    con.close()
# table_html2=table_html2
    return render_template('data_table.html', table_html1=table_html1, )


if __name__ == '__main__':
    app.run(debug=True)
