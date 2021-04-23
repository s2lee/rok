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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crazylab_post_author')
    all_recommend = models.IntegerField(default=0, null=True)
    star = models.ManyToManyField(User, related_name='star_post', blank=True)
    recommend = models.ManyToManyField(User, related_name='crazylab_recommend', blank=True)
    scrap = models.ManyToManyField(User, related_name='crazylab_scrap', blank=True)
    accused = models.PositiveIntegerField(default=0, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='crazylab_pics')

    def __str__(self):
        return self.title

    def get_total_scrap(self):
        return self.scrap.count()

    def get_total_star(self):
        return self.star.count()

    def get_total_recommend(self):
        return self.recommend.count()

    def get_absolute_url(self):
        return reverse('crazylab:crazylab_detail', args=[self.id])

    @property
    def is_recent(self):
        now = timezone.localtime()
        return (self.date_posted + timedelta(hours=1)) > now

    class Meta:
        ordering = ["-date_posted"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crazylab_comment_author')
    contents = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    total = models.IntegerField(default=0)
    up = models.ManyToManyField(User, related_name='crazylab_comment_up', blank=True)
    accused = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.contents

    def get_total_up(self):
        return self.up.count()

    @property
    def is_recent(self):
        now = timezone.localtime()
        return (self.created_date + timedelta(hours=1)) > now
