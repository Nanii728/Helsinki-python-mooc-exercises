def main():
    all_total_points = []
    all_grades = []

    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break

        parts = user_input.split()
        exam_points = int(parts[0])
        exercises_completed = int(parts[1])

        # Convert exercises to exercise points (rounded down)
        exercise_points = exercises_completed // 10
        total_points = exam_points + exercise_points
        all_total_points.append(total_points)

        # Determine grade
        if exam_points < 10:
            grade = 0
        elif 0 <= total_points <= 14:
            grade = 0
        elif 15 <= total_points <= 17:
            grade = 1
        elif 18 <= total_points <= 20:
            grade = 2
        elif 21 <= total_points <= 23:
            grade = 3
        elif 24 <= total_points <= 27:
            grade = 4
        else:
            grade = 5

        all_grades.append(grade)

    print("Statistics:")

    # Handle the edge case of no input
    if len(all_grades) == 0:
        return

    # 1. Points average
    points_average = sum(all_total_points) / len(all_total_points)
    print(f"Points average: {points_average:.1f}")

    # 2. Pass percentage
    passing_students = 0
    for grade in all_grades:
        if grade > 0:
            passing_students += 1
            
    pass_percentage = (passing_students / len(all_grades)) * 100
    print(f"Pass percentage: {pass_percentage:.1f}")

    # 3. Grade distribution
    print("Grade distribution:")
    for grade in range(5, -1, -1):
        stars = "*" * all_grades.count(grade)
        print(f"  {grade}: {stars}")


# Call the main execution block directly in the global scope
main()
