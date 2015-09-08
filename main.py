from flask import Flask
from flask import render_template
import os
import MySQLdb

print(os.environ['APP_SETTINGS'])

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/")
def main():
    return "Schools and houses go here!"

@app.route("/house-data")
def house_data():
    conn = MySQLdb.connect(host=os.environ['DATABASE_URL'], port=int(os.environ['DATABASE_PORT']), db='test', user=os.environ['DATABASE_USER'], passwd=os.environ['DATABASE_PASSWORD'])
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    # sample query
    cursor.execute("SELECT post_code_clean, AVG(price) as avg_price, COUNT(*) as sales_no FROM house_sales \
                    GROUP BY post_code_clean \
                    HAVING COUNT(*) > 5 \
                    ORDER BY avg_price DESC \
                    LIMIT 100")

    house_sales = cursor.fetchall()

    cursor.close()
    conn.close()    

    return render_template('house_data.html', house_sales = house_sales)

if __name__ == "__main__":
    app.run()