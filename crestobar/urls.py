from django.urls import path
from . import views
from .views import login_view
urlpatterns = [
    path('', views.home_page, name = 'Homepage'),
    path('reservation/', views.reservation_page, name = 'reservation'),
    path('baradmin/', views.admin_page, name = 'admin'),
    path('product/', views.product_page, name = 'product'),
    path('table/', views.table_page, name = 'table'),
    path('r_form/', views.r_form_page, name = 'r_form'),
    path('T_add/', views.T_add_page, name = 'T_add'),
    path('delete/<int:id>', views.deleteTable, name = 'delete'),
    path('delete_reserve/<int:id>', views.deleteReservation, name = 'deleteR'),
    path('delete_prod/<int:id>', views.deleteProduct, name = 'deleteP'),
    path('product_add/', views.p_add_page, name = 'product_add'),
    path('update_reservation/<reservation_id>', views.update_reservation, name = 'update_reservation'),
    path('update_product/<product_id>', views.update_product, name = 'update_product'),
    path('update_table/<table_id>', views.update_table, name = 'update_table'),
    path('login/', login_view, name='login'),









]