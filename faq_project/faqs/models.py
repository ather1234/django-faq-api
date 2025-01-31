from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def get_translated_question(self, lang='en'):
        # Language-specific field selection
        return getattr(self, f"question_{lang}", self.question)

    def get_translated_answer(self, lang='en'):
        # Language-specific field selection
        return getattr(self, f"answer_{lang}", self.answer)

    def __str__(self):
        return self.question
from googletrans import Translator

def translate_faq(self):
    translator = Translator()
    if not self.question_hi:
        self.question_hi = translator.translate(self.question, src='en', dest='hi').text
    if not self.question_bn:
        self.question_bn = translator.translate(self.question, src='en', dest='bn').text
    if not self.answer_hi:
        self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
    if not self.answer_bn:
        self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
    self.save()
