# 结构体

结构体类, 可以想象成一个没有方法只有属性的类

## 定义方法

```cpp
[typedef] struct type_name {
member_type1 member_name1;
member_type2 member_name2;
member_type3 member_name3;
...
...
} object_name_temps;
```

type_name           --- 结构体名

member_type         --- 属性类型

member_name         --- 属性名

object_name_temps   --- 结构体变量名

## 访问结构体

结构体创建完成后相当于创建安好了一个结构体类, 想要对一个结构体进行初始化需要先将其进行实体化

```cpp
// typedef后的
type_name object_name1, object_name2;

// 无typedef的
struct type_name object_name1, object_name2;
```

实体化后, 需要用到成员访问符`.`

```cpp
object_name1.member_name1 = [data];
...
```

## 指向结构的指针

创建结构体后, 就相当于创建了一种新的数据结构, 当然也可以创建这种类型的指针

```cpp
// typedef后的
type_name* object_name1ptr, object_name2ptr;

// 无typedef的
struct type_name* object_name1ptr, object_name2ptr;
```

现在，您可以在上述定义的指针变量中存储结构变量的地址。为了查找结构变量的地址，请把` & `运算符放在结构名称的前面，如下所示:

```cpp
object_name1ptr = &object_name1;
```

为了使用指向该结构的指针访问结构的成员，您必须使用`->`运算符，如下所示:

```cpp
object_name1ptr -> member_name1;
```

## typedef 关键字

您可以使用` typedef `关键字来定义非结构类型, 如下所示:

```cpp
typedef long int *pint32;

pint32 x, y, z;
```

x, y, z 都是指向长整型 long int 的指针
