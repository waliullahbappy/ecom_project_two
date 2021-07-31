from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


# Categories Model Start From Here
class Categories(models.Model):
    status = (
        ('True','True'),
        ('False','False'),
    )
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='category/')
    status = models.CharField(max_length=20,choices=status)
    slug = models.SlugField(null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title
# Categories Model end Here 
     
     
     
     
# Products Model Start From Here       
class Products(models.Model):
    status = (
        ('True','True'),
        ('False','False'),
    )
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='products/')
    old_price = models.DecimalField(decimal_places=2,max_digits=15,default=0)
    new_price = models.DecimalField(decimal_places=2,max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    details = models.TextField()
    status = models.CharField(max_length=20,choices=status)
    slug = models.SlugField(null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    
    def __str__(self):
        return self.title
    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ''
        
    
# Products Model end Here 

# images Model for Every Products

class Images(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(blank=True,upload_to='products/')
    
    def __str__(self):
        return self.title
    