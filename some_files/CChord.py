import pandas as pd
import copy
import math

class Note:


    def __init__(self, note: str):
        
        self.NOTE = {"A": 1, "D": 2, "G": 3, "C": 4, "F": 5, "Bb": 6, "Eb": 7, "Ab": 8, "Db": 9, "Fsharp": 10, "B": 11,
                     "E": 12}
        self.IND = {1:"A",2:"D",3:"G",4:"C",5:"F",6:"Bb",7:"Eb",8:"Ab",9:"Db",10:"Fsharp",11:"B",12:"E"}
        self.index = self.NOTE[note]
        self.name = note

    def __repr__(self):
        return "Note--'{}'".format(self.name)

    @property
    def angle(self):
        return self.index * 30 - 15
    def get_xy(self):
        angle = self.angle
        #计算angle对应的x,y坐标
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        return (x,y)
    def angle_to(self, other):
        return (self - other) * 30

    # 获取从self到other逆时针方向的纯五跨度数
    def __sub__(self, other) -> int:

        if not isinstance(other, Note):
            raise TypeError("unsupported operand type(s) for -: 'Note' and '{}'".format(type(other).__name__))
        if other.index == self.index:
            return 0
        interval = other.index - self.index
        return interval if interval > 0 else interval + 12

    def __gt__(self, other):
        return self.index > other.index

    def __lt__(self, other):
        return self.index < other.index

    def __eq__(self, other):
        return self.index == other.index

    # 返回逆时针方向第n个音符_Note
    def next(self, n:int=1):
        new_ind = self.index + n
        if n >= 0:
            if new_ind > 12:
                new_ind -= 12
        else:
            if new_ind <= 0:
                new_ind += 12

        return Note(self.IND[new_ind])
    #翻转
    def mir(self):
        step = {"A": 5, "D": 3, "G": 1, "C": -1, "F": -3, "Bb": -5, "Eb": 5, "Ab": 3, "Db": 1, "Fsharp": -1, "B": -3,
                "E": -5}
        return self.next(step[self.name])
class CChord:

    def __init__(self, notes: list, rootnote:Note, typename:str, harmony:float):
        self.notes_str  = notes
        self.harmony = harmony
        self.notes = []
        for i in notes:
            self.notes.append(Note(i))
        self.notes.sort()
        self.rootNote = rootnote
        self.typeName = typename
        

    def __repr__(self):
        return f"Chord(rootNote={self.rootNote}, typeName={self.typeName},notes={self.notes})"
    def contains(self,note:str):
        return int(note in self.notes_str)
    def rotate(self, n: int):
        new_notes = []
        for i in self.notes:
            new_notes.append(i.next(n).name)
        rootnote = self.rootNote.next(n)

        return CChord(new_notes, rootnote, typename=self.typeName, harmony=self.harmony)
    def mir(self):
        new_notes = []
        for i in self.notes:
            new_notes.append(i.mir().name)
        rootnote = self.rootNote

        return  CChord(new_notes,rootnote,self.typeName,harmony=self.harmony)
    def get_vec_angle(self):
        x_sum = 0
        y_sum = 0
        for i in self.notes:
            x,y = i.get_xy()
            x_sum += x
            y_sum += y
        #计算向量（x_sum,y_sum）的角度
        if abs(x_sum)<0.001 and abs(y_sum)<0.001:
            return None
        theta = math.atan2(y_sum, x_sum)*180/math.pi
        if theta < 0:
            theta += 360
        return theta
    def get_theta(self) -> list:
        # 计算和弦内音符对应向量的平均方向,角度值
        thetas = []
        intervals = []
        for i in range(len(self.notes)):
            intervals.append(self.notes[i] - self.notes[(i + 1) % len(self.notes)])
        max_interval = max(intervals)
        for i in range(len(intervals)):
            if (intervals[i] == max_interval):

                n_begin = self.notes[(i + 1) % len(self.notes)]
                theta = 0
                for n in self.notes:
                    theta += 30 * (n_begin - n)
                thetas.append((theta / len(self.notes) + n_begin.angle) % 360)
        if len(thetas) == 1:
            self.temp_theta = thetas[0]
        return thetas
    @staticmethod
    def angle_diff(angle1, angle2):
        diff = angle1 - angle2
        diff = diff % 360
        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360
        return abs(diff)
    def get_theta2(self):
        
        
        # 找到距离最近的角度值
        thetas = self.get_theta()
        angle_vec = self.get_vec_angle()
        if angle_vec is None:
            return thetas
        min_diff = float("inf")
        closest_thetas = []
        for theta in thetas:
            diff = self.angle_diff(theta, angle_vec)
            if diff < min_diff:
                min_diff = diff
        for theta in thetas:
            if self.angle_diff(self.angle_diff(theta,angle_vec), min_diff)<0.01:
                closest_thetas.append(theta)
        
        return closest_thetas

def test():
    t = pd.read_excel("C:\\Users\\31574\\Desktop\\色彩和声\\2.xlsx")
    #逐行读取
    Chords = []
    for i in range(104):
        notes_names = []
        note_names = []
        rootNote = t.loc[i,"根音"]
        typename = t.loc[i,"性质"]
        harmony = t.loc[i,"协和度"]

        if t.loc[i,"Db"] == 1:
            note_names.append("Db")
        if t.loc[i,"Ab"] == 1:
            note_names.append("Ab")
        if t.loc[i,"Eb"] == 1:
            note_names.append("Eb")
        if t.loc[i,"Bb"] == 1:
            note_names.append("Bb")
        if t.loc[i,"F"] == 1:
            note_names.append("F")
        if t.loc[i,"C"] == 1:
            note_names.append("C")
        if t.loc[i,"G"] == 1:
            note_names.append("G")
        if t.loc[i,"D"] == 1:
            note_names.append("D")
        if t.loc[i,"A"] == 1:
            note_names.append("A")
        if t.loc[i,"E"] == 1:
            note_names.append("E")
        if t.loc[i,"B"] == 1:
            note_names.append("B")
        if t.loc[i,"Fsharp"] == 1:
            note_names.append("Fsharp")
        Chords.append(CChord(note_names,Note(rootNote),typename,harmony))
    d = []


    for i in Chords:
        l = [i.rootNote.name+str(i.typeName),i.rootNote.name,i.typeName,i.harmony,i.contains("Db"),i.contains("Ab"),i.contains("Eb"),i.contains("Bb"),i.contains("F"),i.contains("C"),i.contains("G"),i.contains("D"),
                i.contains("A"),i.contains("E"),i.contains("B"),i.contains("Fsharp"),i.get_theta2()]
        d.append(l)
    df = pd.DataFrame(d, columns=['和弦名','根音','性质',"协和度","Db","Ab","Eb","Bb","F","C","G","D","A","E","B","Fsharp","角度"])
    df.to_excel("test_output.xlsx",index=False)


def main(path,n,output,行数:int):
    Chord_of_D_func = []
    AllChords = []
    t = pd.read_excel(path)




    for i in range(行数):
        note_names = []
        rootNote = t.loc[i,"根音"]
        typename = t.loc[i,"性质"]
        harmony = t.loc[i,"协和度"]

        if t.loc[i,"Db"] == 1:
            note_names.append("Db")
        if t.loc[i,"Ab"] == 1:
            note_names.append("Ab")
        if t.loc[i,"Eb"] == 1:
            note_names.append("Eb")
        if t.loc[i,"Bb"] == 1:
            note_names.append("Bb")
        if t.loc[i,"F"] == 1:
            note_names.append("F")
        if t.loc[i,"C"] == 1:
            note_names.append("C")
        if t.loc[i,"G"] == 1:
            note_names.append("G")
        if t.loc[i,"D"] == 1:
            note_names.append("D")
        if t.loc[i,"A"] == 1:
            note_names.append("A")
        if t.loc[i,"E"] == 1:
            note_names.append("E")
        if t.loc[i,"B"] == 1:
            note_names.append("B")
        if t.loc[i,"Fsharp"] == 1:
            note_names.append("Fsharp")
        Chord_of_D_func.append(CChord(note_names,Note(rootNote),typename,harmony))
    Chords1=[]
    for i in Chord_of_D_func:
        Chords1.append(i.rotate(n))
    d = []


    for i in Chords1:
        l = [i.rootNote.name+str(i.typeName),i.rootNote.name,i.typeName,i.harmony,i.contains("Db"),i.contains("Ab"),i.contains("Eb"),i.contains("Bb"),i.contains("F"),i.contains("C"),i.contains("G"),i.contains("D"),
                i.contains("A"),i.contains("E"),i.contains("B"),i.contains("Fsharp"),i.get_theta()[0]]
        d.append(l)
    df = pd.DataFrame(d, columns=['和弦名','根音','性质',"协和度","Db","Ab","Eb","Bb","F","C","G","D","A","E","B","Fsharp","角度"])
    df.to_excel(output,index=False)



