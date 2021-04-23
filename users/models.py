from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import time, datetime
from django.db.models import Q



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    dream = models.CharField(max_length=10, null=True)
    hobby = models.CharField(max_length=10, null=True)
    nickname = models.CharField(max_length=10, null=True, unique=True)
    interest = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class JProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ORIENTATION = (
        ("progressivism", "진보"),
        ("centrism", "중도/선택안함"),
        ("conservatism", "보수")
    )

    political_orientation = models.CharField(
        max_length=15,
        choices=ORIENTATION,
        null=True,
        help_text="정치성향"
    )

    eighteen = 18
    seventeen = 17
    sixteen = 16
    fifteen = 15
    fourteen = 14
    thirteen = 13
    twelve = 12
    eleven = 11
    ten = 10
    nine = 9
    eight = 8
    seven = 7
    six = 6
    five = 5
    four = 4
    three = 3
    two = 2
    one = 1

    LEVEL_CHOICES = (
        (eighteen, "從九品"),
        (seventeen, "正九品"),
        (sixteen, "從八品"),
        (fifteen, "正八品"),
        (fourteen, "從七品"),
        (thirteen, "正七品"),
        (twelve, "從六品"),
        (eleven, "正六品"),
        (ten, "從五品"),
        (nine, "正五品"),
        (eight, "從四品"),
        (seven, "正四品"),
        (six, "從三品"),
        (five, "正三品"),
        (four, "從二品"),
        (three, "正二品"),
        (two, "從一品"),
        (one, "正一品"),
    )

    levels = models.PositiveIntegerField(
        default=18,
        null=True,
        choices=LEVEL_CHOICES
    )

    position = models.CharField(max_length=10, null=True, default="없음", blank=True)

    DEPARTMENT_CHOICES = (
        ('d','선택안함'),
        ('MSIT','공조'),
        ('MPM','이조'),
        ('BAI','사간원'),
        ('SPO','사헌부'),
        ('NPA','의금부')
    )
    department = models.CharField(
        max_length=10,
        choices=DEPARTMENT_CHOICES,
        null=True,
        default='d'
    )

    def __str__(self):
        return self.user.username

class Coin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blackcoin = models.PositiveIntegerField(default=0, null=True)
    bluecoin = models.PositiveIntegerField(default=0, null=True)
    greencoin = models.PositiveIntegerField(default=0, null=True)
    orangecoin = models.PositiveIntegerField(default=0, null=True)
    pinkcoin = models.PositiveIntegerField(default=0, null=True)
    purplecoin = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    spear = models.PositiveIntegerField(default=0, null=True)
    shield = models.PositiveIntegerField(default=0, null=True)
    sword = models.PositiveIntegerField(default=0, null=True)
    armor = models.PositiveIntegerField(default=5, null=True)
    getsword = models.PositiveIntegerField(default=0, null=True)
    letter = models.PositiveIntegerField(default=0, null=True)
    star = models.PositiveIntegerField(default=0, null=True)
    reference_letter = models.PositiveIntegerField(default=0, null=True)
    refutation = models.PositiveIntegerField(default=0, null=True)
    impeachment = models.PositiveIntegerField(default=0, null=True)
    swordOfGod = models.PositiveIntegerField(default=0, null=True)
    spearOfGod = models.PositiveIntegerField(default=0, null=True)
    shieldOfGod = models.PositiveIntegerField(default=0, null=True)
    recommended = models.PositiveIntegerField(default=0, null=True)
    impeached = models.PositiveIntegerField(default=0, null=True)
    accused = models.PositiveIntegerField(default=0, null=True)
    impeachment_shield = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.user.username

    def get_total_sword(self):
        return self.getsword - self.armor

    def get_total_impeached(self):
        return self.impeached - self.impeachment_shield


class Certificate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MSITcertificate = models.PositiveIntegerField(default=0, null=True)
    MPMcertificate = models.PositiveIntegerField(default=0, null=True)
    BAIcertificate = models.PositiveIntegerField(default=0, null=True)
    SPOcertificate = models.PositiveIntegerField(default=0, null=True)
    NPAcertificate = models.PositiveIntegerField(default=0, null=True)
    OPCcertificate = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.user.username


class UserKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MSITfirstkey = models.PositiveIntegerField(default=0, null=True)
    MSITsecondkey = models.PositiveIntegerField(default=0, null=True)
    MSITthirdkey = models.PositiveIntegerField(default=0, null=True)
    MSITfourthkey = models.PositiveIntegerField(default=0, null=True)
    MSITfifthkey = models.PositiveIntegerField(default=0, null=True)

    MPMfirstkey = models.PositiveIntegerField(default=0, null=True)
    MPMsecondkey = models.PositiveIntegerField(default=0, null=True)
    MPMthirdkey = models.PositiveIntegerField(default=0, null=True)
    MPMfourthkey = models.PositiveIntegerField(default=0, null=True)
    MPMfifthkey = models.PositiveIntegerField(default=0, null=True)

    BAIfirstkey = models.PositiveIntegerField(default=0, null=True)
    BAIsecondkey = models.PositiveIntegerField(default=0, null=True)
    BAIthirdkey = models.PositiveIntegerField(default=0, null=True)
    BAIfourthkey = models.PositiveIntegerField(default=0, null=True)

    SPOfirstkey = models.PositiveIntegerField(default=0, null=True)
    SPOsecondkey = models.PositiveIntegerField(default=0, null=True)
    SPOthirdkey = models.PositiveIntegerField(default=0, null=True)
    SPOfourthkey = models.PositiveIntegerField(default=0, null=True)
    SPOfifthkey = models.PositiveIntegerField(default=0, null=True)

    NPAfirstkey = models.PositiveIntegerField(default=0, null=True)
    NPAsecondkey = models.PositiveIntegerField(default=0, null=True)
    NPAthirdkey = models.PositiveIntegerField(default=0, null=True)
    NPAfourthkey = models.PositiveIntegerField(default=0, null=True)
    NPAfifthkey = models.PositiveIntegerField(default=0, null=True)

    OPCfirstkey = models.PositiveIntegerField(default=0, null=True)
    OPCsecondkey = models.PositiveIntegerField(default=0, null=True)
    OPCthirdkey = models.PositiveIntegerField(default=0, null=True)
    OPCfourthkey = models.PositiveIntegerField(default=0, null=True)
    OPCfifthkey = models.PositiveIntegerField(default=0, null=True)
    OPCsixthkey = models.PositiveIntegerField(default=0, null=True)
    OPCseventhkey = models.PositiveIntegerField(default=0, null=True)

    SSkey = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.user.username

class Ranker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rankpoint = models.PositiveIntegerField(default=0, null=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-rankpoint"]

class Classification(models.Model):
    political_orientation = models.CharField(max_length=15)
    numberOfUser = models.PositiveIntegerField(default=1)
    date_changed = models.DateTimeField(auto_now=True)
