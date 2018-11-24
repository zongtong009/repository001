# DocStrings 文档字符串使用惯例：
# 它的首行简述函数功能，第二行空行，第三行为函数的具体描述,
    且只能用''' '''三括号表达。
def printMax(x,y):
    '''打印两个数中的最大值。
    
    两个值必须都是整数。'''
    x=int(x)
    y=int(y)
    if x>y:
        print(x,'最大')
    else:
        print(y,'最大')
        
printMax(3,5)
print (printMax.__doc__) # 调用 doc

###################################深浅拷贝##################################
在 Python 中，对象赋值实际上是对象的引用。当创建一个对象，然后把它赋给另一个变量的时候，
	Python 并没有拷贝这个对象，而只是拷贝了这个对象的引用，我们称之为浅拷贝。
在 Python 中，为了使当进行赋值操作时，两个变量互补影响，
	可以使用 copy 模块中的 deepcopy 方法，称之为深拷贝。
当 list 类型的对象进行 append() 函数操作时，实际上追加的是该对象的引用。
	使用id() 函数返回对象的唯一标识，可以类比成该对象在内存中的地址。
>>>alist = []
>>> num = [2]
>>> alist.append( num )
>>> id( num ) == id( alist[0] )
# 结果为True
如上例所示，当 num 发生变化时(前提是 id(num) 不发生变化），alist 的内容随之会发生变化。往往会带来意想不到的后果，想避免这种情况，可以采用深拷贝解决：
alist.append( copy.deepcopy( num ) )

jupyter notebook哈-希-表   'sha1:1c3090730423:77b303ef833db8048a6a938388a2481d42d9e2dd'
    