import xml.etree.ElementTree as ET

class ConfigReader:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.folders = {}

    def read_config(self):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        for child in root:
            self.folders[child.tag] = child.text
        return self.folders
