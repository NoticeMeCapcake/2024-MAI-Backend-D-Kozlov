from datetime import timezone

from django.db import models


class UserProfile(models.Model):
    uid = models.UUIDField()
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.login


class Post(models.Model):
    uid = models.UUIDField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    uid = models.UUIDField()
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.content
