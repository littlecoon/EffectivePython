编写高质量python代码的方法8：不要使用含有两个以上表达式的列表推导
除了基本的用法之外,列表推导也支持多重循环。例如,要把矩阵（也就是二维列表）简化成一维列表,使原来的每个单元格都成为新列表中的普通元素。这个功能采用包含两个for表达式的列表推导即可实现,这些for表达式会按照从左至右的顺序来评估。

上面这个例子简单易易懂,这就是多重循环的合理用法。还有一种包含多重循环的合理用法,那就是根据输入列表来创建有两层深度的新列表。例如,我们要对二维矩阵的每个单元格取平方,然后用这些平方值构建新的矩阵。由于要多使用一对中括号,所以实现该功能的代码会经上例稍微复杂一点,但依然不难理解。

如果表达式里还有一层循环,那么列表推导就会变得很长,这时必须把它分成多行来写,才能看得清楚一些

可以看出此时列表推导并不比普通写法更加简单,如果用普通写法的话：
#4

列表推导也支持多个if条件。处在同一循环级别中的多项条件,彼此之间默认形成and表达式。例如,要从数字列表中选出大于4的偶数,那么下面这两种列表推导方式是等效的。
#5

每一级循环的for表达式后面都可以指定条件。例如,要从原矩阵中把那些本身能为3所整除,且其所在行的各元素之和又大于等于10的单元格挑出来。我们只需编写很简短的代码,就可用列表推导来实现此功能,但是,这样的代码非常难懂。

