from django.utils import timezone
from django.db import models
from django.conf import settings
import os
import shutil

# Create your models here.
class User_info(models.Model):
    user_id         = models.AutoField(primary_key=True)
    user_name       = models.CharField(max_length=12, unique=True)
    user_nickname   = models.CharField(max_length=12)
    user_password   = models.TextField()
    user_balance    = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    user_role = models.CharField(max_length=30, default="user")

    def tojson(self):
        return {
            "user_id": int(self.user_id), 
            "user_name": str(self.user_name), 
            "item_user_nickname": str(self.user_nickname), 
            "item_user_password": str(self.user_password), 
            "item_user_balance": float(self.user_balance),
            "item_user_role": str(self.user_role),
        }

    def __str__(self):
        return f"User_info(user_id: {self.user_id}, user_name: {self.user_name}, user_nickname: {self.user_nickname}, user_password: {self.user_password}, user_balance: {self.user_balance}, user_role:{self.user_role})"


class Store_item(models.Model):
    item_id     = models.AutoField(primary_key=True)
    item_name   = models.CharField(max_length=50, unique=True,default="N/A")
    item_image = models.ImageField(upload_to="keyboardApp/static/img/keyboardImg/", null=True, blank=True)
    # item_image = models.ImageField(upload_to="keyboardApp/static/img/keyboardImg/", null=True, blank=True)
    item_description = models.CharField(max_length=50, default="N/A")
    item_key_color = models.CharField(max_length=50, default="N/A")
    item_price  = models.DecimalField(max_digits=10, decimal_places=2)
    item_brand = models.CharField(max_length=50, default="N/A")


    # def __str__(self):
    #     return f"Store_item(item_id: {self.item_id}, item_name: {self.item_name}, item_description: {self.item_description}, item_key_color: {self.item_key_color}, item_price: {self.item_price}, item_brand: {self.item_brand} )"
    # def __init__(self):
    #     return {
    #             "item_id": int(self.item_id), 
    #             "item_name": str(self.item_name), 
    #             "item_description": str(self.item_description), 
    #             "item_key_color": str(self.item_key_color), 
    #             "item_price": float(self.item_price),
    #             "item_brand": str(self.item_brand)
    #         }
    

    # def tojson(self):
    #     filename = self.item_image.name.split('/')[-1] if self.item_image else ""
    #     return {
    #         "item_id": int(self.item_id), 
    #         "item_name": str(self.item_name), 
    #         # "item_image": str(self.item_image), 
    #         "item_image": f"/static/img/keyboardImg/{filename}" if filename else "",
    #         "item_description": str(self.item_description), 
    #         "item_key_color": str(self.item_key_color), 
    #         "item_price": float(self.item_price),
    #         "item_brand": str(self.item_brand)
    #     }
    def tojson(self):
    # # Generate image filename based on item_id
    #     expected_filename = f"keyboard{self.item_id}.png"
    #     if self.item_image:
    #         # Get the actual filename from the ImageField
    #         actual_filename = os.path.basename(self.item_image.name)
    #         # If the actual filename does not match the expected filename, rename it
    #         if actual_filename != expected_filename:
    #             new_path = os.path.join(settings.MEDIA_ROOT, "keyboardApp/static/img/keyboardImg", expected_filename)
    #             shutil.move(self.item_image.path, new_path)
    #             self.item_image.name = f"keyboardApp/static/img/keyboardImg/{expected_filename}"
    #             self.save()
        expected_filename = f"keyboard{self.item_id}.png"


        return {
            "item_id": int(self.item_id),
            "item_name": str(self.item_name),
            "item_image": f'src="/static/img/keyboardImg/{expected_filename}"',
            "item_description": str(self.item_description),
            "item_key_color": str(self.item_key_color),
            "item_price": float(self.item_price),
            "item_brand": str(self.item_brand),
    }


class Transaction(models.Model):
    transaction_id         = models.AutoField(primary_key=True)
    transaction_user    = models.ForeignKey("User_info", on_delete=models.CASCADE, related_name="user_transaction" )
    item                = models.ForeignKey("Store_item", on_delete=models.CASCADE, related_name="bought_by")
    transaction_date = models.DateTimeField(auto_now_add=True)
    reviewed_flag = models.IntegerField(default=0)
    
    def to_json(self):
        return {
            "transaction_id": self.transaction_id,
            "transaction_user": self.transaction_user,
            "item": self.item,
            "transaction_date": self.transaction_date,
            "reviewed_flag": self.reviewed_flag
        }

    # def __str__(self):
    #     return f"Transaction(transaction_id: {self.transaction_id}, transaction_user_id: {self.transaction_user}, item_id: {self.item})"


class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User_info", on_delete=models.CASCADE, related_name="user_review")
    store_item_id = models.ForeignKey("Store_item", on_delete=models.CASCADE, related_name="user_review_item")
    rating = models.IntegerField()
    review_text = models.TextField(default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return {
            "review_id": self.review_id,
            "user_id": self.user_id,
            "store_item_id": self.store_item_id,
            "rating": self.rating,
            "review_text": self.review_text,
            "created_at": self.created_at
        }

# Table reviews {
#   review_id integer [primary key]
#   user_id integer
#   store_item_id integer
#   rating integer
#   review_text text
#  s created_at timestamp
# }

class Discount_code(models.Model):
    discount_id = models.AutoField(primary_key=True)
    code = models.TextField(unique=True)
    discount_percentage = models.IntegerField()
    valid_from = models.DateTimeField(auto_now_add=True)        # we can validate with timezone.now() by python
    valid_to = models.DateTimeField()
    is_activate = models.IntegerField()

    # check and make sure it valid as user call this method
    def is_valid(self):
        if self.valid_to <= timezone.now():
            return False
        return True

    def to_json(self):
        return {
            "discount_id": self.discount_id,
            "code": self.code,
            "discount_percentage": self.discount_percentage,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "is_activate": self.is_activate
        }

# table discount_codes {
#   discount_id integer [primary key]
#   code Text unique
#   discount_percentage integer
#   valid_from datetime
#   valid_to datetime
#   is_active integer
# }

