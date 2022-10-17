from os import path


class FileStatistics:
    def __init__(self, new_file):
        if not isinstance(new_file, str):
            raise Exception("Given file path isn't a string")
        if not path.exists(new_file):
            raise Exception("Given file doesn't exist")
        self._file = open(new_file)
        self._path = new_file

    @property
    def path(self):
        return self._path

    def set_file(self, new_file):
        if not isinstance(new_file, str):
            raise Exception("Given file path isn't a string")
        if not path.exists(new_file):
            raise Exception("Given file doesn't exist")
        self._file = open(new_file)
        self._path = new_file

    def size(self):
        return path.getsize(self.path)

    def amount_of_chars(self):
        self._file.seek(0)
        number = 0
        while True:
            read_data = self._file.read(1000)
            if read_data == "":
                break
            number += len(read_data)
        return number

    def words_count(self):
        self._file.seek(0)
        words = 0
        while True:
            read_data = self._file.readline()
            if read_data == "":
                break
            line = read_data.split()
            words += len(line)
        return words

    def __str__(self):
        output = ""
        output += "Path: ".__add__(self.path).__add__("\n")
        output += "Size in bytes: ".__add__(str(self.size())).__add__("\n")
        output += "Amount of chars: ".__add__(str(self.amount_of_chars())).__add__("\n")
        output += "Amount of words: ".__add__(str(self.words_count())).__add__("\n")
        return output
