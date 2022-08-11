
## Food Ordering System

Using this system the users can lookup for nearby restaurants in thier locatlity using thier location or by searching. They can view the restaurant details and the food served/available for them to order. Users can also pay for the thier orders using the payment gateway provided (Razorpay). The sellers also have an interface through which they can view and edit orders, Add/Edit/Delete Products offered in thier restaurant. The order analytics graph is also available for sellers to analyse thier product.
Customer authentication is done using *Django Authentication*. Database used is *SQLite3* which is django's default database. Payment Gateway used is *Razorpay*.

### 🔗 Content

* [Overview](#food-ordering-system)
* [Content](#-content)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Environment Variables](#-environment-variables)
* [Run Locally](#-run-locally)
* [Documentation](#-documentation)
* [Demo](#-demo)
* [Screen-Shots](#-screen-shots)
* [Author](#-author)


### 📋 Features

- **USER AUTHENTICATION :** Users can Signup for a new account, Verify thier email id, Login using email and password, make a Forgot request to reset thier password. 

- **PRODUCTS AND BLOGS :** Users can view all products and blogs.

- **REVIEWS AND RATING :** User can add blogs comments, product review and rateings.

- **CONTACT US FORM :** User can fill up the Contact Us form. (Auto Corrospondence email sending feature)

- **CART FUNCTIONALITY :** User can add and remove products from cart. Users can also change the quantity of items in thier cart.

- **PAYMENT GATEWAY :** Users can make payment using Net-Banking, UPI, Card Payments, etc. through Razorpay Payment Gateway which is integrated in the system.

- **AUTO INVOICE :** After payment, users would recieve invoice (auto-generated) in thier mailbox.

- **SELLER AUTHENTICATION :** Seller (Shop-keepers) can Signup for a new account, Verify thier email id, Login using email and password, make a Forgot request to reset thier password. 

- **SELLER CMS :** Seller can manage thier content on the site. They can add, modify, delete thier online shop and the products that they sell in thier shop.

- **SELLER ORDER MANAGEMENT :** Seller can manage thier orders through the dashboard.


### 🧰 Tech Stack

- **`BACKEND`** : Django *(Python)*

- **`DATABASE`** : SQLite3

- **`FRONTEND`** : HTML, CSS, Javascript


### 🔐 Environment Variables

To run this project, you will need to add the following environment variables to your **.env** file

- `EMAIL_ID`  -  Email ID (which would be used to send emails)

- `EMAIL_PW`  -  Email Password

- `PUBLIC_KEY` - Razorpay API Public Key

- `PRIVATE_KEY` - Razorpay API Private Key

![ENV file](docs/env.png)


### 💻 Run Locally

***Step#1 : Clone Project Repository***

```bash
git clone https://github.com/atharvparkhe/food.git && cd food
```

***Step#2 : Create Virtual Environment***

- If *virtualenv* is not istalled :
```bash
pip install virtualenv && virtualenv env
```
- **In Windows :**
```bash
    env/Scripts/activate
```
- **In Linux or MacOS :**
```bash
    source env/bin/activate
```

***Step#3 : Install Dependencies***

```bash
pip install --upgrade pip -r requirements.txt
```

***Step#4 : Add .env file***

- ENV file contents
    - **In Windows :**
    ```bash
        copy .env.example .env
    ```
    - **In Linux or MacOS :**
    ```bash
        cp .env.example .env
    ```
- Enter Your Credentials in the *".env"* file. Refer [Environment Variables](#-environment-variables)

***Step#5 : Run Server***

```bash
python manage.py runserver
```

- Open `http://127.0.0.1:8000/` or `http://localhost:8000/` on your browser.

*Check the terminal if any error.*


### 📄 Documentation

The docs folder contain all the project documentations and screenshots of the project.

The Frontend is a ready-made template, which i downloaded from [here](https://www.nulledtemplates.com).

**Local Server Base Link :** http://localhost:8000/

**Admin Pannel Access :**
- ***Email :*** "admin@admin.com"
- ***Password :*** "password"


### 🧑🏻‍💻 Demo

YouTube Link : https://youtu.be/LkcjY7wBPgs


### 🌄 Screen-Shots

- **Home Page**

![hero](docs/project/customer/main/hero.png)
![main](docs/project/customer/main/top-restaurants.png)
![About](docs/project/customer/main/about.png)
![Featured Product](docs/project/customer/main/featured-products.png)
![Blogs](docs/project/customer/main/blogs.png)
![Footer](docs/project/customer/main/footer.png)

- **Authentication**

![Signup](docs/project/customer/auth/signup.png)
![Login](docs/project/customer/auth/login.png)
![Forgot](docs/project/customer/auth/forgot.png)

- **Blogs**

![Blog](docs/project/customer/blogs/all-blogs.png)
![Blog](docs/project/customer/blogs/blog1.png)
![Blog](docs/project/customer/blogs/blog2.png)

- **Product**

![All Restaurants](docs/project/customer/products/all-restaurants.png)
![Single Products](docs/project/customer/products/restaurant-products.png)
![Single Product](docs/project/customer/products/single-product.png)

- **Cart**

![Cart](docs/project/customer/cart/cart.png)
![Address](docs/project/customer/cart/checkout.png)
![Payment](docs/project/customer/cart/payment.png)
![Payment Processing](docs/project/customer/cart/payment-processing.png)

- **Admin Authentication**

![Login](docs/project/seller/auth/seller-login.png)
![Forgot](docs/project/seller/auth/seller-forgot.png)

- **Admin Dashboard**

![Login](docs/project/seller/main/dashboard.png)
![Forgot](docs/project/seller/main/seller-products.png)
![Forgot](docs/project/seller/main/new-product.png)


### 🙋🏻‍♂️ Author

**🤝 Connect with Atharva Parkhe**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atharva-parkhe-3283b2202/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/atharvparkhe/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.twitter.com/atharvparkhe/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/atharvparkhe/)
[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/patharv777/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UChimOJO64hOqtE7HCgtiIig)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/8WNC43Xsfc)
