from rest_framework import serializers

from apps.core.models import UUIDUser as User
from apps.quizzes.models import Answer, Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)

    class Meta:
        model = Answer
        fields = ["id", "description", "right_answer"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    id = serializers.UUIDField(required=False)

    class Meta:
        model = Question
        fields = ["id", "quiz", "description", "answers"]

    def create(self, validated_data):
        answers_data = validated_data.pop("answers")
        question = Question.objects.create(**validated_data)

        for answer in answers_data:
            Answer.objects.create(question=question, **answer)

        return question

    def update(self, instance, validated_data):
        instance.description = validated_data["description"]

        answers = validated_data.get("answers")
        serializer = AnswerSerializer()

        for answer in answers:
            if answer.get("id"):
                old_answer = Answer.objects.filter(pk=answer["id"]).first()
                serializer.update(old_answer, answer)
            else:
                serializer = AnswerSerializer(data={**answer, "quiz": instance.id})
                serializer.is_valid()
                serializer.save()

        instance.save()

        return instance


class QuizSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "category", "questions", "code", "user", "status"]
        extra_kwargs = {"code": {"read_only": True}}

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")
        user = User.objects.filter(pk=self.data["user"]).first()
        quiz = Quiz.objects.create(user=user, **validated_data)

        for questions in questions_data:
            question_serializer = QuestionSerializer(data={**questions, "quiz": quiz.id})
            question_serializer.is_valid()
            question_serializer.save()

        return quiz

    def update(self, instance, validated_data):
        instance.title = validated_data["title"]
        instance.status = validated_data["status"]
        instance.category = validated_data["category"]

        questions = validated_data.get("questions")
        serializer = QuestionSerializer()

        for question in questions:
            if question.get("id"):
                old_question = Question.objects.filter(pk=question["id"]).first()

                serializer.update(old_question, question)
            else:
                serializer = QuestionSerializer(data={**question, "quiz": instance.id})
                serializer.is_valid()
                serializer.save()

        instance.save()

        return instance
