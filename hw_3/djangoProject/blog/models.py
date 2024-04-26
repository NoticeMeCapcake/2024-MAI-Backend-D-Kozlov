from django.utils import timezone

from django.db import models


class UserProfile(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.login


class UserPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class Like(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(UserPost, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author_id) + ": " + str(self.post_id)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author_id', 'post_id'], name='unique_author-post')
        ]