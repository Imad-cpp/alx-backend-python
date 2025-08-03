from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)  # New field to track read status

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # e.g., 'created', 'edited', 'deleted'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for {self.message.id} - {self.action} at {self.timestamp}"