##### 目前实现了给定一组音符，计算和弦的角度和模长的功能，以及给定两个和弦，计算和弦的色彩变化，新鲜度，和紧张度变化的功能
##使用方法

首先import colorChord
~~~ python
from colorChord import *
~~~

#####初始化和弦
~~~python
a = Chord([cNote.A, cNote.Db, cNote.F])
b = Chord([cNote.F, cNote.A, cNote.C, cNote.Eb,cNote.G], name ="myfirstchord")
~~~
可以看到Chord类初始化需要一个列表参数，列表中为枚举类cNote,按任意顺序通过列表输入音符；name为可选参数，对计算过程无影响

#####计算和弦的角度和模长
~~~python
print(a.get_theta())
print(b.get_harmony)
~~~

#####计算两个和弦的色彩变化，紧张度变化和新鲜度
~~~python
print(Chord.get_color_change色彩变化(a,b))
print(Chord.get_tension_change紧张度变化(a,b))
print(Chord.get_fressness新鲜度(a,b))
~~~
这三个函数名含有中文，可能会产生乱码

##注意
目前没有考虑到紧张度VIII级以上的情况，计算这类和弦可能会给出错误的结果

##更新记录
### 2023.3.30
1. 修复了两个增和弦新鲜度计算报错的问题
2. 为cNote枚举类增加了get_cNote_by_name(name:str)静态方法，通过这个方法可以获取cNote对象
~~~Python
get_cNote_by_name("F#")
~~~
3. 对于VIII级紧张度以上和弦计算时不再报错，直接返回1.77777