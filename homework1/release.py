import sys
import os
import subprocess
import re
def confirm(type: str) -> int:
	# Check if user wants to continue

	choice = input(f"Are you sure you want to {type}? (y/n): ")
	if choice.lower() == 'y':
		return 0
	elif choice.lower() == 'n':
		return 1
	print("Invalid input: exiting")
	return 1

def get_hostname() -> str:
	# Get hostname
	#Safe Characters allowed for name mainly to prevent // or \
	SAFE_NAME = re.compile(r"^[A-Za-z0-9._-]+$")

	hostname = input("Enter hostname: ").split()[0]
	if not hostname:
		raise ValueError("Hostname cannot be empty")
	if not SAFE_NAME.match(hostname):
		raise ValueError("Hostname contains unsafe characters")
	return str(hostname)

def build_binary():
	tar_name = "homework1"
	if confirm("binary release") == 1:
		print("Exiting...")
		return
	print("Building binary release...")
	subprocess.call(["make", "clean"])
	subprocess.call(["make", "all"])
	hostname = get_hostname()
	tar_name += "_" + hostname
	#Generate TARBALL THAT INCLUDES a  tar -czf homework1_bin_contents.tar.gz -C homework1/bin contents
	return_code = subprocess.call(["tar", "-czf", f"{tar_name}.tar", "-C",  ".." ,"homework1/bin"])
	if return_code != 0:
		print("Failed to create tarball")
		return

	print(f"Tarball created: {tar_name}.tar")

def build_source():
	tar_name = "homework1"
	if confirm("source release") == 1:
		print("Exiting...")
		return
	print("Building binary release...")
	subprocess.call(["make", "clean"])
	#Generate TARBALL THAT INCLUDES a  tar -czf homework1_bin_contents.tar.gz -C homework1/bin contents
	return_code = subprocess.call(["tar", "-czf", f"{tar_name}.tar", "-C",  ".." ,"homework1"])
	if return_code != 0:
		print("Failed to create tarball")
		return
	print(f"Tarball created: {tar_name}.tar")

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