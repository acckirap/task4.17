from django.urls import path

from apps.shop.views import CategoriesView, ProductView, ProductsView, ProductsByCategoryView, ProductsBySellerView, \
    CartView, CheckoutView, ReviewView#, ReviewViewUUID

urlpatterns = [
    path("categories/", CategoriesView.as_view()),
    path("categories/<slug:slug>/", ProductsByCategoryView.as_view()),
    path("sellers/<slug:slug>/", ProductsBySellerView.as_view()),
    path("products/", ProductsView.as_view()),
    path('products/<slug:slug>/reviews/', ReviewView.as_view()),
    #path('products/reviews/<str:uuid>/', ReviewViewUUID.as_view()),
    path("products/<slug:slug>/", ProductView.as_view()),
    path("cart/", CartView.as_view()),
    path("checkout/", CheckoutView.as_view()),]