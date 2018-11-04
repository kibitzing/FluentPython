#/bin/sh
day=$(date +%A)
pre2=$(date -d '2 day ago' +%m-%d)
pre3=$(date -d '3 day ago' +%m-%d)
pre4=$(date -d '4 day ago' +%m-%d)
pre5=$(date -d '5 day ago' +%m-%d)
pre6=$(date -d '6 day ago' +%m-%d)
day1=$(date -d '1 day' +%m-%d)
day2=$(date -d '2 day' +%m-%d)
day3=$(date -d '3 day' +%m-%d)
day4=$(date -d '4 day' +%m-%d)
day5=$(date -d '5 day' +%m-%d)

folder_name=To$pre6

echo "updating..."

if [ $day == "일요일" ]; then
if [ "$(ls thisweek | grep $day1)" != "$day1" ]; then
	mkdir archive/$folder_name
	mv ThisWeek/* archive/$folder_name

	git add archive/*

	for dayz in $day1 $day2 $day3 $day4 $day5
	do
		mkdir ThisWeek/$dayz
		echo "" > ThisWeek/$dayz/.init
		git add --all ThisWeek/$dayz
	done
	for prez in $pre2 $pre3 $pre4 $pre5 $pre6
	do
		git add --all ThisWeek/$prez/*
	done

	git commit -m "automatically generated"
#	git push origin master
fi
fi


