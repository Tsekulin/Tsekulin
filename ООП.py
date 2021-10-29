class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses = []

    def lecture_score(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in lecturer.courses) and (
                (course in self.finished_courses) or (course in self.courses_in_progress)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def average_rating(self):
        s = 0
        c = 0
        for i in self.grades.values():
            for m in i:
                s += m
                c += 1
        return (s / c)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка по домашкам: {self.average_rating()}\nКурсы изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses = []

    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}'
        return a


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.courses = []
        self.grades = {}


class Reviewer(Mentor):
    def _init_(self, name, surname):
        super().__init__(self, name)


    def rate_rv(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_best = Student('Медведев', 'Дмитрий', 'муж')
student_best.finished_courses += ['основы Python']
student_best.courses_in_progress += ['Python']

reviewer_best = Reviewer('Путин', 'Владимир')
reviewer_best.courses += ['Python']
reviewer_best.courses += ['основы Python']

reviewer_best.rate_rv(student_best, 'Python', 5)
reviewer_best.rate_rv(student_best, 'Python', 8)
reviewer_best.rate_rv(student_best, 'Python', 9)
reviewer_best.rate_rv(student_best, 'Python', 10)

print(student_best)