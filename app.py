from flask import Flask, render_template, request, redirect, json, flash, url_for
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)
app.secret_key = "caircocoders-ednalan-2020"
app.config['MYSQL_HOST'] = '192.168.1.5'
app.config['MYSQL_USER'] = 'sarasas'
app.config['MYSQL_PASSWORD'] = 'sarasas'
app.config['MYSQL_DB'] = 'markeda_autoveziai'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def main():
    return redirect('/sarasas')


@app.route('/sarasas')
def sarasas():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM autoveziai")
    employee = cur.fetchall()
    return render_template('sarasas.html', employee=employee)

@app.route('/updateemployee', methods=['POST'])
def updateemployee():
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if name == 'numeriai':
           cur.execute("UPDATE autoveziai SET numeriai = %s WHERE id = %s ", (value, pk))
        elif name == 'vairuotojas':
           cur.execute("UPDATE autoveziai SET vairuotojas = %s WHERE id = %s ", (value, pk))
        elif name == 'tel_nr':
           cur.execute("UPDATE autoveziai SET tel_nr = %s WHERE id = %s ", (value, pk))
        elif name == 'planuojamas_reisas':
            cur.execute("UPDATE autoveziai SET planuojamas_reisas = %s WHERE id = %s ", (value, pk))
        elif name == 'isvaziavimo_data':
            cur.execute("UPDATE autoveziai SET isvaziavimo_data = %s WHERE id = %s ", (value, pk))
        elif name == 'lokacija':
            cur.execute("UPDATE autoveziai SET lokacija = %s WHERE id = %s ", (value, pk))
        elif name == 'remonto_stovis':
            cur.execute("UPDATE autoveziai SET remonto_stovis = %s WHERE id = %s ", (value, pk))

        mysql.connection.commit()
        cur.close()
        return json.dumps({'status':'OK'})

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        numeriai = request.form['numeriai']
        vairuotojas = request.form['vairuotojas']
        tel_nr = request.form['tel_nr']
        planuojamas_reisas = request.form['planuojamas_reisas']
        isvaziavimo_data = request.form['isvaziavimo_data']
        lokacija = request.form['lokacija']
        remonto_stovis = request.form['remonto_stovis']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO autoveziai (numeriai, vairuotojas, tel_nr, planuojamas_reisas, isvaziavimo_data, lokacija, remonto_stovis) VALUES (%s, %s, %s, %s, %s, %s, %s)", (numeriai, vairuotojas, tel_nr, planuojamas_reisas, isvaziavimo_data, lokacija, remonto_stovis))
        mysql.connection.commit()
        return redirect(url_for('sarasas'))




if __name__ == '__main__':
    app.run(host= '0.0.0.0')