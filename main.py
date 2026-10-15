class Student:  #super().init  #super().method

      def __init__(self , nachname , alter):
          self.nachname = nachname
          self._alter = 0
          self.alter = alter
      @property
      def alter(self):
          return self._alter
      @alter.setter
      def alter(self, alter):
          if alter <= 0 :
              raise TypeError("The Age must be greater than zero")
          self._alter = alter

      def __str__(self) -> str:
          return f"This Student is called {self.nachname} and is {self._alter}"

class Student_assistant(Student):

      def __init__(self , nachname , alter):

            super().__init__(nachname , alter)
            self.salary = 500


student = Student("Teddy" , 20)
try:
    student2=Student("Dongmo" , -5)
except TypeError as e :
      print(str(e))