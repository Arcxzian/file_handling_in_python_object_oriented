class LifeWriter:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def write_multiple_lines(self):
        """Prompts user for input and writes lines to a text file"""
        try:
            # Using 'w' mode to create the file i cant change it to write because it is a text file and not a binary file
            with open(self.filename, mode='w') as file_object:
                while True:
                    line_input = input("Enter line: ")
                    file_object.write(line_input + "\n")

                    user_choice = input("Are there more lines yes/no? ").lower()
                    if user_choice != 'yes':
                        break
            print(f"\nSuccessfully wrote to {self.filename}")

        except Exception as error_information:
            print(f"An error occurred: {error_information}")
# --- Main Execution ---
if __name__ == "__main__":
    life_instance = LifeWriter()
    life_instance.write_multiple_lines()