from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.utils import timezone
from decimal import Decimal
from .serializers import (
    KeyStatsSerializer,
    EngagementOverviewSerializer,
    FinancialSnapshotSerializer,
    ChartsSerializer,
    GenderDistributionSerializer,
    StudentsByAreaSerializer,
)


class KeyStatsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Demo numbers matching user's specification
        payload = {
            "total_students": 1245,
            "male_students": 720,
            "female_students": 525,
            "this_month_registrations": 89,
            "growth_rates": {
                "total": "+12.5%",
                "male": "+8.3%",
                "female": "+18.2%",
                "registrations": "+15.4%",
            },
        }
        ser = KeyStatsSerializer(payload)
        return Response(ser.data)


class EngagementOverviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        payload = {
            "new_registrations": 156,
            "expected_collection": Decimal("125000.00"),
            "due_in_7_days": 34,
            "total_visitors": 5620,
            "growth": {"registrations": "+3.2%", "visitors": "+1.1%"},
        }
        ser = EngagementOverviewSerializer(payload)
        return Response(ser.data)


class FinancialSnapshotView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        payload = {
            "yesterdays_balance": Decimal("450000.00"),
            "todays_collection": Decimal("75000.00"),
            "total_visitors": 5620,
        }
        ser = FinancialSnapshotSerializer(payload)
        return Response(ser.data)


class EnrollmentTrendsChartView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        period = request.query_params.get("period", "3m")
        # Demo monthly points (labels and values)
        data = [
            {"label": "Jan", "value": Decimal("12")},
            {"label": "Feb", "value": Decimal("19")},
            {"label": "Mar", "value": Decimal("15")},
        ]
        ser = ChartsSerializer({"title": "Enrollment Trends", "data": data})
        return Response(ser.data)


class GenderDistributionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        payload = {"male": 55, "female": 45}
        ser = GenderDistributionSerializer(payload)
        return Response(ser.data)


class MonthlyRevenueChartView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = [
            {"label": "Jan", "value": Decimal("45000")},
            {"label": "Feb", "value": Decimal("52000")},
            {"label": "Mar", "value": Decimal("38000")},
        ]
        ser = ChartsSerializer({"title": "Monthly Revenue", "data": data})
        return Response(ser.data)


class VisitorAnalyticsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = [
            {"label": "Jan", "value": Decimal("120")},
            {"label": "Feb", "value": Decimal("140")},
            {"label": "Mar", "value": Decimal("180")},
        ]
        ser = ChartsSerializer({"title": "Visitor Analytics", "data": data})
        return Response(ser.data)


class StudentsByAreaView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Demo list as requested
        payload = [
            {"area": "North Campus", "count": 285, "trend": "+12%"},
            {"area": "South Campus", "count": 320, "trend": "+18%"},
            {"area": "Central Hub", "count": 245, "trend": "0%"},
            {"area": "East Wing", "count": 195, "trend": "-8%"},
            {"area": "West District", "count": 200, "trend": "+14%"},
        ]
        ser = StudentsByAreaSerializer(payload, many=True)
        return Response(ser.data)


class RevenueVisitorsCombinedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Return the revenue chart and visitor analytics together
        revenue = [
            {"label": "Jan", "value": Decimal("45000")},
            {"label": "Feb", "value": Decimal("52000")},
            {"label": "Mar", "value": Decimal("38000")},
        ]
        visitors = [
            {"label": "Jan", "value": Decimal("120")},
            {"label": "Feb", "value": Decimal("140")},
            {"label": "Mar", "value": Decimal("180")},
        ]
        return Response({"revenue": {"title": "Monthly Revenue", "data": revenue}, "visitors": {"title": "Visitor Analytics", "data": visitors}})
