from django.db import models

class Contact(models.Model):
    """ Model for Contact """

    ENQUIRY_SELECTION = [
        ('ORDER_ENQUIRY', 'Order Enquiry'),
        ('PRODUCT_QUESTION', 'Product Question'),
        ('GENERAL_ENQUIRY', 'General Enquiry'),
        ('FEEDBACK', 'Feedback or Suggestions')
        ]


    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, choices=ENQUIRY_SELECTION, default=0)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject