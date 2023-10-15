from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Work(models.Model):
    """Work model.

    Adds title, description, created_at, link and image fields.
    """

    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    image = models.ImageField('Фото', upload_to='post_images')
    link = models.CharField('Ссылка', max_length=256)

    class Meta:
        verbose_name = 'работа'
        verbose_name_plural = 'Работы'
        default_related_name = 'works'

    def __str__(self):
        """Set the field title as a string representation of a class."""
        return self.title


class Profile(models.Model):
    """Profile model.

    Related to User model.
    Adds user, bio, location, avatar, techs and birth_date fields.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    job = models.CharField('Должность', max_length=50)
    bio = models.TextField('Био', max_length=1000)
    techs = models.TextField('Технологии', max_length=100)
    location = models.CharField('Местоположение', max_length=30)
    birth_date = models.DateField('Дата рождения', null=True)
    avatar = models.ImageField('Аватар', upload_to='avatars')

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'
        default_related_name = 'profiles'

    def __str__(self):
        """Set the field title as a string representation of a class."""
        return self.user.first_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
