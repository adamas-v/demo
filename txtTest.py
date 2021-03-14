# lines = ['1','2','3','\n']
# with open('test.txt','w') as f:
#     f.writelines(lines)

with open('test.txt','r') as f:
    lines = f.readlines()
    print(lines)
    