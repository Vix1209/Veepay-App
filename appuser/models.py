from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #This denotes that one user is to one profile field.. ## on_delete = models.CASCADE helps handle when a user is deleted from the databse, so does his profile as well
    phone =  models.CharField(max_length=20, null = True)
    image = models.ImageField(default='person_fill_icon.png', upload_to = 'Profile_Images') #the 'avatar.jpg' is a default image which will be placed when no imgae has been added... then the "upload_to = 'Profile_Images'" will automatically create a folder Profile_Images where the images will be stored
    
    
    def __str__(self):
        return f"{self.staff.username}'s profile"