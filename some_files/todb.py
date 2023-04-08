import sqlite3
import json

# 读取JSON文件中的所有和弦数据
with open('color_full_chords.json', 'r') as f:
    all_chords = json.load(f)

# 连接到 SQLite 数据库
conn = sqlite3.connect('color_full_chords.db')

# 创建一个名为 "chords" 的表格来存储和弦数据
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE color_full_chords
(tensionlevel TEXT, chordname TEXT, rootnote TEXT, quality TEXT,
harmony float, angles TEXT, Db INTEGER, Ab INTEGER, Eb INTEGER,
Bb INTEGER, F INTEGER, C INTEGER, G INTEGER, D INTEGER, A INTEGER,
E INTEGER, B INTEGER, Fsharp INTEGER, multdirection INTEGER,
symmetry INTEGER, function TEXT)
""")
#'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#'
# 将所有和弦数据插入到表格中
for chord in all_chords.values():
    chord_data = (chord['tensionlevel'], chord['chordname'],
                  chord['rootnote'], chord['quality'], float(chord['harmony']),
                  json.dumps(chord['angles']), int(chord['Db']),
                  int(chord['Ab']), int(chord['Eb']), int(chord['Bb']),
                  int(chord['F']), int(chord['C']), int(chord['G']),
                  int(chord['D']), int(chord['A']), int(chord['E']),
                  int(chord['B']), int(chord['Fsharp']), int(chord['multdirection']),
                  int(chord['symmetry']), chord['function'])
    cursor.execute("INSERT INTO color_full_chords VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", chord_data)

# 提交更改并关闭连接
conn.commit()
conn.close()
