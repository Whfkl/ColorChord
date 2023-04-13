# 简介
color_full_chords.json是一个包含了几乎所有和弦的JSON文件，注意和弦名 chordname有重复，因为一个和弦可能有多个功能，它们将被分别保存。

color_full_chords.db 是一个相应的数据库

音符字段或属性均为int数据，1表示该和弦含有这个音，0表示和弦不含有这个音
## 1. color_full_chords.json
~~~json
{
    "0": {
        "function": "6s",
        "tensionlevel": "Ia",
        "chordname": "A maj",
        "rootnote": "A",
        "quality": "maj",
        "harmony": 10.0,
        "angles": [
            325.0
        ],
        "multdirection": false,
        "symmetry": false,
        "Db": 1,
        "Ab": 0,
        "Eb": 0,
        "Bb": 0,
        "F": 0,
        "C": 0,
        "G": 0,
        "D": 0,
        "A": 1,
        "E": 1,
        "B": 0,
        "Fsharp": 0
    },}
~~~
    function: 和弦功能组，这里的功能组是在C中心调下的。
    tensionlevel：紧张度级别
    rootnote:和弦根音
    harmony：协和度
    angles: 角度的列表（角度可能有多个），使用角度制
    multdirection: 是否有多个方向
    symmetry: 是否在五度圈上对称


## 2. color_full_chords2.json
相比color_full_chords.json,这个文件中存储了一些事实上不存在的功能组，比如7D，8D，9D，10D，7s, 8s,9s,10s，这样的设计是为了获得其他调中心下的和弦功能。比如7D组，在C中心调中不存在，但这些和弦是F中心调的6D组。也就是说：如果你想获得其他调中心的和弦数据，只需要改动function这一个属性即可。

## 3. color_full_chords.db 数据库定义：
~~~
CREATE TABLE color_full_chords
(
tensionlevel TEXT,  --紧张度
chordname TEXT,  -- 和弦名
rootnote TEXT,   -- 根音
quality TEXT,    -- 性质，如maj
harmony float,  -- 协和度
angles TEXT,     -- 角度 如 '[55.0]'
Db INTEGER, 
Ab INTEGER, 
Eb INTEGER,
Bb INTEGER, 
F INTEGER, 
C INTEGER, 
G INTEGER, 
D INTEGER, 
A INTEGER,
E INTEGER, 
B INTEGER, 
Fsharp INTEGER, 
multdirection INTEGER,  -- 是否有多个方向
symmetry INTEGER,       -- 是否在五度圈上对称
function TEXT           -- 所属功能组
)
~~~
