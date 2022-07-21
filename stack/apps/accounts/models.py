from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.template.defaultfilters import slugify



from .managers import CustomUserManager
from . import utils
# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    slug = models.SlugField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    class Meta:
        ordering = ['email']
        verbose_name = 'User'

    # returning the username as an identifier 
    def __str__(self):
        return self.email
    
    
    def gen_rand_slug(self):
    # creating a default slug/username for users if blank
        random_slug = slugify(self.first_name + self.last_name + utils.generates_random_id())
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(self.first_name + self.last_name + utils.generates_random_id())
        return random_slug
    def save(self, *args, **kwargs):
        #performs a logic that checks for slug and if not create 
        if not self.slug:
            #create default slug
            self.slug = self.gen_rand_slug()
        
        # finally save
        super().save(*args, **kwargs)

