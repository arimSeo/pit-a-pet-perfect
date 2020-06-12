from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from address.models import AddressField

# class MyModel(models.Model):
#     address1 = AddressField()
#     address2 = AddressField(related_name='+', blank=True, null=True)

class Person(models.Model):
  address = AddressField(on_delete=models.CASCADE)

# Create your models here.
class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    ispermit = models.BooleanField('위치정보 허용동의', default=False)
    
class RegiProfile(models.Model):
    M_or_F = (
    ('남', '남'),
    ('여', '여'),
    ('중성', '중성'),
    )
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    pet_name = models.CharField('1. 펫 이름', max_length=20, null=True)
    pet_type = models.CharField('2. 펫 종류', max_length=20, null=True)
    pet_age = models.IntegerField('3. 펫 나이',null=True)
    pet_gender = models.CharField('4. 성별', choices=M_or_F, max_length=2, null=True)
    # pet_locate = models.TextField('5. 주소', max_length=50, null=True)         #지도 만들면 추가
    pet_image = models.ImageField('6. 프로필 사진', null=True, blank=True)
    pet_intro = models.TextField('7. 소개', max_length=100, null=True)

    def __str__(self):
        return str(self.user)
# 1. 펫 이름(닉네임): _form
# 2. 펫 종류: _form
# 3. 펫 나이: _form
# 4. 펫 성별: combo-box
# 5. 펫 (거주)위치 설정
# 6. 프로필 사진 등록
# 7. 자기소개 키워드 입력/ 동물성향

class PlusPhoto(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    plus_image = models.ImageField('사진추가하기', null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        RegiProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.regiprofile.save()

    # def __str__(self):
        # return self.pet_name