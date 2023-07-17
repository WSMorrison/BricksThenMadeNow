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

#### Cart page (Logged-in User)

The cart page differs for logged-in users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

#### Cart page (Logged-in Super User)

The Cart page differs for logged in Super Users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Admin bar       | Display  | Admin bar displays below nav bar. It shows that it is the admin bar and has two links, one to create a new Item and one to create a new Sku                                                                                                                                         | Pass    |
| New Item link   | Interact | Indicates as a link on hover. Opens correct page for Super User to create a new Item object in the database.                                                                                                                                                                        | Pass    |
| New Sku link    | Interact | Indicates as a link on hover. Opens correct pave for Super User to create a new Sku object in the database.                                                                                                                                                                         | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

### Checkout page

#### Checkout page (Unlogged-in User)

| Element                      | Condition                                                                               | Action   | Expected Result                                                                                                | Outcome |
|------------------------------|-----------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------|---------|
| Checkout page                | Customer is not logged in.                                                              | Display  | None                                                                                                           | Pass    |

The checkout page is inaccessible to unlogged-in users. In order to download instructions, the user will need to be logged in. So they must have an account, and be logged in, at the time of purchase so that the instructions are added to their account and can be downloaded in the future. When an unlogged-in user clicks the checkout button, they are redirected to the Log In page, where they can log in or follow the link to the Sign Up and create a new account.

#### Checkout page (Logged in User)

| Element | Action | Expected Result | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon | Pass |
| Title       | Interact | Indicates link on hover, click takes user to index page | Pass |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search | Pass |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total. | Pass |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link | Pass |
| Theme links | Interact | Indicate links on hover, open correct list of items. | Pass |
| Login link  | Interact | Indicates link on hover, opens correct login page. | Pass |
| Info bar                 | Display  | Indicate that the user is navigated to the checkout page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Pass    |
| Info bar                 | Interact | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Pass    |
| Cart card                | Display  | Display an abridged cart to the left of the forms on large screens, above on small screens. Each item in cart  is listed by name and type, with quantity and extended price for each. At the bottom of the car is the total  physical items to ship, the shipping cost, and the grand total.                                                                                                                                                                                                                                                                                                                            | Pass    |
| Cart card                | Interact | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Pass    |
| Shipping form            | Display  | The shipping form displays a title bar of its own. It also displays a "Contact" title above a Name for field,  an email form field, and phone number form field. Under that is the "Shipping address" title, which is followed  by two street address fields, a city field, a state field, a zipcode field, and country field. After that is the payment title, which is above a field for the customer's payment information. Below that is a checkbox to save the delivery information to the user's profile. Finally, below that, is a button to retun the user to more  shopping and a button to process the order. | Pass    |
| Shipping form            | Interact | See individual form fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Pass    |
| Name field               | Interact | Displays placeholder "Full name" and indicates it is required. Indicates CharField on hover. Accepts input. Will  not validate if blank. If it is filled with spaces instead of characters, it will fail the form submission.                                                                                                                                                                                                                                                                                                                                                                                           | Pass    |
| Email field              | Interact | Displays placeholder "Email Address" and indicates that it is required. Indicates EmailField on hover. Accepts input. Will not validate if blank. Will not validate if an invalid email address, typical to Django EmailFields.                                                                                                                                                                                                                                                                                                                                                                                         | Pass    |
| Phone number field       | Interact | Displays placeholder "Phone number." May be blank. All whitespace will fail the form submission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Pass    |
| Shipping address 1 field | Interact | Displays placeholder "Shipping address 1" and indicates it is required. Indicates CharField on hover. Accepts  input. Will not validate if blank. All whitespace will fail the form submission.                                                                                                                                                                                                                                                                                                                                                                                                                         | Pass    |
| Shipping address 2 field | Interact | Displays placeholder "Shipping address 2." Indicates CharField on hover. Accepts  input. May be blank. All whitespace will fail the form submission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Pass    |
| Town or city field       | Interact | Displays placeholder "Town or City" and indicates it is required. Indicates CharField on hover. Accepts input.  Will not validate if blank. All whitespace will fail the form submission.                                                                                                                                                                                                                                                                                                                                                                                                                               | Pass    |
| State field              | Interact | Display placeholder "State" and indicates it is required. Indicates CharField on hover. Accepts input. Will not  validate if blank. All whitespace will fail the form submission.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Pass    |
| Zipcode field            | Interact | Displays placeholder "ZIP" and indicates it is required. Indicates CharField on hover. Accepts input. Will not  validate if blank. All whitespace will fail the form submission.                                                                                                                                                                                                                                                                                                                                                                                                                                        | Pass    |
| Country dropdown         | Interact | Required field will not validate unless set. Customer must choose their country.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Pass    |
| Payment field            | Interact | Placeholder is an image of a card and "Card number." Will not validate if blank. Stripe integration of card  validation, including expiry date, postcode and CVC. Will either not validate or will fail the form submission  if it is not a valid number.                                                                                                                                                                                                                                                                                                                                                               | Pass    |
| Shop button              | Interact | Indicates button as link with hover. Will return user to Items page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Pass    |
| Process button           | Interact | Indicates submit button with hover. Will submit form for Stripe integrated processing if form is valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Pass    |
| Footer | Display | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass |
| Sign up | Interact | Button indicates link on hover, click takes user to correct page with sign up form. | Pass |
| Find BTMN | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com. | Pass |
| Support | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page | Pass |

### Checkout success page

#### Checkout success page (Unlogged-in User)

| Element                      | Condition                                                                               | Action   | Expected Result                                                                                                | Outcome |
|------------------------------|-----------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------|---------|
| Checkout success page                | Customer is not logged in.                                                              | Display  | None                                                                                                           | Pass    |

The checkout page is inaccessible to unlogged-in users. They presumably could ender the url into their browser and get a meaningless confirmation, but a meaningful checkout success page can only be reached by a successful order processing through the Logged-in accessible only Checkout page.

#### Checkout success page (Logged-in users)

| Element | Action | Expected Result | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon | Pass |
| Title       | Interact | Indicates link on hover, click takes user to index page | Pass |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search | Pass |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total. | Pass |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link | Pass |
| Theme links | Interact | Indicate links on hover, open correct list of items. | Pass |
| Login link  | Interact | Indicates link on hover, opens correct login page. | Pass |
| Info bar              | Display  | Indicates user is currently navigated to the Checkout Success page | Pass |
| Info bar              | Interact | None                                                               | Pass |
| Checkout success card | Display  | Text indicates customer had a successfull transaction.             | Pass |
| Checkout success card | Interact | None                                                               | Pass |
| Footer | Display | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass |
| Sign up | Interact | Button indicates link on hover, click takes user to correct page with sign up form. | Pass |
| Find BTMN | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com. | Pass |
| Support | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page | Pass |

#### Checkout success page (Logged-in Super User)

The Cart page differs for logged in Super Users in the following ways:

| Element         | Action   | Expected Result                                                                                                                                                                                                                                                                     | Outcome |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Nav bar         | Display  | Bar displays, showing selectable themes, log out link.                                                                                                                                                                                                                              | Pass    |
| Logout link     | Interact | Indicates link on hover, opens correct log out page.                                                                                                                                                                                                                                | Pass    |
| Admin bar       | Display  | Admin bar displays below nav bar. It shows that it is the admin bar and has two links, one to create a new Item and one to create a new Sku                                                                                                                                         | Pass    |
| New Item link   | Interact | Indicates as a link on hover. Opens correct page for Super User to create a new Item object in the database.                                                                                                                                                                        | Pass    |
| New Sku link    | Interact | Indicates as a link on hover. Opens correct pave for Super User to create a new Sku object in the database.                                                                                                                                                                         | Pass    |
| Footer          | Display  | Displays a user account section, find section, and support section. User account section includes links to user information and order history pages. Find section has icons and links to social media and an in information page. Support section shows links to information pages. | Pass    |
| Account section | Interact | Buttons indicate link on hover. When clicked, links open the correct pages on the website.                                                                                                                                                                                          | Pass    |

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

### Admin pages

#### Admin pages (Not logged-in or not Super Users)

| Element        | Action  | Expected Result | Outcome |
|----------------|---------|-----------------|---------|
| Add item page  | Display | None            | Pass    |
| Add sku page   | Display | None            | Pass    |
| Edit item page | Display | None            | Pass    |
| Edit sku page  | Display | None            | Pass    |

The admin pages are only accessible by logged in Super Users. These have been tested to not work for other users, both by the links not being provided and by protecting the urls.

#### Create Item page (Logged in Super User)

| Element | Action | Expected Result | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon | Pass |
| Title       | Interact | Indicates link on hover, click takes user to index page | Pass |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search | Pass |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total. | Pass |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link | Pass |
| Theme links | Interact | Indicate links on hover, open correct list of items. | Pass |
| Login link  | Interact | Indicates link on hover, opens correct login page. | Pass |
| Info bar               | Display  | Indicates that Super User is navigated to the create Item page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Pass    |
| Info bar               | Interact | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Pass    |
| New Item form          | Display  | The form displays with a field for the Item number, with text explaining the convention. The next field  is the Item name field, with text describing the field. A dropdown field is next, allowing the Super User  to select the correct theme for the item from the existing themes. There is a text field for the description. The following three Fields are ImageFields and while the first of the four is described as required it is intentionally NOT required, it's more of a... strong suggestion. The following three ImageFields are separated in a light gray box. The UrlField for the instructions .pdf follows. Finally is the parts count CharField. At the bottom is a cancel button that takes the customer to the Items pages, or a button to add the Item to the  database.  | Pass    |
| New Item form          | Interact | See form fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Pass    |
| Item number field      | Interact | Item number field is limited to 5 characters, and are RegEx validated. Otherwise, the Super User is allowed to  use their best judgement. It may not be blank and all whitespace will fail the form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Pass    |
| Item name field        | Interact | The item name field is whitespace protected and may not be blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Pass    |
| Theme dropdown         | Interact | The Super User can only select one of the already created themes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Pass    |
| Item description       | Interact | The item description box is whitespace protected and may not be blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Pass    |
| Image fields           | Interact | All four image fields may be left unfilled. They feature django built in image validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Pass    |
| Instructions URL field | Interact | The instructions URL field features Django URL validation, and is required so it cannot be left blank. It also  benefits from a customer validator that checks that the URL starts with https://cloudinary/ and ends with .pdf.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Pass    |
| Parts count field      | Interact | The parts count field may not left blank, and must be given a number, not characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Pass    |
| Cancel button          | Interact | Indicates link on hover. Takes Super User to items page when clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Pass    |
| Add Item button        | Interact | Indicates link on hover. Adds Item to the database when clicked, if forms are valid and item number is unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Pass    |
| Footer | Display | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass |
| Sign up | Interact | Button indicates link on hover, click takes user to correct page with sign up form. | Pass |
| Find BTMN | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com. | Pass |
| Support | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page | Pass |

#### Edit Item page

The look and function of the Edit Item page is identical to the Add Item page, except all the fields come prefilled with the values of the Item the user selected to edit.

| Element        | Action   | Expected Result                                                                        | Outcome |
|----------------|----------|----------------------------------------------------------------------------------------|---------|
| Edit Item page | Display  | Identical to Add Item page except prepopulated with values from correct existing Item. | Pass    |
| Edit Item page | Interact | Identical to Add Item page except prepopulated with values from correct exitinng Item. | Pass    |

#### Create Sku page

| Element | Action | Expected Result | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon | Pass |
| Title       | Interact | Indicates link on hover, click takes user to index page | Pass |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search | Pass |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total. | Pass |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link | Pass |
| Theme links | Interact | Indicate links on hover, open correct list of items. | Pass |
| Login link  | Interact | Indicates link on hover, opens correct login page. | Pass |
| Info bar       | Display  | Indicates to Super User that they are navigated to the Add Sku page.                                                                                                                                                                                                                                                                                                                                                                       | Pass    |
| Info bar       | Interact | None                                                                                                                                                                                                                                                                                                                                                                                                                                       | Pass    |
| Add Sku card   | Display  | The card displays the add Sku form. The first field is a dropdown field  for the Super User to select the Item that the Sku will be related to.  The next field is a CharField for the Sku number. The Sku type dropdown is next,  followed by the DecimalField for the price. There is a checkbox for an item being  physical or not, and an IntegerField for the item's inventory. Then there is a  cancel button and an Add Sku button. | Pass    |
| Add Sku card   | Interact | See form fields.                                                                                                                                                                                                                                                                                                                                                                                                                           | Pass    |
| Related field  | Interact | The Dropdown menu prevents the user from selecting anything than an existing Item.  Additional validation on the Sku type will prevent duplication by misselecting the  item in this box.                                                                                                                                                                                                                                                  | Pass    |
| Sku number     | Interact | The Sku number is CharField that is limited for whitespace and limited to five characters, though convention will proscribe four. Otherwise, this field is left  the Super User's discretion.                                                                                                                                                                                                                                              | Pass    |
| Sku type       | Interact | This dropdown box gives the customer three options: Instructuons, ModernSet, or  FullSet. To make sure a duplicate Sku type isn't being submitted for an Item, which  would harm the database, the Sku type is checked against the existing Skus for the  item selected earlier. If the Sku type already exists, the Super User will be returned  to the form to fix their mistake.                                                        | Pass    |
| Physical item  | Interact | This checkbox works.                                                                                                                                                                                                                                                                                                                                                                                                                       | Pass    |
| Inventory      | Interact | Inventory must be an integer, but it can be a rather high inventory.                                                                                                                                                                                                                                                                                                                                                                       | Pass    |
| Cancel button  | Interact | Indicates a link on hover, when clicked it returns the Super User to the items page  without creating a new Sku object.                                                                                                                                                                                                                                                                                                                    | Pass    |
| Add Sku button | Interact | Indicates a link on hover, when clicked it checks the form and if valid, it creates a  new Sku object in the database.                                                                                                                                                                                                                                                                                                                     | Pass    |
| Footer | Display | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass |
| Sign up | Interact | Button indicates link on hover, click takes user to correct page with sign up form. | Pass |
| Find BTMN | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com. | Pass |
| Support | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page | Pass |

#### Edit Sku page

The Edit Sku page is very similar to the Add Sku page, with some key differences.

| Element          | Action   | Expected Result                                                                                                                                                                                                                                                                                                                                                                     | Outcome |
|------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Sku Item field   | Display  | Displays the Sku item and that this field cannot be edited.                                                                                                                                                                                                                                                                                                                         | Pass    |
| Sku Item field   | Interact | None                                                                                                                                                                                                                                                                                                                                                                                | Pass    |
| Sku Type field   | Display  | Displays the Sku type and that this field cannot be edited.                                                                                                                                                                                                                                                                                                                         | Pass    |
| Sku Type field   | Interact | None                                                                                                                                                                                                                                                                                                                                                                                | Pass    |
| Other Sku fields | Display  | Prefilled with the correct values based on the Sku selected for editing.                                                                                                                                                                                                                                                                                                            | Pass    |
| Other Sku fields | Interact | Otherwise identical to Add Sku                                                                                                                                                                                                                                                                                                                                                      | Pass    |

The uneditable fields are to help prevent errors in copy and errors in the database. If the fields need to be edited, the sku can easily be deleted and a new Sku made.

#### Delete Item confirmation page.

| Element | Action | Expected Result | Outcome |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon | Pass |
| Title       | Interact | Indicates link on hover, click takes user to index page | Pass |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search | Pass |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total. | Pass |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link | Pass |
| Theme links | Interact | Indicate links on hover, open correct list of items. | Pass |
| Login link  | Interact | Indicates link on hover, opens correct login page. | Pass |
| Info bar     | Display  | Indicates that Super User is on the Delete Item confirmation page.                                                                                                                         | Pass    |
| Info bar     | Interact | None                                                                                                                                                                                       | Pass    |
| Confirm card | Display  | Gives the user a message to remind them that the item cannot be undeleted, and that the related Skus will also be deleted. It also has a Yes and No button that the Super User can select. | Pass    |
| Confirm card | Interact | See the Confirm buttons.                                                                                                                                                                   | Pass    |
| Yes button   | Interact | Indicates link on hover. Removes Item from the database, and all related Skus.                                                                                                             | Pass    |
| No buttons   | Interact | Indicates link on hover. Returns Super User safely to the Items page.                                                                                                                      | Pass    |
| Footer | Display | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass |
| Sign up | Interact | Button indicates link on hover, click takes user to correct page with sign up form. | Pass |
| Find BTMN | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com. | Pass |
| Support | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page | Pass |

#### Delete Sku confirmation page.

| Element | Action | Expected Result | Outcome |
|-------------|----------|---------------------------------------------------------|---------|
| Title Bar   | Display  | Show title, search bar, cart icon | Pass |
| Title       | Interact | Indicates link on hover, click takes user to index page | Pass |
| Search bar  | Interact | Indicates input on hover, accepts input, search icon  indicates link on hover, click searches properly,  outcome appropriate for search | Pass |
| Cart icon   | Interact | Indicates link on hover, reacts to items in cart with a slightly different icon, dollar amount show running total. | Pass |
| Nav bar     | Display  | Bar dispalys, shows selectable themes, log in link | Pass |
| Theme links | Interact | Indicate links on hover, open correct list of items. | Pass |
| Login link  | Interact | Indicates link on hover, opens correct login page. | Pass |
| Info bar     | Display  | Indicates that Super User is on the Delete Sku confirmation page.                                                                            | Pass    |
| Info bar     | Interact | None                                                                                                                                         | Pass    |
| Confirm card | Display  | Gives the user a message to remind them that the Sku cannot be undeleted. There are also a Yes and No button that the Super User can select. | Pass    |
| Confirm card | Interact | See the Confirm buttons.                                                                                                                     | Pass    |
| Yes button   | Interact | Indicates link on hover. Removes Sku from the database.                                                                                      | Pass    |
| No buttons   | Interact | Indicates link on hover. Returns Super User safely to the Items page.                                                                        | Pass    |
| Footer | Display | Displays a sign up section, find section, and support section. Sign up section has information and a button to a newsletter signup form. Find section has icons as links to social media and an information page. Support section shows links to information pages. | Pass |
| Sign up | Interact | Button indicates link on hover, click takes user to correct page with sign up form. | Pass |
| Find BTMN | Interact | Icons indicate link on hover; clicking on Instagram icon takes user to correct Instagram page, Facebook icon takes customer to Facebook page, and envelope icon opens email app on customer machine with an email started to bricksthenmadenow@gmail.com. | Pass |
| Support | Interact | FAQ, Terms of Service, and Privacy links indicate link on hover and take user to correct information page | Pass |

<br>
<hr>



### Representative User Manual Testing

<hr>

In addition to formal manual testing, the site was shown to friends who would be representative as users for this website. Most of these testers are active in the Lego community, or at least Lego community adjacent. Regardless, even non-Lego testers understand how to use the internet and e-commerce and were therefore able to give relevant and valuable feedback. The following testing was completed by representative testers.

- Representative User testers were able to visit the site, view the Items, view the Skus and get information about all the items for sale.
- Testers were able to sign up for accounts, and confirm their email address.
- Testers were able to add items to their cart, in various quantities.
- Testers were happy to see that they could not accidentally pay for instructions included with other items.
- Testers were able to complete the checkout successfully.
- Testers were able to sign up for newsletters and received emails confirming.

Feedback from tester lead to improvements.
- The item images on the item pages were changed to be a link to the item detail page, instead of just the button.
- The text was clarified on the Item and Sku descriptions to make it more clear what was included in each purchase. 

Some suggestions have not yet been implemented.
- Some testers would like for there to be larger pictures. There is opportunity for larger pictures in the Item models, but larger pictures do not exist. 
- Some testers would really like the products. The products don't exist is saleable quantities.

<br>
<hr>

### Bugs

<hr>

Several bugs were found during development, and most were fixed.

#### Fixed Bugs

The following bugs were fixed during development:

- When using the Sku creation form in new-sku.html, the newly created Skus were sending infomration and were not being added to the item-detail.html when viewing item details. Troubleshooting found that using get_object_or_404 would for some reason work with the admin panel created Skus, but weren't the correct choice for use on a queryset. Since the view was already try/excepting finding the Skus, object.get is perfectly functional. The correct Sku details are being correctly displayed on the correct Item object detail page.
- Bad checkout data was crashing the site when an order process was attempted. Troubleshooting found that a postcode was being passed that the Stripe integration was not looking form, causing a data mismatch with an error 500. Removed the postcode from that particular field, so it would not be passed to Stripe.
- The zipcode was not getting passed correctly through the form in checkout/stripe_element.js. The problem was simillar as above, Stripe wasn't looking for that information in that process, whichw as causing an error 500. The zipcode was changed to only be be passed when asked.
- Customers can increment the quantity of instructions in the cart, which can lead them to pay for more than one set of instructions. The buttons are rendered but made display-none, so that there isn't a problem with form submission but the customer cannot change the value.
- Email button in the footer does nothing. Code was changed so that it opens an email application on the customer computer, and starts a preaddressed email.
- Carousel links did not work in Heroku but did work in Gitpod. Troubleshooting found that the links were working, but the Gitpod usage was logged in, and that allowed the links to actually do something meaningful. If the user was logged in, they were just redirected to the index page, making it seem like nothing was happening. The links were changed to thake a logged-in customer to their customer information, and an unlogged-in customer to a sign-up page.
- Sorting is not sorting items in a particular theme, but returning a list of all items sorted. Troubleshooting found that the current theme was not being passed to the view that made the sort happen. Afterward, it was discovered that if no theme was selected, an error 404 occured. So the whole sort code was wrapped in an if statement checking if a theme was currently selected before passing it.
- Newly added Skus were not appearing on the Item detail page when created in the front end. Troubleshooting found that the view was asking get_object_or_404 when it should have been using a try statement. The code was corrected and the Skus are being properly displayed.
- Ordering caused duplicate orders to be sent to the database, with different totals, while Stripe was processing information correctly. Troubleshooting found that calculating the shipping in the context was giving a value where trying to calculate it in the view or model wasn't working, causing a data mismatch. The error didn't throw an error 505 but instead just had Stripe keep tryint to push the order through until a second one was pushed through on the top of the incomplete one made previously. The shipping was reorganized and the order work properly now.
- New Sku and New Item were not working, but instead throwing an error 500. Troubleshooting found that the URLs were trying to send "new_item" to "item_detail," so "item_detail" was getting arguments it didn't like, and throwing a fit. Urls were reorganized and cleaned up. Item and Sku creation working as intended.
- New item, new sku, edit item, edit sku not working. Troubleshooting that semantic revisions removed an important > from a form tag. Fixed the code. Database control working as intended.
- Checkout fail page not rendering. Troubleshooting found that the template should be "checkout/checkout_fail.html" not "checkout_fail.html." The unhappy path is working.
- Edit Sku form is not working. Troubleshooting found that having just removed the fields that shouldn't be edited caused the form to attempt a submit while invalid. The solution was to add the form fields back into the page but with d-none so they could not be edited. Everything working as intended.
- After writing code that set the instructions quantity to zero if any sku associated to the same item was added to the cart, the cart would just add quantity 0 instructions any time instructions were added. Troubleshooting found that it was just an order of operations issue - buy doing the check before the add, the instructions would be added with quantity 1 and left alone unless they should be set to 0 by another Sku.
- Super Users adding Skus could inadvertantly add duplicate Skus. Code was added to prevent duplicates by checking for the Sku that was being added before saving the new one.

#### Unfixed Bugs:

The following bugs have not yet been fixed:

- Toasts seem to be working intermittently, and all Javascript components seem to be quite small. Troubleshooting has yet to crack this stubborn issue.
- Using the Heroku deployed site, emails are working for new account signup, and new newsletter signups and being actually sent by Gmail SMTP. However, when an order is placed, the email is not sent. When in the Gitpod IDE, the email is logged to the console as is the way, but the problem has not been resolved in Heroku.

<hr>
For educational purposes only.