import factory
from factory import fuzzy

from apps.core.models import UUIDUser
from apps.quizzes.models import Answer, Category, Question, Quiz


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UUIDUser

    username = "mblopes"

    email = "bbbbbb@gmail.com"

    first_name = "Matheus"

    last_name = "Bachiste Lopes"

    password = "mtbl2706"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")


class QuizFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quiz

    title = factory.Faker("name")

    category = factory.SubFactory(CategoryFactory)

    user = factory.SubFactory(UserFactory)

    status = "public"


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer

    description = factory.Faker("sentence")

    right_answer = fuzzy.FuzzyChoice(choices=[True, False])


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    description = factory.Faker("sentence")

    answers = factory.SubFactory(AnswerFactory)
