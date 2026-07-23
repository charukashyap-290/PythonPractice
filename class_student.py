class student:
    def __init__(self,name,student_id,roll_no,course):
        self.name=name
        self.student_id=student_id
        self.roll_no=roll_no
        self.course=course

    def details(self):
        print(f"name:{self.name}") 
        print(f"student_id:{self.student_id}") 
        print(f"roll_no:{self.roll_no}") 
        print(f"course:{self.course}")  
 
student_1=student("charu","02303ite003","2300770130003","B.tech")

student_1.details()
