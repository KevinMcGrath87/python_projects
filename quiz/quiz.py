class Question:

    # {prompt:"answer"} format
    def __init__(self, prompt,answer ):
        self.prompt = prompt.lower()
        self.answer = answer.lower()
        self.eval = False
        
    def take_answer(self):
        input_answer = input(self.prompt)
        if input_answer.lower() == self.answer:
            self.eval = True
            print('Correct!')
        else:
            print('Sorry thats incorrect')
        return self.eval

class Quiz:
    # quiz maintains a collection of questions and score
    def __init__(self, questions):
        self.questions = questions

    def present_question(self,question):
            question.take_answer()


    def score(self):
        correct = 0
        total = len(self.questions)
        for question in self.questions:
            if question.eval == True:
                correct += 1
        print(f'you scored {correct} out of {total}')
        return(correct/total)
    

class QuizGame:
    def __init__(self, quiz):
        self.quiz = quiz


    def start_game(self):
        print("Lets start the quiz!")
        for question in quiz.questions:
            quiz.present_question(question)
        quiz.score()
        return



quizOneQuestionDict = {"who is the current president of the united states?": "Joe Biden","What state is the city of chicago in?":"Illinois","what is 7 x 11?":"77"}


questionList = []

for prompt in quizOneQuestionDict:
    questionList.append(Question(prompt=prompt,answer=quizOneQuestionDict[prompt]))

quiz = Quiz(questionList)

game = QuizGame(quiz)

game.start_game()


# abs_property = ""
# prop = str(abs_property)
# exec(f'{abs_property}={prop}')