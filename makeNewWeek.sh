#!/bin/bash
today_day=$(date +%u)
day_diff=$(expr 7 - $today_day)
day="d"

if [ -d ThisWeek ]
then
    cd ThisWeek
    LastDate=$(ls -td -- */ | head -n 1)
    cd ..
    mv ThisWeek ./archive/To$LastDate
    mkdir ThisWeek
    cd ThisWeek
    for i in {1..5}
    do 
	dirPath=$(date -v +$(expr $day_diff + $i)$day +%m-%d)
	mkdir $dirPath
	touch $dirPath/jingu_$dirPath.py
   done
else
    mkdir ThisWeek
    cd ThisWeek
    for i in {1..5}
    do 
	dirPath=$(date -v +$(expr $day_diff + $i)$day +%m-%d)
	mkdir $dirPath
	touch $dirPath/jingu_$dirPath.py
    done
fi
