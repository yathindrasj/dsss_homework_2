import random


def limit(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def math_ops():
    return random.choice(['+', '-', '*'])


def numericals(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2 #this function performs addition of 2 numbers
    elif o == '-': a = n1 - n2 #this function performs subtraction of 2 numbers
    else: a = n1 * n2 #this function performs multiplication of 2 numbers
    return p, a

def math_quiz():
    s = 0
    t_q = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = limit(1, 5); n2 = limit(1, 5); o = math_ops()

        PROBLEM, ANSWER = numericals(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
