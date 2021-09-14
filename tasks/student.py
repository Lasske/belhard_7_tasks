"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname = str
    name = str
    group = int
    average_score = int

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __repr__(self):
        return repr(self.average_score)


if __name__ == "__main__":
    st1 = Student("surname1", "name1", 1, 8)
    st2 = Student("surname2", "name2", 1, 9)
    st3 = Student("surname3", "name3", 1, 6)
    st4 = Student("surname4", "name4", 1, 5)
    st5 = Student("surname5", "name5", 1, 9)
    stud = [st1, st2, st3, st4, st5]
    stud_lambda = filter(lambda s: s.average_score > 5, stud)
    print(sorted(stud))
    print(sorted(stud, reverse=True))
    print(list(stud_lambda))
    print(Student.__eq__(st2, st5))
    print(Student.__lt__(st1, st4))
    print(Student.__le__(st1, st2))
