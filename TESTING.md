# Bricks Then Made Now

Bricks Then Made Now is an ecommerce site that sells fan made Lego designs to other Lego fans. The site will appeal to adult followers of Lego (AFOL), by reimagining vintage Lego from the 1970s, '80s, and '90s with modern elements and contemporary design techniques.

![Front page of Bricks Then Made Now as input to AmIResponsive.](#)

[AmIResponsive](https://ui.dev/amiresponsive)

### The site, deployed to Heroku, can be found here: [Bricks Then Made Now](#)
#### The repository in GitHub can be found here: [WSMorrison/bricksthenmadenow](#)

<br>
<hr>

## Contents

<hr>

- [Testing](#testing)
  - [Responsiveness](#responsiveness)
  - [Accessibility](#accessibility)
  - [Code Validation](#code-validation)
  - [Systematic Manual Testing](#systematic-manual-testing)
    - [Testing tables](#)
    ...
    - [Testing tables](#)
  - [Representative User Manual Testing](#representative-user-manual-testing)
  - [Bugs](#bugs)
      - [Fixed bugs](#fixed-bugs)
      - [Unfixed bugs](#unfixed-bugs)

<br>
<hr>

## Testing

<hr>

## Responsiveness

The page was checked for responsiveness by using [AmIResponsive.](https://ui.dev/amiresponsive)

![Front page of Bricks Then Made Now as input to AmIResponsive.](#)

## Accessibility

Care was taken to make sure the website was accessible.

  - The page is developed to use high contrast text, simple interface and easy to follow buttons. 
  - Aria labels are on any button that is not labelled.
  - The tabs are all marked current so that the nav bar indicates where the user is currently navigated. 
  - The HTML follows a clear semantic flow.

Accessibility was checked by using Google Chrome [Lighthouse.](https://chrome.google.com/webstore/detail/lighthouse/)

![Lighthouse score for page](#)

The accessibility score is less than 100% because

## Code Validation

The HTML for the website was put through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Each page of the site was tested by opening the page, viewing page source, and copying and pasting the source code into the validator. This avoided any issues with the template tags upsetting the validator to the point that it did not check the rest of the code. Any errors found were fixed. As credit to Django's automated page generation through template tags, the only errors were in the hand written code of the base.html; a stray closing italic tag in the footer, and an attempt at a responsive break in the blockquote to try to influence the line break that did not have any effect. Both were fixed, and each page was returned without errors.

![W3C Markup validator representative return](#)

The CSS was put through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

![W3C CSS validator representative return](#)

The Python code was checked with the [Code Institute Python linter](https://pep8ci.herokuapp.com/).py, and views.py. Each was returned without errors.

![CI Python linter representative return](#)

<br>
<hr>

## Systematic Manual Testing

<hr>

The following tables will describe the systematic manual testing done to ensure that the app is working properly.

<hr>

### Unlogged-in User

<hr>

The following features were tested as an unlogged-in user:

#### Index page (Unlogged-in User):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Splash Image            | Hover    | Indicate link                                                          | Pass    |
| Splash Image            | Click    | Navigate to home tab                                                   | Pass    |
...

...
| Promote user to organizer  | Pass    |
| Demote organizer to user   | Pass    |

<br>
<hr>

### Representative User Manual Testing

<hr>

In addition to formal manual testing, the site was shown to friends who would be representative as users for this website. Most of these testers are active in the Lego community, or at least Lego community adjacent. Regardless, even non-Lego testers understand how to use the internet and e-commerce and were therefore able to give relevant and valuable feedback. The following testing was completed by representative testers.

- Representative User testers were able to visit the site, view event lists and event details.
- Navigation was clear and easy to follow.
- Users were able to sign up for user accounts.
- 

<br>
<hr>

### Bugs

<hr>

Several bugs were found during development, and most were fixed.

#### Fixed Bugs

The following bugs were fixed during development:

1. When using the Sku creation form in new-sku.html, the newly created Skus were sending infomration and were not being added to the item-detail.html when viewing item details. Troubleshooting found that using get_object_or_404 would for some reason work with the admin panel created Skus, but weren't the correct choice for use on a queryset. Since the view was already try/excepting finding the Skus, object.get is perfectly functional. The correct Sku details are being correctly displayed on the correct Item object detail page.
2.  

#### Unfixed Bugs:

The following bugs have not yet been fixed:

1. Sorting dropdown menu does not sort a currently selected Theme or search result.
2.  

<hr>
For educational purposes only.