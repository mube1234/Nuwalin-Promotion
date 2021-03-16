from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .decorators import unauthenticated_user,admin_only,allowed_users
from.forms import *
from .models import Add_News

@unauthenticated_user
def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request,'Registered Successfully')
            return redirect('register')
    context={'form':form}
    return render(request,'promotion/signup.html',context)

def index(request):
    promotion_post = AttachPromotion.objects.all().order_by('-date_posted')
    context = {'promotion_post': promotion_post}
    return render(request,'promotion/index.html',context)
@login_required(login_url='login')
def notification(request):
    return render(request,'promotion/notification.html')
def forgotpassword(request):
    return render(request, 'promotion/forgot_password.html')

def promotion_listing(request):
    promotion = AttachPromotion.objects.all().order_by('-date_posted')
    question = Fqa.objects.all().order_by('-timestamp')

    paginator1 = Paginator(promotion, 3) # Show 3 posts per page
    paginator2 = Paginator(question, 2)
    page = request.GET.get('page')

    posts = paginator1.get_page(page)
    questionpost = paginator2.get_page(page)

    context={'posts': posts,
             'questionpost':questionpost,
             }
    return render(request, 'promotion/index.html',context )

def promotion_detail(request,id):
    post=get_object_or_404(AttachPromotion,id=id)
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        is_liked=True

    #for ip address
    def get_ip(request):
        address=request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip=address.split(',').strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=PromotionView(ip_address=ip,promotion=post)
    result=PromotionView.objects.filter(ip_address=ip, promotion=post)

    if len(result)==1:
        print("user exist")
    elif len(result)>1:
        print("user exist more")
    else:
        u.save()
        print("user is unique")
    count=PromotionView.objects.filter(promotion=post).count()
    print("total count is",count)
    context={
             'post':post,
             'is_liked':is_liked,
              'total_likes': post.total_likes(),
              'count': count
             }
    return render(request,'promotion/promotion_detail.html',context)
@login_required(login_url='login')
def promotion_like(request):
    post=get_object_or_404(AttachPromotion,id=request.POST.get('post_id'))
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())
@login_required(login_url='login')
def user_follower(request):
    follow=get_object_or_404(Profile,id=request.POST.get('fp_id'))
    is_follower=False
    if follow.follower.filter(id=request.user.id).exists():
        follow.follower.remove(request.user)
        is_follower = False
    else:
        follow.follower.add(request.user)
        is_follower = True
    return HttpResponseRedirect(follow.get_absolute_url2())
def helppage(request):
    return render(request, 'promotion/help.html')
@login_required(login_url='login')
def make_money(request):
    form = MoneyStartForm(initial={'user':request.user})
    if request.method == 'POST':
        form = MoneyStartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asetting')
    context = {'form': form}
    return render(request, 'promotion/make_money.html', context)
@login_required(login_url='login')
def account(request):
    return render(request, 'promotion/account.html')
@login_required(login_url='login')
def accountsetting(request):
    return render(request, 'promotion/account_setting.html')
@login_required(login_url='login')
def give_suggeestion(request):
    form = SuggestForm(initial={'user':request.user})
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'suggestion sent successfully ')
            return redirect('suggestion')

    context = {'form': form}
    return render(request, 'promotion/give_suggestion.html', context)
@login_required(login_url='login')
def ask_question(request):
    fqa = Fqa.objects.all().order_by('-timestamp')
    form = FqaForm(initial={'user':request.user})
    if request.method == 'POST':
        form = FqaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'question sent successfully ')
            return redirect('fqa')

    context = {'form': form,'fqa':fqa}
    return render(request, 'promotion/ask_question.html', context)
@login_required(login_url='login')
@admin_only
def total_suggestion(request):
    suggest=Suggestion.objects.all()
    total_suggestion=suggest.count()
    context = {'total_suggestion': total_suggestion}
    return render(request, 'promotion/dashboard.html', context)
class SuggestionListView(ListView):
    model=Suggestion
    template_name = 'promotion/view_suggestion.html'
    context_object_name = 'suggestion'
    paginate_by = 10
    ordering = ['-timestamp']

def promotion_category(request):
    form = PromotionCategory.objects.all()
    if request.method=='POST':
        if "category==publicity" in request.POST:
            return redirect('home')
        if "category==advertising" in request.POST:
            return redirect('salespromo')

    context = {'form': form}
    return render(request, 'promotion/promotion_category.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addnews(request):
    newspost = Add_News.objects.all().order_by('-date_posted')
    form=AddNewsForm(initial={'author':request.user})
    if request.method=='POST':
        form=AddNewsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'News added successfully')
            return redirect('add_news')
    context={'form':form,'newspost':newspost}
    return render(request,'promotion/add_news_form.html',context)
def readnews(request):
    newspost = Add_News.objects.filter(type='news').order_by('-date_posted')
    context = {
            'newspost': newspost,

                }
    return render(request, 'promotion/view_news.html', context)
def readentertainment(request):
    funnypost = Add_News.objects.filter(type='entertainment').order_by('-date_posted')
    context = {
            'funnypost': funnypost
                }
    return render(request, 'promotion/view_entartainment.html', context)
@login_required(login_url='login')
def salespromotionrequest(request):
    form=SalesPromotionForm(initial={'owner':request.user})
    if request.method=='POST':
        form=SalesPromotionForm(request.POST,request.FILES,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Request sent successfully')
            return redirect('sales_promo')
    context={'form':form}
    return render(request,'promotion/form_sales_promo.html',context)
@login_required(login_url='login')
def otherpromotinrequest(request):
    form=OtherPromotionForm(initial={'owner':request.user})
    if request.method=='POST':
        form=OtherPromotionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Request sent successfully')
            return redirect('otherpromotion')
    context={'form':form}
    return render(request,'promotion/form_other_promotion.html',context)
@login_required(login_url='login')
def friend_list(request):
    friend=User.objects.exclude(id=request.user.id,)
    query = request.GET.get('q')
    if query:
        friend = User.objects.filter(Q(first_name__icontains=query) |
                                    Q(last_name__icontains=query) |
                                    Q(username__icontains=query))
    context={'friendlist':friend}
    return render(request,'promotion/friend_list.html',context)
def get_all_users():
    return  User.objects.all()
def get_entertainment():
    return  Add_News.objects.filter(type='entertainment')
def get_fqa():
    return  Fqa.objects.all().order_by('-timestamp')

@login_required(login_url='login')
def friend_profile(request,id):
    profile = get_object_or_404(Profile, id=id)
    is_followed = False
    if profile.follower.filter(id=request.user.id).exists():
        is_followed = True
    fp=Profile.objects.get(user_id=id)
    context = {'fp': fp,'is_followed':is_followed}
    return render(request, 'promotion/friend_profile.html', context)
def news_detail(request,id):
    news=get_object_or_404(Add_News,id=id)
    context={'news':news,}
    return render(request,'promotion/news_detail.html',context)
def entertainment_detail(request,id):
    funny=get_object_or_404(Add_News,id=id)
    context={'funny':funny,}
    return render(request,'promotion/entertainment_detail.html',context)
@login_required(login_url='login')
def profile(request,id):
    customer = User.objects.get(id=id)
    profiles = Profile.objects.get(user=id)
    user_follower=profiles.follower.last()
    all_follower=profiles.follower.all()
    all_follows=all_follower.count()-1
    context = {'customer': customer,
               'profiles':profiles,
               'user_follower':user_follower,
               'all_follows':all_follows,
               'all_follower':all_follower,

               }

    return render(request, 'promotion/profile.html', context)
@login_required(login_url='login')
def myfollowers(request,id):
    profiles = Profile.objects.get(user=id)
    all_follower = profiles.follower.all()
    context = {
               'all_follower': all_follower,

               }

    return render(request, 'promotion/my_followers.html', context)
@login_required(login_url='login')
def editprofile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account is updated successfully!')
            return redirect('edit_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'promotion/edit_profile.html',context)
@login_required(login_url='login')
def salespromotion(request):
    form=SalesPromotionForm(initial={'owner':request.user})
    if request.method=='POST':
        form=SalesPromotionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Request submitted successfully')
            return redirect('sales_promo')
    context={'form':form}
    return render(request,'promotion/form_sales_promo.html',context)
@login_required(login_url='login')
def advertising(request):
    form=AdvertisingForm(initial={'ad_owner':request.user})
    if request.method=='POST':
        form=AdvertisingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Request submitted successfully')
            return redirect('advertising')
    context={'form':form}
    return render(request,'promotion/form_advertising.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def attachpromotion(request):
    form=AttachPromotionForm(initial={'author':request.user})
    if request.method=='POST':
        form=AttachPromotionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Promotion attached successfully')
            return redirect('attach_promotion')
    context={'form':form}
    return render(request,'promotion/attach_promotion.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def promotion_update(request,id):
    promotion = get_object_or_404(AttachPromotion,id=id)
    if request.method=='POST':
        form=EditAttachPromotionForm(request.POST or None,request.FILES, instance=promotion)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect(promotion.get_absolute_url())
    else:
        form=EditAttachPromotionForm(instance=promotion)
    context={'form':form}
    return render(request,'promotion/edit_promotion.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def news_update(request,id):
    news = get_object_or_404(Add_News,id=id)
    if request.method=='POST':
        form=EditNewsForm(request.POST or None,request.FILES, instance=news)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect(news.get_absolute_url3())
    else:
        form=EditNewsForm(instance=news)
    context={'form':form}
    return render(request,'promotion/edit_news.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def approve(request,id):
    approve = get_object_or_404(SalesPromotion, id=id)
    if request.method == 'POST':
        form = SalesPromotionConfirmForm(request.POST,request.FILES,instance=approve)
        if form.is_valid():
            form.save()
            return redirect('sales_order')
    else:
        form=SalesPromotionConfirmForm(instance=approve)
    context = {'form': form}
    return render(request, 'promotion/approve_sales_promotion.html', context)
def approve_advert(request,id):
    approve = get_object_or_404(Adertising, id=id)
    if request.method == 'POST':
        form = AdvertisementConfirmForm(request.POST,request.FILES,instance=approve)
        if form.is_valid():
            form.save()
            return redirect('advertising_order')
    else:
        form=AdvertisementConfirmForm(instance=approve)
    context = {'form': form}
    return render(request, 'promotion/approve_advert_promotion.html', context)
def approve_other(request,id):
    approve = get_object_or_404(OtherPromotion, id=id)
    if request.method == 'POST':
        form = OtherPromotionConfirmForm(request.POST,request.FILES,instance=approve)
        if form.is_valid():
            form.save()
            return redirect('other_order')
    else:
        form=AdvertisementConfirmForm(instance=approve)
    context = {'form': form}
    return render(request, 'promotion/approve_other_promotion.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletepromotion(request,id):
    promotion=get_object_or_404(AttachPromotion,id=id)
    promotion.delete()
    return redirect('home')
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletefqa(request,id):
    promotion=get_object_or_404(Fqa,id=id)
    promotion.delete()
    return redirect('home')
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteuser(request,id):
    deuser=get_object_or_404(User,id=id)
    if not request.user.is_staff:
        raise Http404()
    deuser.delete()
    return redirect('dashboard')
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    salespromo=SalesPromotion.objects.all()
    advert=Adertising.objects.all()
    other=OtherPromotion.objects.all()
    suggest=Suggestion.objects.all()
    customer=User.objects.all()
    total_user=customer.count()
    total_sales_promo=salespromo.count()
    total_other=other.count()
    total_advert=advert.count()
    total_suggestion=suggest.count()

    context={'salespromo':salespromo,'advert':advert,
             'total_sales_promo':total_sales_promo,
             'total_advert':total_advert,
             'total_user':total_user,
             'customer':customer,
             'total_suggestion':total_suggestion,
             'total_other':total_other,
}
    return render(request,'promotion/dashboard.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def viewsalesorder(request):
    salespromo = SalesPromotion.objects.all()
    context = {'salespromo': salespromo
               }
    return render(request, 'promotion/views_sales_order.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def viewadvertisingsorder(request):
    advert = Adertising.objects.all()
    context = {'advert': advert
               }
    return render(request, 'promotion/views_advertising_order.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def viewotherorder(request):
    other = OtherPromotion.objects.all()
    context = {'other': other
               }
    return render(request, 'promotion/views_other_order.html', context)
@login_required(login_url='login')
def user_order(request):
    advorder=Adertising.objects.filter(ad_owner=request.user)
    salesorder=SalesPromotion.objects.filter(owner=request.user)
    otherorder=OtherPromotion.objects.filter(owner=request.user)
    context={'advorder':advorder,
             'salesorder':salesorder,
             'otherorder':otherorder,
             }
    return render(request,'promotion/myorder.html',context)
@unauthenticated_user
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')

    context={}
    return render(request,'promotion/login.html',context)
@login_required(login_url='login')
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'password changed successfully')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'promotion/change_password.html',{'form':form})
def signout(request):
    logout(request)
    return redirect('login')
