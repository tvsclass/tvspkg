#!/bin/env python3

# a)

from os import system
from os import system as bash
from os import name
from libtvs import *


from sys import argv
import re

def eroot():
	if system('[ $USER == \'root\' ]') != 0:
		error('you need root accsess to run this function')
		exit(2)




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


def giti():

	try:
		print('arg1: ' + s2)
		print('arg2: ' + s3)
	except NameError:
		error('more arguments needed')
		exit(2)


	if s2 == '-t':
		eroot()
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


	elif s2 == '-m':
		print('running ' + 'git clone https://github.com/' + s4 + '/' + s3 + '...')
		if system('git clone https://github.com/' + s4 + '/' + s3) == 0:
			check('make')
			if system('cd ' + s3 + ' && find ./configure') != 0:
				if system('cd ' + s3 + ' && find ./autogen.sh >> /dev/null') != 0 or system('cd ' + s3 + ' && find ./bootstrap >> /dev/null') != 0: 
					if system('cd ' + s3 + ' && chmod +x ./autogen.sh && ./autogen.sh') != 0:
						system('cd ' + s3 + ' && chmod +x ./bootstrap && ./bootstrap')
	
				else:
					if system('cd ' + s3 + '''
aclocal
autoheader
automake --gnu --add-missing --copy --foreign
autoconf -f -Wall ''') != 0:
						error('configuring error')
						bash('rm -r ' + s3 + ' -f')
						exit(2)
				if bash('cd ' + s3 + ' && chmod +x ./configure && ./configure') != 0:
					error('configuring error')
					bash('rm -r ' + s3 + ' -f')
					exit(2)
				if bash('cd' + s3 + ' && make -B && make install DESTDIR=/usr') != 0:
					error('making error')
					bash('rm -r ' + s3 + ' -f')
					exit(2)
				else:
					ok(purple(s3) + ' installed')
					bash('rm -r ' + s3 + ' -f')

			else:
				system('cd ' + s3 + ' && chmod +x ./configure && ./configure')	
				if bash('cd ' + s3 + ' && make -B && make install DESTDIR=/usr') != 0:
					error('making error')
					bash('rm -r ' + s3 + ' -f')
					exit(2)
				else:
					ok(purple(s3) + ' installed')
					bash('rm -r ' + s3 + ' -f')
					
					
						




	else:
		error('wrong parameter')


def main():
	if s1 == '-git':
		giti()
	else:
		error('option \'' + s1 + '\' not found')
		exit(2)


ok('tvspkg loaded')
main()
