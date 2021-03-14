import argparse
##首先定义两个不同的函数
def a(x):
    return x 

def b(x):
    return -x

parser = argparse.ArgumentParser()#获得一个主解释器
subparser =  parser.add_subparsers(dest = 'command')#获取子命令解释器

parser_a = subparser.add_parser('commanda')#在子命令解释器添加子命令a
parser_a.add_argument('-x',type = int)
parser_a.set_defaults(func = a)

parser_b = subparser.add_parser('commandb')#在子命令解释器添加子命令b
parser_b.add_argument('-x',type = int)
parser_b.set_defaults(func = b)



if __name__ == '__main__':
    arg = parser.parse_args()#解析主解释器即可

    print(arg.func(22))    #启用函数

	
