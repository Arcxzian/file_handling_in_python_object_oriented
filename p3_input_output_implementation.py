import datetime

class LifeWriter:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def _process_text(self, text):
        """Helper method to handle text formatting before writing."""
        return text
    
    def Write_Multiple_Lines(self):
        try:
            # Using 'w' mode to create the file i cant change it to write because it is a text file and not a binary file
            with open(self.filename, mode='a') as file_object:
                while True:
                    line_input = input("Enter line: ")
                    file_object.write(line_input + "\n")

                    user_choice = input("Are there more lines yes/no? ").lower()
                    if user_choice != 'yes':
                        break
            print(f"\nSuccessfully wrote to {self.filename}")

        except Exception as error_information:
            print(f"An error occurred: {error_information}")

class JournalWriter(LifeWriter):
    """A specialized LifeWriter that automatically timestamps entries"""

    def _process_text(self, text):
        """overides the parent method to inject the current time"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {text}"
    
# --- Main Execution ---
if __name__ == "__main__":
    journal = JournalWriter("my_diary.txt")
    journal.Write_Multiple_Lines()
