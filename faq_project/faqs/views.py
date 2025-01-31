from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        # Get the 'lang' query parameter, default to 'en' if not provided
        lang = request.query_params.get('lang', 'en')  
        
        # Fetch all FAQ objects from the database
        faqs = FAQ.objects.all()
        
        # Create a list to hold translated FAQ data
        translated_faqs = []
        
        # Loop through each FAQ, get the translated question based on language
        for faq in faqs:
            faq_data = FAQSerializer(faq).data
            faq_data['question'] = faq.get_translated_question(lang)  # Translate question
            translated_faqs.append(faq_data)
        
        # Return the translated FAQ data as a JSON response
        return Response(translated_faqs)
