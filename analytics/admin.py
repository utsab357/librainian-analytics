from django.contrib import admin
from .models import Area, Student, Payment, VisitorStat, RevenueRecord, EnrollmentTrend, DashboardSnapshot


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender", "area", "registration_date", "status")
    list_filter = ("gender", "status", "area")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student", "amount", "due_date", "paid_date", "status")
    list_filter = ("status",)


@admin.register(VisitorStat)
class VisitorStatAdmin(admin.ModelAdmin):
    list_display = ("date", "visitors")


@admin.register(RevenueRecord)
class RevenueRecordAdmin(admin.ModelAdmin):
    list_display = ("date", "amount")


@admin.register(EnrollmentTrend)
class EnrollmentTrendAdmin(admin.ModelAdmin):
    list_display = ("month", "year", "enrolled")


@admin.register(DashboardSnapshot)
class DashboardSnapshotAdmin(admin.ModelAdmin):
    list_display = ("created",)
