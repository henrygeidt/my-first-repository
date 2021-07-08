def input_value(string_to_print):
    name = input(string_to_print)
    return name

def grade_maths(a, b, c):
    ict_score = ((a + b + c) / 175 * 100)
    return ict_score

student_name = input_value("What is your name?")
homework_score = int(input_value("What is your homework score?"))
assessment_score = int(input_value("What is your assessment score?"))
final_exam_score = int(input_value("What is your exam score?"))

final_score = grade_maths(homework_score, assessment_score, final_exam_score)

final_output = f"({student_name}, {final_score})"

print(final_output)
    