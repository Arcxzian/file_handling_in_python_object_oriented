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
        valid_numbers = []
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
                self.odd_results.append(num ** 3)
        def generate_report(self):
        """Prints a summary report of the operations."""
        print("-" * 30)
        print("PROCESS SUMMARY")
        print("-" * 30)
        print(f"Even numbers squared: {len(self.even_results)}")
        print(f"Odd numbers cubed: {len(self.odd_results)}")
        print(f"Invalid entries found: {self.error_count}")
        print("-" * 30 )
        print("Files 'double.txt' and 'triple.txt' updated successfully.")

    def run(self):
        """Orchestrates the entire flow."""
        try:
            # step 1: read raw data
            print(f"opening {self.filename}...")
            raw_content = self.read_data()

            # step 2: validate and convert to integers
            clean_numbers = self.validate_and_convert(raw_content)

            # step 3: perform math operations
            self.compute_math(clean_numbers)

            # step 4: write results to files
            self.write_to_file("double.txt", self.even_results)
            self.write_to_file("tripe.txt", self.odd_results)

            #step 5: generate report
            self.generate_report()

        except FileNotFoundError as e:
            print(f"[CRITICAL ERROR] {e}")
            print(f"Please create 'integers.txt' with 20 numbers first.")
        except Exception as e:
            print(f"[UNEXPECTED ERROR] {e}")

# Main execution
if __name__ == "__main__":
    # this is only look for 'integers.txt' in the same folder. If the file doesn't exist, it will trigger the custom error message.
    app =IntegerFileProcessor("integers.txt")
    app.run()
