import csv
 
if __name__ == '__main__':

    tableau = [['temps : ', 2, 3], ['Altitude : ', 5, 6]]

    with open("tableau.csv", "w") as f_write:
        writer = csv.writer(f_write)
        for row in tableau:
            writer.writerow(row)