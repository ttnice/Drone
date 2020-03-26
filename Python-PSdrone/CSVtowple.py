import csv

def write(name, item):
    with open(f"{name}.csv", "w") as f_write:
        writer = csv.writer(f_write)
        for row in item:
            writer.writerow(row)