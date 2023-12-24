from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain) -> None:
    self.quiz = quiz_brain
    self.count = 0
    #create windows
    self.window = Tk()
    self.window.title("Quiz App")
    self.window.config(bg=THEME_COLOR, padx=20, pady=20)

    #create label to keep track of the score 
    self.score = Label()
    self.score.config(bg=THEME_COLOR, highlightthickness=0)
    self.score["text"] = f"Score: 0"
    self.score.grid(column=1, row=0)




    #create the canva 
    self.canva = Canvas()
    self.canva.config(bg="white", width=300, height=250, highlightthickness=0)
    self.question_text = self.canva.create_text(
      150, 
      125, 
      text="Yo", 
      font=("Arial", 20, "italic"),  
      fill="black", 
      width=200
      )
    self.canva.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    # Create Buttons
    #import button image
    true_image = PhotoImage(file="./quizzler-app-start/images/true.png")
    false_image = PhotoImage(file="./quizzler-app-start/images/false.png")

    self.button_true = Button(image=true_image) 
    self.button_true.config( highlightbackground=THEME_COLOR, highlightthickness=0 ,command=self.true_response) 
    self.button_true.grid(column=0, row=2)

    self.button_false = Button(image=false_image)
    self.button_false.config( highlightbackground=THEME_COLOR, highlightthickness=0 ,command=self.false_response) 
    self.button_false.grid(column=1, row=2)
    self.get_next_question()

    self.window.mainloop()

  def get_next_question(self):
    self.canva.config(bg="white")
    if self.quiz.still_has_questions:
      self.score.config(text=f"Score: {self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canva.itemconfig(self.question_text, text=q_text)
    else:
      self.canva.itemconfig(self.question_text, text="No more question")
      self.button_true.config(state="disabled")
      self.button_false.config(state="disabled")

  def true_response(self):
    is_right = self.quiz.check_answer("True")
    self.give_feedback(is_right)
  
  def false_response(self):
    is_right = self.quiz.check_answer("False")
    self.give_feedback(is_right)

  def give_feedback(self, is_right):
    if is_right:
      self.canva.config(bg="green")
    else:
      self.canva.config(bg="red")
    self.window.after(1000, self.get_next_question)
    

 
