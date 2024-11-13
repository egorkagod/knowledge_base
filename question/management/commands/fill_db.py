from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from question.models import Profile, Question, Answer, Tag, QuestionLike, AnswerLike
import random


class Command(BaseCommand):
    help = 'Наполняет базу данных тестовыми данными'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Количество элементов для создания')

    def handle(self, *args, **options):
        ratio = options['ratio']
        self.stdout.write(self.style.SUCCESS(f'Начало наполнения с коэффициентом: {ratio}'))


        users = []
        for i in range(ratio):
            username = f'user_{i}'
            user = User(username=username, password='password')
            users.append(user)
        User.objects.bulk_create(users)

        profiles = []
        for user in User.objects.all():
            profile = Profile(
                user=user,
                login=user.username,
                email=f'{user.username}@example.com',
                nickname=f'Nickname_{user.id}' if random.choice([True, False]) else None,
                avatar=None
            )
            profiles.append(profile)
        Profile.objects.bulk_create(profiles)

        self.stdout.write(self.style.SUCCESS(f'Создано пользователей и профилей: {ratio}'))


        tags = [Tag(name=f'Tag_{i}') for i in range(ratio)]
        Tag.objects.bulk_create(tags)
        self.stdout.write(self.style.SUCCESS(f'Создано тегов: {ratio}'))

        users = User.objects.all()
        questions = []
        for i in range(ratio * 100):
            question = Question(
                title=f'Question {i}',
                body=f'Text for question {i}',
                author=random.choice(users)
            )
            questions.append(question)

        Question.objects.bulk_create(questions)
        self.stdout.write(self.style.SUCCESS(f'Все вопросы созданы'))

        tag_objects = list(Tag.objects.all())
        for question in Question.objects.all():
            question.tags.set(tuple(random.sample(tag_objects, k=random.randint(1, min(3, len(tag_objects))))))

        self.stdout.write(self.style.SUCCESS(f'Теги раставлены'))

        answers = []
        for i in range(ratio * 100):
            answer = Answer(
                question=random.choice(questions),
                body=f'Text for answer {i}',
                correct=False,
            )
            answers.append(answer)

        Answer.objects.bulk_create(answers)
        self.stdout.write(self.style.SUCCESS(f'Создано ответов: {ratio * 100}'))

        question_likes = []
        for i in range(ratio * 200):
            question_like = QuestionLike(
                author=random.choice(users),
                question=random.choice(questions)
            )
            question_likes.append(question_like)

        QuestionLike.objects.bulk_create(question_likes)
        self.stdout.write(self.style.SUCCESS(f'Создано оценок для вопросов: {ratio * 200}'))


        answers = Answer.objects.all()
        answer_likes = []
        for i in range(ratio * 200):
            answer_like = AnswerLike(
                author=random.choice(users),
                answer=random.choice(answers)
            )
            answer_likes.append(answer_like)

        AnswerLike.objects.bulk_create(answer_likes)
        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена!'))
