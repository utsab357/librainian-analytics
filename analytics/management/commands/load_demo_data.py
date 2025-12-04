from django.core.management.base import BaseCommand
from django.utils import timezone
from decimal import Decimal
from datetime import date, timedelta
from analytics.models import Area, Student, Payment, VisitorStat, RevenueRecord, EnrollmentTrend
import random


class Command(BaseCommand):
    help = "Load idempotent demo data for analytics app"

    def handle(self, *args, **options):
        self.stdout.write("Loading demo data...")

        # Create areas
        area_names = ["North Campus", "South Campus", "Central Hub", "East Wing", "West District"]
        areas = []
        for name in area_names:
            area, _ = Area.objects.get_or_create(name=name)
            areas.append(area)

        # Clear existing demo students/payments/stats/trends/revenue for idempotence
        # We will keep non-demo data if present by only clearing items that match our demo patterns
        # For simplicity, remove all EnrollmentTrend/RevenueRecord/VisitorStat rows created by this command
        EnrollmentTrend.objects.all().delete()
        RevenueRecord.objects.filter(amount__in=[Decimal("45000.00"), Decimal("52000.00"), Decimal("38000.00")]).delete()
        VisitorStat.objects.filter(visitors__in=[120, 140, 180]).delete()
        Payment.objects.filter(amount__in=[Decimal("125000.00")]).delete()

        # Create 1245 students distributed among areas with genders matching totals
        total_students = 1245
        male_total = 720
        female_total = 525

        # Remove previous demo students by a naive filter (names starting with DemoUser_)
        Student.objects.filter(first_name__startswith="DemoUser_").delete()

        # Distribute students
        students = []
        # assign counts roughly proportional across areas
        per_area = [int(total_students / len(areas)) for _ in areas]
        # adjust for remainder
        for i in range(total_students - sum(per_area)):
            per_area[i % len(per_area)] += 1

        # Create male and female lists
        genders = ["M"] * male_total + ["F"] * female_total
        # If totals mismatch, adjust
        if len(genders) < total_students:
            genders += [random.choice(["M", "F"]) for _ in range(total_students - len(genders))]

        random.shuffle(genders)

        idx = 0
        for area_idx, count in enumerate(per_area):
            for n in range(count):
                g = genders[idx]
                idx += 1
                first = f"DemoUser_{area_idx}_{n}"
                last = "Demo"
                # distribute registration dates across Jan/Feb/Mar of current year
                today = date.today()
                year = today.year
                month = random.choice([1, 2, 3])
                day = random.randint(1, 28)
                reg_date = date(year, month, day)
                student = Student.objects.create(
                    first_name=first,
                    last_name=last,
                    gender=g,
                    area=areas[area_idx],
                    registration_date=reg_date,
                    status="active",
                )
                students.append(student)

        # EnrollmentTrend rows - last 12 months
        today = date.today()
        for i in range(12):
            m = (today.month - i - 1) % 12 + 1
            y = today.year - ((today.month - i - 1) // 12)
            # generate demo counts in sensible range
            enrolled = random.randint(50, 350)
            EnrollmentTrend.objects.create(month=m, year=y, enrolled=enrolled)

        # RevenueRecord rows for Jan/Feb/Mar with specified numbers
        current_year = date.today().year
        RevenueRecord.objects.get_or_create(date=date(current_year, 1, 1), defaults={"amount": Decimal("45000.00")})
        RevenueRecord.objects.get_or_create(date=date(current_year, 2, 1), defaults={"amount": Decimal("52000.00")})
        RevenueRecord.objects.get_or_create(date=date(current_year, 3, 1), defaults={"amount": Decimal("38000.00")})

        # VisitorStat rows for Jan/Feb/Mar
        VisitorStat.objects.get_or_create(date=date(current_year, 1, 1), defaults={"visitors": 120})
        VisitorStat.objects.get_or_create(date=date(current_year, 2, 1), defaults={"visitors": 140})
        VisitorStat.objects.get_or_create(date=date(current_year, 3, 1), defaults={"visitors": 180})

        # Payments to make due_in_7_days = 34 and expected_collection = 125000
        # We'll create 34 payments due within next 7 days, with total sum 125000
        for p in Payment.objects.filter(due_date__gte=date.today(), due_date__lte=date.today() + timedelta(days=7)):
            p.delete()

        remaining = Decimal("125000.00")
        num_due = 34
        # distribute amounts roughly equally
        base = (remaining / num_due).quantize(Decimal("0.01"))
        for i in range(num_due):
            amt = base
            # adjust last one to match total
            if i == num_due - 1:
                amt = remaining - base * (num_due - 1)
            due = date.today() + timedelta(days=random.randint(0, 7))
            Payment.objects.create(student=random.choice(students) if students else None, amount=amt, due_date=due, status="DUE")

        self.stdout.write(self.style.SUCCESS("Demo data loaded."))
