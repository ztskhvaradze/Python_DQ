import xml.etree.ElementTree as ET


class XMLFileRecords:
    def __init__(self, filename):
        self.filename = filename

    def read_records(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        records = []
        for record in root.findall("record"):
            records.append(record)
        return records
