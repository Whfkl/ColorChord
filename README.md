# color_full_chords.json
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
    function: 和弦功能组
    tensionlevel：紧张度级别
    rootnote:和弦根音
    harmony：协和度
    angles: 角度的列表（角度可能有多个），使用角度制
    multdirection: 是否有多个方向
    symmetry: 是否在五度圈上对称
    
# color_full_chords.db 数据库定义：
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
