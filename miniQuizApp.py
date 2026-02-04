'''30. Quiz game with scoring
   - Hint: Store questions and answers in a dictionary, then check user answers and keep score.'''
print("Quiz game, the game contain 5 multiple choice queations for each subject.\n \n"
      "Select one of the following subject:\n"
      "1, maths \n2, C++ \n3, Emerging tech")

subject = input("what subject do want to take?(1,2,3): ")

user_answer = []  # user answer input.


def user_input(inputs):
    for i in inputs:
        print(i)
        answer = input("Enter answer: ").upper()
        while True:
            if answer == "A" or answer == "B" or answer == "C" or answer == "D":
                user_answer.append(answer)
                break
            else:
                print("Invalid CHOISE RANGE!!")
                answer = input("Enter answer: ").upper()


point_counter = []  # count the point from the answer comparision


def point_checker(answers):
    for i in range(5):
        if answers[i] == user_answer[i]:
            point_counter.append(1)
        else:
            pass
    print(f"   You get: {len(point_counter)} out of 5.")


def maths():
    print("Five applied math calculus multiple choise questions.\n\n")
    mathquestion = ["▎Question 1: Area Between Curves Find the area between the curves  y = x²  and  y = 4 - x². \nA)  16/3   \nB)  8/3   \nC)  8   \nD)  4 ",
                    "▎Question 2: Volume of Revolution A region is bounded by the curve  y = √(x)  and the x-axis, from  x = 0  to  x = 4 . \nWhat is the volume of the solid obtained by rotating this region about the x-axis? \nA)  16π/3   \nB)  8π   \nC)  4π   \nD)  32π/3",
                    "▎Question 3: Arc Length Find the length of the curve defined by the parametric equations  x(t) = t²  and  y(t) = t³ , \nfor  t  in the interval [1, 2]. \nA)  5   \nB)  7   \nC)  17/3   \nD)  9",
                    "▎Question 4: Surface Area of Revolution Calculate the surface area of the solid formed by rotating the curve  y = ln(x),  \nfrom  x = 1  to  x = e  around the x-axis.\nA)  2π   \nB)  3π   \nC)  4π   \nD)  π",
                    "▎Question 5: Improper Integrals Evaluate the improper integral: \n∫₁^∞ 1/x²dx, What is its value? \nA) Diverges  \nB)  1   \nC)  2   \nD)  0."]

    user_input(mathquestion)
    correctAnswer = ["A", "B", "B", "C", "B"]
    point_checker(correctAnswer)


def Cplus():
    print("Five C++ multiple choise questions.\n\n")
    cplusquestion = ["▎Question 1: What is the correct way to declare a function in C++ that returns an integer and takes two integer parameters? \nA) int function(int a, int b);  \nB) function int(int a, int b);  \nC) int function(a: int, b: int);  \nD) function int(int a, b);",
                     "▎Question 2: Which of the following is NOT a valid access specifier in C++? \nA) public  \nB) private  \nC) protected  \nD) hidden",
                     "▎Question 3: What does the keyword virtual indicate when used in a class member function?\nA) The function can only be called from derived classes.  \nB) The function is not implemented.  \nC) The function can be overridden in derived classes.  \nD) The function can be called without creating an object.",
                     "▎Question 4: Which of the following containers is NOT part of the Standard Template Library (STL)?\nA) std::vector  \nB) std::map  \nC) std::array  \nD) std::tuple  ",
                     "▎Question 5: What will happen if you try to delete a pointer that has already been deleted in C++?\nA) The program will compile successfully.  \nB) It will cause a memory leak.  \nC) It will lead to undefined behavior.  \nD) The pointer will be automatically reset to nullptr."
                     ]
    user_input(cplusquestion)
    correctanswer = ["A", "D", "C", "D", "C"]
    point_checker(correctanswer)


def emerging():
    print("Five Emerging multiple choise questions.\n\n")
    emergingquestion = ["▎Question 1: Which of the following technologies is primarily associated with decentralized finance (DeFi)?\nA) Cloud Computing  \nB) Blockchain  \nC) Quantum Computing  \nD) Augmented Reality",
                        "▎Question 2: What is the primary purpose of 5G technology?\nA) To increase battery life in devices  \nB) To provide faster and more reliable internet connectivity  \nC) To enhance virtual reality experiences  \nD) To improve data storage capacity",
                        "▎Question 3: Which of the following is a key feature of Artificial Intelligence (AI)?\nA) It can only perform tasks that are explicitly programmed.  \nB) It can learn from data and improve over time.  \nC) It requires constant human supervision to function.  \nD) It is limited to specific industries like finance and healthcare.",
                        "▎Question 4: What does the term \"Internet of Things \" (IoT) refer to?\nA) The use of social media platforms for marketing.  \nB) The network of physical devices connected to the internet that can collect and exchange data. \nC) The development of new internet protocols.  \nD) The process of creating virtual environments for gaming.",
                        "▎Question 5: Which emerging technology is expected to revolutionize data processing by using quantum bits (qubits)?\nA) Classical Computing  \nB) Blockchain  \nC) Quantum Computing  \nD) Edge Computing"]
    user_input(emergingquestion)
    correctanswer = ["B", "B", "B", "B", "C"]
    point_checker(correctanswer)


while True:
    if subject == "1":
        maths()
        break
    elif subject == "2":
        Cplus()
        break
    elif subject == "3":
        emerging()
        break
    else:
        print("  WRONG!! You enter invalid choice!!!\n\n")
        subject = input("what subject do want to take?(1,2,3): ")
