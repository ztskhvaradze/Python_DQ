import os

class Text_filele_records:
    def __init__(self, filename):
        # Initialize the TextFileRecords object with the provided filename
        self.filename = filename

    def read_records(self):
        # Initialize an empty list to hold the records read from the file
        records = []
        # Open the file in read mode
        with open(self.filename, 'r') as f:
            # Initialize an empty list to hold the lines of each record
            record_lines = []
            for line in f:
                if line.strip() == "":
                    # If the line is blank, then the current record is complete
                    # and can be added to the list of records
                    records.append(record_lines)
                    # Start a new empty list for the next record
                    record_lines = []
                else:
                    # If the line is not blank, add it to the current record
                    record_lines.append(line)
            # Save the last record if there is one
            if record_lines:
                records.append(record_lines)
        # Return the list of records
        return records

    def write_processed_records(self, records):
        # Open a new file in write mode to hold the processed records
        with open('records_from_file.txt', 'w') as f:
            # Write each line of each record to the file
            for record in records:
                for line in record:
                    f.write(line)
                    f.write('\n')

    def remove_file(self):
        # Attempt to remove the file, and print an error message if it can't be found
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            print(f"{self.filename} not found.")
