from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail
from accounts.models import User
from datetime import datetime, timedelta
from  django.utils import timezone

# Create your models here.
class Review(models.Model):
    content = models.TextField()
    review_image = ProcessedImageField(
        upload_to="images/reviews/",
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 100},
    )
    review_thumbnail = ImageSpecField(
        source="images/reviews/",
        processors=[ResizeToFill(150, 150)],
        format='JPEG',
        options={'quality' : 100},
    )
    # stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=2):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
    review_comments = models.PositiveIntegerField(verbose_name='댓글 수', null=True)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        # elif time < timedelta(hours=1):
        #     return str(int(time.seconds / 60)) + '분 전'
        # elif time < timedelta(days=1):
        #     return str(int(time.seconds / 3600)) + '시간 전'
        # elif time < timedelta(days=2):
        #     time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
        #     return str(time.days) + '일 전'
        else:
            return False