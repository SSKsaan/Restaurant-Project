
# Django Restaurant Project [![Live Demo](https://img.shields.io/badge/Live-darkgreen?logo=rocket&logoColor=white)](https://best-khawar-restaurant.onrender.com/)
_Django-powered restaurant platform with custom UI, smooth ordering flow, and responsive design._



### Developed By [@SSKsaan](https://www.github.com/SSKsaan)


## 📦 Tech Stack

- **Backend:** 

  ![Django](https://img.shields.io/badge/Django-darkgreen?logo=django&logoColor=white)

- **Frontend:** 

  ![HTML5](https://img.shields.io/badge/HTML5-gray?logo=html5)
  
  ![CSS3](https://img.shields.io/badge/CSS3-gray?logo=css)

  ![Bootstrap 5](https://img.shields.io/badge/Bootstrap5-gray?logo=bootstrap)
    
  ![JavaScript](https://img.shields.io/badge/JavaScript-gray?logo=javascript)

## 🛠 Additional Tools

- **FontAwesome** – for all icons  
- **Unsplash** – for most images  
- **Google Maps** – for location embedding


## 💡 Features Overview

- Responsive navbar and footer
- **Homepage** includes custom carousels, embedded map, sliding image strips
- **Menu** card list, with category filtering
- **Item details** with recommendation carousel and toggleable reviews section
- **Review** modal (Boostrap-based popup window) with Javascript-based star selector
- AJAX-based (action without page reload) Add to Cart button
- AJAX quantity update in **cart** page, with quick delete and clear cart features
- **Order** Confirmation Email sent on successful placement
- Shared **login / register** with smooth animated side-swap transition
- Updatable **profile** with consistent order history and invoice access
- Dismissable alerts for every prominent action

**Check [Documentation →](https://github.com/SSKsaan/Restaurant-Project/blob/gh-pages/docs/features.md) for Detailed Overview**


## 📸 Preview

![Restaurant Platform](https://raw.githubusercontent.com/SSKsaan/Restaurant-Project/gh-pages/assets/restaurant-preview.gif)


## ⚙ Setup / Installation
- **Clone the repo**

   ```bash
   git clone https://github.com/SSKsaan/Restaurant-Project.git
   cd Restaurant-Project
   ```

- **Create and activate virtual environment** (Recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate        # For Linux/macOS
   venv\Scripts\activate           # For Windows
   ```

- **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
   | _**Requirements Preview:** Django, pillow, python-decouple, ..._ 

- **Create `.env` file**

   Your `.env` should contain:

   ```
   SECRET_KEY=generatedRandomKey
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=yourEmailAddress
   EMAIL_HOST_PASSWORD=yourAppPassword
   DEFAULT_FROM_EMAIL=yourEmailAlias
   ```

   **Generate a random Secret Key:**
   (Run this in your terminal or command prompt)
   ```
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

- **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

- **Create Superuser** (Optional)
  
   ```bash
   python manage.py createsuperuser
   ```

- **Run the server**

   ```bash
   python manage.py runserver
   ```


## 📄 License

This project does not currently use a license. Please contact the author for reuse.
