#!/bin/bash

counter=0

while [ $counter -lt 50 ]; do
	((counter+=1))
	
	name=$(nl people.txt | grep -w $counter | awk '{print $2}' | awk -F ',' '{print $1}')
	lastname=$(nl people.txt | grep -w $counter | awk '{print $2}' | awk -F ',' '{print $2}')
	age=$(shuf -i 10-60 -n 1)
	
	mysql -u user -p"$PASSWORD" people -e "INSERT into register values ($counter, '$name', '$lastname', $age)"
	echo "$counter, $name, $lastname, $age successfuly inputed into database"
done
