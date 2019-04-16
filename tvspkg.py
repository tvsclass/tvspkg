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



def make(si3):
	check('make')
	ans=input('Configure ' + purple(si3) + ' with configure.sh? ' + green('[y]yes ') + red('[n]no '))
	if ans != 'y':
		print(red('Aborted.'))
		exit(5)
	if system('cd ' + si3 + ' && find ./configure') != 0:
		if system('cd ' + si3 + ' && find ./autogen.sh >> /dev/null') != 0 or system('cd ' + si3 + ' && find ./bootstrap >> /dev/null') != 0:
			if system('cd ' + si3 + ' && chmod +x ./autogen.sh && ./autogen.sh') != 0:
				if not system('cd ' + si3 + ' && chmod +x ./bootstrap && ./bootstrap'):
					print('Configuring files not found.')
					print('creating...')

					if system('cd ' + si3 + '''
aclocal >> /dev/null
autoheader >> /dev/null
automake --gnu --add-missing --copy --foreign >> /dev/null
autoconf -f -Wall >> /dev/null ''') != 0:
						error('configuring error')
						bash('rm -r ' + si3 + ' -f')
						exit(2)
		if bash('cd ' + si3 + ' && chmod +x ./configure && ./configure') != 0:
			error('configuring error')
			bash('rm -r ' + si3 + ' -f')
			exit(2)


		ans=input('Make and install ' + purple(si3) + ' ? ' + green('[y]yes ') + red('[n]no '))
		if ans != 'y':
			print(red('Aborted.'))
			exit(5)

		if bash('cd' + si3 + ' && make -B && make install DESTDIR=/usr') != 0:
			error('making error')
			bash('rm -r ' + si3 + ' -f')
			exit(2)
		else:
			ok(purple(si3) + ' installed')
			bash('rm -r ' + si3 + ' -f')

	else:
		system('cd ' + si3 + ' && chmod +x ./configure && ./configure')
		ans=input('Make and install ' + purple(si3) + ' ? ' + green('[y]es ') + red('[n]o '))
		if ans != 'y':
			print(red('Aborted.'))
			exit(5)
		if bash('cd ' + si3 + ' && make -B && make install DESTDIR=/usr') != 0:
			error('making error')
			bash('rm -r ' + si3 + ' -f')
			exit(2)
		else:
			ok(purple(si3) + ' installed')
			bash('rm -r ' + si3 + ' -f')



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
		bash('pwd')
	except:
		error('more arguments needed')
		exit(2)


	if s2 == '-t':
		eroot()
		check('git')
		if system('git clone https://github.com/tvsclass/' + s3) == 0:
			check('unzip')
			system('cd ' + s3 + ' && unzip -d ./.' + s3 + ' ./' + s3 + '.tvs')
			ans=input('Install ' + purple(s3) + ' with tvs_PKGengine? ' + green('[y]es ') + red('[n]o '))
			if not ans == 'y':
				print('Aborted.')
				exit(3)
			if system('cd ' + s3 + '/.' + s3 + ' && find iscript.sh') == 0:
				print('reading iscript...')
				print('=========================================================')
				system('cat ./' + s3 + '/.' + s3 + '/iscript.sh')
				print()
				print('=========================================================')
				print()
				ans=input('Run ' + purple(s3) + ' iscript.sh? ' + green('[y]es ') + red('[n]o '))
				if not ans == 'y':
					print('Aborted.')
					system('rm -r ' + s3 + ' -f')
					exit(3)

				if system('bash ./' + s3 + '/.' + s3 + '/iscript.sh') != 0:
					error('iscript failed')
					system('rm -r ' + s3 + ' -f')
					exit(2)
			bash('rm -r ./' + s3 + ' -f')
		else:
			error('git error')
			exit(2)


	elif s2 == '-m':
		print('running ' + 'git clone https://github.com/' + s4 + '/' + s3 + '...')
		if system('git clone https://github.com/' + s4 + '/' + s3) == 0:
			check('make')
			print('running \'make(s3)...\'')
			make(s3)
					
						




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
