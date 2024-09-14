# Room Rental Platform

Welcome to the Room Rental Platform project! This Django-based web application allows house owners with extra rooms to list their rooms for rent, and customers to browse, view details, and book rooms from anywhere.

## Features

- **User Authentication:** Sign up, log in, and manage profiles for house owners and customers.
- **Room Listings:** House owners can list their rooms with detailed descriptions, photos, and availability.
- **Search and Filter:** Customers can search for rooms and filter results by location, price, and amenities.
- **Booking System:** Customers can book rooms, and house owners can manage bookings.
- **Ratings and Reviews:** Customers can leave feedback on their stay.
- **Notifications:** Email or SMS notifications for booking confirmations and updates.
- **Admin Dashboard:** Manage users, room listings, and bookings through an admin interface.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.0 or higher

### Steps

1. Clone the repository
 ```bash
 git clone https://github.com/yourusername/your-repo-name.git
 cd your-repo-name
 ```
2. Create a virtual environment
 ```bash
 python -m venv venv
```
3. Activate the virtual environment
```bash
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

4. Apply migrations
```bash
python manage.py migrate
```
5. Create a superuser (for accessing the admin dashboard)
```bash
python manage.py createsuperuser
```
6. Run the development server
```bash
python manage.py runserver
```
7. Open your web browser and navigate to http://127.0.0.1:8000/ to view the application
