from colorChord import *

#初始化和弦
a = Chord([cNote.A, cNote.Db, cNote.F])
b = Chord([cNote.F, cNote.A, cNote.C, cNote.Eb,cNote.G], name ="myfirstchord")
#角度，get_theta()返回包含所有可能角度的列表
a.get_theta()
#模长
a.get_harmony()

print(Chord.get_fressness新鲜度(a,a))