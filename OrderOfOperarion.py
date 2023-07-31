import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def generate_random_expression():
    operators = ['+', '-', '*', '/']
    num_operations = random.randint(2, 4)
    num = random.randint(1, 10)
    factors = get_factors(num)
    
    expression = str(num)
    for _ in range(num_operations):
        operator = random.choice(operators)
        if operator == '/':
            if len(factors) > 1:
                divisor = random.choice(factors[1:])  # Ensure division by a factor (excluding 1)
            else:
                divisor = 1
            expression += f' {operator} {divisor}'
        else:
            num = random.randint(1, 10)
            expression += f' {operator} {num}'

    return expression

def generate_random_question(num_questions):
    questions = []
    for _ in range(num_questions):
        expression = generate_random_expression()
        question = f'({expression}) ='
        questions.append(question)
    return questions

def save_questions_to_pdf(filename, questions):
    c = canvas.Canvas(filename, pagesize=letter)

    # Set font size and starting position
    font_size = 13
    column_width = 250
    x_initial = 50
    x_positions = [x_initial + i * column_width for i in range(3)]
    y = 750

    for i in range(len(questions)):
        problem = questions[i]

        # Calculate the current row and column
        row = i // 2
        column = i % 2

        # Calculate the x and y coordinates for the current problem
        x = x_positions[column]
        y_current_row = y - (row + 1) * (font_size + 130) + 150
        c.drawString(x, y_current_row, problem)

    c.save()

if __name__ == "__main__":
    num_questions = 10  # Change this to the number of questions you want (must be a multiple of 10)
    questions = generate_random_question(num_questions)
    y = 750  # Reset y-coordinate to the top of the page
    save_questions_to_pdf("random_order_of_operations_questions.pdf", questions)  # Pass the filename as a string
    print("PDF file with random order of operations questions has been created.")

