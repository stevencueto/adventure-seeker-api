from django.urls import path
from . import views
from .views import UserPost

urlpatterns = [
    path('api/post/', views.PostList.as_view(), name='post_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/post/user/', UserPost.as_view({'get': 'list', 'post': 'create'})), # api/contacts will be routed to the ContactDetail view for handling
    path('api/post/<int:pk>', views.PostDetail.as_view(), name='post_detail'), # api/contacts will be routed to the ContactDetail view for handling
]


