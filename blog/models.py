from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    content=models.TextField()
    slug=models.SlugField(max_length=255, null=True, blank=True)
    cover_image=CloudinaryField('image', overwrite=True, format='jpg')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        to_assign=slugify(self.title)

        # since slug which is title has to be unique, check if it exists in db 
        if Post.objects.filter(slug=to_assign).exists():
            # if true count total post doucments and add one to create a unique no and add to slug 
            to_assign=to_assign+str(Post.objects.all().count())

        self.slug=to_assign

        super().save(*args, **kwargs)



class User(models.Model):
    post=models.ForeignKey(to=Post, on_delete=models.DO_NOTHING)
    email=models.EmailField(max_length=255)
    username=models.CharField(unique=True, max_length=255)
    display_image=CloudinaryField('image', overwrite=True, format='jpg')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return self.email