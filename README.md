# NotX
Product Expiry Alert System using Django REST API
This project implements a simple alert system using a Django REST API to notify users when the expiry date of registered products is approaching. This system helps users stay informed about products that are about to expire, enabling them to take timely actions.

Features
User Registration and Authentication: Users can register and log in to the system.
Product Registration: Users can add products by providing details such as name, expiry date, and quantity.
Expiry Alert Generation: The system automatically generates alerts when a product's expiry date is close (configurable).
Notification System: Users receive notifications via email or other channels when expiry alerts are triggered.

Installation and Setup

Clone the Repository:
git clone ...
cd product-expiry-alert

Create a Virtual Environment (Optional but Recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Set Up Database:
python manage.py makemigrations
python manage.py migrate
Configure Email Settings (for notifications):

Edit the settings.py file and provide your email configuration details.

Start the Development Server:
python manage.py runserver
