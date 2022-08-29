import getpass, sys

def question_and_answer(prompt):
    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)
    
def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 3
correct = 0

print('Welcome to my soccer quiz, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")

rsp = question_with_response("How many balon d'ors has Lionel Messi won?")
if rsp == "7":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Who has won the most amount of champions league titles?")
if rsp == "Real Madrid":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Who won the 2018 edition of the FIFA World Cup?")
if rsp == "France":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))