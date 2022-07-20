from rest_framework import serializers

from apps.quizzes.models import Answer, Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "description", "right_answer"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "quiz", "description", "answers"]

    def create(self, validated_data):
        answers_data = validated_data.pop("answers")
        question = Question.objects.create(**validated_data)

        for answer in answers_data:
            Answer.objects.create(question=question, **answer)

        return question


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "category", "questions", "code"]
        extra_kwargs = {"code": {"read_only": True}}

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")
        quiz = Quiz.objects.create(**validated_data)

        for questions in questions_data:
            question_serializer = QuestionSerializer(data={**questions, "quiz": quiz.id})
            question_serializer.is_valid()
            question_serializer.save()

        return quiz
