poem = '''
Programming is fun
When the work is done
if you wanna make your work also fun:
      use Python!
I want to do th right things,but i push myself
too hard,and it does not work,because things should be done 
nicely.Be a quite girl.Do not push yourself too hard,be slowly
it is a good thing to be slow.
...........................
'''
f = open('poem.txt','w')
f.write(poem)
f.close
f = open('poem.txt')
while True:
    line=f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()