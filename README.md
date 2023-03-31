## 色彩和声理论
https://www.bilibili.com/read/cv21690345
UP主：色彩和声-小田田
https://space.bilibili.com/24728563
##### 目前实现了给定一组音符，计算和弦的角度和模长的功能，以及给定两个和弦，计算和弦的色彩变化，新鲜度，和紧张度变化的功能
## 使用方法

首先import colorChord
~~~ python
from colorChord import *
~~~
### cNote类
这是一个枚举类，定义如下：
~~~Python
class cNote(Enum):
    A = 1
    D = 2
    G = 3
    C = 4
    F = 5
    Bb = 6
    Eb = 7
    Ab = 8
    Db = 9
    Fsharp = 10
    B = 11
    E = 12
~~~
**可见数字的编号遵循五度循环圈**


该类有一个get_cNote_by_name(name:str)函数:可以通过音符名称字符串获取cNote枚举对象
~~~python
a = cNote.C
b = cNote.E
c = cNote.get_cNote_by_name("G")
#通过上面三个音来创建和弦Chord类
Cmaj = Chord([a,b,c],name = "myCmajor")
~~~
### _Note类
#### 初始化
该类不允许其它文件使用，仅用于colorChord.py内部
~~~Python
    a = _Note(cNote.A)
    b = _Note.init_by_note_name("A")
~~~
#### 属性
self.index 音符在五度圈上的编号，A=1,D=2,G=3...
self.name 音符的名称str
#### 方法
##### self.next(self,n=1)
返回逆时针方向第n个音符_Note对象
~~~python
    a = _Note.init_by_note_name("A")
    print(a.next(1))#_Note--'D'
    print(a.next(-1))#_Note--'E'
~~~
##### 比较运算符>,< ,==
进行index的比较，
##### 重载-号
返回在五度循环圈上，从a到b的纯五跨度数（每隔30°为一个纯五跨度数）
~~~python
    a = _Note.init_by_note_name("A")
    b = a.next(5)
    print(a-b)#结果是5
~~~
### Chord类
#### 创建Chord实例
~~~python
a = Chord([cNote.A, cNote.Db, cNote.F])#用cNote初始化
b = Chord([cNote.F, cNote.A, cNote.C, cNote.Eb,cNote.G], name ="myfirstchord")
c = Chord.initBy_Note([_Note(cNote.A),_Note(cNote.Fsharp)],name = "test")#用_Note列表初始化
d = Chord.init_by_note_name_str(["A","B","G"])#用音符名称初始化
~~~
可以看到Chord类初始化需要一个列表参数，列表中为枚举类cNote,按任意顺序通过列表输入音符；name为可选参数，对计算过程无影响
#### 一些可能用到的方法
##### self.get_fifth_span()
获取和弦的纯五跨度数，和弦的纯五跨度数定义参见专栏
##### self.rotate(n:int,new_name=None)
返回一个新的Chord实例，把self的所有音符在五度圈上逆时针旋转n*30°
#### 计算和弦的角度和模长
~~~python
print(a.get_theta())
print(b.get_harmony)
~~~

#### 计算两个和弦的色彩变化，紧张度变化和新鲜度
~~~python
print(Chord.get_color_change色彩变化(a,b))
print(Chord.get_tension_change紧张度变化(a,b))
print(Chord.get_fressness新鲜度(a,b))
~~~
这三个函数名含有中文，可能会产生乱码

## 注意
目前没有考虑到紧张度VIII级以上的情况，计算这类和弦可能会给出错误的结果

## 更新记录
### 2023.3.30
1. 修复了两个增和弦新鲜度计算报错的问题
2. 为cNote枚举类增加了get_cNote_by_name(name:str)静态方法，通过这个方法可以获取cNote对象
~~~Python
get_cNote_by_name("F#")
~~~
3. 对于VIII级紧张度以上和弦计算时不再报错，直接返回1.77777
### 2023.3.31
1. 为Chord类新增两种初始化方式
~~~python
    c = Chord.initBy_Note([_Note(cNote.A)])
    d = Chord.init_by_note_name_str(["A","B","G"])
~~~
2. 为Chord类新增一个方法 *self.rotate(n:int,new_name=None)*
   
   返回一个新的Chord实例，把self的所有音符在五度圈上逆时针旋转n*30°
3. 为_Note新增一种初始化方式
~~~Python
    b = _Note.init_by_note_name("A")
~~~
4. 修复了cNote类get_cNote_by_name(name:str)方法的一个bug