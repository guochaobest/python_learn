# coding:utf-8
##############

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\ cat."

# \t 是输出8个空格
# \n换行
print(tabby_cat)
print(persian_cat)
print(backslash_cat)

fat_cat = """"
I will do a alist:
\t* cat food
\t* fishes
\t* catnip\n\t* Grass
"""

print(fat_cat)

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i)