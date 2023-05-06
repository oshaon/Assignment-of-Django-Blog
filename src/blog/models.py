from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Blog_info(models.Model):
    blog_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    nav_logo = models.ImageField(upload_to='nav_logo/', null=True, blank=True)

    def __str__(self):
        return self.blog_name

class Blog_section(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null= True)

    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Category.objects.filter(slug = self.slug).exists():
                self.slug = f'{slugify(self.title)}-{get_random_string(3)}'
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = 'Categories'




class BlogPost(models.Model):
    STATUS =[
        ('draft','Draft'),
        ('pubished', 'Publish')
    ]

    title = models.CharField(max_length=200)
    featured_img = models.ImageField(upload_to= 'blogs/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default='published')
    
    meta_title = models.CharField(max_length=200, blank= True, null=True)
    meta_description = models.CharField(max_length=200, null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while BlogPost.objects.filter(slug = self.slug).exists():
                self.slug = f'{slugify(self.title)}-{get_random_string(4)}'
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blog posts"

