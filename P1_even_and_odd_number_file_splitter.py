class NumberSorter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []

    def read_numbers(self):
        """Read integers from input file and store them in a list"""
        try:
            with open(self.input_file, 'r') as file:
                #this filter out empty lines and converts to integers
                self.numbers = [int(line.strip()) for line in file if line.strip()]
        except FileNotFoundError:
            print(f"error: {self.input_file} not found.")
        except ValueError:
            print("Error: files contain non-integer data.")
    
    def sort_and_save(self, even_filename, odd_filename):
        """Seperates numbers into even and odd files."""
        if not self.numbers:
            print("No data to process.")
            return
        
        try:
            with open(even_filename, 'w') as even_file, \
                open(odd_filename, 'w') as odd_file:

                for num in self.numbers:
                    if num % 2 == 0:
                        even_file.write(f"{num}\n")
                    else:
                        odd_file.write(f"{num}\n")
            
            print(f"Succesfully processed {len(self.numbers)}) numbers.")
            print(f"check {even_filename} and {odd_filename} for results.")
        except IOError as e:
            print(f"An error occured while writing files: {e}")

if __name__ == "__main__":
    #create an instance (object) of the class
    sorter = NumberSorter('numbers.txt')
    # call methods
    sorter.read_numbers()
    sorter.sort_and_save('even.txt', 'odd.txt')


            
