import sys
def putmovie(the_list,fn=sys.stdout):
    for inneritem in the_list:
        if isinstance(inneritem,list):
            putmovie(inneritem)
        else:print(inneritem)

try:
    with open('test1.txt','w') as file_data:
        print("测试下with的用法哦哦哦哦哦哦！",file=file_data)
except IOError as err:
    print('file error'+str(err))
finally:
    if 'file_data' in locals():
        print('finnally close the file')
        file_data.close()