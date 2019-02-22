#!/bin/bash

case $USER in

root)
echo
;;

*)
ошибка: недостаточно прав для запуска itvsgui
exit 2
;;

esac


echo 'установить tvspkg (y/n)?'

read bAn

case $bAn in

y)
echo
;;

*)
echo операция отменена пользавателем
exit 0
;;

echo iscript не найден. Автоматическая устанвка...

cp tvspkg /usr/bin/

chmod +x /usr/bin/tvspkg

echo tvspkg установлен
