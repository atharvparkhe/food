
# Food Ordering Application

Using this system the users can lookup for nearby restaurants in thier locatlity using thier location or by searching.
They can view the restaurant details and the food served/available for them to order.
Users can also pay for the thier orders using the payment gateway provided (Razorpay).
The sellers also have an interface through which they can view and edit orders, Add/Edit/Delete Products offered in thier restaurant.
The order analytics graph is also available for sellers to analyse thier product.


## Author - Atharva Parkhe

- Github - [atharvparkhe](https://www.github.com/atharvparkhe/)
- LinkedIn - [Atharva Parkhe](https://www.linkedin.com/in/atharva-parkhe-3283b2202/)
- Instagram - [atharvparkhe](https://www.instagram.com/atharvparkhe/)
- Twitter - [atharvparkhe](https://www.twitter.com/atharvparkhe/)

## Features

- View All Restaurants nearby.
- Check Restaurant details and the food available there.
- Order multiple food items.
- Make Online Payment using Razorpay
- Get confirmation email.
- Sellers also recieve order order email.
- Seller can add/modify/delete the restaurant and the product details.
- Sellers can manage orders.



## Tech Stack

**Backebd:** Django *(Python)*

**Frontend:** HTML, CSS, Javascript

## Run Locally

***Step#1 :*** Create Virtual Environment

```bash
  virtualenv env
```

***Step#2 :*** Activate Virtual Environment

```bash
  source env/bin/activate
```

***Step#3 :*** Clone the project

```bash
  git clone https://github.com/atharvparkhe/food.git
```

***Step#4 :*** Go to the project directory

```bash
  cd food
```

***Step#5 :*** Install dependencies

```bash
  pip install -r requirements.txt
```

***Step#6 :*** Make Migrations

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

***Step#7 :*** Run Server

```bash
  python3 manage.py runserver
```

Check the terminal if any error.

## Documentation

The docs folder contain all the project documentations and screenshots related the project.

## Demo

Youtube Tutorial - I will upload tutorial video soon. Stay Tuned.