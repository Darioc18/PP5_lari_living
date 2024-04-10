# Lari Living Testing

## Table of Contents

- [User Story Testing](#user-story-testing)
- [Site Administration](#site-administration)
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
    - [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Manual Testing](#manual-testing)
    - [Site Navigation](#site-navigation)
    - [Home Page](#home-page)    
    - [Products](products)
    - [Product Details](#product-details)
    - [Products Management](#products-management)
    - [Bag](#bag)
    - [Checkout](#checkout)
    - [Profile](#profile)
    - [Testimonials](#testimonials)
    - [Contact](#contact)
    - [Allauth](#allauth)
- [Bugs](#bugs)

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
| Checkout Success               |![screenshot](documentation/readme_images/testing/html_checkout_success.jpg)|Pass|
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

## Lighthouse

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