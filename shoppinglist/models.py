from django.db import models
from django.core import validators

from user.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100
    )
    created_at = models.DateTimeField(
        verbose_name='新規登録日時',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )
    
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100
    )
    price = models.IntegerField(
        verbose_name = '金額',
        default=0,
        validators=[
            validators.MinValueValidator(0)
        ]
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name='新規登録日時',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )
    
    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name='担当',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name='新規登録日時',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )
    
    def __str__(self):
        return self.name


class ShoppingItem(models.Model):
    shoppinglist = models.ForeignKey(
        ShoppingList,
        verbose_name='ショッピングリスト',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        verbose_name='商品',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        verbose_name='個数',
        default=0,
        validators=[
            validators.MinValueValidator(0)
        ]
    )
    created_at = models.DateTimeField(
        verbose_name='新規登録日時',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )
    
    def sub_total(self):
        # 小計 = 商品の金額 x 個数
        return self.item.price * self.quantity
    
    def __str__(self):
        return self.id

