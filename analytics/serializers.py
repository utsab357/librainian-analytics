from rest_framework import serializers
from .models import Area, Student, Payment, VisitorStat, RevenueRecord, EnrollmentTrend


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "name"]


class StudentSerializer(serializers.ModelSerializer):
    area = AreaSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "area", "registration_date", "status"]


class PaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ["id", "student", "amount", "due_date", "paid_date", "status"]


class VisitorStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorStat
        fields = ["id", "date", "visitors"]


class RevenueRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueRecord
        fields = ["id", "date", "amount"]


class EnrollmentTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentTrend
        fields = ["id", "month", "year", "enrolled"]


# --- Custom serializers for dashboards ---
class KeyStatsSerializer(serializers.Serializer):
    total_students = serializers.IntegerField()
    male_students = serializers.IntegerField()
    female_students = serializers.IntegerField()
    this_month_registrations = serializers.IntegerField()
    growth_rates = serializers.DictField(child=serializers.CharField())


class EngagementOverviewSerializer(serializers.Serializer):
    new_registrations = serializers.IntegerField()
    expected_collection = serializers.DecimalField(max_digits=14, decimal_places=2)
    due_in_7_days = serializers.IntegerField()
    total_visitors = serializers.IntegerField()
    growth = serializers.DictField(child=serializers.CharField())


class FinancialSnapshotSerializer(serializers.Serializer):
    yesterdays_balance = serializers.DecimalField(max_digits=14, decimal_places=2)
    todays_collection = serializers.DecimalField(max_digits=14, decimal_places=2)
    total_visitors = serializers.IntegerField()


class ChartPointSerializer(serializers.Serializer):
    label = serializers.CharField()
    value = serializers.DecimalField(max_digits=14, decimal_places=2)


class ChartsSerializer(serializers.Serializer):
    title = serializers.CharField()
    data = serializers.ListField(child=serializers.DictField())


class GenderDistributionSerializer(serializers.Serializer):
    male = serializers.IntegerField()
    female = serializers.IntegerField()


class StudentsByAreaSerializer(serializers.Serializer):
    area = serializers.CharField()
    count = serializers.IntegerField()
    trend = serializers.CharField()
