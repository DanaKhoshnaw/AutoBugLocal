from os import path

# individual bugs in each file would need to be separated by two new lines [YOU CAN CHANGE DELIMITER IF YOU WANT]

DELIMITER = '\n\n'


class filterBugReport:
    def __init__(self):
        """
        put contents of blackfile into list according to delimiter
        does not do anything if there is no files that exist
        """
        if path.exists("black.list"):
            blackfile = open("black.list", 'r')
            self.black_data = blackfile.read().split(DELIMITER)
            blackfile.close()

    def blacklist_check(self, traceback):
        """
        boolean:    - TRUE if traceback (bug) appears in black data list
                    - FALSE if no black data (DOES NOT EXIST)
                    - FALSE if traceback (bug) DOES NOT appear in black data list
        """
        if self.black_data:
            if traceback in self.black_data:
                return True
        return False