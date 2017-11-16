# 笨方法学Python（第四版）习题5：更多的变量和打印
# -- coding:utf-8 --
# 单引号 双引号 三引号的区别
# 格式化输出 %r 的用法 %d %s %f


my_name='Zed A. Shaw'
my_age=35
my_height=74
my_weight=180
my_eyes='Blue'
my_teeth='white'
my_hair='Brown'
print("Let's talk about %s."%my_name)
print("He's %d inches tall."%my_height)
print("He's %.2f cm tall."%(2.54*my_height))
print("He's %d pounds heavy."%my_weight)
print("He's %.4f kg heavy."%(0.45359237*my_weight))
print("Actually that's too heavy.")
print("He's got %s eyes and %s hair."%(my_eyes,my_hair))
print("He's got %r eyes and %r hair."%(my_eyes,my_hair))
print("His teeth are usually %s depending on the coffee."%my_teeth)
print("His teeth are usually %r depending on the coffee."%my_teeth)
print("If i add %d,%d,and %d I get %d."%(my_age,my_height,my_weight,my_age+my_height+my_weight))
print("If i add %r,%r,and %r I get %r."%(my_age,my_height,my_weight,my_age+my_height+my_weight))