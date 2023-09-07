import os
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def evaluate_expression(expr):
    try:
        return eval(expr)
    except ZeroDivisionError:
        return None

def is_valid_expression(expr):
    """Checks if the expression results in a positive whole number."""
    result = evaluate_expression(expr)
    return result is not None and result % 1 == 0 and result > 0

def generate_random_expression():
    # Create a list of operators and shuffle it to randomize the order
    operators = ['+', '-', '*', '/']
    random.shuffle(operators)
    
    while True:
        # Choosing a starting number
        num1 = random.randint(1, 10)

        if operators[0] == '/':
            factors = [i for i in range(1, num1+1) if num1 % i == 0]
            num2 = random.choice(factors)
        else:
            num2 = random.randint(1, 10)

        expr1 = f"{num1} {operators[0]} {num2}"
        if not is_valid_expression(expr1):
            continue

        num3 = random.randint(1, 10)
        if operators[1] == '/':
            factors = [i for i in range(1, num3+1) if num3 % i == 0]
            num4 = random.choice(factors)
        else:
            num4 = random.randint(1, 10)

        expr2 = f"{expr1} {operators[1]} {num3}"
        if not is_valid_expression(expr2):
            continue

        num5 = random.randint(1, 10)
        if operators[2] == '/':
            factors = [i for i in range(1, num5+1) if num5 % i == 0]
            num6 = random.choice(factors)
        else:
            num6 = random.randint(1, 10)

        inner_expr = f"{num4} {operators[3]} {num5}"
        if not is_valid_expression(inner_expr):
            continue

        final_expr = f"{expr2} {operators[2]} ({inner_expr})"
        if is_valid_expression(final_expr):
            return final_expr

def generate_random_question(num_questions):
    questions = []
    while len(questions) < num_questions:
        expression = generate_random_expression()
        questions.append(f'{expression} =')
    return questions

def save_questions_to_pdf(filename, questions):
    c = canvas.Canvas(filename, pagesize=letter)

    font_size = 13
    column_width = 250
    x_initial = 50
    x_positions = [x_initial + i * column_width for i in range(3)]
    y = 750

    for i, question in enumerate(questions):
        row = i // 2
        column = i % 2
        x = x_positions[column]
        y_current_row = y - (row + 1) * (font_size + 130) + 150
        c.drawString(x, y_current_row, question)

    c.save()

if __name__ == "__main__":
    num_questions = 10
    questions = generate_random_question(num_questions)
    y = 750
    num_files_to_generate = 100
    # save_questions_to_pdf("random_order_of_operations_questions.pdf", questions)
    # print("PDF file with random order of operations questions has been created.")
    try:
        # input_date = datetime.strptime(input_date_str, "%Y-%m-%d")
        output_folder = "Order of Operation sets"
        
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i in range(num_files_to_generate):
            output_file = os.path.join(output_folder, f"set{i + 1}.pdf")
            save_questions_to_pdf(output_file, questions)
            print(f"PDF file '{output_file}' created with {num_questions} random multiplication and division problems.")
        # for i in range(num_files_to_generate):
        #     # output_date = input_date + timedelta(weeks=i)
        #     # output_date_str = output_date.strftime("%Y-%m-%d")
        #     output_file = os.path.join(output_folder, f"set{i + 1}.pdf")
        #     save_questions_to_pdf(output_file, num_questions)
        #     print(f"PDF file '{output_file}' created with {num_questions} random multiplication and division problems.")
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
