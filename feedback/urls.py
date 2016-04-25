from django.conf.urls import url
from feedback import views


urlpatterns = [

    url(r'^user/authenticate/$',
        views.GoogleAuthenticateView.as_view(),
        name='verify'
        ),

    url(r'^user/home/$',
        views.UserHomeView.as_view(),
        name='dashboard'
        ),

    url(r'^user/signout/$',
        views.SignOutView.as_view(),
        name='signout'
        ),

    url(r'^send/$',
        views.SendFeedbackView.as_view(),
        name='send_feedback'
        ),

    url(r'^reply/(?P<reply_hash>([a-z0-9A-Z])+)$',
        views.ReplyFeedbackView.as_view(),
        name='reply_feedback'
        ),
]
