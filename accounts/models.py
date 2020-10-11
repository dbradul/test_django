from PIL import Image
from django.contrib.auth.models import User
from django.db import models

class UserActions(models.Model):
    class USER_ACTION(models.IntegerChoices):
        LOGIN = 0, "Login"
        LOGOUT = 1, "Logout"
        CHANGE_PASSWORD = 2, "Change Password"
        CHANGE_PROFILE = 3, "Change Profile"
        CHANGE_PROFILE_IMAGE = 4, "Change Profile Image"

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    write_date = models.DateTimeField(auto_now_add=True)
    action = models.PositiveSmallIntegerField(choices=USER_ACTION.choices)
    info = models.CharField(max_length=128, null=True)


class Profile(models.Model):
    user = models.OneToOneField(
        to=User, # settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = models.ImageField(null=True, default='default.jpg', upload_to='pics/')
    interests = models.CharField(max_length=128, null=True)

    # def save(self, **kwargs):
    #     print('')



    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        img = Image.open(self.user.profile.image.file.name)
        width = img.width
        height = img.height
        new_width = 300

        if width > new_width:
            percent = (new_width/width)
            new_height = int(height*percent)
            new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
            new_img.save(self.user.profile.image.file.name, 'JPEG')

        return result