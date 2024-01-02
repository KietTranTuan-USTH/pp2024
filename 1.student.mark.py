def get_number_of_students():
    return int(input("How many students are there in the class? "))

def get_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DoB): ")
    return {"id": student_id, "name": name, "dob": dob}

def get_number_of_courses():
    return int(input("How many courses are there? "))

def get_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return {"id": course_id, "name": name}

def get_student_marks(students, course):
    marks = {}
    print(f"Enter marks for {course['name']} course:")
    for student in students:
        mark = float(input(f"Enter mark for {student['name']} ({student['id']}): "))
        marks[student['id']] = mark
    return marks

def list_all_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']}")

def list_all_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"{student['id']}: {student['name']}")

def show_student_marks(students, course, marks):
    print(f"\nStudent marks for {course['name']} course:")
    for student in students:
        print(f"{student['name']} ({student['id']}): {marks.get(student['id'], 'N/A')}")

def main():
    students = []
    courses = []

    num_students = get_number_of_students()
    for _ in range(num_students):
        student_info = get_student_info()
        students.append(student_info)

    num_courses = get_number_of_courses()
    for _ in range(num_courses):
        course_info = get_course_info()
        courses.append(course_info)

    while True:
        print("\nOptions:")
        print("1. List Courses")
        print("2. List Students")
        print("3. Show Student Marks for a Course")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_all_courses(courses)
        elif choice == '2':
            list_all_students(students)
        elif choice == '3':
            list_all_courses(courses)
            course_id = input("Enter the course ID to show marks: ")
            selected_course = next((course for course in courses if course['id'] == course_id), None)
            if selected_course:
                marks = get_student_marks(students, selected_course)
                show_student_marks(students, selected_course, marks)
            else:
                print("Invalid course ID. Please try again.")
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
