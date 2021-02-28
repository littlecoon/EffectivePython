class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}
        
    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total/count
        

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein','Math', 75)
book.report_grade('Albert Einstein','Math', 65)
book.report_grade('Albert Einstein','Gym', 90)
book.report_grade('Albert Einstein','Gym', 95)

