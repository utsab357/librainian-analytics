from django.urls import path
from . import views

urlpatterns = [
    path("key-stats/", views.KeyStatsView.as_view(), name="key-stats"),
    path("engagement-overview/", views.EngagementOverviewView.as_view(), name="engagement-overview"),
    path("financial-snapshot/", views.FinancialSnapshotView.as_view(), name="financial-snapshot"),
    path("charts/enrollment-trends/", views.EnrollmentTrendsChartView.as_view(), name="enrollment-trends"),
    path("charts/gender-distribution/", views.GenderDistributionView.as_view(), name="gender-distribution"),
    path("charts/monthly-revenue/", views.MonthlyRevenueChartView.as_view(), name="monthly-revenue"),
    path("charts/visitor-analytics/", views.VisitorAnalyticsView.as_view(), name="visitor-analytics"),
    path("students-by-area/", views.StudentsByAreaView.as_view(), name="students-by-area"),
    path("revenue-visitors/", views.RevenueVisitorsCombinedView.as_view(), name="revenue-visitors"),
]
