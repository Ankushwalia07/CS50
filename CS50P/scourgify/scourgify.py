import csv
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input.csv output.csv")

    in_file, out_file = sys.argv[1], sys.argv[2]

    if not in_file.endswith(".csv") or not out_file.endswith(".csv"):
        sys.exit("Both files must be in CSV format")

    clean_data(in_file, out_file)

def clean_data(input_file, output_file):
    try:
        with open(input_file) as infile:
            reader = csv.DictReader(infile)
            with open(output_file, "w", newline='') as outfile:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
