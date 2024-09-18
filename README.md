# 题目二代码说明

## 运行环境
python 3.9.17

## 运行方式
```sh
python unification.py
```

## 输入数据
代码主函数如下所示：
```python
if __name__ == '__main__':
	fol1 = FOL('Knows', ['John', 'x'])
	fol2 = FOL('Knows', ['y', FOL('Mother', ['y'])])
	
	result = unify(fol1, fol2)
	print_result(result)
```
在主函数中可以对<b>fol1</b>和<b>fol2</b>进行赋值。在代码中，使用<b>FOL</b>类表示一条FOL语句。为创建一个<b>FOL</b>类，可以使用代码：
```python
fol = FOL(operation, argument)
```
其中，operation为字符串类型，表示FOL语句的谓词或函词；argument是一个列表，表示FOL语句的变量。列表中元素可以为变量variable，常量constant，或FOL类，以实现FOL语句的嵌套。

在上面代码中，<b>fol1</b>表示$ Konws(John, x) $，<b>fol2</b>表示$ Konws(y,Mother(y)) $。

## 输出数据
代码的输出只有一行，表示两条FOL语句的合一置换。对于代码中给出的数据，输出为$ \{y/John,x/Know(z,Mother(John))\} $。

可以通过改变<b>fol1</b>和<b>fol2</b>来得到指定FOL语句的合一置换。

## 备注
本代码将只含有小写字母的字符串视为变量，将含有大写字母的字符串视为常量。
