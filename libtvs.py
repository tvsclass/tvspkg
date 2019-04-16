#import tvslogo


from os import system as bash



try:
    from termcolor import colored
except:
    print('can\'t find termcolor.')                 
    print('launching installer...')
    print('welcome to tpipinstaller-py3')
    if bash('pip -h >> /dev/null') == 0:
        print('[OK] pip check')
    else:
        print('can\'t find pip. Try to install python-pip package')                                       
        exit(2)
    if bash('sudo pip install termcolor') == 0:
        print('[OK] termcolor installed')
        from termcolor import colored
    elif bash('pip install termcolor') == 0:
        print('[OK] termcolor installed')                   
        from termcolor import colored
    else:
        error('an error occured while installing termcolor. Try to install it yourself')
        exit(2)




import itertools
import time

def red(what):
 a=colored(what,'red')
 return a
def blue(what):
 a=colored(what,'blue')
 return a
def green(what):
 a=colored(what,'green')
 return a
def yellow(what):
 a=colored(what,'yellow')
 return a
def purple(what):
 a=colored(what,'magenta')
 return a

def ok(what):
	print('[' + green('OK') + '] ' + what)
def error(what):
	print('[' + red('ERROR') + '] ' + what)
def loading(what):
	print('[' + blue('***') + '] ' + what)
def wsnloading(what, t, r):
	print('[' + blue('***') + '] ' + what, end='')
	it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
	for x in range(r):
		time.sleep(t)
		print(next(it), end='', flush=True)
	#print('\n'))


def clear():
	system('clear')

