def grades(grade):
    grades_list = {'A', 'B', 'C', 'D', 'F'}
    assert grade in grades_list
    return f"You have got {grade}"
