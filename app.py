from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector 

# initializations
app = Flask(__name__)


# Mysql Connection


conexion1=mysql.connector.connect(host="192.168.100.60", 
                                  user="wpuser", 
                                  passwd="1270130", 
                                  database="compliance_server")


@app.route('/')
def Index():
    cursor1 = conexion1.cursor()
    cursor1.execute('SELECT * FROM tabla_servidores')
    sql = cursor1.fetchall()
    cursor1.close()
    return render_template('index.html', servidor = sql[0], servidores = sql)



if __name__ == "__main__":
    app.run(host='192.168.100.60', port=5010, debug=True)
    
    
    
    
    
    
    