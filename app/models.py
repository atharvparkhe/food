from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from froala_editor.fields import FroalaField
from base.models import *
from authentication.models import *

class ContactUs(BaseModel):
    user = models.ForeignKey(CustomerModel, related_name="contactus", on_delete=models.CASCADE)
    message = models.TextField()

class BlogModel(BaseModel):
    author = models.ForeignKey(BaseUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    img = models.ImageField(upload_to='blog')
    def __str__(self) :
        return self.title

class BlogCommentsModel(BaseModel):
    blog = models.ForeignKey(BlogModel, related_name="related_blog", on_delete=models.CASCADE)
    commenter = models.ForeignKey(BaseUser, on_delete=models.PROTECT)
    comment = models.TextField()

@receiver(post_save, sender=BlogModel)
def generate_slug(sender,instance,created, **kwargs):
    instance.slug = slugify(instance.title)

class Newsletter(BaseModel):
    subject = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    content = FroalaField()
    to = models.ForeignKey(CustomerModel, related_name="newsletter_list", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="newsletter", max_length=None, null=True, blank=True)
    attachments = models.FileField(upload_to="newsletter", max_length=100, null=True, blank=True)
