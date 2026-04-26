class students:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)

class GWAAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip():
                        # Split name and GWA (assuming format: Name, GWA)
                        parts = line.strip().split(',')
                        name = parts[0].strip()
                        gwa = parts[1].strip()
                        self.students.append(students(name, gwa))
        except FileNotFoundError:
            print(f"Error: The file 'student.txt' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def get_highest_student(self):
        if not self.students:
            return None
        
        highest = max(self.students, key=lambda s: s.gwa)
        return highest

if __name__ == "__main__":
    analyzer = GWAAnalyzer('student.txt')
    analyzer.load_data()

    top_student = analyzer.get_highest_student()

    if top_student:
        print(f"Student with the highest GWA: {top_student.gwa}")