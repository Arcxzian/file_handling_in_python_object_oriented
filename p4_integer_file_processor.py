import os

class FileHandler:
    """Base class to handle raw file reading and writing operations."""
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        """Reads data from the file and returns it as a list of integers."""
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"The file {self.filename} does not exist.")
        
        with open(self.filename, 'r') as file:
            return file.read().split()
    
    def write_to_file(self, target_file, data_list):
        """Writes a list of data to a specific text file."""
        with open(target_file, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")

class IntegerFileProcessor(FileHandler):
    """Subclass that handles the math logic and filtering"""
    def __init__(self, source_file= "integers.txt"):
        super().__init__(source_file)
        self.even_results = []
        self.odd_results = []
        self.error_count = 0

    def validate_and_convert(self, raw_data):
        """filters out non-numeric strings to prevent crashes."""
        valid_numbers : []
        for item in raw_data:
            try:
                valid_numbers.append(int(item))   
            except ValueError:
                self.error_count += 1
        return valid_numbers

    def compute_math(self, numbers):
        """seperates numbers and performs square/ cube operations."""
        for num in numbers:
            if num % 2 == 0:
                # square even numbers
                self.even_results.append(num ** 2)
            else:
                # cube odd numbers
                self.odd_result.append(num ** 3)


      

