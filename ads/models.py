from django.db import models
from django.contrib.auth.models import User

# Объявление товара для обмена
class Ad(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Новый'),
        ('used', 'Б/у'),
    ]

    # кто разместил объявление
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # заголовок
    description = models.TextField()  # описание товара
    # ссылка на картинку (необязательно)
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)  # категория
    condition = models.CharField(
        max_length=10, choices=CONDITION_CHOICES)  # состояние
    # дата создания (ставится автоматически)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # как объявление будет отображаться в админке


# Предложение обмена между двумя объявлениями
class ExchangeProposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('accepted', 'Принята'),
        ('declined', 'Отклонена'),
    ]

    ad_sender = models.ForeignKey(
        Ad, related_name='sent_proposals', on_delete=models.CASCADE)  # кто предложил
    ad_receiver = models.ForeignKey(
        Ad, related_name='received_proposals', on_delete=models.CASCADE)  # кому предложили
    comment = models.TextField()  # комментарий к предложению
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')  # статус
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self):
        return f"Обмен от {self.ad_sender} к {self.ad_receiver} - {self.status}"
