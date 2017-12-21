import sys
def putmovie(the_list,fn=sys.stdout):
    for inneritem in the_list:
        if isinstance(inneritem,list):
            putmovie(inneritem)
        else:print(inneritem)

