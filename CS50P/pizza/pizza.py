import sys
import csv
import tabulate

try:
    # Checking if there are no arguments
    if len(sys.argv) == 1:
        print("Missing command line argument")
        sys.exit(1)

    # Checking if there are more than 2 arguments
    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)

    # Checking if it's a CSV file or not
    if len(sys.argv) == 2:
        file = sys.argv[1]
        if not file.endswith(".csv"):
            print("File must have a .csv extension")
            sys.exit(1)

        # Opening the file
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader)

            # Reading all rows into a list
            data = list(reader)

        # Printing the table
        table = tabulate.tabulate(data, headers=header, tablefmt='grid')
        print(table)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
