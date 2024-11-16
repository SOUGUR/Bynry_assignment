
# Gas Utility Requests Management System

A web-based application for managing and resolving service requests. This project allows representatives to view, manage, and resolve customer service requests efficiently.


## Features
- **User Authentication**: Secure login for representatives and customers.
- **view user profile and resolve Pending Requests**: Logged in user can view his/her profile and logged-in Representatives can view all pending service requests to resolve.
- **View Requests**: A logged-in user can view his/her request history along with status (pending or resolved).
- **Send requests**: A customer can send description of request along with a file attached.
- **Role Based Access Control**: A logged in user can either be a representative or a customer.
- **Dynamic Updates**: Updates the request status dynamically without page refresh.
  
---

## Prerequisites
- Python 3.10+ installed on your machine
- Django 5.1.3 or compatible version
- SQLite3 (or an alternative database if configured)
- pip for managing Python packages

---

## Installation

1. **Clone the Repository**  

   git clone https://github.com/SOUGUR/Bynry_assignment.git



2. **Set Up Virtual Environment**  
   Create and activate a virtual environment:
 
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
  

3. **Install Dependencies**  
   Install the required Python packages:

   pip install -r requirements.txt
  

4. **Apply Migrations**  
   Initialize the database:
   python manage.py makemigrations
   python manage.py migrate
   

5. **Create a Superuser**  
   You can set up an admin account if required:
 
   python manage.py createsuperuser
  

6. **Run the Development Server**  
   Start the application:
 
   python manage.py runserver
 


## Running the Application
1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. navigation bar helps the user logged in to navigate different links.
3. **`/pending_requests/`**: Displays all pending service requests for representatives only.
2. **`/resolve-request/<int:request_id>/`**: Resolves a specific service request by ID and changes its status to resolved.
3. **`/logout/`**: Logs out the current user.
4. **`/`**: Handles user signup.
5. **`/login/`**: Logs in a user.
6. **`/request/`**: Allows users to create a new service request.
7. **`/my-requests/`**: Lists all requests created by the logged-in user.
8. **`/profile/`**: Displays the user's profile details.




## Functionalities
1. View Pending Requests
Representatives only can view a list of all pending service requests on the Pending Requests page. Each request displays the subject,
description, status and creation date for clarity and ease of access.

2. Resolve a Request
Representatives can then click on the "Mark as Resolved" button to update a request's status to resolved.
Once resolved, the button text dynamically changes to "Resolved", and the button is disabled,
ensuring no duplicate actions are performed.

3. Secure Access
The service request management interface is protected through authentication, allowing only logged-in representatives to view
and manage pending service requests. Unauthorized access is restricted by redirecting users to the home page.

4. Real-Time Updates
The AJAX-based functionality ensures a easy user
experience by dynamically updating the status of requests.

5. User-Friendly Interface
The interface is designed to be intuitive, displaying pending requests in a structured list. Each request includes key details
like the subject, description, and timestamp, making it easy for representatives to act promptly.

6. Dynamic URL Management
The URLs for resolving requests are dynamically generated, ensuring accuracy and reducing potential errors in routing.




## File Structure
``````
gas_utility/
├── representatives/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── representatives/
│   │   │   ├── pending_requests.html
│   │   │   └── navigation_bar.html
│   ├── static/
│   │   ├── representatives/
│   │   │   └── styles.css
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── customers/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── customers/
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   │   └── profile.html
|   |       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
└── gas_utility/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
                    
```````


## License
This is a part of assignment for Backend Intern role at Bynry Inc. Hence anyone is free to utilize this as per their requirement



## Contact
For any inquiries or support, please contact:
- **Name**: Sourabh  Santosh  Gurav
- **Email**: sourabhgurav23@gmail.com
- **GitHub**: https://github.com/SOUGUR


### Notes:
1. Replace `<repository-url>` with the actual GitHub repository URL.
2. Update contact details, repository folder name, and GitHub profile link to reflect your project and identity.
3. Ensure the `requirements.txt` file lists all dependencies. You can generate it with:
   pip freeze > requirements.txt

Sign Up
![image](https://github.com/user-attachments/assets/a7b06833-4ad0-4caf-a1a7-8946390bcfc6)

Login 
![image](https://github.com/user-attachments/assets/cc6b8b27-c68b-421e-b114-d0f1f3943a42)

Pending Requests for Representatives
![image](https://github.com/user-attachments/assets/0b93e99c-982b-49b1-89e5-68f4f8cc8bfe)

User Profile
![image](https://github.com/user-attachments/assets/fa5ca58a-4af2-46ec-8a9a-a4a4e52440fc)

Create a Request
![image](https://github.com/user-attachments/assets/040d4922-24e5-4836-affb-fcabab8eebb3)

Request History of a user
![image](https://github.com/user-attachments/assets/dda78943-1e29-4527-a815-fc365d9add48)




