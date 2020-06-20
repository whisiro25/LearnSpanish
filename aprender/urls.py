from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('tense', views.tense, name='tense'),
    path('tense/<str:id>', views.tense, name='tense'),
    path('vocab', views.vocab, name='vocab'),
    path('vocab/<str:id>', views.vocab, name='vocab'),
    path('grammar', views.grammar, name='grammar'),
    path('grammar/<str:id>', views.grammar, name='grammar'),
    path('practice', views.practice, name='practice'),
   # path('practice/<slug:the_slug>', views.practice, name='practice'),
    path('practice/<str:id>', views.practice, name='practice'),
    path('update_session/',views.update_session,name='updateSession'),
    path('help',views.help,name='help'),

]