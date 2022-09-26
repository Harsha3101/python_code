def percentage(student_marks,query_name):
    total=0
    for i in range(len((student_marks[query_name]))):
        total=total+student_marks[query_name][i]
    avg=total/len((student_marks[query_name]))
    return avg



