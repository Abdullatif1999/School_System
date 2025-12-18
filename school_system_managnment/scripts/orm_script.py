from school.models import School
from faker import Faker
import random
from user.models import User
from employee.models import Employee
from student.models import Student
from clas.models import Clas
from teacher.models import Teacher
from subject.models import Subject
from django.utils import timezone
from session.models import Session
from article.models import Article
from quiz.models import Quiz , Option
from video.models import Video , Media

def create_school(faker:Faker):
    name = faker.first_name()
    types = ['primary' , 'preparatory' , 'high']
    type = types[random.randint(0,2)]
    school = School.objects.create(name=name , type=type)
    return school

def base_create_user(faker , school_id , first_name=None , last_name=None):
    user_data = {}
    user_data['first_name'] = first_name or faker.first_name()
    user_data['last_name'] = last_name or faker.last_name()
    user_data['phone'] = faker.phone_number()
    if not user_data['phone'].startswith('+'):
        user_data['phone'] = '+' + user_data['phone']
    cities = ['homs' , 'damascus']
    user_data['city'] = cities[random.randint(0,1)]
    user_data['email'] = faker.email()
    user_data['password'] = user_data['first_name']
    user_data['school_id'] = school_id
    return user_data
    

def create_superuser(faker , school_id):
    user_data = base_create_user(faker , school_id)
    user =User.objects.create_superuser(**user_data)
    return user

def create_user(faker , school_id):
    user_data = base_create_user(faker , school_id)
    user =User.objects.create_user(**user_data)
    return user

def create_member_user(faker , member):
    user_data = base_create_user(faker , school_id=member.school.id , first_name=member.first_name , last_name=member.last_name)
    user =User.objects.create_user(**user_data)
    member.user_id = user.id
    member.save()
    return user


def create_employee(faker:Faker , school_id):
    employee_data ={} 
    employee_data['first_name'] = faker.first_name()
    employee_data['last_name'] = faker.last_name()
    roles = ['manager' , 'mentor']
    employee_data['role'] = roles[random.randint(0,1)]
    employee_data['school_id'] = school_id
    employee = Employee.objects.create(**employee_data)
    return employee


def create_clas(school_id ,  name=None ):
    clases = ['1st' , '2nd' , '3th' , '4th' , '5th' , '6th' , '7th' , '8th' , '9th']
    clas_data = {}
    clas_data['name'] = name or clases[random.randint(0 , len(clases)-1)]
    clas_data['school_id'] = school_id
    clas = Clas.objects.create(**clas_data)
    return clas

def create_clases(school_id):
    clases_name = ['1st' , '2nd' , '3th' , '4th' , '5th' , '6th' , '7th' , '8th' , '9th']
    clases = []
    for clas_name in clases_name:
        clas =create_clas(school_id=school_id , name = clas_name)
        clases.append(clas)
    return clases

def create_student(faker:Faker , school_id , clas_id):
    student_data ={} 
    student_data['first_name'] = faker.first_name()
    student_data['last_name'] = faker.last_name()
    student_data['school_id'] = school_id
    student_data['date_of_birth'] = faker.date_of_birth()
    student_data['clas_id'] = clas_id
    student = Student.objects.create(**student_data)
    return student


def create_subject(faker:Faker , school_id , clas_id , clas_name):
    subject_data = {}
    subject_data['name'] = clas_name + faker.first_name()
    subject_data['school_id'] = school_id
    subject_data['clas_id'] = clas_id
    subject = Subject.objects.create(**subject_data)
    
    return subject


def craete_subjects(faker:Faker , school_id , clas_id , clas_name , number_of_subjects):
    subjects = []
    for _ in range(0 , number_of_subjects):
        subject = create_subject(faker, school_id , clas_id , clas_name)
        subjects.append(subject)
    return subjects

def get_some_subject_ides(subjects):
        subject_ides = []
        for subject in  subjects:
            x = random.randint(0,10)
            if x < 3:
                subject_ides.append(subject.id)
        return subject_ides
def create_teacher(faker:Faker , school_id , subjects):
    subjects_ides = get_some_subject_ides(subjects=subjects)
    teacher_data ={} 
    teacher_data['first_name'] = faker.first_name()
    teacher_data['last_name'] = faker.last_name()
    specializations = ['ca' , 'ph' , 'ma']
    teacher_data['specialization'] = specializations[random.randint(0,1)]
    teacher_data['school_id'] = school_id
    teacher = Teacher.objects.create(**teacher_data)
    teacher.subjects.set(subjects_ides)
    return teacher

def create_seasson(faker:Faker , school_id , subject_id ):
    session_data = {}
    session_data['title'] = faker.paragraph(nb_sentences=1)
    session_data['time_from'] = timezone.now() + timezone.timedelta(hours=random.randint(1,50))
    session_data['time_to'] = session_data['time_from'] +timezone.timedelta(hours=random.randint(1,3))
    session_data['school_id'] = school_id
    session_data['subject_id'] = subject_id
    session = Session.objects.create(**session_data)
    return session


def create_article(faker:Faker , session_id , school_id):
    article_data = {}
    article_data['title'] = faker.paragraph(nb_sentences=1)
    article_data['content'] =  faker.paragraph(nb_sentences=10)
    article_data['school_id'] = school_id
    article_data['session_id'] = session_id
    article = Article.objects.create(**article_data)
    return article

def create_quiz(faker:Faker , session_id , school_id):
    quiz_data = {}
    quiz_data['question'] = faker.paragraph(nb_sentences=2) + "?"
    quiz_data['school_id'] = school_id
    quiz_data['session_id'] = session_id
    quiz = Quiz.objects.create(**quiz_data)
    return quiz

def create_option(faker:Faker , quiz_id , is_success):
    option_data = {}

    option_data['text'] = faker.paragraph(nb_sentences=1)
    option_data['is_success'] = is_success
    option_data['quiz_id'] = quiz_id
    option = Option.objects.create(**option_data)
    return option


def create_options(faker:Faker , quiz_id):
    oprions = []
    is_success_status = [True , False , False , False]
    random.shuffle(is_success_status)
    for _ in range(0 , 4):
        option = create_option(faker , quiz_id , is_success_status.pop())
        oprions.append(option)
    return oprions


def create_video(faker:Faker , session_id , school_id , media_id):
    video_data = {}
    video_data['school_id'] = school_id
    video_data['session_id'] = session_id
    video_data['title'] = faker.paragraph(nb_sentences=1)
    video_data['media_id'] = media_id
    video = Video.objects.create(**video_data)
    return video

def create_media(faker:Faker):
    media_data = {}
    media_data['url'] = faker.image_url()
    media = Media.objects.create(**media_data)
    return media

def insert_fake_data_in_database():

    number_of_schools = 5#random.randint(1,5)
    number_of_employee = random.randint(1,5)
    number_of_students = random.randint(5,15)
    number_of_subjects = random.randint(3,8)
    number_of_teachers = random.randint(4,8)
    number_of_sessions = random.randint(10,20)
    number_of_article = random.randint(1,3)
    number_of_quiz = random.randint(5,10)
    number_of_video = random.randint(1,2)

    faker = Faker()
    for school_number in range(0 , number_of_schools):
        try:
            print(f"insert a school number {school_number}")
            school = create_school(faker=faker)
            user = create_superuser(faker=faker , school_id=school.id)
            for employee_number in range(0 , number_of_employee):
                try:
                    print(f"insert a an employee number {employee_number} in {school_number}")
                    employee = create_employee(faker , school_id=school.id)
                    user_member = create_member_user(faker , employee)
                except:
                    continue
            clases = create_clases(school_id=school.id)
            for clas in clases:
                try:
                    for student_number in range(0 , number_of_students):
                        try:
                            # print(f"insert a  student number {student_number} in class {clas.id}_id in school {school_number}")
                            student = create_student(faker , school_id=school.id , clas_id = clas.id)
                            user_member = create_member_user(faker , student)
                        except:
                            continue
                    subjects = craete_subjects(faker , school_id=school.id , clas_id=clas.id , clas_name = clas.name , number_of_subjects=number_of_subjects)
                    for teacher_number in range(0 , number_of_teachers):
                        try:
                            # print(f"insert a  teacher number {teacher_number}  in school {school_number}")
                            teacher = create_teacher(faker , school.id , subjects)
                            user_member = create_member_user(faker , teacher)
                        except:
                            continue
                    for subject in subjects:
                        try:
                            for session_number in range(0 , number_of_sessions):
                                try:
                                    # print(f"insert a session number {session_number} for subject {subject.id} in school {school_number}")
                                    sessions = []
                                    session = create_seasson(faker , school.id , subject.id)
                                    sessions.append(session)
                                    for session in sessions:
                                        try:
                                            for article_number in range(0 , number_of_article):
                                                # print(f"insert an article number {article_number} for session {session.id} for subject {subject.id} in school {school_number}")
                                                article = create_article(faker , session.id , school.id)
                                            for quiz_number in range(0 , number_of_quiz):
                                                # print(f"insert an quiz number {quiz_number} for session {session.id} for subject {subject.id} in school {school_number}")
                                                quiz = create_quiz(faker , session.id , school.id)
                                                options = create_options(faker , quiz.id)
                                            for video_number in range(0 , number_of_video):
                                                # print(f"insert an video number {video_number} for session {session.id} for subject {subject.id} in school {school_number}")
                                                media = create_media(faker)
                                                video = create_video(faker , session.id , school.id , media.id)
                                        except:
                                            continue
                                except:
                                    continue
                        except:
                            continue
                except:
                    continue
            print("#################################################################################")
        except:
            continue

def run():
    insert_fake_data_in_database()
    
