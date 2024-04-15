from flask import Flask, render_template
import pandas as pd
import sqlite3

app = Flask(__name__)

# Initialize SQLite database connection
conn = sqlite3.connect("Group Project/pd_data.db")


@app.route('/')
def index():
    return render_template('index.html', app_name='Our ML Group project')


@app.route('/about')
def about():
    return render_template('about.html', app_name='Our ML Group project')


@app.route("/data")
def data():
    # Reading CSV files into pandas DataFrames
    read_file1 = pd.read_csv("../dataset/euros.csv")
    read_file2 = pd.read_csv("../dataset/my2024-fuel-consumption-ratings.csv")

    # now here we are Write DataFrames to SQLite tables
    read_file1.to_sql('pd_euros', conn, if_exists='replace', index=False)
    read_file2.to_sql('pd_fuel', conn, if_exists='replace', index=False)

    # we have select All query for SQLite database to read data
    result_1 = pd.read_sql_query("SELECT * FROM pd_euros", conn)
    result_2 = pd.read_sql_query("SELECT * FROM pd_fuel", conn)

    # Converting DataFrames to HTML tables
    table_html1 = result_1.to_html(index=False)
    table_html2 = result_2.to_html(index=False)
    # rendering data html
    return render_template('data_table.html', table_html1=table_html1, table_html2=table_html2)


if __name__ == '__main__':
    app.run(debug=True)

# Close the database connection
conn.close()
