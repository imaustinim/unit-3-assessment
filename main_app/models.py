from django.db import models
from django.forms import ModelForm

class Widget(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return (f"{self.get_season_display()} on {self.name}")

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ["description", "quantity"]