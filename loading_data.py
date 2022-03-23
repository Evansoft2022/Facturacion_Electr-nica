import sqlite3, pymysql.cursors,sqlite3
MyDB = pymysql.connect(host="159.203.170.123",port=3306,user="root",passwd="medellin100",db="payroll",charset='utf8',cursorclass=pymysql.cursors.DictCursor)
cursor = MyDB.cursor()
cursor.execute("select * from Type_Workers")
data = cursor.fetchall()
con = sqlite3.connect('db.sqlite3')
c = con.cursor()
for i in data:
	query = "insert into data_Type_Worker(_id,name)values(?,?)"
	args = (int(i['id']), str(i['name']))
	c.execute(query,args)

con.commit()