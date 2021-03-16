from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class Add_News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='newsadder')
    type = models.CharField(null=True, blank=True, max_length=100, choices=(('news', 'news'), ('entertainment', 'entertainment')))
    title=models.CharField(max_length=700)
    body=models.CharField(max_length=3000)
    image = models.ImageField()
    date_posted=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

    def get_absolute_url3(self):
        return reverse('news_detail', kwargs={'id': self.id})
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='userprofile')
    image=models.ImageField(null=True,blank=True,default="user1.png")
    address = models.CharField(null=True,blank=True, max_length=100)
    gender = models.CharField(null=True,blank=True, max_length=100,choices=(('male', 'male'), ('female', 'female')))
    work = models.CharField(null=True, blank=True, max_length=100)
    phone = models.IntegerField(null=True, blank=True,unique=True)
    follower = models.ManyToManyField(User, related_name='userfollower', blank=True)

    def get_absolute_url2(self):
        return reverse('friend_profile', kwargs={'id': self.id})

    def __str__(self):
        return self.user.username+" "+ "Profile "
class SalesPromotion(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Accepted', 'Accepted'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ownerprofile')
    business_name=models.CharField(max_length=300)
    address = models.CharField(max_length=100)
    specific_area = models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField(null=True, blank=True)
    contact_info=models.TextField(max_length=100)
    status = models.CharField(max_length=100,choices=STATUS, default='pending')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.business_name

class Adertising(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Accepted', 'Accepted'),
    )
    ad_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adownerprofile')
    business_name=models.CharField(max_length=300)
    address = models.CharField(max_length=100)
    specific_area = models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField(null=True, blank=True)
    contact_info=models.TextField(max_length=100)
    status=models.CharField(max_length=100,choices=STATUS,default='pending')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.business_name
class OtherPromotion(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Accepted', 'Accepted'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otherowner')
    description=models.TextField(max_length=2000)
    phone=models.TextField(max_length=100)
    status=models.CharField(max_length=100,choices=STATUS,default='pending')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.owner

class PromotionCategory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class AttachPromotion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorprofile')
    business_name = models.CharField(max_length=300)
    address = models.CharField(max_length=100)
    specific_area = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image1 = models.ImageField()
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    contact_info = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.business_name

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('promotion_detail', kwargs={'id': self.id})
class PromotionView(models.Model):
    promotion=models.ForeignKey(AttachPromotion,on_delete=models.CASCADE,related_name='promotype')
    ip_address=models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ip_address
class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='who')
    suggestion = models.TextField(max_length=200,)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' by ' + self.user.username
class Fqa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asker')
    question = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
class MoneyQuestion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='whosay')
    place = models.CharField(max_length=100)
    check = models.CharField(max_length=100)
    def __str__(self):
        return ' by ' + self.user.username