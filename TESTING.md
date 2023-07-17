# Bricks Then Made Now

Bricks Then Made Now is an ecommerce site that sells fan made Lego designs to other Lego fans. The site will appeal to adult followers of Lego (AFOL), by reimagining vintage Lego from the 1970s, '80s, and '90s with modern elements and contemporary design techniques.

![Front page of Bricks Then Made Now as input to AmIResponsive.](/assets/readme-images/am-i-responsive.png)

[AmIResponsive](https://ui.dev/amiresponsive)

### The site, deployed to Heroku, can be found here: [Bricks Then Made Now](https://bricks-then-made-now-5bd876713bd4.herokuapp.com/)
#### The repository in GitHub can be found here: [WSMorrison/bricksthenmadenow](https://github.com/WSMorrison/BricksThenMadeNow)


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

The website was built for responsive use. Most customers will engage the site on a mobile site, and staff members will likely use a computer. However, all aspects of the site work on both small and larger devices.

![Front page of Bricks Then Made Now as input to AmIResponsive.](/assets/readme-images/am-i-responsive.png)

The front page, showing how some of the arrangement changes based on different screen sizes.

![Items page tested for responsiveness.](/assets/readme-images/testing/items-responsive.png)

The items page looking at the City theme, showing how some of the arrangement changes based on different screen sizes.

![Item detail tested for responsiveness.](/assets/readme-images/testing/item-detail-responsive.png)

An item detail page, showing how some of the arrangement changes based on different screen sizes.

[AmIResponsive](https://ui.dev/amiresponsive)

## Accessibility

Care was taken to make sure the page met accessibility guidelines. Accessibility is important so that everyone is welcome and included on Bricks Then Made Now. 

- All images have alt text, and all links and buttons have aria labels.
- Semantic web structure was maintained, making sure to use headers, footers, body, sections and divs appropriately to organize the page not just visually but for screen readers as well.
- Colors and images were carefully selected to make sure that contrast was great enough so that anyone could read the website. Colors were checked for contrast during development using Coolers' [Color Contrast Checker](https://coolors.co/contrast-checker/0067b2-d2d5da)

![Google Lighthouse scores](/assets/readme-images/lighthouse-score.png)

The accessibility was scored at 96% based on the the footer background and text contrast. It wasn't possible to make any real change to the score while still indicating that the footer section was different than the rest. Other accessibility aspects were detected and fixed, bringing the score to 96%.

Accessibility, Best Practices and SEO scores calculated by [Google Lighthouse.](https://developer.chrome.com/docs/lighthouse/overview/)

## Code Validation

Code was validated by using online validators and linters. Any errors were solved, until the code returned no errors.

![HTML validation representative return](/assets/readme-images/testing/w3c-html-valdiation.png)

The HTML for the website was put through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Each page of the site was tested by opening the page, viewing page source, and copying and pasting the source code into the validator. This avoided any issues with the template tags upsetting the validator to the point that it did not check the rest of the code. Any errors found were fixed. As credit to Django's automated page generation through template tags, the only errors were in the hand written code of the base.html; a stray closing italic tag in the footer, and an attempt at a responsive break in the blockquote to try to influence the line break that did not have any effect. Both were fixed, and each page was returned without errors.

![W3C CSS validator return](/assets/readme-images/testing/w3c-css-validation.png)

The CSS was put through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

![CI Python linter representative return](/assets/readme-images/testing/ci-python-linter-validation.png)

The Python code was checked with the [Code Institute Python linter](https://pep8ci.herokuapp.com/).py, and views.py. Each either was returned without errors or errors were solved until there were none.

<br>
<hr>

## Systematic Manual Testing

<hr>

The following tables will describe the systematic manual testing done to ensure that the app is working properly.

The following features were tested on each page as indicated:

### Index page
#### Index page (All Users):

| Element      | Action   | Expected Result                                                                                                                                                                                                                                                     | Outcome |
|--------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar    | Display  | Show title, search bar, cart icon                                                                                                                                                                                                                                   | Pass    |
| Title        | Interact | Indicates link on hover, click takes user to index page.                                                                                                                                                                                                            | Pass    |
| Search bar   | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly, outcome appropriate for search                                                                                                                              | Pass    |
| Cart icon    | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount shows running total.                                                                                                                                                 | Pass    |
| Nav bar      | Display  | Bar displays, show selectable themes, log in link                                                                                                                                                                                                                   | Pass    |
| Theme links  | Interact | Indicate links on hover, open correct list of items                                                                                                                                                                                                                 | Pass    |
| Login link   | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                                                                  | Pass    |
| Splash image | Display  | Shows image responsively.                                                                                                                                                                                                                                           | Pass    |
| Carousel     | Display  | Shows rotating informational images.                                                                                                                                                                                                                                | Pass    |
| Carousel     | Interact | Indicates link on hover, pauses on hover, user can advance the images, links take customer to correct page                                                                                                                                                          | Pass    |
| Theme tiles  | Display  | Display stylish tiles for user to select a theme to view                                                                                                                                                                                                            | Pass    |
| City tile    | Interact | Indicates link on hover, click takes user to city theme.                                                                                                                                                                                                            | Pass    |
| Space tile   | Interact | Indicates link on hover, click takes user to space theme.                                                                                                                                                                                                           | Pass    |
| Castle tile  | Interact | Indicates link on hover, click takes user to castle theme.                                                                                                                                                                                                          | Pass    |
| Train tile   | Interact | Indicates link on hover, click takes user to train theme.                                                                                                                                                                                                           | Pass    |
| Account tile | Interact | Indicates link on hover, click takes uer to account info.                                                                                                                                                                                                           | Pass    |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                          | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

#### Index page (Logged-in User):

The index page differs for logged-in users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

#### Index page (Logged-in Super User):

The index page differs for logged in Super Users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Admin bar       | Display  | Admin bar displays below nav bar. It shows that it is the admin bar and has two links, one to create a new Item and one to create a new Sku                                                                                                                                         | Pass    |
| New Item link   | Interact | Indicates as a link on hover. Opens correct page for Super User to create a new Item object in the database.                                                                                                                                                                        | Pass    |
| New Sku link    | Interact | Indicates as a link on hover. Opens correct pave for Super User to create a new Sku object in the database.                                                                                                                                                                         | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

### Items page

#### Items page (All Users):

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar    | Display  | Indicates currently selected theme or "All" if none  selected. Sort by: link is accessible, opens a drop down menu and will sort appropriately from any theme selection or none.                                          | Pass    |
| Item tiles  | Display  | Items dispaly on tiles in an clean organized manner,  responsively to screen size. Images display when available, placeholder image when not. Displays item  name, item number, and appropriate parts count to each item | Pass    |
| Item tiles  | Interact | Indicate links on hover over image or button. Click takes user to the correct item detail page.                                                                                                                          | Pass    |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                                 | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

#### Item page (Logged-in User)

The item page differs for logged-in users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

#### Item page (Logged-in Super User)

The item page differs for logged in Super Users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Admin bar       | Display  | Admin bar displays below nav bar. It shows that it is the admin bar and has two links, one to create a new Item and one to create a new Sku                                                                                                                                         | Pass    |
| New Item link   | Interact | Indicates as a link on hover. Opens correct page for Super User to create a new Item object in the database.                                                                                                                                                                        | Pass    |
| New Sku link    | Interact | Indicates as a link on hover. Opens correct pave for Super User to create a new Sku object in the database.                                                                                                                                                                         | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

### Item detail page
#### Item detail page (All Users)

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar    | Interact | None                                                                                                                                                                                                                                                                            | Pass |
| Item detail | Display  | Displays large hero image of item, and two additional images when available. If no hero image is available, a placeholder image is displayed and a placeholder html card is displayed for other images. Item name, item  number, item description, and part count are displayed | Pass |
| Item detail | Interact | None                                                                                                                                                                                                                                                                            | Pass |
| Sku display | Display  | Skus are displayed in order: Instructions,  ModernSet, FullSet when available. If Instructions or ModernSet are not availble, a coming soon message is displayed. Nothing is displayed if there is no Fullset available.                                                        | Pass |
| Sku inst    | Display  | A purchase message, item:sku numbers, and a  message about what is included is displayed. A button displays with the price if no sku related to the item is in the cart.                                                                                                        | Pass |
| Sku inst    | Interact | Button with price indicates link on hover, adds appropriate sku to cart.                                                                                                                                                                                                        | Pass |
| Sku mdst    | Display  | A purchase message, item:sku numbers, and a  message about what is included is displayed. A  quantity selector with increment buttons is displayed, and a purchase button with the price.                                                                                       | Pass |
| Sku mdst    | Interact | Increment buttons indicate on hover, increment the quantity when clicked. Purchase button with price adds the item to cart, reflecting the  quantity the user selected.                                                                                                         | Pass |
| Sku flst    | Display  | A limited edition message is displayed, a purchase message is displayed, item:sku numbers are displayed, and a message about what is included are displayed. A quantity selector with increment buttons is displayed, and a purchase button with the price is displayed.        | Pass |
| Sku flst    | Interact | Increment buttons indicate on hover, increment the  quantity when clicked. Purchase button with the price  adds the item to cart, reflecting the quantity the user selected.                                                                                                    | Pass |
| Back button | Display  | Back button displays.                                                                                                                                                                                                                                                           | Pass |
| Back button | Interact | Indicates link on hover, takes customer to items page  when clicked.    | Pass |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                                | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

#### Item detail page (Logged-in User)

The item detal page differs for logged-in users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

#### Item detail page (Logged-in Super User)

| Element          | Action   | Expected Result                                                                                                                                                                                                                                                                                           | Outcome |
|------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar          | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                                                    | Pass    |
| Logout link      | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                                      | Pass    |
| Admin bar        | Display  | Admin bar displays below nav bar. It shows that it is the admin bar and has two links, one to create a new Item and one to create a new Sku                                                                                                                                                               | Pass    |
| New Item link    | Interact | Indicates as a link on hover. Opens correct page for Super User to create a new Item object in the database.                                                                                                                                                                                              | Pass    |
| New Sku link     | Interact | Indicates as a link on hover. Opens correct page for Super User to create a new Sku object in the database.                                                                                                                                                                                               | Pass    |
| Item detail cart | Display  | In addition to the above features, the item detail card displays an Edit and Delete bar at the bottom of the item detail card                                                                                                                                                                             | Pass    |
| Edit bar         | Display  | The edit bar displays a button for the Item. If available, it shows a button for the Instructions, the ModernSet  and the FullSet. If these are not available, the buttons are not displayed at all. This bar is light red for  contrast and to indicate to the Super User that this requires intention.  | Pass    |
| Edit bar         | Interact | Buttons indicate as links on hover. The buttons open the correct pages when clicked, matched to function and item or Sku appropriately.                                                                                                                                                                   | Pass    |
| Delete bar       | Display  | The delete bar displays a button for the Item. If available, it shows a button for the Instructions, the ModernSet, and the FullSet. If these are not available, the buttons are not dipslayed at all. This bar is dark red for  contrast and to indicate to the Super User that this requires intention. | Pass    |
| Delete bar       | Interact | Buttons indicate as link on hover. The buttons open the correct pages when clicked, confirmation pages matched to the item or Sku appropriately.                                                                                                                                                          | Pass    |
| Footer           | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages.                       | Pass    |
| Account section  | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                                                | Pass    |

#### Item detail page (Special features)

| Element                      | Condition                                                                               | Action   | Expected Result                                                                                                | Outcome |
|------------------------------|-----------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------|---------|
| Instructions purchase button | Customer has any sku of associated item in cart.                                        | Display  | Button says "In Cart" and is disabled.                                                                         | Pass    |
| Instructions purchase button | Customer has any sku of associated item in cart.                                        | Interact | None                                                                                                           | Pass    |
| Instructions purchase button | Customer is logged in and has purchased any sku of  the associated item before.         | Display  | Button says "Download."                                                                                        | Pass    |
| Instructions purchase button | Customer is logged in and has purchased any sku of  the associated item before.         | Interact | Button indicates link on hover, and when clicked initiates download of instructions .pdf.                      | Pass    |
| Special                      | Customer has instructions in cart, and adds any sku  of the assicated item to the cart. | Interact | Instructions purchase button remains as "In cart" and the the instructions in the cart are set to  quantity 0. | Pass    |
| Staff Edit bar | If any items are in the cart | Display | The buttons are removed and replaced with text reminding staff member to remove items from cart before editing items. | Pass |
| Staff Delete bar | If any items are in the cart | Display | The buttons are removed and replaced with text reminding staff member to remove items from cart before deleting items. | Pass |

### Cart Page 

#### Cart Page (Unlogged-in User)

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar       | Display  | Shows user is navigated to Shopping Cart                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Pass |
| Info bar       | Interact | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Pass |
| Shopping cart   | Display  | Displays a list of items in cart. Each item shows and image, item:sku number, price and quantity  currently selected. A quantity selector displays with an update and remove button and the extended price displays properly showing the right price for  the quantity of items selected. Below the items, the  total number of physical items to ship (by quantity)  is displayed. Shipping cost and grand total are  displayed. A shop button to return to shopping and a checkout button to proceed with the order are displayed. | Pass |
| Shopping cart   | Interact | See cart items                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Pass |
| Cart item       | Display  | Individual instances of the cart, with the item  picture, name, item:sku number, price, quantity and  buttons with a horizontal rule between each item.                                                                                                                                                                                                                                                                                                                                                                              | Pass |
| Cart item       | Interact | Quantity selector increments the quantity. Update  correctly updates the total and the extended price, remove item correctly removes the item from the cart.                                                                                                                                                                                                                                                                                                                                                                         | Pass |
| Shop button     | Interact | Indicates link on hover, on click takes customer to  items page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Pass |
| Checkout button | Interact | Indicates link on hover, on click takes customer to l ogin page since they are not logged in already.                                                                                                                                                                                                                                                                                                                                                                                                                                | Pass |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                                  | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

### Account Signup Page (Unlogged-in User)

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar     | Display  | Indicates user is navigated to the signup page                                                                                                                                                                                                                                                      | Pass |
| Info bar     | Interact | None                                                                                                                                                                                                                                                                                                | Pass |
| Sign up card | Display  | Sign up card displays properly, with a form for the user to sign up for an account. The form includes and input for e-mail (twice),  an input for the user name, and input for the password (twice). The  sign up button displays above a message for customer who are signed up but not logged in. | Pass |
| Sign up card | Interact | Forms take input, and defend against whitespace and bad characters.  Sign up button commits user's information to dashboard and sends an email for account confirmation. Link in log in message takes customer to log in page.                                                                      | Pass |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                                | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

### Newsletter signup page (Unlogged-in user only)

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar        | Display  | Indicates user is navigated to the newsletter signup form                                                                                                                                               | Pass |
| Info bar        | Interact | None                                                                                                                                                                                                    | Pass |
| Newsletter form | Display  | Displays a message about the information to be put in, displays  name input field, email input field, and four unchecked check boxes for the user's interests. There is a signup button for submission. | Pass |
| Nesletter form  | Interact | See Inputs                                                                                                                                                                                              | Pass |
| Name input      | Interact | Indicates that it is a CharField on hover, accepts name, cleans whitespace.                                                                                                                             | Pass |
| Email input     | Interact | Indicates that is is an input on hover, accepts email address, validates  as email.                                                                                                                     | Pass |
| City checkbox   | Interact | Toggles when clicked                                                                                                                                                                                    | Pass |
| Space checkbox  | Interact | Toggles when clicked                                                                                                                                                                                    | Pass |
| Castle checkbox | Interact | Toggles when clicked                                                                                                                                                                                    | Pass |
| Train checkbox  | Interact | Toggles when clicked                                                                                                                                                                                    | Pass |
| Signup button   | Interact | Indicates button when hover, submits for properly, creates new database  object properly.                                                                                                               | Pass |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                                  | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

### About and FAQ page, All users

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar                | Display  | Indicates user is navigated to the About page                    | Pass |
| Info bar                | Interact | None                                                             | Pass |
| About card              | Display  | Displays About, FAQ, and Contact information.                    | Pass |
| About card              | Interact | See elements below                                               | Pass |
| Brick Sticker Shop link | Display  | Indicates link in styling.                                       | Pass |
| Brick Sticker Shop link | Interact | Indicates link on hover. Opens correct link in new tab on click. | Pass |
| Instagram link          | Display  | Displays icon and "Instagram"                                    | Pass |
| Instagram link          | Interact | Indicates link on hover. Opens correct link in new tab on click. | Pass |
| Facebook link           | Display  | Displays icon and "Facebook"                                     | Pass |
| Facebook link           | Interact | Indicates link on hover. Opens correct link in new tab on click. | Pass |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                                 | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

### Terms page, All Users

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar   | Display  | Indicates user is on the Terms of Service page                                                                                                                                                                                                                                                                        | Pass |
| Info bar   | Interact | None                                                                                                                                                                                                                                                                                                                  | Pass |
| Terms card | Display  | Displays the text of Terms of Service including embedded links. At the bottom of the card is a reminder that this is not a real webstore and is for educational purposes only.                                                                                                                                        | Pass |
| Terms card | Interact | Embedded in the text are links to bricks-then-made-now5bd876713bd4.herokuapp.com,  WebsitePolicies.com that open to the correct link in a new tab without transferring  information. There is also a link that opens the users email on their machine with an email addressed to bricksthenmadenow@gmail.com started. | Pass |
| Footer       | Display  | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass    |
| Sign up      | Interact | Button indicates link on hover, click takes user to correct page with sign up form.                                                                                                                                                                                 | Pass    |
| Find BTMN    | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com.                                  | Pass    |
| Support      | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page                                                                                                                                                           | Pass    |

### Privacy Policy page, All Users

| Element     | Action   | Expected Result                                                                                                                                                                                                          | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon                                                                                                                                                                                        | Pass    |
| Title       | Interact | Indicates link on hover, click takes user to index page                                                                                                                                                                  | Pass    |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search                                                                                  | Pass    |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total.                                                                                                       | Pass    |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link                                                                                                                                                                       | Pass    |
| Theme links | Interact | Indicate links on hover, open correct list of items.                                                                                                                                                                     | Pass    |
| Login link  | Interact | Indicates link on hover, opens correct login page.                                                                                                                                                                       | Pass    |
| Info bar            | Display  | Indicates that user is navigated to Privacy Policy page.                                                        | Pass |
| Info bar            | Interact | None.                                                                                                           | Pass |
| Privacy policy card | Display  | Displays the text of the privacy policy. Displays a link to the Privacy Policy Generator used.                  | Pass |
| Privacy policy card | Intarct  | Link indicates link on hover. Link opens new tab without sharing information with the  correct, linked website. | Pass |
| Footer | Display | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass |
| Sign up | Interact | Button indicates link on hover, click takes user to correct page with sign up form. | Pass |
| Find BTMN | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com. | Pass |
| Support | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page | Pass |



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