from logging import Handler, log
import os
from flask import Flask ,jsonify
from flask_sqlalchemy import SQLAlchemy 
import configparser
import pymysql
import logging 
'''init'''
app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)
logger =logging.getLogger('werkzeug')
'''read config file'''
config = configparser.ConfigParser()
config.read('config.ini')

''' absolute path'''
basedir = os.path.abspath(os.path.dirname(__file__))

'''set flask connect mysql'''   
user = config.get('SQL_server', 'user')
password = config.get('SQL_server','password')
IP = config.get('SQL_server','IP')
DBname = config.get('SQL_server','DBname')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 設定監控修改
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{IP}/{DBname}'

''''''




@app.route('/home')
def home():
    app.logger.info('info log')
    app.logger.warning('warning log')
    #app.logger.debug('A value for debugging')

    #app.logger.error('An error occurred')
    sql = '''
        SELECT id 
        FROM oltp.test
    '''
    try:
        query_data = db.engine.execute(sql)
        
        return jsonify({"mysql_status":"OK"})
    except:
        return jsonify({"mysql_status":"ERROR"})


if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log',encoding='utf-8')
    handler.setLevel(logging.DEBUG)
    #logging_format = logging.Formatter(
    #    "%(asctime)s - %(levelname)s -%(filename)s - %(funcName)s - %(lineno)s - %(message)s"
    #)
    #print(type(logging_format))

    #handler.setLevel(logging_format)
    app.logger.addHandler(handler)
    app.run()
