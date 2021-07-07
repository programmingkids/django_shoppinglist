from django.urls import path
from . import views

app_name = "shoppinglist"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('category/list/', views.CategoryListView.as_view(), name="category_list"),
    path('category/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category/update/<int:pk>', views.CategoryUpdateView.as_view(), name="category_update"),
    path('item/list/', views.ItemListView.as_view(), name="item_list"),
    path('item/create/', views.ItemCreateView.as_view(), name="item_create"),
    path('item/update/<int:pk>', views.ItemUpdateView.as_view(), name="item_update"),
    path('shoppinglist/list/', views.ShoppingListListView.as_view(), name="shoppinglist_list"),
    path('shoppinglist/create/', views.ShoppingListCreateView.as_view(), name="shoppinglist_create"),
    path('shoppinglist/update/<int:pk>', views.ShoppingListUpdateView.as_view(), name="shoppinglist_update"),
    path('shoppinglist/detail/<int:pk>', views.ShoppingListDetailView.as_view(), name="shoppinglist_detail"),
    path('shoppingitem/create/<int:shoppinglist_id>', views.ShoppingItemCreateView.as_view(), name="shoppingitem_create"),
    path('shoppingitem/update/<int:pk>', views.ShoppingItemUpdateView.as_view(), name="shoppingitem_update"),
]
