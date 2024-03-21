# Sk-Fashion-ecommerce Project Documentation

## Overview

This Django project is an e-commerce platform that allows users to view, browse, and purchase products. The project includes features such as user authentication, product categorization, and a shopping cart system.

## Project Structure

The project consists of the following components:

1. **Models**
   - `Product`: Represents a product with details like name, description, price, and category.
   - `Category`: Represents a category to which products can be assigned.

2. **Views**
   - `category_summary`: Displays a summary of all product categories.
   - `category`: Displays products belonging to a specific category.
   - `product`: Displays detailed information about a specific product.
   - `home`: Displays a list of all products.
   - `about`: Displays information about the project.
   - `login_user`: Handles user login functionality.
   - `logout_user`: Handles user logout functionality.
   - `register_user`: Handles user registration functionality.
   - `update_user`: Allows users to update their information.
   - `update_password`: Allows users to update their passwords.
   - `cart_summary`: Displays a summary of the items in the user's shopping cart.
   - `cart_add`: Adds products to the shopping cart.
   - `cart_delete`: Deletes products from the shopping cart.
   - `cart_update`: Updates the quantity of products in the shopping cart.

3. **Forms**
   - `SignUpForm`: Form for user registration.
   - `UpdateUserFrom`: Form for updating user information.
   - `ChangePassswordForm`: Form for changing user passwords.

4. **Templates**
   - Various HTML templates for rendering the views and forms.

5. **Cart Management**
   - Utilizes a custom shopping cart (`Cart`) for handling cart-related operations.

## User Authentication

- Users can register for an account using the registration form.
- Users can log in using their credentials.
- Authenticated users can update their profile information.
- Authenticated users can change their passwords.
- Users can log out of their accounts.

## Product Management

- Products are categorized into different categories.
- Users can view all available categories and their respective products.
- Users can view detailed information about a specific product.
- The home page displays a list of all products.
- The about page provides information about the project.

## Shopping Cart

- Users can add products to their shopping cart.
- Users can view a summary of the items in their shopping cart.
- Users can update the quantity of items in their shopping cart.
- Users can delete items from their shopping cart.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sk-sanju/Sk-Fashion-ecommerce.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Sk-Fashion-ecommerce
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the admin interface at `http://127.0.0.1:8000/admin/` to add products and categories.

## Conclusion

This Django e-commerce project provides a foundation for building a robust online shopping platform. Developers can further extend and customize the project to meet specific business requirements.
