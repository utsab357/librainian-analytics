from django.db import models
from django.utils import timezone
from decimal import Decimal


class Area(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    STATUS_CHOICES = (("active", "Active"), ("inactive", "Inactive"))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, related_name="students")
    registration_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payment(models.Model):
    STATUS_CHOICES = (("DUE", "Due"), ("PAID", "Paid"))

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name="payments")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="DUE")

    def __str__(self):
        return f"Payment {self.amount} - {self.status} ({self.student})"


class VisitorStat(models.Model):
    date = models.DateField()
    visitors = models.IntegerField()

    class Meta:
        verbose_name = "Visitor Stat"
        verbose_name_plural = "Visitor Stats"

    def __str__(self):
        return f"{self.date}: {self.visitors} visitors"


class RevenueRecord(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal("0.00"))

    def __str__(self):
        return f"{self.date}: {self.amount}"


class EnrollmentTrend(models.Model):
    month = models.IntegerField()  # 1-12
    year = models.IntegerField()
    enrolled = models.IntegerField()

    class Meta:
        unique_together = ("month", "year")

    def __str__(self):
        return f"{self.month}/{self.year}: {self.enrolled}"


class DashboardSnapshot(models.Model):
    # Optional single-row table to cache computed numbers
    created = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(default=dict)

    def __str__(self):
        return f"Snapshot {self.created.isoformat()}"
