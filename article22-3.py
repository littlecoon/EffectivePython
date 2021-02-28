class WeightedGradebook(object):
    # ...
    def report_grade(self,name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(score, weight)        

    def average_grade(self, name):
        by_subject = self._grades[name]    
        score+_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                # ...
        return score_sum/ score_count


book.report_grade('Albert Einstein', 'Math', 80, 0.10)           

grades = []
grades.append(95, 0.45)
# ...
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight fro _, weight in grades)
average_grade = total/ total_weight


grades = []
grades.append((95, 0.45, 'Great job'))
# ...
total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight fro _, weight, _ in grades)
average_grade = total/ total_weight


