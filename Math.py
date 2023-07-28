from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
from datetime import datetime, timedelta

def generate_random_problem():
    operator = random.choice(["*", "/"])  # Choose between multiplication (*) and division (/)
    if operator == "*":
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        result = num1 * num2
        problem_str = f"{num1} * {num2} ="
    else:
        # Generate a random divisor and ensure the result is a whole number
        divisor = random.randint(1, 12)
        result = random.randint(0, 12) * divisor
        num1 = result
        num2 = divisor
        problem_str = f"{num1} ÷ {num2} ="

    return problem_str

def create_pdf_with_problems(file_path, num_problems):
    c = canvas.Canvas(file_path, pagesize=letter)

    # Set font size and starting position
    font_size = 13
    column_width = 150
    x_initial = 50
    x_positions = [x_initial + i * column_width for i in range(3)]
    y = 750

    for i in range(num_problems):
        problem = generate_random_problem()

        # Calculate the current row and column
        row = i // 3
        column = i % 3

        # Calculate the x and y coordinates for the current problem
        x = x_positions[column]
        y_current_row = y - (row + 1) * (font_size + 5)
        c.drawString(x, y_current_row, problem)

    c.save()

if __name__ == "__main__":
    # input_date_str = input("Enter the start date (YYYY-MM-DD): ")
    input_date_str = "2023-07-28"
    num_files_to_generate = 100  # You can change this to generate more or fewer files
    num_problems_per_file = 120  # Three columns of ten problems each

    try:
        input_date = datetime.strptime(input_date_str,"%Y-%m-%d")
        for i in range(num_files_to_generate):
            output_date = input_date + timedelta(weeks=i)
            output_date_str = output_date.strftime("%Y-%m-%d")
            # output_file = f"{'output_date_str'}.pdf"
            output_file = f"{'set' + str(i+1)}.pdf"
            create_pdf_with_problems(output_file, num_problems_per_file)
            print(f"PDF file '{output_file}' created with {num_problems_per_file} random multiplication and division problems for {output_date_str}.")
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
