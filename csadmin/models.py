from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=255)
    video = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='pic.png', null=True)
    dob = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    address = models.TextField(blank=True)
    def __str__(self):  
        return self.user.username
    
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pictures', null=True, blank=True)
    posttitle = models.CharField(max_length=150)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    
    def likes_count(self):
        return self.likes.count()
    
    def __str__(self):
        return self.posttitle
    class Meta:
        ordering = ['-post_date']
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    class Meta:
        ordering = ['-comment_date']
        