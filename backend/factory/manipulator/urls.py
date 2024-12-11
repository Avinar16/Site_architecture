"""
АВТОРИЗАЦИЯ
Добавить url на classes
добавить classes
запросы к бд
темплейты на фронт
сделать корс
логика7?

"""
from django.urls import path
from .views import send_report, move, load_grid, grab, get_reports, load_save


app_name = 'manipulator'
urlpatterns = [
    path("command/", move, name="move_manipulator"),
    path("load/", load_grid, name="load_grid"),
    path("grab/", grab, name="grab"),
    path("send_report/", send_report, name='send_report'),
    path("get_reports/", get_reports, name='get_reports'),
    path('load_save/', load_save, name='load_save')
]
