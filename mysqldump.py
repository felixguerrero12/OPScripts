import MySQLdb, os,  datetime

con = MySQLdb.connect(host='db', user='XXXXXXXXX', passwd='XXXXXXXXX', db='XXXXXXXXX')
cur = con.cursor()

cur.execute("SHOW TABLES")
data = ""
tables = [table[0] for table in cur.fetchall()]
for table in tables:
    #data += "DROP TABLE IF EXISTS `" + str(table) + "`;"
    cur.execute(f"SHOW CREATE TABLE `{str(table)}`;")
    data += "\n" + str(cur.fetchone()[1]) + ";\n\n"

    cur.execute(f"SELECT * FROM `{str(table)}`;")
    for row in cur.fetchall():
        data += f"INSERT INTO `{str(table)}` VALUES("
        first = True
        for field in row:
            if not first:
                data += ', '
            data += '"' + str(field) + '"'
            first = False


        data += ");\n"
    data += "\n\n"

now = datetime.datetime.now()
filename = str(os.getenv("HOME")) + "/backup_" + now.strftime("%Y-%m-%d_%H:%M") + ".sql"

with open(filename,"w") as FILE:
    FILE.writelines(data)
