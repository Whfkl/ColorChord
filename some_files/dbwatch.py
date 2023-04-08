import sqlite3

# 连接数据库
conn = sqlite3.connect("color_full_chords.db")
c = conn.cursor()


c.execute("SELECT * FROM color_full_chords where chordname='C maj'")
rows = c.fetchall()

# 输出查询结果
print(rows)

# 关闭数据库连接
conn.close()
