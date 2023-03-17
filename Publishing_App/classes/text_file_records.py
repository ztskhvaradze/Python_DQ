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
            # Initialize an empty string to hold the lines of each record
            record_text = ""
            for line in f:
                if line.strip() == "":
                    # If the line is blank, then the current record is complete
                    # and can be added to the list of records
                    records.append(record_text.strip())
                    # Start a new empty string for the next record
                    record_text = ""
                else:
                    # If the line is not blank, add it to the current record
                    record_text += line
            # Save the last record if there is one
            if record_text:
                records.append(record_text.strip())
        # Return the list of records
        return records

    @staticmethod
    def write_processed_records(records_text, output_filename):
        # write processed records to output file
        with open(output_filename, 'w') as f:
            # concatenate the strings in the records_text list
            records_text = '\n'.join(records_text)
            f.write(records_text)

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
