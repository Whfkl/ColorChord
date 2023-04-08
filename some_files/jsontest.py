import json

# 读取JSON文件中的所有和弦数据
with open('color_full_chords.json', 'r') as f:
    all_chords = json.load(f)

# 初始化一个空列表，用于存储所有function为“D”的和弦
d_chords = []

# 遍历所有和弦数据，将function为“D”的和弦添加到d_chords列表中
for chord in all_chords.values():
    if chord['function'] == '6s':
        d_chords.append(chord)

print(len(d_chords))