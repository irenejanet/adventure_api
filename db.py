import MySQLdb

# MySQL Connection Configuration
mysql_config = {
    'user': 'root',
    'password': 'computing',
    'host': 'localhost',
    'database': 'AdventureWorks2019',
    
}
# Connect to MySQL
conn = MySQLdb.connect(**mysql_config)