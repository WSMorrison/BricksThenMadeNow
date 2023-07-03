# Bricks Then Made Now

Bricks Then Made Now is an ecommerce site that sells fan made Lego designs to other Lego fans. The site will appeal to adult followers of Lego (AFOL), by reimagining vintage Lego from the 1970s, '80s, and '90s with modern elements and contemporary design techniques.

![Front page of Bricks Then Made Now as input to AmIResponsive.](#)

[AmIResponsive](https://ui.dev/amiresponsive)

### The side, deployed to Heroku, can be found here: [Bricks Then Made Now](#)
#### The repository in GitHub can be found here: [WSMorrison/bricksthenmadenow](#)

<br>
<hr>
<br>
<br>

## Contents

<hr>

- [User Experience](#user-experience)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [Planning](#planning)
  - [Models](#models)
  - [Wireframes](#wireframes)
    -[Large Screen Wireframes](#large-screen-wireframes)
    -[Mobile Wireframes](#mobile-wireframes)
  - [Flowchart](#flowchart)
  - [User Stories and Agile Technologies](#user-stories-and-agile-technologies)
- [Features](#features)
  - [General Features on All Pages](#general-features-on-all-pages)
  - [Features of Individual Pages](#features-of-individual-pages)
  - [Defensive Design](#defensive-design)
  - [Future Implementations](#future-implementations)
  - [Accessibility](#accessibility)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Local Development and Deployment](#local-development-and-deployment)
  - [Note On Commit History](#note-on-commit-history)
  - [Local Development](#local-development)
  - [Deployment](#deployment)
  - [How to Fork or Clone](#how-to-fork-or-clone)
- [Testing](#testing)
  - [Code Validation](#code-validation)
  - [Systematic Manual Testing](#systematic-manual-testing)
  - [Representative User Manual Testing](#representative-user-manual-testing)
- [Credits](#credits)
  - [Code Used](#code-used)
  - [Media](#media)

<br>
<hr>
<br>
<br>

## User Experience

<hr>

Portfolio Project 5 example

### User Stories

User Stories example

<br>
<hr>
<br>
<br>

## Design
<hr>
<br>

### Colour Scheme

Color scheme example

The Color scheme was developed with help from [Color Shades Online Generator](https://gradients.app/en/shades)

![Example Bootswatch Spacelab colorscheme](/assets/readme-images/BootswatchSpacelab.png)

[Bootswatch Spacelab](https://bootswatch.com/spacelab/)

### Typography

Typography example

![Bebas Neue font from Google Fonts](/assets/readme-images/BebasNeue.png)

[Bebas Neue, Google Fonts](https://fonts.google.com/specimen/Bebas+Neue)

### Imagery

Imagery example, for example:

The splash image is by [Trevor Yale Ryan](https://www.tyrphoto.com/), and was originally published on the [Speedhunters](http://www.speedhunters.com/2020/01/slippers-and-sunsets-the-osixhi-meet/). It will serve as a placeholder until an appropriate new image can be taken at a local event.

<br>
<hr>
<br>
<br>

## Planning
<hr>
<br>

A project of even such a small scope as this requires careful planning before any development can begin.

<hr>
<br>

### Models
<hr>
<br>

Custom models had to be developed to hold the appropriate information the website's database. Care had to be taken to plan the way the models would interact, since there are two instances of having one model extended by another. This was necessary to have a few different purchasable SKUs related to a single item, and to have a unique siteuser model that uses the Django authorization functionality as its base.

**Item model**

This model contains information about the items listed for sale on the site. The item model will only include information that is common to all three SKUs related to a particular item, including the item number, item name, related themes, the description, images, and the partcount. It will be extended with the SKU model which will hold information about each individual SKU that are part of the item.

| Key                        | Field        | Form                 |
|----------------------------|--------------|----------------------|
| item_number                | Integerfield | Integer              |
| item_name                  | Charfield    | Text                 |
| item_theme                 | Foreignkey   | Many to many         |
| item_desc                  | Textfield    | Text                 |
| item_image_vintage         | Imagefield   | Image                |
| item_image_vintage_url     | URLfield     | URL                  |
| item_image_render          | Imagefield   | Image                |
| item_image_render_url      | URLfield     | URL                  |
| item_image_modern          | Imagefield   | Image                |
| item_image_modern_url      | URLfield     | URL                  |
| item_image_detail          | Imagefield   | Image                |
| item_image_detail_url      | URLfield     | URL                  |
| item_partcount             | Integerfield | Integer              |

**SKU model**

The SKU model containst he rest of the information about what the customer can buy. It extends the item model, which describes the Bricks Then Made Now set, and adds the price, an inventory field, and fields that indicate whether its a SKU for a physical, shippable item or a SKU for a digital instructions download that will not need to be shipped and have shipping fees included. The SKU model will also include an included instructions field that will contain the SKU for the digital instructions that will be included with a digital purchase, so that they will be unlocked for the customer with all purchases.

| Key                        | Field        | Form                  |
|----------------------------|--------------|-----------------------|
| sku_item_no                | Foreignkey   | One to many with item |
| Sku_sku                    | Integerfield | Integer               |
| sku_price                  | Decimalfield | Decimal to two places |
| sku_physical               | Boolean      | Checkbox              |
| sku_inventory              | Integerfield | Integer               |
| sku_included_instructions  | Foreignkey   | Many to one with sku  |

**Order model**

The order model contains all the information about the order, including a python generated order number, an order date set to the date the order was created, and links the order to a site user. It will also hold the payment information from Stripe.

| Key              | Field        | Form                             |
|------------------|--------------|----------------------------------|
| order_number     | Charfield    | Generated                        |
| order_date       | Datefield    | Generated, current date          |
| order_siteuser   | Foreignkey   | One to many                      |
| order_name       | Charfield    | Text                             |
| order_address_1  | Charfield    | Text                             |
| order_address_2  | Charfield    | Text                             |
| order_city       | Charfield    | Text                             |
| order_county     | Charfield    | Text                             |
| order_state      | Charfield    | Text                             |
| order_postcode   | Charfield    | Text                             |
| order_country    | Charfield    | Text                             |
| order_total      | Decimalfield | Generated, decimal to two places |
| order_shipping   | Decimalfield | Generated, decimal to two places |
| order_grandtotal | Decimalfield | Generated, decimal to two places |
| order_bag        | Textfield    | Text                             |
| order_stripe_pid | Charfield    | Taken from Stripe                |

**Line item model**

This small model is used to control the information about individual items in an order.

| Key              | Field        | Form                             |
|------------------|--------------|----------------------------------|
| li_order_number  | Foreignkey   | Order number                     |
| li_product       | Foreignkey   | Item Sku                         |
| li_quantity      | Integerfield | Integer                          |
| li_total         | Decimalfield | Decimal to two places            |

**SiteUser model**

The SiteUser model extends the Django AllAuth user model, holding information that can auto populate the shipping and billing forms during checkout, as well as give the user the correct permissions as a site user or site administrator and hold information about what items a user owns so they can access their digital downloads.

| Key               | Field        | Form                                    |
|-------------------|--------------|-----------------------------------------|
| user              | Foreignkey   | One to one                              |
| user_name         | Charfield    | Text                                    |
| user_email        | Emailfield   | Email                                   |
| user_phone        | Charfield    | Text                                    |
| user_address_1    | Charfield    | Text                                    |
| user_address_2    | Charfield    | Text                                    |
| user_city         | Charfield    | Text                                    |
| user_county       | Charfield    | Text                                    |
| user_state        | Charfield    | Text                                    |
| user_postcode     | Charfield    | Text                                    |
| user_country      | Charfield    | Text                                    |
| user_permissions  | Integerfield | Integer                                 |
| user_orders       | List         | List or order numbers                   |
| user_instructions | List         | List of user owned digital instructions |

<br>
<hr>
<br>

### Wireframes
<hr>
<br>

Wireframes were made to describe how the site would look on both large and mobile screens.

#### Large Screen Wireframes
<br>

![Index page on large screens.](/assets/readme-images/large-1-index.jpg)

This wireframe of the index page shows the planned organization of the page. The site title, search bar and cart ling will remain at the very top of the screen, with a nav bar just below it. Below that is the splash image, with a planned carousel for specials or site news. The center of the page is dominated with a paginated list of all items, that the user can sort by price, or using the nav bar, can filter by theme. The bottom of the page has a footer that is visually distinct like the header. It will hold a form for users to sign up for the mailing list, feature related social media, and links to supporting documents like an FAQ and the T&Cs that suppor the site. Many of the header and footer aspects will carry through the rest of the site, but the splash image and carousel will be only visible on the index page.

Other large screen wireframes can be seen below:

<details>
<summary>Expand to view large screen wireframes.</summary>
<br>

<details>
<summary>Large screen product detail page.</summary>
<br>

![Product detail page, large screen](/assets/readme-images/large-2-detail.jpg)

The detail page will feature a large image displayed, with smaller images that can be selected below. The item description and other details will be featured to the right of the image, with space for buttons for the three different packages available related to each item.

</details>

<details>
<summary>Large screen shopping cart page.</summary>
<br>

![Shopping cart page, large screen](/assets/readme-images/large-3-cart.jpg)

The shopping cart page will list the items the customer has added, with a small image. It will also show selected details, including the price. There will be a quantity selector for physical items, and an extended price. Note, the quantity is set to one and is not selectable for the instructions only digital download. The page will also show the subtotal, shipping cost, and grand total. These will be lined up with the extended totals for consistency, and the checkout button will be directly below to encourage the customer to buy with a clear call to action.

</details>

<details>
<summary>Large screen create item page.</summary>
<br>

![Create item page, large screen](/assets/readme-images/large-4-create-item.jpg)

The form to add an item will have it's own page, with a simple form for staff to fill with each field in the item model.

</details>

<details>
<summary>Large screen create SKU page.</summary>
<br>

![Create SKU page, large screen](/assets/readme-images/large-5-create-sku.jpg)

The form to add an item's indivdual SKUs will have another page, which will allow the user to add an individual SKU suffix to the item number. The related item number will be chosen from a dropdown menue, as will the SKU suffix. The staff will be able to add information specific to each SKU including price, whether the SKU represents a phyical item, how many are inventory for sale, and what digital instructions would be included with the physical items.

</details>

<details>
<summary>Large checkout success page.</summary>
<br>

![Checkout success page, large screen](/assets/readme-images/large-6-success.jpg)

The success page is a simple page indicating that the purchase was successful, with a button to return the user to the index page.

</details>

<details>
<summary>Large screen information item pages</summary>
<br>

![Information pages, large screen](/assets/readme-images/large-7-infopages.jpg)

The pages for the FAQ, shipping information, Terms and Conditions, Terms of Service (if applicable) will all be very similar; just extending the base, index template.

</details>

<details>
<summary>Large screen error 404 item page</summary>
<br>

![Error 404 page, large screen](/assets/readme-images/large-8-404.jpg)

The site will also have a custom 404 page, which is also quite simple and will feature a button to return the user to the index page.

</details>

</details>
<hr>
<br>
<br>

#### Mobile Wireframes
<br>

![Index page on mobile screens.](/assets/readme-images/mobile-1-index.jpg)

The mobile index page will be similar in structure to the large screen page, except the paginated list of items will be stacked instead of stacks of rows. It will contain the same information, as well as the the sort and filter functionalities as the large screen page.

Other large screen wireframes can be seen below:

<details>
<summary>Expand to view mobile wireframes.</summary>
<br>

<details>
<summary>Mobile product detail page.</summary>
<br>

![Product detail page, mobile](/assets/readme-images/mobile-2-detail.jpg)

Continuing with the similar structure and equal functionality, the detail page will be slightly differently organzied, with the three small images below both the larger image and the description. The purchase options will be below the entirety of the description and images, to allow as much room as possible for the add to cart buttons to make it easy for customers to add items to the cart. Note that again, the splash image and news carousel will be omitted, but the navbar and shopping cart will remain at the top of the page.

</details>

<details>
<summary>Mobile shopping cart page.</summary>
<br>

![Shopping cart page, mobile](/assets/readme-images/mobile-3-cart.jpg)

The shopping cart page will maintain the structure of keeping the totals to the right, in line, and lined up with the checkout button.

</details>

<details>
<summary>Mobile create item page.</summary>
<br>

![Create item page, mobile](/assets/readme-images/mobile-4-create-item.jpg)

Though it's unlikely the site staff will be adding items from a mobile device, there will be a mobile friendly version of the form.

</details>

<details>
<summary>Mobile create SKU page.</summary>
<br>

![Create SKU page, mobile](/assets/readme-images/mobile-5-create-sku.jpg)

Though it's unlikely the site staff will be adding items from a mobile device, there will be a mobile friendly version of the form.

</details>

<details>
<summary>Mobile checkout success page.</summary>
<br>

![Checkout success page, mobile](/assets/readme-images/mobile-6-success.jpg)

The success page is a simple page indicating that the purchase was successful, with a button to return the user to the index page.

</details>

<details>
<summary>Mobile information item pages.</summary>
<br>

![Information pages, mobile](/assets/readme-images/mobile-7-infopages.jpg)

The pages for the FAQ, shipping information, Terms and Conditions, Terms of Service (if applicable) will all be very similar; just extending the base, index template.

</details>

<details>
<summary>Mobile error 404 item page.</summary>
<br>

![Error 404 page, mobile](/assets/readme-images/mobile-8-404.jpg)

The site will also have a custom 404 page, which is also quite simple and will feature a button to return the user to the index page.

</details>

</details>

<br>

Wireframes were built in [Balsamiq's online application.](https://balsamiq.cloud/)
<hr>
<br>

### Flowchart
<hr>
<br>

A flowchart was developed to track a user or staff member's movement through the site. Their actions ultimately effect the database that stores not only information about the items available, but information about what a customer has purchased. This is important, because some of the purchases are of digital goods which remain available for download on the site when the customer is logged in.

<details>
<summary>Bricks Then Made Now development flowchart.</summary>
<br>

![HardParkers Flowchart](/assets/readme-images/flowchart.jpg)

</details>
<br>

Flowchart was built with [LucidChart.](https://lucid.app/lucidchart/) 
<hr>
<br>

### User Stories and Agile Technologies
<hr>
<br>

Agile examples


<br>
<hr>
<br>
<br>

## Features
<hr>
<br>

### General Features on All Pages

Features examples

<details>
<summary>General page features</summary>
<br>

![General features](#)

Examples

</details>

<br>

### Features of Individual Pages

Features Examples

<details>
<summary>Index page features</summary>
<br>

![Index page](/assets/readme-images/AllUpcPage.png)

Examples

</details>

<br>

### Defensive Design

Defensive design examples


<br>

### Future Implementations

Future implementations example

### Accessibility

Colors were checked for contrast during development using Coolers' [Color Contrast Checker](https://coolors.co/contrast-checker/0067b2-d2d5da)

Accessibility examples

<br>
<hr>
<br>
<br>

## Technologies Used
<hr>
<br>

### Languages Used

This project uses HTML, CSS, [Python](https://www.python.org/) and Javascript programming languages. 

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.cloud/)
- [Bootstrap](https://getbootstrap.com/)
- [Bulk Resize Photos](https://bulkresizephotos.com/en)
- Code Institute Gitpod Full Template - Available on request.
- [Color Contrast Checker](https://coolors.co/contrast-checker/)
- [Color Shates Online Generator](https://gradients.app/en/shades/)
- [Django](https://www.djangoproject.com/)
  - [Allauth](https://django-allauth.readthedocs.io/en/latest/)
- [Django Countries](https://github.com/SmileyChris/django-countries)
- [Favicon.io](https://favicon.io/)
- [GitHub](https://github.com/)
- [GitHub Issues](https://github.com/features/issues)
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [GitPod](https://gitpod.io/)
- [Gnu Image Manipulation Program](https://www.gimp.org/)
- [Google Fonts](https://fonts.google.com/)
- [LucidChart](https://lucid.app/lucidchart/) 
- [MiniWebtool Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
- [Pillow]https://pillow.readthedocs.io/en/stable/index.html
- [SQLite](https://sqlite.org/index.html)
- [Stud.io](https://www.bricklink.com/v3/studio/download.page)
- [Tables Generator - Markdown](https://www.tablesgenerator.com/markdown_tables)
- [TinyPNG](https://tinypng.com/)


<!--Frameworks unused so far (Copy Past above as used)

- [AmIResponsive](https://ui.dev/amiresponsive)
- [Bootswatch](https://bootswatch.com/)
- [Cloudinary](https://cloudinary.com/)
- [Code Institute Python linter](https://pep8ci.herokuapp.com/)
  - [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Elephant SQL](https://www.elephantsql.com/)
- [Google Maps](https://www.google.com/maps/@53.281599,-6.2396888,14z)
- [Heroku](https://www.heroku.com)
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/)
- [Markup, the native Android photo editing tool](https://www.android.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)

-->

<br>
<hr>
<br>
<br>

## Local Development and Deployment
<hr>
<br>

### Local Development

Information on local development can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

### Deployment

Information on deployment can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

### How to Fork or Clone

Information on how to fork or clone the repository can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

<br>
<hr>
<br>
<br>

## Testing
<hr>
<br>

Information on testing can be found in [the testing ReadMe](/TESTING.md)

<br>
<hr>
<br>
<br>

## Credits
<hr>
<br>

### Help and Support

- Code Institute Full Stack lessons for the bulk of the understanding about Django, Bootstrap, and other frameworks. [Code Institute](https://codeinstitute.net/ie/)
- Code Institute instructor Simen Daehlin for almost everything else. [Simen Daehlin Github](https://github.com/Eventyret)
- Code Institute mentor Jubrile Akolade provided guidance on where to focus time building the project and an almost infinite amount of other support.
- All of my Code Institute UCD July 2022 cohort, who have been available to answer questions through Slack.
- Code Institute tutors accessed through the Code Institute LMS have been helpful with understanding various concepts during instruction.
- An explanation about how to have Django/Pillow upladed image files go to a specific folder was found [here.](https://youtu.be/O5YkEFLXcRg) The [Django documentation](https://docs.djangoproject.com/en/4.2/topics/files/) could have been a lot clearer about WHERE the example code goes, which is a frustrating aspect throughout working with Django.

- Big thanks to [Lego](https://www.lego.com/en-ie) for having a toy that allows a tremendous amount of aftermarket and web based support, and for just being pretty rad.
- A tremendous amount of Lego research was done on [Bricklink](https://www.bricklink.com/v2/main.page) and [Brickset.](https://brickset.com/sets/6301-1/Town-Mini-Figures)

### Code Used

- The button used throughout is a modified version of Button 13 from CSS Scan's [page of example buttons](https://getcssscan.com/css-buttons-examples), which is in turn attributed to Amazon.
- The countries dropdown menu in the checkout form is by Chris Beaven and can be found [here.](https://github.com/SmileyChris/django-countries)

### Media

- Favicon is "Four Brick, Lego, Blue, Toy, Four" as provided by [ClipArtMax.](https://www.clipartmax.com/middle/m2i8d3Z5H7i8G6i8_four-brick-lego-blue-toy-four-api-icon/)
- Fonts are [Vina Sans](https://fonts.google.com/specimen/Vina+Sans) and [Staatliches](https://fonts.google.com/specimen/Staatliches) for the Bricks Then Made Now logo and [Mina](https://fonts.google.com/specimen/Mina) for the text, the code provided by [Google Fonts](https://fonts.google.com)
- The original image used as the basis for the splash image is from [Brickset.](https://brickset.com/sets/6301-1/Town-Mini-Figures)
- All computer generated renders are done in [Stud.io.](https://www.bricklink.com/v3/studio/download.page)
- "Scooty Puff Jr" model is named for a [Futurama](https://www.imdb.com/title/tt0149460/) gag, and is based on a simple design by [troublesbricking](https://www.instagram.com/troublesbricking/).
- Terms of service is sampled from [www.websitepolicies.com](https://www.websitepolicies.com/blog/sample-terms-service-template).

### Other Thanks

- The Code Institute assessment team; I can't imagine what kind of patience and knowledge it would take to look over these projects without losing it.
- Finally, heartfelt appreciaton to my partner, Stevie, for infinite patience and encouragement. Also, no thanks to Lemon and Beckett for all their non-contributions throughout all five projects, though being fuzzy is it's own moral support.

<br>
<hr>
For educational purposes only.