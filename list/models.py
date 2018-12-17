from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from django.contrib.auth.models import User


class List(models.Model):
    class Meta:
        db_table = 'list'

    ## 名称
    title = models.CharField(max_length=50)

    ## 内容
    content = models.TextField()

    ## 期日
    due_date = models.DateField(blank=True, null=True)

    ## カテゴリー
    ## 今後実装
    #category = models.IntegerField(default=0)

    ## ランク（重要度）
    ## 1:A（すぐにやる）、2:B（そのうちやる）、3:C（いつかやる）
    rank = models.IntegerField(default=0)

    ## 登録日
    created_at = models.DateTimeField(auto_now_add=True)

    ## Userテーブルとのリレーション
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ## イメージ画像
    image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/',
        blank=True
    )
    
    image_edit = ImageSpecField(
        source="image",
        processors=[ResizeToFill(537, 250)],
        format='JPEG'
    )

    ## 達成ステータス（True：達成済み、False：実行中）
    status = models.BooleanField(default=False)

    ## 公開ステータス
    ## 1:公開する、2:公開しない
    share = models.IntegerField(default=2)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    ## コメント
    comment = models.TextField(max_length=100)

    ## 登録日
    created_at = models.DateTimeField(auto_now_add=True)


    ## listテーブルとのリレーション
    list = models.ForeignKey(List, on_delete=models.CASCADE)
