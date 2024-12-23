class Memo:
    def __init__(self, filename):
        self.filename = filename

    def load_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty list.")
            return []
        except IOError:
            print("Error reading file.")
            return []

    def save_to_file(self, content):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.writelines(content)

    def append_to_file(self, line):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(line)
