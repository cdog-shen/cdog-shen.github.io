# pygame 游戏模块

## 绘制窗口

### 初始化和退出

- 在使用pygame来制作游戏的时候要首先使用`pygame.init()`导入并初始化所有相关模块

    |        |
    | :----: |
    | init() |
    |  code  |
    | quit() |

    所有代码要保持这样的结构

### 坐标系

- 在python中，几乎所有的坐标系起始点都在对象的左上角(数学运算除外)

    X沿着水平方向向右增加
    Y沿着竖直方向向下增加

### 矩形区域

```python
pygame.Rect(x, y, width, height) -> Rect
```

专门用来生成矩形的类

共有：`x` `y` `left` `top` `bottom` `right` `center` `centerx` `centery` `size` `width` `height`几个属性

### 生成游戏主窗口

- 专门用来创建、管理游戏窗口 `pygame.display.方法名`

    |方法|说明|
    |:-|:-|
    |set_mode()|初始化游戏显示窗口|
    |update()|刷新屏幕显示|

    `set_mode(resolution=(0, 0), flags=0, depth=0) -> Surface`

    resolution是窗口大小，默认等于屏幕

    flags参数指定的屏幕附加项，默认不用传递

    depth颜色位数

    其返回值可以暂时理解为游戏的界面，其游戏元素都要被绘制到界面上

    `set_mode()`的返回值必须被保存到变量中

## 绘制图像

图像数据是保存在磁盘中的, 想要运行, 就首先需要加载到磁盘中(背景图像也是如此, 位置始终为(0,0))

- 加载

    `pygame.image.load(file_path)`方法来加载图像

- 绘制

    `pygame.Surface.blit(图像对象, 位置坐标)`来绘制图像到相应位置

- 更新游戏界面

    `pygame.display.update()`

- 获取图像大小

    调用image实例的`get_rect()`方法可以返回一个`pygame.Rect(0, 0, 图像宽, 图像高)`的对象

## 游戏循环

游戏循环保证游戏不会立即终止, 还承担了检测交互 刷新屏幕 以及其他的数据处理 通常由一个有条件判断的无限循环构成

## 游戏时钟

- `pygame.time.Clock`类可以非常方便的设置屏幕刷新率

    初始化以后建立一个时钟对象 `cl = pygame.time.Clock`

    在游戏循环中调用`cl.tick(帧率)`方法

## 事件监听

- 事件 event

    实践就是用户的操作

- 监听 get

    接收事件, 对用户的动作进行捕获

代码实现

利用`pygame.event.get()`即可获得用户的所有操作, 其返回值是一个列表

利用遍历来获取列表中的值，利用type关键字来获取其特征整数来对应其事件大类(键盘输入，鼠标移动)

- 查看实践特征码:

    `print(pygame.QUIT)`查看关闭按键的特征码

## 精灵

利用精灵类来创建一个对象，来建立一个游戏元素

- 精灵类`pygame.sprite.Sprite`

    两个重要属性：`image=图像数据`，`rect=记录在屏幕的位置`

    两个重要方法：`update((0,0))`更新图像位置，`kill()`从所有组删除

- 精灵组`pygame.sprite.Group`

    四个方法：`__init__(self, *sprite)`, `add(*sprite)`添加精灵, `sprites()->list`返回精灵列表, `update(*args)`组内所有精灵调用update, `draw(Surface)`将所有精灵的image绘制到surface上各自的rect位置

- 针对精灵的面向对象游戏程序结构：

    初始化：创建精灵，精灵组

    游戏循环内：精灵组update，精灵组draw，刷新界面