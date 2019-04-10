#!/bin/env python3

# a)

from os import system
from os import system as bash
from os import name
from libtvs import *


from sys import argv
import re





######## ESSER V1 BY tvsclass #########
# простая обработка параметров bash-like style

try:
    s1=(argv[1:])[0]
except IndexError:
    error('e01. Need function or option.')
    exit(2)

sall=argv[1:]

count=0
while count < 20:
    try:
       exec("s%d = %s" % (count + 1, repr((argv[1:])[count])))
       count+=1
    except IndexError:
      break


########### end. ##############
###############################

def check(what):
	if bash(what + ' --help >> /dev/null') == 0:
		return True
	else:
		error('can\'t find ' + what)
		exit(2)

def n():
	print('',end='')


def giti(what):
	if s2 == '-t':
		check('git')

		if system('git clone https://github.com/tvsclass/' + s3) == 0:
			check('unzip')
			system('cd ' + s3 + ' && unzip -d ~/.' + s3 + ' ./' + s3 + '.tvs')
			ans=input('install ' + purple(s3) + ' from ' + green('tvs-git') + ' (y/n)? ')
			if not ans == 'y':
				print('Aborted.')
				exit(3)
			if system('cd ' + s3 + ' && find iscript.sh'):
				system('bash ./' + s3 + '/iscript.sh')			
			bash('rm -r ' + s3 + ' -f')


		else:
			error('git error')
			exit(2)


def main():
	if s1 == '-git':
		giti(s2)
	else:
		error('option \'' + s1 + '\' not found')
		exit(2)


ok('tvspkg loaded')
main()
