import math
import random
from datetime import datetime

from myschool.models import *

classes = {
    "OVAL": 25, 
    "RECTANGULAR": 15, 
    "CANOPY": 20, 
    "ELEVATED": 15
}
for shape in classes.keys():
    if shape in ["RECTANGULAR", "ELEVATED"]:
        has_web_support = True
    else:
        has_web_support = False
    ClassRoom.objects.create(**{
        'seating_capacity': classes.get(shape),
        'has_web_lecture_support': has_web_support,
        'shape': shape
    })



subjects = [
    "Math", "English", "Sports", "Health Science", 
    "Music", "Botany", "Zoology", "Science",
    "Political Science", "Business Administration",
    "Foreign Affairs", "Negotiations", "Philosophy",
    "Moral Science"
]

chapters = [11, 12, 13, 11, 14, 16, 18, 15, 9, 8, 12, 10, 20, 14]

per_class = [30, 30, 45, 45, 60, 90, 30, 120, 90, 30, 120, 45, 30, 60]

total = [20, 22, 30, 34, 18, 20, 16, 16, 20, 45, 22, 34, 20, 24, 40]


for i in range(14):
    d = {
        'name': subjects[i],
        'chapters': chapters[i],
        'per_class_duration': per_class[i],
        'total_duration_in_hours': total[i]
    }

    Subject.objects.create(**d)


teachers = [
    {
        'name': 'Turing',
        'date_of_joining': datetime(2017, 8, 22).date(),
        'salary': 1800000.0,
        'takes_web_lecture': True,
    },
    {
        'name': 'Dinho',
        'date_of_joining': datetime(2016, 1, 1).date(),
        'salary': 2500000.0,
        'takes_web_lecture': False
    },
    {
        'name': 'Adele',
        'date_of_joining': datetime(2015, 3, 1).date(),
        'salary': 1000000.0,
        'takes_web_lecture': False
    },
    {
        'name': 'Freddie',
        'date_of_joining': datetime(2017, 8, 1).date(),
        'salary': 2000000.0,
        'takes_web_lecture': True
    },
    {
        'name': 'Dalton',
        'date_of_joining': datetime(2017, 3, 1).date(),
        'salary': 900000.0,
        'takes_web_lecture': True
    },
    {
        'name': 'Harish',
        'date_of_joining': datetime(2017, 2, 1).date(),
        'salary': 1800000.0,
        'takes_web_lecture': False
    },
    {
        'name': 'Trump',
        'date_of_joining': datetime(2017, 8, 1).date(),
        'salary': 800000.0,
        'takes_web_lecture': False
    },
    {
        'name': 'Swaraj',
        'date_of_joining': datetime(2019, 9, 1).date(),
        'salary': 2800000.0,
        'takes_web_lecture': True
    },
    {
        'name': 'Socrates',
        'date_of_joining': datetime(2015, 6, 1).date(),
        'salary': 1150000.0,
        'takes_web_lecture': True
    }
]

subs = {
    'Turing': [1, 2],
    'Dinho': [3, 4],
    'Adele': list([2]),
    'Freddie': [2, 5],
    'Dalton': [6, 7],
    'Harish': [1, 8],
    'Trump': [9, 10, 11],
    'Swaraj': [11, 12],
    'Socrates': [13, 14]
}

for teacher in teachers:
    teacher = Teacher.objects.create(**teacher)
    subjects = Subject.objects.filter(id__in=subs.get(teacher.name))
    teacher.subjects.set(subjects)



men = [
    'James', 'John', 'Robert', 'Michael', 'William', 'David', 
    'Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher', 
    'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 
    'Steven', 'Andrew', 'Kenneth', 'Joshua', 'George', 'Kevin', 
    'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 
    'Ryan', 'Jacob', 'Gary', 'Nicholas', 'Eric', 'Stephen', 
    'Jonathan', 'Larry', 'Justin', 'Scott', 'Brandon', 'Frank', 
    'Benjamin', 'Gregory', 'Samuel', 'Raymond', 'Patrick', 'Alexander', 
    'Jack', 'Dennis', 'Jerry', 'Tyler', 'Aaron', 'Jose', 'Henry', 'Douglas', 
    'Adam', 'Peter', 'Nathan', 'Zachary', 'Walter', 'Kyle', 'Harold', 'Carl', 'Jeremy', 
    'Keith', 'Roger', 'Gerald', 'Ethan', 'Arthur', 'Terry', 'Christian', 'Sean', 
    'Lawrence', 'Austin', 'Joe', 'Noah', 'Jesse', 'Albert', 'Bryan', 'Billy', 'Bruce', 
    'Willie', 'Jordan', 'Dylan', 'Alan', 'Ralph', 'Gabriel', 'Roy', 'Juan', 'Wayne',
    'Eugene', 'Logan', 'Randy', 'Louis', 'Russell', 'Vincent', 'Philip', 'Bobby', 
    'Johnny', 'Bradley'
]


women = [
    'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 
    'Jessica', 'Sarah', 'Karen', 'Nancy', 'Margaret', 'Lisa', 'Betty', 'Dorothy', 
    'Sandra', 'Ashley', 'Kimberly', 'Donna', 'Emily', 'Michelle', 'Carol', 'Amanda', 
    'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Laura', 'Sharon', 'Cynthia', 
    'Kathleen', 'Helen', 'Amy', 'Shirley', 'Angela', 'Anna', 'Brenda', 'Pamela', 
    'Nicole', 'Ruth', 'Katherine', 'Samantha', 'Christine', 'Emma', 'Catherine', 
    'Debra', 'Virginia', 'Rachel', 'Carolyn', 'Janet', 'Maria', 'Heather', 'Diane', 
    'Julie', 'Joyce', 'Victoria', 'Kelly', 'Christina', 'Joan', 'Evelyn', 'Lauren', 
    'Judith', 'Olivia', 'Frances', 'Martha', 'Cheryl', 'Megan', 'Andrea', 'Hannah', 
    'Jacqueline', 'Ann', 'Jean', 'Alice', 'Kathryn', 'Gloria', 'Teresa', 'Doris', 
    'Sara', 'Janice', 'Julia', 'Marie', 'Madison', 'Grace', 'Judy', 'Theresa', 'Beverly', 
    'Denise', 'Marilyn', 'Amber', 'Danielle', 'Abigail', 'Brittany', 'Rose', 'Diana', 
    'Natalie', 'Sophia', 'Alexis', 'Lori', 'Kayla', 'Jane'
]

mobiles = [
    '9496499061', '9878459353', '9941361992', '9801351110', '9318156574', '9170478496', 
    '9264174955', '9972688318', '9042824020', '9094396343', '9049577892', '9452594148', 
    '9946558524', '9111848462', '9897090653', '9603020495', '9617679546', '9316746536', 
    '9216738401', '9428128169', '9575727222', '9625987130', '9092532829', '9750754937', 
    '9895287788', '9438923890', '9009447109', '9497512353', '9771383809', '9336027696', 
    '9066931235', '9762633600', '9544240434', '9955454630', '9928086953', '9106929198', 
    '9535938149', '9125836988', '9419054207', '9752088606', '9109787622', '9547248544', 
    '9285738573', '9040048425', '9586964811', '9678113857', '9033564846', '9142397935', 
    '9000938526', '9808946168', '9491114057', '9214573844', '9824566259', '9219650352', 
    '9734656780', '9322553735', '9956013670', '9012206795', '9693689262', '9217697063', 
    '9624199001', '9285249190', '9564997819', '9431388787', '9466643263', '9207622036', 
    '9385130626', '9255253507', '9890690948', '9322397872', '9162510553', '9798759693', 
    '9654184281', '9752637225', '9783737765', '9211921253', '9121404548', '9683971625', 
    '9724965067', '9864541857', '9548299453', '9866156763', '9256258193', '9529076922', 
    '9394213618', '9037861486', '9606447639', '9438172419', '9597498584', '9437430779', 
    '9177172578', '9068665779', '9251129874', '9586945119', '9031079338', '9377917746', 
    '9632394954', '9807567829', '9913237237', '9951147775'
]


men_relations = ['Father', 'Brother', 'Uncle', 'Grandfather', 'Gardian']
women_relations = ['Mother', 'Sister', 'Aunt', 'Grandmother', 'Gardian']

for i in range(100):
    d = {}
    if i%2 == 0:
        d['name'] = men[i]
        d['relation'] = men_relations[i%5]
    else:
        d['name'] = women[i]
        d['relation'] = women_relations[i%5]
    d['contact_number'] = mobiles[i]
    Relative.objects.create(**d)

for i in range(100): 
    d = {} 
    if i % 2 == 0: 
        d['name'] = women[i] 
    else: 
        d['name'] = men[i] 
    standard = random.randint(1,12) 
    year = 2020 - standard 
    month = random.randint(1, 12) 
    day = random.randint(1, 28)
    doj = datetime(year=year, month=month, day=day).date() 
    rank = random.randint(1, 100)
    poc = Relative.objects.filter(id__in=[i+1, 100-i]) 
    d['date_of_joining'] = doj 
    d['standard'] = standard 
    d['roll_no'] = i+1 
    d['rank'] = rank 
    instance = Student.objects.create(**d) 
    instance.point_of_contact.set(poc) 



web_classes = ["ELEVATED", "RECTANGULAR"]
normal_classes = ["OVAL", "CANOPY"]

teachers = Teacher.objects.all()

for teacher in teachers:
    for subject in teacher.subjects.all():
        ids = set()
        while len(ids) < 15:
            id = random.randint(1,100)
            ids.add(id)
        if teacher.takes_web_lecture:
            room = web_classes[random.randint(0,1)]
            class_room = ClassRoom.objects.get(shape=room)
        else:
            room = normal_classes[random.randint(0,1)]
            class_room = ClassRoom.objects.get(shape=room)
        students = Student.objects.filter(id__in=ids)
        d = {}
        d['class_room'] = class_room
        d['teacher'] = teacher
        d['subject'] = subject
        instance = Class.objects.create(**d)
        instance.students.set(students)