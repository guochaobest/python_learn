# coding:utf-8
##############

formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (
    "I had this thing",
    "That you could type up right",
    "But it didn't sing",
    "So I said goodnight"
))

# 笔记
# 1.%r的原理是：代表的字符串有“‘”就自动提添加"''"
# 2. 格式化输出字符串
# 3.输出中文的话就用%s
