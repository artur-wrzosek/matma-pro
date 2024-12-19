from rest_framework import serializers
from .models import School, Student, Parent, Subject, Payment, Event, BaseUser

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['id', 'username', 'phone', 'phone_prefix', 'created_by', 'created_at']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'type', 'created_by', 'created_at']

class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'username', 'grade', 'school', 'created_by', 'created_at']

class ParentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)

    class Meta:
        model = Parent
        fields = ['id', 'username', 'student', 'created_by', 'created_at']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'created_by', 'created_at']

class PaymentSerializer(serializers.ModelSerializer):
    payer = ParentSerializer(many=True)

    class Meta:
        model = Payment
        fields = ['id', 'is_paid', 'payment_dt', 'payer', 'method', 'created_by', 'created_at']

class EventSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)
    payment = PaymentSerializer()

    class Meta:
        model = Event
        fields = ['id', 'event_dt', 'online_url', 'subject', 'extended_level', 'payment', 'notes', 'was_rescheduled', 'created_by', 'created_at']
