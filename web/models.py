from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return '%s' %(self.user.first_name)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.IntegerField()
    msg = models.TextField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)

class Blog(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=130, blank=False)
    desc = models.TextField(blank=False)
    img = models.ImageField(default='blog_post/default.jpg', upload_to='blog_post', null=True, blank=True)
    pubdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' %(self.title)

    def save(self):
        super().save()

        pic = Image.open(self.img.path)

        if pic.height > 300 or pic.width > 300:
            output_size = (300, 300)
            pic.thumbnail(output_size)
            pic.save(self.img.path)
