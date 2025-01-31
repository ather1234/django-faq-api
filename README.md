FAQ Management API
A Django-based API for managing multilingual FAQs with caching and WYSIWYG editor support.

Installation Instructions
Clone the repository:

Copy
Edit
git clone <https://github.com/ather1234/django-faq-api/tree/ather1234-patch-1>
Navigate to the project directory:

Copy
Edit
cd faq_project
Set up a virtual environment (optional but recommended):

Copy
Edit
python3 -m venv venv
Activate the virtual environment:

On Windows:

Copy
Edit
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations to set up the database:

bash
Copy
Edit
python manage.py migrate
Create a superuser to access the Django admin (if needed):

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Usage Instructions
The API exposes the following endpoints:

GET /api/faqs/: Fetch all FAQs in the default language (English).
GET /api/faqs/?lang=hi: Fetch FAQs in Hindi.
GET /api/faqs/?lang=bn: Fetch FAQs in Bengali.
To interact with the API, you can use tools like Postman or curl:

Example of a request to get FAQs in English:

bash
Copy
Edit
curl http://localhost:8000/api/faqs/
Example of a request to get FAQs in Hindi:

bash
Copy
Edit
curl http://localhost:8000/api/faqs/?lang=hi
The server will return the FAQs in the requested language.

Features
Multilingual FAQ support.
WYSIWYG editor for formatting FAQ answers.
Caching using Redis for faster translations.
Dynamic translation support using Google Translate API.
Admin interface for managing FAQs.
How to Contribute
Fork the repository.
Create a new branch: git checkout -b feature-name.
Make your changes and commit them: git commit -m "feat: add new feature".
Push to your forked repository: git push origin feature-name.
Open a pull request. Please ensure your code follows the project’s coding style and includes tests where necessary.
License
This project is licensed under the MIT License - see the LICENSE file for details.

API Documentation
GET /api/faqs/: Get all FAQs.
Query Parameters:

lang (optional): Language for the FAQs (e.g., en, hi, bn).
Example Request:

bash
Copy
Edit
curl http://localhost:8000/api/faqs/?lang=hi
Example Response:

json
Copy
Edit
[
{
"id": 1,
"question": "What is Django?",
"answer": "Django is a web framework for building web applications.",
"language": "hi"
}
]
