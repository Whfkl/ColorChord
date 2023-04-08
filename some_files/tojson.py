import pandas as pd
import json
import CChord
class Chord(CChord.CChord):
    def __init__(self,notes,rootNote=CChord.Note("C"),typename="a",harmony=0):
        mynotes = []
        #'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#'
        if notes[0] == 1:
            mynotes.append("Db")
        if notes[1] == 1:
            mynotes.append("Ab")
        if notes[2] == 1:
            mynotes.append("Eb")
        if notes[3] == 1:
            mynotes.append("Bb")
        if notes[4] == 1:
            mynotes.append("F")
        if notes[5] == 1:
            mynotes.append("C")
        if notes[6] == 1:
            mynotes.append("G")
        if notes[7] == 1:
            mynotes.append("D")
        if notes[8] == 1:
            mynotes.append("A")
        if notes[9] == 1:
            mynotes.append("E")
        if notes[10] == 1:
            mynotes.append("B")
        if notes[11] == 1:
            mynotes.append("Fsharp")
        if len(mynotes) == 0:
            print(notes)
            raise("无音符")
        super().__init__(mynotes,rootNote,typename,harmony)


# 读取Excel文件
xls = pd.ExcelFile('各功能组和弦数据.xlsx')

# 初始化一个空字典，用于存储所有的和弦数据
all_chords = {}
id = 0
# 遍历每个sheet
for sheet_name in xls.sheet_names:
    # 读取sheet中的数据，仅读取前105行
    df = pd.read_excel(xls, sheet_name)
    success_count = 0

    for index, row in df.iterrows():

        if index == 0:
            pass
        # 将multdirection和symmetry列中为0的数据转换为False
        multdirection = False if row['multdirection'] == 0 else True
        symmetry = False if row['symmetry'] == 0 else True
        # 将和弦内音的字符串转换为列表
        notes = [row[note] for note in ['Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#']]
        # 计算角度值
        angles = Chord(notes).get_theta()
        # 构造和弦字典
        chord_dict = {
            'function': sheet_name,
            'tensionlevel': row['tensionlevel'],
            'chordname': row['chordname'],
            'rootnote': row['rootnote'],
            'quality': row['quality'],
            'harmony': row['harmony'],
            'angles': angles,
            'multdirection': multdirection,
            'symmetry': symmetry,
            'Db': notes[0],
            "Ab": notes[1],
            'Eb': notes[2],
            'Bb': notes[3],
            'F': notes[4],
            'C': notes[5],
            'G': notes[6],
            'D': notes[7],
            'A': notes[8],
            'E': notes[9],
            'B': notes[10],
            'Fsharp': notes[11]
        }

        # 将和弦字典添加到all_chords字典中，以和弦名为key
        chord_name = row['chordname']
        all_chords[id] = chord_dict
                # 记录成功读取的行数
        success_count += 1
        id+=1
        # 如果已经读取了104行，则退出循环
        if success_count == 104:
            print(sheet_name)
            break
# 将all_chords字典写入JSON文件
print(id)
with open('color_full_chords.json', 'w') as f:
    json.dump(all_chords, f, indent=4)