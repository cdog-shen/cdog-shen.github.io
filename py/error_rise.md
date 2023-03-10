# 异常处理

当python的解释器遇到编译的问题的时候, 会停止翻译程序码, 并且终止进程

一般程序员都无法考虑到所有情况的错误, 所以就需要异常捕获来收集所有抛出的异常, 从而提高程序的稳定性

## 捕获

当遇到可能出错的代码时, 使用`try`语句来测试程序能否稳定运行

```python
try:
    #这里放置需要测试的代码
    pass
except:
    #这里是出错时执行的代码
    pass

```

指定类型的异常捕获:

```python
try:
    # 需要测试的代码
    pass
except ErrorType1:
    # 错误类型1的对应处理
    pass
except ErrorType2:
    # 错误类型2的对应处理
    pass
except:
    # 其他异常的对应处理
    pass
```

任意类型的异常捕获输出

```python
try:
    pass
except Exception as result:
    print("异常==%s" % result)
    # Exception是针对异常的一个类, 表示任意错误类型
    # result是一个变量名, 用来存放错误信息
```

以上代码结合, 完整的错误捕获:
```python
try: # 尝试执行
    pass
except Error1: # 错误1执行
    pass
except (Error2, Error3) # 错误2,3执行
    pass
except Exception as result: # 其他未知错误
    pass
else: # 无错误执行
    pass
finally: # 都执行的
    pass
```

## 异常的传递性

在调用一个函数的时候, 可能会在函数的内部出现异常, 但函数也有可能含有嵌套, 所以在编写异常处理时就不清楚在什么位置捕获

这时候就可以利用异常的传递性来在主程序中来捕获异常, 这样就可以减少异常捕获的代码量

## 异常的主动抛出

之前提到的`Exception`类就是用来抛出异常的

- 用Exception类先来创建一个对象
- 使用`raise`关键字来抛出

```python
ex = Exception("这里是错误信息") # 创建对象, 错误信息是一个多值元组, 可以用来输出多个值

raise ex # 抛出
```
