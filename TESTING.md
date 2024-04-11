# Lari Living Testing

This document presents an outline of the testing methodologies utilized during the development of the Lari Living store.

Back to Lari Living [README.md](README.md).

## Table of Contents

- [User Story Testing](#user-story-testing)
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
    - [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing) 
- [Manual Testing](#manual-testing)
    - [Site Navigation](#site-navigation)
    - [Home Page](#home-page)
    - [All Auth Pages](#all-auth-pages)
    - [Products](#products)
    - [Product Details](#product-details)
    - [Products Management](#products-management)
    - [Bag](#bag)
    - [Checkout](#checkout)
    - [Profile](#profile)
    - [Testimonials](#testimonials)
    - [Contact](#contact)
- [Bugs](#bugs)

## User Story Testing

The users stories can be found in the GitHub Projects [kanban board](https://github.com/users/Darioc18/projects/4/views/1), created for this application.

**EPIC | Registration and User Accounts**

| User Story | Notes | Result |
|------------|-------|--------|
|As a site user I can easily register for an account so that I can have a personal account and I can view my profile.| Allauth has been implemented to enable users to manage their accounts efficiently.| Pass |
|As a site user I can easily login or logout so that I can access my personal account information.|Allauth provides login and logout functionality for the application.| Pass |
|As a site user I can easily recover my password in case I forget it so that I can recover access to my account.|Allauth provides password reset functionality.|Pass|
|As a site user I can receive an email confirmation after registering so that I can verify that my account registration was successful.|Upon registration, a message is displayed and the user receives a confirmation link to finalize the sign-up process.|Pass|
|As a site user I can have a personalized user profile so that I can view my personal order history and order confirmations, and save my payments information.|A profile page is easily accessible from the header. On this page, users can save their details for future purchases and track their order history.|Pass|

**EPIC | Admin & Store Management**

| User Story | Notes | Result |
|------------|-------|--------|
|As a store owner I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.|The superuser can oversee product management through a designated link, allowing them to add new products. The products can be directly edited or deleted from both the products page and the individual product detail page.| Pass |

**EPIC | Sorting and Searching**

| User Story | Notes | Result |
|------------|-------|--------|
|As a shopper I can sort the list of available products so that I can identify the best priced and categorically sorted products.|A sorting feature is available on the products page, enabling users to sort products by price or name. Users can also sort products by category by clicking on the products dropdown in the navigation bar.| Pass |
|As a shopper I can sort a specific category of products so that I can find the best price products in a specific category, or sort the products in that category by name.|Users can sort products by category by clicking on the products dropdown in the navigation bar.| Pass |
|As a shopper I can search for a product by name or description so that I can find a specific product I'd like to purchase.|A search bar is consistently positioned at the top of the screen, allowing users to input the name of the item they are looking for.| Pass |
|As a shopper I can easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.|Upon entering a keyword in the search bar, a number of products containing the word in their title or description are displayed.| Pass |

**EPIC | Newsletter**

| User Story | Notes | Result |
|------------|-------|--------|
|As a store owner I can send out a newsletter via email so that I keep customers updated with news and events about my store.|The superuser has access to the newsletter page, where they can compose an email to send to the mailing list of subscribers.| Pass |
|As a store owner I can unsubscribe subscribers from newsletter.|Currently, the superuser can only delete subscribers from the admin panel. However, a feature could be implemented in the future to display the list of subscribers on a page of the website. Alternatively, a marketing email tool such as Mailchimp could be implemented for newsletter management.| Pass |
|As a site user I can sign up for the website's newsletter so that I can keep up to date with new products, promotions, and events.|A subscribe form is always visible in the footer allowing users to easily subscribe to the newsletter.| Pass |

**EPIC | Contact**

| User Story | Notes | Result |
|------------|-------|--------|
|As a site user I can easily find the contact form so that I can reach out to the company with any inquiries or issues.|The contact form is always visible in the header for easy access.| Pass |
|As a site user I can use a simple and intuitive contact form with clear instructions so that I can quickly send my message without confusion.|The contact form offers a predefined subject, streamlining the user's input to only include their name, email, and message.| Pass |
|As a site user I can receive a confirmation message after submitting the contact form so that I know my message has been successfully sent.|A confirmation message is displayed once the contact form is submitted| Pass |
|As a site user I want the contact form to have built-in validation to prevent errors, such as submitting the form without filling in required fields or entering an invalid email address.|Error messages are promptly displayed when the user inputs invalid info (e.g., an invalid email or leaves fields blank) in the form.| Pass |
|As a site user I can fill in fields for important information such as my name, email address, and the nature of my inquiry so that the company can respond effectively.|The contact form includes all of these fields.| Pass |

**EPIC | Purchasing and Checkout**

| User Story | Notes | Result |
|------------|-------|--------|
|As a shopper I can select and see the quantity of a product when purchasing it so that I don't accidentally select the wrong product quantity.|The quantity of products is always displayed in the shopping bag and in the toast messages when adding a product.| Pass |
|As a shopper I can view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.|The breakdown of costs, including the grand total, is visible in the shopping bag.| Pass |
|As a shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.|Clear buttons are provided in the shopping bag to easily increase or decrease the quantity of products to be ordered.| Pass |
|As a shopper I can easily enter my payment information so that I can checkout quickly and with no hassles.|The checkout form features placeholders that facilitate seamless payment completion for users.| Pass |
|As a shopper I can view an order confirmation after checkout so that I can verify that I haven't made any mistakes.|After checkout, a message and an order confirmation page are displayed. Additionally, users receive an order confirmation via email.| Pass |
|As a shopper I can receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records.|Users receive an email containing the order details and confirmation after making a purchase.| Pass |

[Back to Contents](#table-of-contents)

## Code Validation

### HTML
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). Results in the table below

| Page                    | Screenshot | Result |
|-------------------------|------------|:------:|
| Home                    |![screenshot](documentation/readme_images/testing/html_home.jpg)|Pass|
| Products                |![screenshot](documentation/readme_images/testing/html_products.jpg)|Pass|
| Add Product             |![screenshot](documentation/readme_images/testing/html_add_product.jpg)|Pass|
| Edit Product            |![screenshot](documentation/readme_images/testing/html_edit_product.jpg)|Pass|
| Confirm Delete Product  |![screenshot](documentation/readme_images/testing/html_confirm_delete.jpg)|Pass|
| Bag                     |![screenshot](documentation/readme_images/testing/html_bag.jpg)|Pass|
| Checkout                |![screenshot](documentation/readme_images/testing/html_checkout.jpg)|Pass|
| Checkout Success        |![screenshot](documentation/readme_images/testing/html_checkout_success.jpg)|Pass|
| Profile                 |![screenshot](documentation/readme_images/testing/html_profile.jpg)|Pass|
| Order History           |![screenshot](documentation/readme_images/testing/html_order_history.jpg)|Pass|
| Testimonials            |![screenshot](documentation/readme_images/testing/html_testimonials.jpg)|Pass|
| Add Testimonial         |![screenshot](documentation/readme_images/testing/html_testimonial_add.jpg)|Pass|
| Edit Testimonial        |![screenshot](documentation/readme_images/testing/html_testimonial_edit.jpg)|Pass|
| Delete Testimonial      |![screenshot](documentation/readme_images/testing/html_testimonials_delete.jpg)|Pass|
| Contact                 |![screenshot](documentation/readme_images/testing/html_contact.jpg)|Note|
| Sign In                 |![screenshot](documentation/readme_images/testing/html_sign_in.jpg)|Pass|
| Sign Up                 |![screenshot](documentation/readme_images/testing/html_signup.jpg)|Note|
| Log Out                 |![screenshot](documentation/readme_images/testing/html_logout.jpg)|Pass|
| Password Reset          |![screenshot](documentation/readme_images/testing/html_forgot_pass.jpg)|Note|
| 404.html                |![screenshot](documentation/readme_images/testing/html_error_page.jpg)|Pass|


Notes: Contact, Sign Up and Password Reset pages are presenting the same error, where Django renders the same id attribute ```id="id_email"``` for both the email input fields used in the newsletter subscription form created for the newsletter subscription in the footer and the email fields present in the other pages where the error is displayed.

Two possible solutions have been considered:
- Update the name of the email field in the newsletter subscribers model
- Use the Django widget to set a custom id attribute for the email that won't clash with the attributes of the other email fields. 

```
class SubscibersForm(forms.ModelForm):
class Meta:
    model = Subscribers
    fields = ['email', ]
    labels = {
        'email': ''
    }
    widgets = {
        'email': forms.TextInput(attrs={'id': 'form-sub'})
    }
```

However, due to time constraints, these solutions were not tested before submission. They will be tested in the future to ensure proper functionality and adherence to best practices.

### CSS

No errors were detected when running the CSS files through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input).

| Page             | Screenshot | Result |
|------------------|:----------:|:-----:|
| *base.css*       |![screenshot](documentation/readme_images/testing/css_base.jpg)|Pass|
| *checkout.css*   |![screenshot](documentation/readme_images/testing/css_checkout.jpg)|Pass|
| *profile.css*    |![screenshot](documentation/readme_images/testing/css_profile.jpg)|Pass|

### JavaScript

No errors were detected when running the JavaScript files through the official [JSHint](https://jshint.com/).

| Page             | Screenshot | Result |
|------------------|:----------:|:-----:|
| *base.html* script       |![screenshot](documentation/readme_images/testing/js_base.jpg)|Pass|
| *products.html* script   |![screenshot](documentation/readme_images/testing/js_products.jpg)|Pass|
| *bag.html* script    |![screenshot](documentation/readme_images/testing/js_bag.jpg)|Pass|
| profile: *countryfield.js*    |![screenshot](documentation/readme_images/testing/js_profile.jpg)|Pass|
| checkout: *stripe_elements.js* script    |![screenshot](documentation/readme_images/testing/js_checkout.jpg)|Pass|
| *quantity_input_script.html* script    |![screenshot](documentation/readme_images/testing/js_quantity.jpg)|Pass|
| *bag.html* script    |![screenshot](documentation/readme_images/testing/js_bag.jpg)|Pass|
| *edit_product.html* script    |![screenshot](documentation/readme_images/testing/js_edit_product.jpg)|Pass|

### Python

No errors were detected when running the Python files through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/#). Screenshot of the most relevant files are displayed below:

**Bag**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *contexts.py*                     | ![contexts](documentation/readme_images/testing/py_bag_context.jpg)  | Pass |
| *views.py*                     | ![views](documentation/readme_images/testing/py_bag_views.jpg)  | Pass |

**Checkout**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *admin.py*                     | ![contexts](documentation/readme_images/testing/py_checkout_admin.jpg)  | Pass |
| *forms.py*                     | ![views](documentation/readme_images/testing/py_checkout_forms.jpg)  | Pass |
| *models.py*                     | ![views](documentation/readme_images/testing/py_checkout_models.jpg)  | Pass |
| *signals.py*                     | ![views](documentation/readme_images/testing/py_checkout_signals.jpg)  | Pass |
| *views.py*                     | ![views](documentation/readme_images/testing/py_checkout_views.jpg)  | Pass |
| *webhook_handler.py*                     | ![views](documentation/readme_images/testing/py_checkout_webhook_handler.jpg)  | Pass |
| *webhooks.py*                     | ![views](documentation/readme_images/testing/py_checkout_webhooks.jpg)  | Pass |

**Contact**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *forms.py*                     | ![views](documentation/readme_images/testing/py_checkout_forms.jpg)  | Pass |
| *models.py*                     | ![views](documentation/readme_images/testing/py_contact_models.jpg)  | Pass |
| *views.py*                     | ![views](documentation/readme_images/testing/py_contact_views.jpg)  | Pass |

**Lari Living Main**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *settings.py*                     | ![views](documentation/readme_images/testing/py_main_settings.jpg)  | The three lines in the screenshot cannot be split |
| *urls.py*                     | ![views](documentation/readme_images/testing/py_main_urls.jpg)  | Pass |

**Newsletter**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *forms.py*                     | ![views](documentation/readme_images/testing/py_newsletter_forms.jpg)  | Pass |
| *models.py*                     | ![views](documentation/readme_images/testing/py_newsletter_models.jpg)  | Pass |
| *views.py*                     | ![views](documentation/readme_images/testing/py_newsletter_views.jpg)  | Pass |

**Products**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *admin.py*                     | ![views](documentation/readme_images/testing/py_products_admin.jpg)  | Pass |
| *forms.py*                     | ![views](documentation/readme_images/testing/py_products_forms.jpg)  | Pass |
| *models.py*                     | ![views](documentation/readme_images/testing/py_products_models.jpg)  | Pass |
| *views.py*                     | ![views](documentation/readme_images/testing/py_products_views.jpg)  | Pass |

**Profiles**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *forms.py*                     | ![views](documentation/readme_images/testing/py_profile_forms.jpg)  | Pass |
| *models.py*                     | ![views](documentation/readme_images/testing/py_profile_models.jpg)  | Pass |
| *views.py*                     | ![views](documentation/readme_images/testing/py_profile_views.jpg)  | Pass |

**Testimonials**

| File                           | Screenshot | Notes     |
|--------------------------------|------------|-----------|
| *models.py*                     | ![views](documentation/readme_images/testing/py_testimonials_models.jpg)  | Pass |
| *urls.py*                     | ![views](documentation/readme_images/testing/py_testimonials_urls.jpg)  | Pass |
| *views.py*                     | ![views](documentation/readme_images/testing/py_testimonials_views.jpg)  | Pass |

### Lighthouse

Lighthouse validation was used on all pages to assess performance, accessibility, best practices and SEO. Numerous warnings were addressed, notably concerning insufficient contrast ratio between background and foreground colors, resulting in the following scores:

| Page                     | Performance | Accessibility | Best Practices | SEO |
|--------------------------|:-----------:|:-------------:|:--------------:|:---:|
| Home                     |71|95|100|100|
| Products                 |74|91|100|100|
| Add Product              |95|94|100|100|
| Edit Product             |95|94|96|100|
| Confirm Delete Product   |96|95|100|100|
| Bag                      |92|95|100|100|
| Checkout                 |84|82 (note)|100|100|
| Checkout Success         |86|95|100|100|
| Profile                  |91|92|100|100|
| Order History            |84|95|100|100|
| Testimonials             |91|95|100|100|
| Add Testimonial          |90|95|100|100|
| Edit Testimonial         |93|95|100|100|
| Delete Testimonial       |96|95|100|100|
| Contact                  |95|100|100|100|
| Sign In                  |94|96|100|100|
| Sign Up                  |96|95|100|100|
| Log Out                  |96|95|100|100|
| Password Reset           |96|95|100|100|

Notes: The score on the checkout page is influenced by the color of the placeholders in the fields and by the issue of repeating IDs discussed in the [HTML](#html) section. Typically, placeholders have a fainter color, so changing them has not been considered an option. It is foreseen that the score will increase to acceptable levels once the issue mentioned in the HTML section is resolved.

[Back to Contents](#table-of-contents)

## Browser Testing

The website was tested on Google Chrome, Firefox, Edge and Safari browsers, with no issues noted.

[Back to Contents](#table-of-contents)

## Device Testing

The website was tested on different devices and displays, including Desktop, Laptop, Android and Apple devices to check responsiveness across different screen sizes in both portrait and landscape modes. The website functioned as expected across all devices, demonstrating its responsiveness. The responsive design was checked using Chrome developer tools on multiple devices.

[Back to Contents](#table-of-contents)

## Manual Testing

### Site Navigation

| Element                          | Action                        | Expected Result                                              | Pass/Fail |
|----------------------------------|-------------------------------|--------------------------------------------------------------|-----------|
| NavBar                           |                               |                                                              |           |
| Site Name (logo area)            | Click                         | Redirect to home                                             | Pass      |
| Search Box Function              | Enter Text and Click Search   | Search both the product's title and description for a match. | Pass      |
| My Account Dropdown              | Click                         | Open profile dropdown                                        | Pass      |
| Sign Up Link                     | Click                         | Redirect to Sign Up page                                     | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
| Login Link                       | Click                         | Redirect to login page                                       | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
| Product Management Link          | Click                         | Redirect to add_product page                                 | Pass      |
|                                  |                               | (Only visible if superuser in session)                       | Pass      |
| My Profile Link                  | Click                         | Redirect to user profile page                                | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Logout Link                      | Click                         | Redirect to logout confirm page                              | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Bag Link                         | Click                         | Redirect to bag page                                         | Pass      |
|                                  |                               |                                                              |           |
| Mobile Top Header                |                               |                                                              |           |
| Search Icon Button               | Click                         | Open up search box                                           | Pass      |
| Search Box Function              | Enter Text and Click Search   | Search both the product's title and description for a match. | Pass      |
| My Account Dropdown              | Click                         | Open profile dropdown                                        | Pass      |
| Sign Up Link                     | Click                         | Redirect to Sign Up page                                     | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
| Login Link                       | Click                         | Redirect to login page                                       | Pass      |
|                                  |                               | (Not visible if user in session)                             | Pass      |
| Product Management Link          | Click                         | Redirect to add_product page                                 | Pass      |
|                                  |                               | (Only visible if superuser in session)                       | Pass      |
| My Profile Link                  | Click                         | Redirect to user profile page                                | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Logout Link                      | Click                         | Redirect to logout confirm page                              | Pass      |
|                                  |                               | (Only visible if user in session)                            | Pass      |
| Bag Link                         | Click                         | Redirect to bag page                                         | Pass      |
|                                  |                               |                                                              |           |
| Main Nav                         |                               |                                                              |           |
| Products Dropdown                | Click                         | Open products dropdown                                       | Pass      |
| All Link                         | Click                         | Redirect all products page                                   | Pass      |
| Sofas Link                       | Click                         | Redirect to prints page filtered to sofas                    | Pass      |
| Chairs Link                      | Click                         | Redirect to prints page filtered to chairs                   | Pass      |
| Tables Link                      | Click                         | Redirect to prints page filtered to tables                   | Pass      |
| Testimonials Link                | Click                         | Open Testimonials Page                                       | Pass      |
| Contact Link                     | Click                         | Open Contact Page                                            | Pass      |
| Hamburger Menu                   | Responsive                    | Display when screen size reduces to small size               | Pass      |
| Home Link                        | Click                         | Redirect to home                                             | Pass      |
|                                  |                               | (Only displays when screen size reduces to medium size)      | Pass      |
| Footer                           |                               |                                                              |           |
| Social Media Icon Links          | Click                         | Open correct location in new tab                             | Pass      |
| Newsletter Email field           | Insert incorrect/empty format | Form won't submit                                            | Pass      |
| Newsletter Email field           | Insert incorrect/empty format | Error message displays                                       | Pass      |
| Subscribe Button                 | Click                         | Form submit                                                  | Pass      |
| Subscribe Button                 | Click                         | Message appears saying Thank You for subscribing!            | Pass      |
| Products Link                    | Click                         | Open Products Page                                           | Pass      |
| Testimonials Link                | Click                         | Open Testimonials Page                                       | Pass      |
| Contact Link                     | Click                         | Open Contact Page                                            | Pass      |
| Privacy Policy Link              | Click                         | Open Privacy Policy Page in new tab                          | Pass      |
| Logo area (mobile)               | Click                         | Redirect to home                                             | Pass      |


### Home Page

| Element                | Action | Expected Result                    | Pass/Fail |
|------------------------|--------|------------------------------------|-----------|
| Shop Now Button        | Click  | Open Product Page                  | Pass      |
| Contact Us             | Click  | Open Contact Form Page             | Pass      |


### Allauth 

| Element                         | Action                                    | Expected Result                              | Pass/Fail |
|---------------------------------|-------------------------------------------|----------------------------------------------|-----------|
| Sign Up                         |                                           |                                              |           |
| Sign in link                    | Click                                     | Redirect to sign in page                     | Pass      |
| Email field                     | Insert incorrect format                   | On submit: form won't submit                 | Pass      |
| Email field                     | Insert incorrect format                   | Error message displays                       | Pass      |
| Email field                     | Insert correct format                     | On submit: form submit                       | Pass      |
| Email field                     | Leave empty                               | On submit: form won't submit                 | Pass      |
| Email field                     | Insert duplicate email                    | On submit: form won't submit                 | Pass      |
| Email field                     | Insert duplicate email                    | Error message displays                       | Pass      |
| Email Confirmation field        | Insert different email                    | On submit: form won't submit                 | Pass      |
| Email Confirmation field        | Insert different email                    | Error message displays                       | Pass      |
| Username field                  | Leave empty/incorrect format              | On submit: form won't submit                 | Pass      |
| Username field                  | Leave empty/incorrect format              | Error message displays                       | Pass      |
| Username field                  | Insert correct format                     | On submit: form submit                       | Pass      |
| Username field                  | Insert duplicate username                 | On submit: form won't submit                 | Pass      |
| Username field                  | Insert duplicate username                 | Error message displays                       | Pass      |
| Password field                  | Insert incorrect format/length            | On submit: form won't submit                 | Pass      |
| Password field                  | Insert incorrect format/length            | Error message displays                       | Pass      |
| Password field                  | Passwords don't match                     | On submit: form won't submit                 | Pass      |
| Password field                  | Passwords don't match                     | Error message displays                       | Pass      |
| Password field                  | Insert correct format and passwords match | On submit: form submit                       | Pass      |
| Sign Up button(form valid)      | Click                                     | Form submit                                  | Pass      |
| Sign Up button(form valid)      | Click                                     | Redirect to Verify Email Address page        | Pass      |
| Sign Up button(form valid)      | Click                                     | Alert message confirming email sent appears  | Pass      |
| Confirmation Email Confirm Link | Click                                     | Open Confirm Email Address Page              | Pass      |
| Confirm Button                  | Click                                     | Success message confirming new user appears  | Pass      |
| Confirm Button                  | Click                                     | Redirect to sign in page                     | Pass      |
|                                 |                                           |                                              |           |
| Log in                          |                                           |                                              |           |
| Sign up link                    | Click                                     | Redirect to sign up page                     | Pass      |
| Username field                  | Leave empty                               | On submit: form won't submit                 | Pass      |
| Username field                  | Leave empty                               | Error message displays                       | Pass      |
| Username field                  | Insert wrong username                     | On submit: form won't submit                 | Pass      |
| Username field                  | Insert wrong username                     | Error message displays                       | Pass      |
| Password field                  | Leave empty                               | On submit: form won't submit                 | Pass      |
| Password field                  | Leave empty                               | Error message displays                       | Pass      |
| Password field                  | Insert wrong password                     | On submit: form won't submit                 | Pass      |
| Password field                  | Insert wrong password                     | Error message displays                       | Pass      |
| Login button(form valid)        | Click                                     | Form submit                                  | Pass      |
| Login button(form valid)        | Click                                     | Redirect to home page                        | Pass      |
| Login button(form valid)        | Click                                     | Success message confirming login appears     | Pass      |
| Forgot Password Link            | Click                                     | Redirect to Password Reset page              | Pass      |
| Email field                     | Leave empty/incorrect format              | On submit: form submit                       | Pass      |
| Reset My Password Button        | Click                                     | Confirmation message that email sent         | Pass      |
| Password Reset Email Link       | Click                                     | Open Change Password Page                    | Pass      |
| Change Password Button          | Click                                     | Success message confirming Password Changed  | Pass      |
|                                 |                                           |                                              |           |
| Sign Out Confirmation           |                                           |                                              |           |
| Sign Out  button                | Click                                     | Redirect to homepage                         | Pass      |
| Sign Out  button                | Click                                     | Success message confirming Sign Out  appears | Pass      |


### Products

| Element                         | Action  | Expected Result                                                                                | Pass/Fail |
|---------------------------------|---------|------------------------------------------------------------------------------------------------|-----------|
| Sort By' Dropdown               | Click   | Open 'sort by' options                                                                         | Pass      |
| Sort By' Options (x3)           | Click   | Re-order products correctly                                                                    | Pass      |
| Product Number                  | Display | Displays correct number of products on page                                                    | Pass      |
| Product Card                    | Click   | Redirect to product detail page                                                                | Pass      |
| If Searched Product             | Display | Only display products with search term in either the product's title or description or excerpt | Pass      |
| If Searched Product             | Display | Display number of products found for "searched product"                                        | Pass      |
| If Superuser in session:        |         |                                                                                                |           |
| Add New Product Button          | Click   | Redirect to add product page                                                                   | Pass      |
| Edit product link               | Click   | Redirect to edit product page                                                                  | Pass      |
| Delete product link             | Click   | Open delete confirmation  page                                                                 | Pass      |
| Confirm Delete -  cancel button | Click   | Redirect to products page                                                                      | Pass      |
| Confirm Delete -  delete button | Click   | Delete product                                                                                 | Pass      |
| Confirm Delete -  delete button | Click   | Success message appears confirming product deleted successfully                                | Pass      |


### Product Detail

| Element                  | Action                    | Expected Result                                                                              | Pass/Fail |
|--------------------------|---------------------------|----------------------------------------------------------------------------------------------|-----------|
| Product Content          | Display                   | Display correct product image, excerpt, price, product details and dispatch time frame       | Pass      |
| Qty control buttons      | Click                     | Increase/decrease quantity                                                                   | Pass      |
| Qty control buttons      | Click                     | Minus button disabled if quantity is 1                                                       | Pass      |
| Qty control buttons      | Click                     | Plus button disabled if quantity is 15                                                       | Pass      |
| Qty control buttons      | Manually Input  <1 or >15 | If quantity >15 or <1 manually entered, error message appears when Add to Bag button clicked | Pass      |
| Keep Shopping button     | Click                     | Redirect to products   page                                                                  | Pass      |
| Add to bag button        | Click                     | Add item to bag                                                                              | Pass      |
| Add to bag button        | Click                     | Toast Success appears                                                                        | Pass      |
| Add to bag button        | Click                     | Product and quantity visible in toast success                                                | Pass      |
| If Superuser in session: |                           |                                                                                              |           |
| Edit product link        | Click                     | Redirect to edit product page                                                                | Pass      |
| Delete product link      | Click                     | Open delete confirmation  page                                                               | Pass      |

### Product Management 

| Element                         | Action                | Expected Result                                                                                                            | Pass/Fail |
|---------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------|-----------|
| Add Product                     | Access                | If a user tries to add a product (by changing the url) without being signed in they are redirected to the login page       | Pass      |
| Add Product                     | Access                | If a user tries to add a product (by changing the url) without being superuser they receive an error message               | Pass      |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | Pass      |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | Pass      |
| Form image select button        | Click                 | Open device storage                                                                                                        | Pass      |
| Form image select button        | Display               | Chosen image name displayed once selected                                                                                  | Pass      |
| Form image select button        | Display               | Default image is used if no image is selected                                                                              | Pass      |
| Cancel button                   | Click                 | Redirect to product page                                                                                                   | Pass      |
| Add Product button(form valid)  | Click                 | Form submit                                                                                                                | Pass      |
| Add Product button(form valid)  | Click                 | Redirect to Product detail page for new product with all information displaying correctly                                  | Pass      |
| Add Product button(form valid)  | Click                 | Success message appears informing the superuser that the product has been added                                            | Pass      |
|                                 |                       |                                                                                                                            |           |
| Edit Product                    |                       |                                                                                                                            |           |
| Edit Product                    | Access                | If a user tries to edit a product (by changing the url) without being signed in they are redirected to the login page      | Pass      |
| Edit Product                    | Access                | If a user tries to edit a product (by changing the url) without being superuser they receive an error message              | Pass      |
| Edit Product Form               | Display               | Form has all the fields filled out with the original content                                                               | Pass      |
| Edit Product Form               | Image Field           | Thumbnail of original image is shown                                                                                       | Pass      |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | Pass      |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | Pass      |
| Cancel button                   | Click                 | Redirect to product page                                                                                                   | Pass      |
| Submit button(form valid)       | Click                 | Form submit                                                                                                                | Pass      |
| Edit Product button(form valid) | Click                 | Redirect to Product detail page for new product with all information displaying correctly                                  | Pass      |
| Edit Product button(form valid) | Click                 | Success message appears informing the superuser that the product has been updated                                          | Pass      |
|                                 |                       |                                                                                                                            |           |
| Confirm Delete Product          |                       |                                                                                                                            |           |
| Delete Product                  | Access                | If a user tries to Delete a product (by changing the url) without being signed in they are redirected to the login page    | Pass      |
| Delete Product                  | Access                | If a user tries to Delete a product (by changing the url) without being superuser they receive an error message            | Pass      |
| Confirm Delete -  cancel button | Click                 | Redirect to the product page                                                                                               | Pass      |
| Confirm Delete -  delete button | Click                 | Delete product                                                                                                             | Pass      |
| Confirm Delete -  delete button | Click                 | Success message appears confirming product deleted successfully                                                            | Pass      |

### Bag

| Element                                                       | Action              | Expected Result                                        | Pass/Fail |
|---------------------------------------------------------------|---------------------|--------------------------------------------------------|-----------|
| No Bag Items                                                  |                     |                                                        |           |
| Keep Shopping button                                          | Click               | Redirect to products page                              | Pass      |
| Bag Items                                                     |                     |                                                        |           |
| Qty control buttons                                           | Click               | Increase/decrease quantity                             | Pass      |
| Qty control buttons                                           | Click               | Minus button disabled if quantity is 1                 | Pass      |
| Qty control buttons                                           | Click               | Plus button disabled if quantity is 99                 | Pass      |
| Qty control buttons                                           | Manually Input  >99 | Error message appears when refresh button is clicked   | Pass      |
| Qty control buttons                                           | Manually Input  <1  | Shopping bag is emptied when refresh button is clicked | Pass      |
| Update button                                                 | Click               | Update bag item quantity                               | Pass      |
| Update button                                                 | Refresh Icon button | Updated confirmation toast appears                     | Pass      |
| Remove button                                                 | Click               | Remove item from bag                                   | Pass      |
| Remove button                                                 | Click               | Removed confirmation toast appears                     | Pass      |
| Line item subtotal / Bag total / Delivery cost / Grand Total  | Calculate           | All numbers are calculated correctly                   | Pass      |
| Continue shopping button                                      | Click               | Redirect to products page                              | Pass      |
| Secure Checkout button                                        | Click               | Redirect to checkout page                              | Pass      |

### Checkout

| Element                             | Action                          | Expected Result                                                     | Pass/Fail |
|-------------------------------------|---------------------------------|---------------------------------------------------------------------|-----------|
| Checkout Page                       | Direct URL input (empty bag)    | redirect to products page                                           | Pass      |
| Checkout Page                       | Direct URL input (empty bag)    | empty bag toast appears                                             | Pass      |
| Form fields(if user logged in)      | On load                         | fields populated with user default info (if previously saved)       | Pass      |
| Text Input(if required)             | Leave blank                     | On submit:form won't submit                                         | Pass      |
| Text Input(if required)             | Leave blank                     | error message on invalid field(s)                                   | Pass      |
| Text Input(if required)             | Just whitespace                 | On submit:form won't submit                                         | Pass      |
| Text Input(if required)             | Just whitespace                 | error message on invalid field(s)                                   | Pass      |
| Text Input(if required)             | Fill in correctly               | On submit: form submits                                             | Pass      |
| Phone number Input                  | Leave blank                     | On submit:form won't submit                                         | Pass      |
| Phone number Input                  | Leave blank                     | error message on field                                              | Pass      |
| Phone number Input                  | Just whitespace                 | On submit:form won't submit                                         | Pass      |
| Phone number Input                  | Just whitespace                 | error message on field                                              | Pass      |
| Phone number Input                  | Use non numeric characters      | On submit:form won't submit                                         | Pass      |
| Phone number Input                  | Use non numeric characters      | error message on field                                              | Pass      |
| Email Input                         | Leave blank                     | On submit:form won't submit                                         | Pass      |
| Email Input                         | Leave blank                     | error message on field                                              | Pass      |
| Email Input                         | Just whitespace                 | On submit:form won't submit                                         | Pass      |
| Email Input                         | Just whitespace                 | error message on field                                              | Pass      |
| Email Input                         | Fill in correctly               | On submit: form submits                                             | Pass      |
| Form Dropdown                       | Click                           | Show dropdown options                                               | Pass      |
| Save to profile checkbox            | On load(user logged in)         | Shown                                                               | Pass      |
| Save to profile checkbox            | On load(user not logged in)     | Not shown                                                           | Pass      |
| Save to profile checkbox            | Checked                         | On submit:Delivery information saved to user profile                | Pass      |
| Save to profile checkbox            | Unchecked                       | On submit:Delivery information not saved to user profile            | Pass      |
| Payment card input                  | Input invalid card number       | Error message on field                                              | Pass      |
| Payment card input                  | Input invalid date              | Error message on field                                              |           |
| Adjust Bag button                   | Click                           | Redirect to bag page                                                | Pass      |
| Complete Order button(form invalid) | Click                           | Form won't submit                                                   | Pass      |
| Complete Order button(form invalid) | Click                           | Error message on invalid fields                                     | Pass      |
| Complete Order button(form valid)   | Payment succeeds                | Loading screen reappears                                            | Pass      |
| Complete Order button(form valid)   | Payment succeeds                | Form submits                                                        | Pass      |
| Complete Order button(form valid)   | Payment succeeds                | Redirect to order confirmation page                                 | Pass      |
| Complete Order button(form valid)   | (if user logged in)             | Order saved to user profile                                         | Pass      |
| Complete Order button(form valid)   | Payment failed                  | Loading animation appears                                           | Pass      |
| Complete Order button(form valid)   | Payment failed                  | Form won't submit                                                   | Pass      |
| Complete Order button(form valid)   | Payment failed                  | Error message at bottom of form                                     | Pass      |
| Complete Order button(form valid)   | Click                           | Success message appears confirming order successfully processed     | Pass      |
| Complete Order button(form valid)   | Payment Requires authentication | Authentication box appears                                          | Pass      |
| Fail Authentication button          | Click                           | Authentication box closes                                           | Pass      |
| Fail Authentication button          | Click                           | User directed back to form                                          | Pass      |
| Fail Authentication button          | Click                           | Error message at bottom of form                                     | Pass      |
| Complete Authentication button      | Click                           | Loading screen reappears                                            | Pass      |
| Complete Authentication button      | Click                           | Form submits                                                        | Pass      |
| Complete Authentication button      | Click                           | Redirect to order confirmation page                                 | Pass      |
| Complete Order button(form valid)   | Click                           | Success message appears confirming order successfully processed     | Pass      |
| Complete Order button(form valid)   | Click                           | User receives an order confirmation email with correct information  | Pass      |
|                                     |                                 |                                                                     |           |
| Checkout Success Page               |                                 |                                                                     |           |
| Element                             | Action                          | Expected Result                                                     | Pass/Fail |
| Order Confirmation                  | Display                         | Display Correct Order Details                                       | Pass      |
| Keep Shopping! button               | Click                           | Redirect to products page                                           | Pass      |

### Profile

| Element                | Action            | Expected Result                                                                                                                | Pass/Fail |
|------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Open Profile Page      | Access            | If a user tries to access the profile page (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Form fields            | On load           | fields populated with user default info(if previously saved)                                                                   | Pass      |
| All input fields       | Leave blank       | On submit: form submits                                                                                                        | Pass      |
| All input fields       | Just whitespace   | On submit: form submits                                                                                                        | Pass      |
| All input fields       | Fill in correctly | On submit: form submits                                                                                                        | Pass      |
| Form Dropdown          | Click             | Show dropdown options                                                                                                          | Pass      |
| Update button          | Click             | Form submits                                                                                                                   | Pass      |
| Update button          | Click             | Success message appears confirming profile successfully updated                                                                | Pass      |
| Previous order number  | Click             | Redirect to previous order page                                                                                                | Pass      |
|                        |                   |                                                                                                                                |           |
| Previous Order Page    |                   |                                                                                                                                |           |
| Element                | Action            | Expected Result                                                                                                                | Pass/Fail |
| Information Display    | Display           | All previous order information displays correctly                                                                              | Pass      |
| Toast                  | On load           | Previous order info toast appears                                                                                              | Pass      |
| Back to Profile button | Click             | Redirect to profile page                                                                                                       | Pass      |

### Testimonials

| Element                 | Action  | Expected Result                                                                    | Pass/Fail |
|-------------------------|---------|------------------------------------------------------------------------------------|-----------|
| Testimonial Content     | Display | Display correct testimonial content, service type, author and date                 | Pass      |
| Add Testimonial button  | Click   | Open Add testimonial form                                                          | Pass      |
| Add Testimonial button  | Click   | If a user has already added a testimonial they receive a warning message           | Pass      |
| Add Testimonial button  | Display | If the user is not logged in the button is not displayed                           | Pass      |
| Edit testimonial link   | Display | Only display if user is the author of the testimonial or if they are the superuser | Pass      |
| Edit testimonial link   | Click   | Redirect to edit testimonial page                                                  | Pass      |
| Delete Testimonial link | Display | Only display if user is the author of the testimonial                              | Pass      |

### Contact

| Element                       | Action                | Expected Result                                                                     | Pass/Fail |
|-------------------------------|-----------------------|-------------------------------------------------------------------------------------|-----------|
| Form Text Input (if required) | Leave blank           | On Submit: Warning appears, form won't submit                                       | Pass      |
| Form Text Input (if required) | Just input whitespace | On Submit: Warning appears Form won't submit                                        | Pass      |
| Email Input                   | Incorrect Format      | On Submit: Warning appears, form won't submit                                       | Pass      |
| Enquiry Type Dropdown         | Click                 | Display all Enquiry Types in Database                                               | Pass      |
| Submit button(form valid)     | Click                 | Form submit                                                                         | Pass      |
| Submit button(form valid)     | Click                 | Redirect to home Page                                                               | Pass      |
| Submit button(form valid)     | Click                 | Success message appears informing the superuser that the enquiry has been submitted | Pass      |
| Submit button(form valid)     | Click                 | User receives confirmation email about their enquiry                                | Pass      |
| Submit button(form valid)     | Click                 | Store owner receives email. The email has Subject: Enquiry Type, Body: Message      | Pass      |

[Back to Contents](#table-of-contents)

## Bugs

Resolved bugs, along with explanations, have been documented within the GitHub Projects [kanban board](https://github.com/users/Darioc18/projects/4). These bugs have been labeled in red to distinguish them from other tasks:

- Fixing navigation category links to display only selected category products. Issue [#9](https://github.com/Darioc18/PP5_lari_living/issues/9)
- Sorting box not visible. Issue [#10](https://github.com/Darioc18/PP5_lari_living/issues/10)
- Enforcing one-review-per-user policy. Issue [#19](https://github.com/Darioc18/PP5_lari_living/issues/19)
- Duplicate email subscription. Issue [#30](https://github.com/Darioc18/PP5_lari_living/issues/10)
- Newsletter form rendering issue. Issue [#38](https://github.com/Darioc18/PP5_lari_living/issues/38)
- handling subscription errors with existing emails. Issue [#39](https://github.com/Darioc18/PP5_lari_living/issues/39)
- Resolving 404 error when editing or deleting testimonials as superuser. Issue [#40](https://github.com/Darioc18/PP5_lari_living/issues/40)
- Fixing newsletter recipient's access to subscriber emails. Issue [#41](https://github.com/Darioc18/PP5_lari_living/issues/41)

[Back to Contents](#table-of-contents)