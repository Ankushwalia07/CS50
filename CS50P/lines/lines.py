import sys
try:
    if len(sys.argv) > 2:
        print("Too many command-line arguments.")
        sys.exit(1)

    if len(sys.argv) == 1:
        print("Missing command-line argument.")
        sys.exit(1)

    if len(sys.argv) == 2:
        file= sys.argv[1]
        if not file.endswith('.py'):
            raise ValueError("File must have a .py extension.")

        with open(file) as file:
            lines = file.readlines()

        count = 0

        for line in lines:
            if line.strip() == '':
                continue
            if line.strip().startswith('#'):
                continue
            count += 1
        print(f"Number of lines of code : {count}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)


