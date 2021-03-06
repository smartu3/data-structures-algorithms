# python的数据结构与算法

## 抽象类型和Python类  
**抽象数据类型**  
抽象数据类型（Abstract Data Type,ADT）的基本思想是抽象，或者说是*数据抽象*,抽象定义与数据表示和数据操作的实现分离。  
**接口与实现**  
*接口*可以用来说明某一程序部分的可用功能，并不限制功能的实现方法。  
**过程抽象和数据抽象**  
围绕一类数据对象构造的模块为*数据抽象*，与函数定义实现为*过程抽象*。  
**类型**  
*类型*是程序设计的基本概念，每个类型包含一集合法的数据对象，并规定了对这些对象的合法操作。  
**内置类型**  
每种语言都提供了一组*内置数据类型*，并为每个内置数据类型提供了一批操作。  
**表示**  
在编程中使用一种对象时，只需考虑如何使用，不需要去关注和触及对象的*内部*表示。  
**不变类型和可变类型**  
类型的对象在创建之后不变，为*不变数据类型*，若创建后对象内部状态可以发生改变，为*可变类型*。  
**类，类定义和类对象**  
*class定义*（类定义）可用来实现抽象数据类型  
后面的概念就不接下去打了，有点费时  

## 数据类型的三类操作  
1）构造操作：操作已知信息；  
2）解析操作：从一个对象取得有用信息；  
3）变动操作：修改被操作对象的内部状态  

## 定义一个数据类型时应当考虑的问题  
定义一个抽象数据类型，目的是要定义一类计算对象，使其具有某些特定功能，可以在计算中使用。  
## 类作用域和函数作用域的差异  
函数定义：局部名字的作用域自动延伸到内部嵌套的作用域。  
类定义，作用域并不自动延伸，如果需要在类中的函数定义里引用这个类的属性，采用基于类名的属性引用方式  