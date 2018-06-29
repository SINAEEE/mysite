from django.db import models
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user가 삭제됬을때 게시판글도 함께 삭제한다.

    def __str__(self):
        return "Board(%s, %s, %d, %s, %d)" % (
            self.title,
            self.content,
            self.hit,
            str(self.regdate),
            self.user.id) #self.user도 가능


