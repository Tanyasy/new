from pymysql import install_as_MySQLdb

# After this function is called, any application that imports MySQLdb or
# _mysql will unwittingly actually use pymysql
# python3的数据库驱动： pymysql
# python2的数据库驱动： MySQLdb
# 当底层使用到MySQLdb的时候会自动转换使用pymysql
install_as_MySQLdb()