# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# Define a dictionary to store student records
students = {"101":"Sara", "18": 18, "12th": 12} {"202":"abby", "17}
    # "student_id": {"name": "Name", "age": Age, "grade": Grade}

def add_student(student_id: str, name: str, age: int, grade: int):
    # Add a new student record to the dictionary
    pass

def average_grade() -> float:
    # Calculate and return the average grade of all students
    pass

# Example usage
add_student("001", "Alice", 16, 85)
add_student("002", "Bob", 17, 92)
print("Average Grade:", average_grade())
