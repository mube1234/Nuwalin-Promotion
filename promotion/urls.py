from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from. import views

urlpatterns = [
    path('',views.promotion_listing,name='home'),
    path('signup/',views.signup,name='register'),
    path('add_news/',views.addnews, name='add_news'),
    path('news/',views.readnews, name='news'),
    path('account_setting/',views.accountsetting, name='asetting'),
    path('entertainment/',views.readentertainment, name='entertainment'),
    path('news_detail/<int:id>',views.news_detail, name='news_detail'),
    path('updatepro/<int:id>',views.promotion_update, name='update'),
    path('updatenews/<int:id>',views.news_update, name='news_update'),
    path('delete_promotion/<int:id>', views.deletepromotion, name='delete_promotion'),
    path('delete_fqa/<int:id>', views.deletefqa, name='deletefqa'),
    path('delete_user/<int:id>', views.deleteuser, name='deleteuser'),
    path('entertainment_detail/<int:id>',views.entertainment_detail, name='entertainment_detail'),
    path('edit_profile/',views.editprofile, name='edit_profile'),
    path('profile/<str:id>',views.profile, name='profile'),
    path('myfollower/<str:id>',views.myfollowers, name='my_follower'),
    path('help/',views.helppage,name='help'),
    path('approve/<str:id>',views.approve,name='approve'),
    path('approve2/<str:id>',views.approve_advert,name='approve2'),
    path('other_approve/<str:id>',views.approve_other,name='other_approve'),
    path('friend_list/',views.friend_list,name='friend_list'),
    path('promotion_category/',views.promotion_category,name='promotion_category'),
    path('sales_promo/',views.salespromotion,name='sales_promo'),
    path('advertising/',views.advertising,name='advertising'),
    path('other/',views.otherpromotinrequest,name='otherpromotion'),
    path('attach_promotion/',views.attachpromotion,name='attach_promotion'),
    path('promotion_detail/<int:id>', views.promotion_detail, name='promotion_detail'),
    path('promotion_like/', views.promotion_like, name='promotion_like'),
    path('user_follower/', views.user_follower, name='user_follower'),
    path('user_order/', views.user_order, name='userorder'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/salespromo',views.viewsalesorder,name='sales_order'),
    path('dashboard/advert',views.viewadvertisingsorder,name='advertising_order'),
    path('dashboard/other',views.viewotherorder,name='other_order'),
    path('friend/<str:id>',views.friend_profile,name='friend_profile'),
    path('login/',views.signin,name='login'),
    path('change_password/', views.change_password, name='change_password'),
    path('account/', views.account, name='account'),
    path('give_suggestion/', views.give_suggeestion, name='suggestion'),
    path('ask_question/', views.ask_question, name='fqa'),
    path('notification/', views.notification, name='notification'),
    path('let_try/', views.make_money, name='make_money'),
    path('suggestion/view', views.SuggestionListView.as_view(), name='view_suggestion'),
    path('forgot_password/',views.forgotpassword,name='forgot_password'),
    path('logout/',views.signout,name='logout')
    ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)