# coding:utf-8
##############
import keyword

# 字符串和文本

x = "There are %d types of documents." % 10
binary = "binary"
do_not = "don't"
y = " Those who know %s and those who %s"% (binary,do_not)


print(x)
print("I said: %r" % x)
# %r 就是原字符串包括引号即原始数据，可以用来调试

print("I also said:'%s'." % y)


hilarious = False;
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)
print("Isn't that joke so funny?! %r" %hilarious)

# 1. 说明了%r会显示原始数据

w = "This is the left side of...."
e = "a string with aright side"

print(w+e)