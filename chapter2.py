import argparse
import hashlib
import sys
import datetime

parser = argparse.ArgumentParser(prog="Program options are:", usage='%(prog)s [list, add, update, delete]')
parser.add_argument('option', help='available options')
parser.add_argument('--name', action='store', help="store a task name", required=sys.argv[1] in ['add', 'update'])
parser.add_argument('--deadline', action='store', help='store a task datetime format YYYY-MM-DD',
                    required=sys.argv[1] in ['add', 'update'])
parser.add_argument('--description', action='store', help='store a task description',
                    required=sys.argv[1] in ['add', 'update'])
parser.add_argument('--hash', action='store', help='store a task unique hash value',
                    required=sys.argv[1] in ['delete', 'update'])
parser.add_argument('--list_option', action='store', help='options to print taksks', choices=['all', 'today'],
                    required='list' in sys.argv)
args = parser.parse_args()


def _make_hash(line):
    new_hash = hashlib.md5(line.encode()).hexdigest()
    return new_hash


def add_method(name, deadline, description):
    with open("tasks.csv", "a") as file:
        line_hash = _make_hash(f'{name}{deadline}{description}')
        file.write(f'{(line_hash, name, deadline, description)}\n')


def delete_method(hash_value):
    with open("tasks.csv", "r") as file:
        lines = file.readlines()
        with open("tasks.csv", "w") as file:
            for line in lines:
                if hash_value not in line:
                    file.write(line)


def update_method(name, deadline, description, hash_value):
    with open("tasks.csv", "r") as file:
        lines = file.readlines()
        line_hash = _make_hash(f'{name}{deadline}{description}')
        new_line = f'{(line_hash, name, deadline, description)}\n'
        with open("tasks.csv", "w") as file:
            for line in lines:
                if hash_value in line:
                    line = new_line
                file.write(line)


def list_method(list_option):
    with open("tasks.csv", "r") as file:
        read_lines = file.readlines()
        now = str(datetime.date.today())
        if list_option == "today":
            for line in read_lines:
                if now in line:
                    print(line)
        else:
            print(read_lines)


if args.option == 'list':
    list_method(args.list_option)
elif args.option == 'add':
    add_method(args.name, args.deadline, args.description)
elif args.option == 'delete':
    delete_method(args.hash)
elif args.option == "update":
    update_method(args.name, args.deadline, args.description, args.hash)