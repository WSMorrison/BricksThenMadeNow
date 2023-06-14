# Bricks Then Made Now

Bricks Then Made Now is an ecommerce site that sells fan made Lego designs to other Lego fans. The site will appeal to adult followers of Lego (AFOL), by reimagining vintage Lego from the 1970s, '80s, and '90s with modern elements and contemporary design techniques.

![Front page of Bricks Then Made Now as input to AmIResponsive.](#)

[AmIResponsive](https://ui.dev/amiresponsive)

### The side, deployed to Heroku, can be found here: [Bricks Then Made Now](#)
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
    - [Testing](#)
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
| Nav Bar                 | Display  | Show All, Log In, Sign Up tabs                                         | Pass    |
| Nav Bar                 | Display  | Indicate navigated tab                                                 | Pass    |
| Footer                  | Display  | Display social meda links                                              | Pass    |


| Delete event               | Pass    |
| Filter events by date      | Pass    |
| Filter events by organizer | Pass    |
| Filter events by attendee  | Pass    |
| Add user to event          | Pass    |
| Remove user from event     | Pass    |
| Promote user to organizer  | Pass    |
| Demote organizer to user   | Pass    |

<br>
<hr>

### Representative User Manual Testing

<hr>

In addition to formal manual testing, the site was shown to friends who would be representative as users for this website. Most of these testers are active in the car community, or at least adjacent enough to the car community to provide relevant, valuable feedback.

- Despite the Code Institute instruction suggesting the website is too visually plain, representative User testers appreciated the simple and clear design.
- Representative User testers were able to visit the site, view event lists and event details.
- Navigation was clear and easy to follow.
- Users were able to sign up for user accounts.
- Users were able to register for events they liked.
- Users were able to view a list of events they were registered for.
- Users were able to unregister for events they decided they didn't like.
- Users given the permissions were able to create events easily.
    - Feedback was given and addressed about certain special characters causing errors.
    - Feedback was given and addressed about form validation error copy being vague.
- Users given the permissions were able to edit events easily.
    - Feedback was given and addressed about an error regarding form validation in the edit view.
- Users were able to input event location URLs without issue.
    - Feedback was given and addressed about URL examples and behavior nudging.
    - Feedback was given and considered, but ultimately rejected, about having the URL be optional or allowing non-Google Maps sources. 
        - The feature is considered too important to the purpose of the site.
        - Non-Google Maps sources are considered non-standard and potentially unreliable, and would conflict with the simplicity and consistency the HardParkers intends to provide.
        - The maps link is considered an MVP for future feature implementations.
    - Feedback was given and addressed about URLs being different from different Google Maps sources, particularly mobile app sources which the HardParkers intends to directly target.
- The printable attendee list printed without any formatting adjustments for a straightforward print. It was also tested for printing to a .pdf, which it did directly and without issue.

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