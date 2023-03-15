import os
from .text_statistics import TextStatistics


class TextFileRecords:
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

    @staticmethod
    def write_processed_records(records):
        # Get the directory where the application is located
        app_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the file path for the output file relative to the application directory
        output_file_path = os.path.join(app_dir, 'records_from_file.txt')
        # Open the output file in write mode
        with open(output_file_path, 'w') as f:
            # Write each line of each record to the file
            for record in records:
                for line in record:
                    f.write(line)

    def remove_file(self):
        # Attempt to remove the file, and print an error message if it can't be found
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            print(f"{self.filename} not found.")

    def get_records_object(self):
        records = TextStatistics(self.filename)
        records.records = self.write_processed_records
        return records
