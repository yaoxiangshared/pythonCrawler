import mysql.connector
import configparser
import platform
import socket



# 创建配置解析器对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

host = config['starrocks-database']['host']
port = 9030
user = config['starrocks-database']['user']
password = config['starrocks-database']['password']
database = config['starrocks-database']['database']

# 数据库连接配置
dbconfig = {
    'user': user,
    'password': password,
    'host': host,
    'database': database,
    'port':port,
    'raise_on_warnings': True
}
print( dbconfig)

# 建立连接
cnx = mysql.connector.connect(**dbconfig)
cursor = cnx.cursor()
