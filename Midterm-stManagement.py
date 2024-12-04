import time, os, json



def loadStudents():
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            data = json.load(file)
            return [Student(student["Name"], student["Roll Number"], student["Grade"]) for student in data]
    return []

def makeRecords(students_data):
    with open("students.json", "w") as file:
        json.dump([student.to_dict() for student in students_data], file, indent=2)




# creating list for uniqueness 
roll_number_list = []

class Student:

    def __init__(self, name : str, roll_number : int, grade : str) -> None:
        self.__name = name
        self.__roll_number = roll_number 
        self.__grade = grade


    def to_dict(self):
        return {
            "Name": self.__name,
            "Roll Number": self.__roll_number,
            "Grade": self.__grade
        }

    @property
    def name(self):
        return self.__name
    
    @property
    def roll_number(self):
        return self.__roll_number
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if len(value) > 1 or value.upper() not in ["A","B","C","D","F"]:
            raise ValueError("შეფასება უნდა იყოს ერთი ასობგერა! [A,B,C,D,F]\n")
        
        self.__grade = value

    




def showMenu():
    return input("1 - ახალი სტუდენტის დამატება\n"
                 "2 - ყველა სტუდენტის ნახვა\n"
                 "3 - სტუდენტის ძებნა ნომრის მიხედვით\n"
                 "4 - მოსწავლის შეფასების განახლება\n"
                 "EXIT - გასვლა\n"
                 "აირჩიეთ: ")
        
def addStudent(name, roll_number, grade):
    # case when student with inputted roll_number is already exists
    if roll_number in roll_number_list:
        raise ValueError("ეს რიცხვი უკვე სიაშია!\n")
    
    # in case if roll_number is not an integer, considering isinstance() and eval() functions
    try:
        if not isinstance(eval(roll_number),int):
            raise ValueError("სიის ნომერი უნდა იყოს მთელი რიცხვი!\n")
    except Exception as ex:
        raise ValueError("სიის ნომერი უნდა იყოს მთელი რიცხვი!\n")
    
    if len(grade) > 1 or grade.upper() not in ["A","B","C","D","F"]:
        raise ValueError("შეფასება უნდა იყოს ერთი ასობგერა! [A,B,C,D,F]\n")
    

    temp = Student(name, int(roll_number), grade.upper())
    studentList.append(temp)  
    roll_number_list.append(int(roll_number))
    makeRecords(studentList)
    print(f"ახალი სტუდენტი, {name}, დამატებულია.")


def searchStudent(roll_number):
    if not isinstance(eval(roll_number),int):
        raise ValueError("სიის ნომერი აუცილებლად უნდა იყოს მთელი რიცხვი! ")
    
    roll_number = int(roll_number)
    for i in studentList:
        if i.roll_number == roll_number:
            return i
        
    raise ValueError("სტუდენტი ამ სიის ნომრით არ არსებობს!\n")


def programExit():
    time.sleep(0.5)
    print("\nპროგრამა ითიშება...\n")
    time.sleep(1)


if __name__ == "__main__":
    # saving all students for future use
    studentList = loadStudents()
    while True:

        ans = showMenu()
        
        # case when input is invalid
        if ans not in ["1","2","3","4","EXIT"]:
            
            print("\n! ციფრი უნდა აირჩიო 1-დან 4-ის ჩათვლით ან 'EXIT'!\n\n")
            continue

        if ans == "EXIT":
            programExit()
            break

        # adding a student
        if ans == "1":
            tempAns = ""
            while tempAns != "N":
                try:
                    addStudent(input("სახელი: "),input("სიის ნომერი: "),input("შეფასება: "))
                    print("\n")
                    break
                except ValueError as ex:
                    print(ex)

                    # checking if user really wants to add a new student or just exit from adding one
                    tempAns = input("გსურთ მოსწავლის დამატება? Y/N: ").upper()
                    print("\n")
                    continue
            else:
                continue

        elif ans == "2":

            # just pretty print students
            print(f"| {'სახელი':^16} | {'სიის ნომერი':^16} | {'შეფასება':^16} |")
            for i in studentList:
                print(f"| {i.name:^16} | {i.roll_number:^16} | {i.grade:^16} |")
            print("\n")

        
        elif ans == "3":
            tempAns = ""
            while tempAns != "N":
                try:
                    st = searchStudent(input("შეიყვანეთ სიის ნომერი: "))
                    print(f"| {'სახელი':^16} | {'სიის ნომერი':^16} | {'შეფასება':^16} |")
                    print(f"| {st.name:^16} | {st.roll_number:^16} | {st.grade:^16} |\n")

                    # after successful search, we ask user if he/she wants to search more
                    tempAns = input("კიდევ გსურთ სტუდენტის მოძებნა? Y/N: ").upper()
                    print("\n")
                    continue

                except ValueError as ex:
                    print(ex)

                    # checking if user really wants to search a student
                    tempAns = input("გსურთ სტუდენტის მოძებნა? Y/N: ").upper()
                    print("\n")
                    continue
            else:
                continue
        
        
        elif ans == "4":
            tempAns = ""
            while tempAns != "N":
                try:
                    st = searchStudent((input("შეიყვანეთ სტუდენტის ნომერი, რომლის შეფასების განახლებაც გინდათ: ")))
                    value = input("შეიყვანეთ ახალი შეფასება: ")
                    st.grade = value
                    makeRecords(studentList)

                    time.sleep(0.5)
                    print("\nშეფასება განახლებულია\n")
                    time.sleep(0.5)

                    tempAns = input("კიდევ გსურთ რომელიმე სტუდენტის შეფასების განახლება? Y/N: ").upper()
                    print("\n")
                    continue

                except ValueError as ex:
                    print(ex)

                    tempAns = input("გსურთ რომელიმე სტუდენტის შეფასების განახლება? Y/N: ").upper()
                    print("\n")
                    continue