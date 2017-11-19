import csv
import sys


def read_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        """Add an extra column in the end to signify the label"""
        """+1 -- good loan, -1 -- bad loan"""
        header = next(reader)
        header.append('label')
        writer.writerow(header)

        for line in reader:
            row = {header[i]:line[i] for i in range(len(line))}
            label = calc_label(row)
            """label 0 means to skip the record"""
            if label != 0:
                row['label'] = str(label)
                output = row.values()
                writer.writerow(output)


def calc_label(row):
    if row['loan_status'] == 'Fully Paid':
        return 1
    elif row['loan_status'] == 'Current':
        return 0
    ######################################
    # Please add more rules
    ######################################
    return -1


if __name__ == '__main__':
    """python3 LendingClub.py <input csv file path> <output cleaned csv file path>"""
    [input_file, output_file] = sys.argv[1:]
    read_csv(input_file, output_file)
