from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    contents = models.TextField(max_length=1400)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joseon_post_author')
    all_recommend = models.IntegerField(default=0, null=True)
    spear = models.ManyToManyField(User, related_name='spear_post',blank=True)
    shield = models.ManyToManyField(User, related_name='shield_post',blank=True)
    scrap = models.ManyToManyField(User, related_name='joseon_scrap', blank=True)
    spearOfGod = models.ManyToManyField(User, related_name='spearOfGod_post',blank=True)
    shieldOfGod = models.ManyToManyField(User, related_name='shieldOfGod_post',blank=True)
    anonymous = models.CharField(max_length=50, null=True)
    nickname_check = models.ManyToManyField(User, related_name='nickname_check',blank=True)
    credibility = models.ManyToManyField(User, related_name='credibility_post',blank=True)
    total_credibility = models.IntegerField(default=50, null=True)

    ORIENTATION = (
        ("default", "선택안함"),
        ("conservatism", "보수"),
        ("progressivism", "진보"),
        ("centrism", "중도"),
    )

    political_orientation = models.CharField(
        max_length=15,
        choices=ORIENTATION,
        null=True,
        default="default",
        help_text="정치성향"
    )

    def __str__(self):
        return self.title

    def get_total_scrap(self):
        return self.scrap.count()

    def get_total_spear(self):
        return self.spear.count()

    def get_total_shield(self):
        return self.shield.count()

    def get_absolute_url(self):
        return reverse('joseon:joseon_detail', args=[self.id])

    @property
    def is_recent(self):
        now = timezone.localtime()
        return (self.date_posted + timedelta(hours=1)) > now

    class Meta:
        ordering = ["-date_posted"]


class Comment(models.Model):
    post = models.ForeignKey('joseon.Post', on_delete = models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joseon_comment_author')
    contents = models.TextField(max_length=600)
    created_date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    total = models.IntegerField(default=0)
    up = models.ManyToManyField(User, related_name='joseon_comment_up', blank=True)
    down = models.ManyToManyField(User, related_name='joseon_comment_down', blank=True)
    anonymous = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.contents

    def get_total_up(self):
        return self.up.count()

    @property
    def is_recent(self):
        now = timezone.localtime()
        return (self.created_date + timedelta(hours=1)) > now
