from flaskext.mysql import MySQL
from flask import Flask

class DBcon():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def conexion(self):
        mysql = MySQL()
        app = Flask(__name__)
        app.config['MYSQL_DATABASE_USER'] = 'adminlab'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'labo2015'
        app.config['MYSQL_DATABASE_DB'] = 'centro_de_computo'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
        return mysql