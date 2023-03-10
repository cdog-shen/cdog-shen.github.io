# 设计模式

## 单例设计模式

- 设计模式

    针对某一特定问题的成熟解决方案

    可以起到代码重用, 易读, 提高可靠性等优点

- 单例模式

    在系统中创建`类`, 用这个类创建`唯一的实例`(每次`类名()`返回的对象内存地址相同)

## __new__方法

用类来创建方法时，首先会调用`__new__`方法给对象新建内存空间

`__new__`时object类中的内置方法，主要有两个作用

- 为对象分配内存空间
- **返回(return)**对象的内存地址来给其他方法引用(self)

    python的解释器获得对象的引用以后，将会把其当作第一个参数传递给`__init__`方法

在进行单例模式的编写的时候，防止创建多个不同的方法，需要重写`__new__`方法

重写`__new__`方法的格式非常固定

必须以这行代码结尾

```python
return super().__new__(cls) # 注意：__new__是一个静态方法，使用时必须传递cls参数
```

否则解释器就会失去该对象的内存地址引用，将无法调用`__init__`方法

### 单例的__new__

想要将`__new__`改成单例模式特有的`__new__`就得对其进行更改

- 因为单例模式只允许存在一个实例，所以在创建新实例的时候进行一次判断即可：

    如果实例数不为0，则取消新建实例，直接返回原有实例的内存地址

    如果实例数为0，新建实例，并返回内存地址

    ```python
    class AClass(object):
        # 定义一个内存地址为类属性，用来保存引用
        addr = None
        def __new__(cls, *arg, **kwargs):
            if cls.addr is None:
                addr = super().__new__(cls) # 调用父类__new__新建对象
            return cls.addr # 调用类属性来返回内存引用
    ```

### 单例的__init__

- 单例的初始化也要保证只执行一次，否侧对象属性总会被清零

    ```python
    class AClass(object):
        # 定义一个内存地址为类属性，用来保存引用
        addr = None
        #定义一个类属性来标记初始化状态
        init_flag = False
        def __new__(cls, *arg, **kwargs):
            if cls.addr is None:
                cls.addr = super().__new__(cls) # 调用父类__new__新建对象
            return cls.addr # 调用类属性来返回内存引用

        def __init__(self):
            if AClass.init_flag:
                print("已初始化")
            else:
                print("初始化完成")
                AClass.init_flag = True
    ```
