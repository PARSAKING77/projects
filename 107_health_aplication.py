class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, age, height, weight):
        self.students.append(Student(age, height, weight))

    def calculate_average(self):
        total_age = sum(student.age for student in self.students)
        total_height = sum(student.height for student in self.students)
        total_weight = sum(student.weight for student in self.students)
        average_age = total_age / len(self.students)
        average_height = total_height / len(self.students)
        average_weight = total_weight / len(self.students)
        return average_age, average_height, average_weight

def main():
    classroom_a = Classroom('A')
    classroom_b = Classroom('B')

    num_students_a = int(input())
    ages_a = list(map(float, input().split()))
    heights_a = list(map(float, input().split()))
    weights_a = list(map(float, input().split()))


    num_students_b = int(input())
    ages_b = list(map(float, input().split()))
    heights_b = list(map(float, input().split()))
    weights_b = list(map(float, input().split()))
    for i in range(num_students_a):
        classroom_a.add_student(ages_a[i], heights_a[i], weights_a[i])

    for i in range(num_students_b):
        classroom_b.add_student(ages_b[i], heights_b[i], weights_b[i])

    avg_age_a, avg_height_a, avg_weight_a = classroom_a.calculate_average()
    avg_age_b, avg_height_b, avg_weight_b = classroom_b.calculate_average()

    print(repr(avg_age_a))
    print(repr(avg_height_a))
    print(repr(avg_weight_a))
    print(repr(avg_age_b))
    print(repr(avg_height_b))
    print(repr(avg_weight_b))

    if avg_height_a > avg_height_b:
        print("A")
    elif avg_height_a < avg_height_b:
        print("B")
    else:
        if avg_weight_a < avg_weight_b:
            print("A")
        elif avg_weight_a > avg_weight_b:
            print("B")
        else:
            print("Same")

if __name__ == "__main__":
    main()