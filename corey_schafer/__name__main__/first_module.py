def main():
	print("First module's __name__ variable:", __name__)
	print("This file is being run directly")

if __name__ == '__main__':
	main()
else:
	print("Run from import")
