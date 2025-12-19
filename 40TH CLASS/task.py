from abc import ABC, abstractmethod

class CourseBase(ABC):
    @abstractmethod
    def enroll_student(self, student_name):
        pass

    @abstractmethod
    def drop_student(self, student_name):
        pass

    @abstractmethod
    def display_course(self):
        pass


class Course(CourseBase):
    def __init__(self, course_name, course_code, max_student):
        self.__course_name = course_name
        self.__course_code = course_code
        self.__max_student = max_student
        self.__students = []

    def enroll_student(self, student_name):
        if len(self.__students) < self.__max_student:
            if student_name not in self.__students:
                self.__students.append(student_name)
                print(f"{student_name} has been enrolled in {self.__course_name}.")
            else:
                print(f"{student_name} is already enrolled in {self.__course_name}.")
        else:
            print(f"Enrollment failed, {self.__course_name} is full.")

    def drop_student(self, student_name):
        if student_name in self.__students:
            self.__students.remove(student_name)
            print(f"{student_name} has been removed from {self.__course_name}.")
        else:
            print(f"Student {student_name} is not enrolled in {self.__course_name}.")

    def display_course(self):
        print(f"\nCourse: {self.__course_name} ({self.__course_code})")
        print(f"Maximum Students: {self.__max_student}")
        print(f"Enrolled Students ({len(self.__students)}): {self.__students}")


# Example Usage
python_course = Course("Python Programming", "CSE101", 3)
ds_course = Course("Data Structures", "CSE202", 2)

python_course.enroll_student("Ali")
python_course.enroll_student("Sara")
python_course.enroll_student("Ahmed")
python_course.enroll_student("Usman")  # Course full

ds_course.enroll_student("Ali")
ds_course.enroll_student("Sara")
ds_course.enroll_student("Ahmed")  # Course full

python_course.drop_student("Sara")
python_course.enroll_student("Usman")  # Now possible

python_course.display_course()
ds_course.display_course()
