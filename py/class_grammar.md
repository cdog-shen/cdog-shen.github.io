# 类的语法

## 调用

python中有很多内置类, 在`import`之后可以直接进行调用

调用语法: `类名.方法名(实参)`

- 查看对象的方法

    在我们之前学过的`函数, 类, 变量`都是对象

    想要查看某个对象的所有方法

    可以利用dir函数

    dir(标识符/关键字)

    其输出就是以`__`框起的*内置*方法或者*属性*名称

    比如:

    `__new__`       创建对象时会自动调用(一般不用)

    `__init__`      对象初始化时自动调用(用于定义属性)

    `__del__`       调用后变量被销毁(用于释放内存空间)

    `__str__`       返回对象描述信息(`print(item.__str__)`)

### 对象的生命周期

对象还存在时，可以对变量的属性，方法进行访问

调用`__del__`方法后，会先执行自己定义的方法语句，然后将实例化的变量将从内存中删除

未经定义的`__del__`方法会直接删除对象

删除后对象就不复存在，无法访问

---

## 定义一个简单类(只含普通方法)

语法:

```python
class ClassName:

    def function_name_1(self,[args]):  #第一个参数必须是self(其代表了自身对象)
        pass

    def function_name_1(self,[args]):
        pass

```

调用时需要将类实例化

```python
item_name = ClassName()
item_name.functiong([args])
```

程序员在调用方法时不需要对`self`进行声明

而在类的**内部**对该类的**其他**方法或属性进行调用的时候就需要用到`self`

### 给对象增加类外属性

`item_name.attribute_name = "data"`

这是一种可以但不推荐的方法, 因为属性应该被封装在`类`的内部, 属性在外部时, 可能会因为解释器执行问题而报错

### 给类增加类内属性

增加类属性就不得不提到一个方法：`__init__`也是一个内置方法

众所周知，init代表initialize, 初始化，而在python中，初始化函数就是专门用来定义类中的属性的方法

```python
class AGuy:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("正在初始化 %s" %(self.name))
    def P(self):
        print("我的名字是 %s" %(self.name))
        print("年龄: %d"%(self.age))


tim = AGuy(name="Tim",age=18)
tim.P()
```

```txt
正在初始化 Tim
我的名字是 Tim
年龄: 18
```

可以看出，有了init方法的类在实例化的时候就需要对类中的形参进行赋值了（否则报错）

而且init方法内的语句会在实例化的时候自动执行

*属性可以看作是类内的全局变量，类方法之间想要交换数据，就必须通过属性，普通的变量定义是不能跨方法读取的**
### 对象的描述

确切的讲是类的描述

用到`__str__`方法

未经定义的str方法会`return`一个字符串值：`<method-wrapper '__str__' of 类名 object at 16进制内存地址>`

定义后会执行你自己的定义语句，但一定要有一个`return`的字符串

### 对象私有属性和方法

想要定义一个对象的私有属性和方法很简单, 在想要定义的属性名和方法名之前添加`__`

**私有概念: 仅仅该`对象个人`能够访问, 其他对象不予访问权限**

## 继承

面向对象有三大特性: 封装, 继承, 多态

建立一个对象是继承的话, 从另一个对象获得该对象的能力, 就是继承

开始继承操作后, 根据继承的方向将被继承方和继承方, 被继承方叫`父类`, 继承方叫`子类`(**子类**又可称为**派生类**, **父类**又可称为**基类**)

继承后: 子类将拥有父类的**全部方法和属性**

语法:

```python
# 继承在定义类时开始

class SonClass(FatherClass1,FatherClass2):

    pass

```

- 一个子类可以同时继承多个父类

    **注意: 在父类之间有`相同方法名或者属性名`时要避免使用多继承(易产生混淆)**

注意：如果一个类的父类不全是`object`，在重写`__init__`的时候要先`super()`一下父类`__init__`确保能正常执行

### 改写

当然, 继承后也有可能父类方法无法满足子类的方法

这时候, 为了更新或者更改子类的方法, 我们需要在子类中对父类方法进行**重写**

如何重写, 其实很简单

只需要把功能不适用的方法重新写一遍即可, 这样子类在引用的时候就不会引用父类的方法, 而是会直接利用自身的重写方法对父类进行覆盖(这对父类不会造成任何影响, 仅仅会更改子类)

若想在重写后还重新调用父类的方法

利用`super().父类方法`的格式来调用原本的父类方法

### 私有方法的继承

记不记得私有方法的定义: 只能被该对象所访问

所以, 继承后的子类是不能直接访问父类的私有属性和私有方法

***但是, 可以通过父类的`公共方法`来间接访问其私有属性和类***

---

## 方法执行顺寻

在python中, 类有个方法叫, `__mro__`方法, 这个方法的输出是一个元组

里面是类的搜索序列, 按照先后顺序, 找到即执行

如:

```python
#上方省略数行代码
class SonClass(FatherClass2,FatherClass1):

    pass

son = SonClass()
son.__mro__()
```

```python
#返回值
(<class '__mian__.SonClass'>, <class '__mian__.FatherClass2'>, <class '__mian__.FatherClass1'>, <class 'object'>)
```

可以看出, 搜索顺序是: 自类 -> 父类元组[0] -> 父类元组[1] -> 主基类object

---

## 新式类 & 经典类

python3中直接创建类, 会自动继承`object`类 -> 新式类

python2中直接创建类, 啥都不会继承 -> 经典类

这会影响到多继承的方法搜索顺序

如果想向下兼容程序

就记得在创建类时手动继承`object`类

```python
class NewClass(object):
    pass
```

---

## 多态

多态 多个子类对象调用一个父类对象而产生不同的执行效果

- 多态可以增加代码的灵活度
- 以继承和重写父方法为前提
- 是调用方法的技巧, 不会影响类的内部设计
