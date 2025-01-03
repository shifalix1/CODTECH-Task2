#TASK 2: STUDENT GRADE TRACKER

class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self):
        subject = input("Enter the Subject name: ").strip()
        while True:
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid grade.")
        
        self.grades[subject] = grade
        print(f"Grade for {subject} added successfully.")

    def calculate_average(self):
        if not self.grades:
            return None
        return sum(self.grades.values()) / len(self.grades)

    def determine_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_summary(self):
        if not self.grades:
            print("No grades available to display.")
            return

        print("\nGrade Summary:")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade:.2f}")

        average = self.calculate_average()
        if average is not None:
            letter_grade = self.determine_letter_grade(average)
            gpa = self.calculate_gpa(average)
            print(f"\nAverage Grade: {average:.2f}")
            print(f"Letter Grade: {letter_grade}")
            print(f"GPA: {gpa:.2f}")

    def run(self):
        print("Welcome to Student Grade Tracker!")
        while True:
            print("\nOptions:")
            print("1: Add Grade")
            print("2: Display Summary")
            print("3: Exit")
            choice = input("Select an option (1-3): ").strip()

            if choice == '1':
                self.add_grade()
            elif choice == '2':
                self.display_summary()
            elif choice == '3':
                print("Thank you for using Student Grade Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    tracker = StudentGradeTracker()
    tracker.run()
