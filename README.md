# Internship
This repository contains my tasks solutions

#Chapter1.py

Create a Car class with pax_count, mass and gear_count attributes, with legal requirements.
c = Car(3, 1600, 5)
it is possible to obtain total mass of a car with passengers using c.total_mass()

#Chapter2.py 

It is a script to manage task list. I've used argparse for this purpose. Run with terminal in saved directory.

Please use YYYY-MM-DD date format for this moment.

examples of use:

$ python chapter2.py add --name Cleaning --deadline 2020-06-01 --description description

it will use hashlib to calculate its hash value and add this task in tasks.csv file. 

$ python chapter2.py list --list_option all  OR $ python chapter2.py list --list_option today

prints a task list from a file, wheter You need todays list, or all tasks list

$ python chapter2.py update --name shopping --deadline 2020-06-15 --description shoes --hash (hash value)

I would recomment to use task list at first to see hash value of a task You want to update

$ python chapter2.py delete --hash (hash value)

It will remove unwanted task from csv file


#Chapter3.py

It will help to find Your sudo password!
