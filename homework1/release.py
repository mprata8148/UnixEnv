import sys
import os


def confirm(type: str) -> int:
	# Check if user wants to continue

	choice = input(f"Are you sure you want to {type}? (y/n): ")
	if choice.lower() == 'y':
		return 0
	elif choice.lower() == 'n':
		return 1
	print("Invalid input: exiting")
	return 1

def build_binary():
	if confirm("binary release") == 1:
		print("Exiting...")
		return
	print("Building binary release...")
	pass

def build_source():
	if confirm("source release") == 1:
		print("Exiting...")
		return
	print("Building binary release...")
	pass
	pass

def main(argv: list[str]):
	# Check if second argument exists
	if len(sys.argv) < 2:
		print("Please use '-b' to build binary release or '-s' to build source release.")
		return
	# Check if second argument is '-b' or '-s'
	if sys.argv[1] != '-b' and sys.argv[1] != '-s':
		print("Please use '-b' to build binary release or '-s' to build source release.")
		return

	if sys.argv[1] == '-b':
		build_binary()
	elif sys.argv[1] == '-s':
		build_source()
	else:
		#SHOULD NOT ENTER HERE BUT JUST IN CASE
		print("Please use '-b' to build binary release or '-s' to build source release.")
		return

if __name__ == '__main__':
	main(sys.argv)