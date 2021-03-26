from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")

    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    # django admin에서 내용을 보일때 db column 이 object 가 아닌 보이고자 하는 컬럼의 내용으로 볼려할 때 사용
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = '게시판 태그'
        verbose_name_plural = '태그'
