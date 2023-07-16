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

- [User Experience](#user-experience)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Color Scheme](#colour-scheme)
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
  - [Features of Individual Large Screen Pages](#features-of-individual-large-screen-pages)
  - [Features of Individual Small Screen Pages](#features-of-individual-small-screen-pages)
  - [Defensive Design](#defensive-design)
  - [Future Implementations](#future-implementations)
  - [Accessibility](#accessibility)
- [Search Engine Optimization](#search-engine-optmization)
- [Marketing](#marketing)
  -[Facebook](#facebook)
  -[Instagram](#instagram)
- [E-Commerce Business Model](#e-commerce-business-model)
  - [Customers](#customers)
  - [Pricing](#pricing)
  - [Shipping](#shipping)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks & Libraries Used](#frameworks--libraries-used)
  - [Programs Used](#programs-used)
- [Local Development and Deployment](#local-development-and-deployment)
  - [Local Development](#local-development)
  - [Deployment](#deployment)
  - [How to Fork or Clone](#how-to-fork-or-clone)
- [Testing](#testing)
  - [Code Validation](#code-validation)
  - [Systematic Manual Testing](#systematic-manual-testing)
  - [Representative User Manual Testing](#representative-user-manual-testing)
- [Credits](#credits)
  - [Help and Support](#help-and-support)
  - [Code Used](#code-used)
  - [Media](#media)
  - [Other Thanks](#other-thanks)

<br>
<hr>

## User Experience

<hr>

Portfolio Project 5 is the culmination of the Code Institute "Diploma in Software Development (E-commerce Applications)" course. It is meant to showcase the student's ability to use all the major languages and frameworks covered in the course. By building an operational e-commerce platform, the student can show their proficiency in HTML, CSS, Javascript, Python, Django, Bootstrap, and others. 

### User Stories

- Customer can view available projects.<br>
  When accessing the items page, a customer is able to see a list of all available items. The list can be sorted by theme, searched by either the item number, item name, or description. The results of a list sorted by theme can be sorted by part count.

- Customer can view detailed descriptions.<br>
  The customer can click on an item and view a more detailed description. The detail page includes a description, additional images, pricing for the Instructions, ModernSet, and Fullset, and the current inventory of each and if each is currently available.

- Customer can decide what package is right for them.<br>
  The customer can view the pricing, the availability and what's included in each of the Skus, based on the Item description and the availability indicated on the item detail page. Questions they may have about what is included in the items is further explained on the about and FAQ page which is accessible from all pages of the site.

- Customer can add items to cart.<br>
  Crucial to any e-commerce platform, users can become customers by adding items to a cart and making a purchase. On the item detail page, there are three add to cart buttons, which would add either the Instructions, the ModernSet, or the FullSet to the cart based on which they want. Adding either the ModernSet or the FullSet to the cart would disable the button to add the instructions, to prevent a customer from double purchasing.

- Customer can see a running cart total.<br>
  In order for a customer to keep an eye on their spending, the cart in the top right corner will indicated if there are items in it and how much they would be charged to process the order.

- Customer can make a purchase.<br>
  A customer can view their cart, decide that they are ready to buy, and with Stripe integration can pay for their purchase securely and quickly. The order will be committed to the database.

- Customer can download instructions after purchase.<br>
  A customer can click a button on the item detail page of any item they have purchased, and download a PDF of the set instructions. Of course, if they purchase a physical product, there will be paper instructions sent. But if they don't, or if they can't wait or if they lose them, the isntructions will be available on the website any time they log in.

- Customer can search or filter items.<br>
  From any of the pages, the user can use the search bar at the very top of the page. Not only will the search bar search the item names and descriptions, but it would search the item number as well, since the item number is based on the Lego item number of the vintage set. From a theme page, the customer can also filter All items, or the items of any theme (City, Space, Castle, Train, or MOC) by part count. This is also a defacto price sorting, since the prices are largely based on parts counts but there are up to three differently prices Skus per Item.

- Customer can sign up for email marketing.<br>
  In the footer of all pages for unlogged in users is a button that will take the user to a form to sign up for marketing emails. The form will take the user name, email, and there are four checkboxes for the user to indicate their interests. Per GDPR rules, all these checkboxes are default unchecked and the customer has to opt in.

- Customer can register an account.<br>
  The customer can register for an account. The account is useful for the user to save their information. The account is also necessary for a customer, because when they purchase any set, they gain access to downloadable instructions. By having an account, they can sign in and access those instructions without making additional payments.

- Customer can log in and log out.<br>
  As part of having an account, the customer will be able to sign in and sign out of their account.

- Customer can view past orders.<br>
  A customer will be able to view orders that they have made in the past. In the footer when a customer is logged in is a link to a separate page showing their order history.

- Customer can view social media.<br>
  There will be a social media presence on both Facebook and Instagram

- Staff can create or update items.<br>
  When a staff member is signed in, the nav bar will have options for the staff member to create a new item or sku. Each of the pages will include a form that will update the database with a new item or sku as appropriate. The item detail page will have bars at the bottom where the staff member can edit either the Item, or any of the associated Skus. The staff member will also be able to delete any of these, and there will be a confirmation page before the items are removed from the database.

- Staff can encourage sign up.<br>
  Staff can encourage user sign up and customer conversion by setting a give away set of instructions. Currently, 2201489 Mobile Crane Car is the free instructions and will be downloadable by any logged in

<hr>

## Design
<hr>
<br>

### Color Scheme

Bricks Then Made now uses a simple, direct color scheme. The text is dark grays, nearly black, on a grouping of background colors that ar similar light gray, nearly white. The title is composed of colors similar to the ones Lego uses on their website, promotional materials and packaging. These colors are carried through the site, also being used on buttons, overlays, and image placeholders.

![Background colors](/assets/readme-images/colors-background.jpg)<br>
The background colors are simple, and light gray. They are just intended to help organize the page into sections, so the customer can see clearly what they are looking at.

![Text colors](/assets/readme-images/colors-text.jpg)<br>
The text colors are nearly black. The main color is essentially black, while muted is a dark gray different enough to indicated a difference in content.

![Accent colors](/assets/readme-images/colors-accent.jpg)<br>
The accent colors are similar to those used by Lego. They are used in the title, for design reasons. The yellow color is used in selected buttons, like the buttons that add items to cart or process payment, to indicated urgency and call the user to action. It is also used in the payment handling overlay. The blue color is used on image place holders, and also used to replace the native blue color used by links. The red is only used around the item and sku deletion buttons on the item detail page, when staff is logged in. The yellow is also used similarly for the edit buttons. When these colors are used for anything other than text, the are used at a level of transparancy to limit their intensity.

The Color scheme was developed with help from [Color Contrast Checker](https://coolors.co/contrast-checker/), [Color Shades Online Generator](https://gradients.app/en/shades/), and [Coolers.](https://coolors.co/)

### Typography

![Font example](/assets/readme-images/text-fonts.png)

The typography was chosen primarily for clarity. Mina is the basic font used for the majority of the text on the page. It is a clear but distinct font. Vina and Staatliches are used for the title. Vina, with the strange formatting and mixing of upper and lower case characters seems more vintage, to evoke the old sets; while Staatliches is slick and modern, evoking the smooth computer renders and contemporary styling of the modern sets.

[Vina, Google Fonts](https://fonts.google.com/specimen/Vina+Sans)<br>
[Mina, Google Fonts](https://fonts.google.com/specimen/Mina)<br>
[Staatliches, Google Fonts](https://fonts.google.com/specimen/Staatliches)<br>

### Imagery

The imagery on the website was intentionally kept simple. This is to highlight the products available. It was decided that the overall look of the site should keep with the computer generated renders of the Lego sets. This meant the colors and the graphics were kept simple and flat, with few highlights but highlights where necessary. There was consideration about using the splash image that mixes a real image of an old set with a rendered image of a modern equivalent, but ultimately this was decided to go well with the item detail pages that display an image of the old sets next to renders the modern equivalents for sale. This maintains a visual throughline that also appeals to a customer's nostalgia.

![Bricks Then Made Now index](/assets/readme-images/imagery.png)<br>
The index page showing the mix of photos of vintage Lego, and renders of modern Lego. 

The photograph is from [Brickset](https://brickset.com/), and the renders were made in [Stud.io](https://www.bricklink.com/v3/studio/download.page)
<hr>

## Planning
<hr>
<br>

A project of even such a small scope as this requires careful planning before any development can begin. Care was taken to plan the models for future implementations, without harming existing databases as the site's needs may grow. For example, there is an imagefield in the item model that is currently unused on the site, but gives space for future implementations.

<hr>

### Models
<hr>
<br>

Custom models had to be developed to hold the appropriate information the website's database. Care had to be taken to plan the way the models would interact, since there are two instances of having one model extended by another. This was necessary to have a few different purchasable SKUs related to a single item, and to have a unique siteuser model that uses the Django authorization functionality as its base.

Three models are custom and new for the project, the [Item model](#item-model), the [Sku model](#sku-model), and the [NewsletterUser model](#newsletteruser-model). The other models are modified, but are still essentially boilerplate eCommerce object models.

#### Item model

This model contains information about the items listed for sale on the site. The item model will only include information that is common to all three SKUs related to a particular item, including the item number, item name, related themes, the description, images, and the partcount. It will be extended with the SKU model which will hold information about each individual SKU that are part of the item.

This model is custom.

| Key                        | Field        | Form                 |
|----------------------------|--------------|----------------------|
| item_number                | Integerfield | Integer              |
| item_name                  | Charfield    | Text                 |
| item_theme                 | Foreignkey   | Foreignkey           |
| item_description           | Textfield    | Text                 |
| item_old                   | Imagefield   | Image                |
| item_old_url               | URLfield     | URL                  |
| item_render                | Imagefield   | Image                |
| item_render_url            | URLfield     | URL                  |
| item_modern                | Imagefield   | Image                |
| item_modern_url            | URLfield     | URL                  |
| item_detail                | Imagefield   | Image                |
| item_detail_url            | URLfield     | URL                  |
| item_intructions_url       | URLfield     | URL                  |
| item_partcount             | Integerfield | Integer              |
| item_user_owned            | ManyToMany   | Many to many         |

#### SKU model

The SKU model containst he rest of the information about what the customer can buy. It extends the item model, which describes the Bricks Then Made Now set, and adds the price, an inventory field, and fields that indicate whether its a SKU for a physical, shippable item or a SKU for a digital instructions download that will not need to be shipped and have shipping fees included. The SKU model will also include an included instructions field that will contain the SKU for the digital instructions that will be included with a digital purchase, so that they will be unlocked for the customer with all purchases.

This model is custom.

| Key                        | Field        | Form                  |
|----------------------------|--------------|-----------------------|
| sku_item                   | Foreignkey   | One to many with item |
| sku_number                 | Integerfield | Integer               |
| sku_type                   | Charfield    | Text, choices         |
| sku_price                  | Decimalfield | Decimal to two places |
| sku_physical               | Boolean      | Checkbox              |
| sku_inventory              | Integerfield | Integer               |

#### Order model

The order model contains all the information about the order, including a python generated order number, an order date set to the date the order was created, and links the order to a site user. It will also hold the payment information from Stripe.

This model is not custom. It is essentially a modified version of the CI equivalent.

| Key              | Field        | Form                             |
|------------------|--------------|----------------------------------|
| order_number     | Charfield    | Generated                        |
| siteuser         | Foreignkey   | One to many                      |
| date             | Datefield    | Generated, current date          |
| full_name        | Charfield    | Text                             |
| phone_number     | Charfield    | Text                             |
| street_address_1 | Charfield    | Text                             |
| street_address_2 | Charfield    | Text                             |
| town_or_city     | Charfield    | Text                             |
| state            | Charfield    | Text                             |
| zipcode          | Charfield    | Text                             |
| country          | Charfield    | Text                             |
| order_total      | Decimalfield | Generated, decimal to two places |
| shipping_cost    | Decimalfield | Generated, decimal to two places |
| grand-total      | Decimalfield | Generated, decimal to two places |
| original_Cart    | Textfield    | Text                             |
| order_stripe_pid | Charfield    | Taken from Stripe                |

#### Line item model

This small model is used to control the information about individual items in an order.

This model is not custom. It is essentially a modified version of the CI equivalent.

| Key              | Field        | Form                             |
|------------------|--------------|----------------------------------|
| order            | Foreignkey   | Order                            |
| item             | Foreignkey   | Item                             |
| sku              | Foreignkey   | Sku                              |
| quantity         | Integerfield | Integer                          |
| lineitem_total   | Decimalfield | Decimal to two places            |

#### SiteUser model

The SiteUser model extends the Django AllAuth user model, holding information that can auto populate the shipping and billing forms during checkout, as well as give the user the correct permissions as a site user or site administrator and hold information about what items a user owns so they can access their digital downloads.

This model is not custom. It is essentially a modified version of the CI equivalent.

| Key                      | Field        | Form                                    |
|--------------------------|--------------|-----------------------------------------|
| user                     | Foreignkey   | One to one                              |
| siteuser_phone_number    | Charfield    | Text                                    |
| siteuser_street_address1 | Charfield    | Text                                    |
| siteuser_street_address2 | Charfield    | Text                                    |
| siteuser_town_or_city    | Charfield    | Text                                    |
| siteuser_state           | Charfield    | Text                                    |
| siteuser_zipcode         | Charfield    | Text                                    |
| siteuser_country         | Charfield    | Text                                    |

#### NewsletterUser model

The NewsletterUser is a separate model that stores information about customers who wish to receive newlsetters. It includes their name, email address, and what they are interested in receiving information about.

This model is custom.

| Key               | Field        | Form     |
|-------------------|--------------|----------|
| newsletter_name   | CharField    | Text     |
| newsletter_email  | EmailField   | Email    |
| newsletter_city   | BooleanField | Checkbox |
| newsletter_space  | BooleanField | Checkbox |
| newsletter_castle | BooleanField | Checkbox |
| newsletter_train  | BooleanField | Checkbox |

<br>
<hr>

### Wireframes
<hr>
<br>

Wireframes were made to describe how the site would look on both large and mobile screens before work began on the actual code. Many changes were made between planning and implementation. Most notably, the index page and the items page are different, but the items page features many of the planned implementations that the index page was initially meant to have. Other changes include the orientation of images on the detail pages and some of the form formatting.

#### Large Screen Wireframes
<br>

![Index page on large screens.](/assets/readme-images/wireframes/large-1-index.jpg)

This wireframe of the index page shows the planned organization of the page. The site title, search bar and cart link will remain at the very top of the screen, with a nav bar just below it. Below that is the splash image, with a planned carousel for specials or site news. The center of the page is dominated with a list of all items that the user can sort by price, or using the nav bar, can filter by theme. The bottom of the page has a footer that is visually distinct like the header. It will hold a form for users to sign up for the mailing list, feature related social media, and links to supporting documents like an FAQ and the T&Cs that suppor the site. Many of the header and footer aspects will carry through the rest of the site, but the splash image and carousel will be only visible on the index page. 

Some changes were ultimately made to the index page, most notably, the index page has a block of graphic links to each theme, instead of a list of items. The list of items shows up on the item page, which is more similar to the index page's initial plan.

Other large screen wireframes can be seen below:

<details>
<summary>Expand to view large screen wireframes.</summary>
<br>

<details>
<summary>Large screen product items page.</summary>
<br>

![Product detail page, large screen](/assets/readme-images/wireframes/large-1-index.jpg)

The items page ended up almost exactly as the index page was planned, so it is included here. 

The site title, search bar and cart link will remain at the very top of the screen, with a nav bar just below it. Below that is the splash image, with a planned carousel for specials or site news. The center of the page is dominated with a list of all items that the user can sort by price, or using the nav bar, can filter by theme. The bottom of the page has a footer that is visually distinct like the header. It will hold a form for users to sign up for the mailing list, feature related social media, and links to supporting documents like an FAQ and the T&Cs that suppor the site. Many of the header and footer aspects will carry through the rest of the site, but the splash image and carousel will be only visible on the index page.

</details>

<details>
<summary>Large screen product detail page.</summary>
<br>

![Product detail page, large screen](/assets/readme-images/wireframes/large-2-detail.jpg)

The detail page will feature a large image displayed, with smaller images that can be selected below. The item description and other details will be featured to the right of the image, with space for buttons for the three different packages available related to each item.

</details>

<details>
<summary>Large screen shopping cart page.</summary>
<br>

![Shopping cart page, large screen](/assets/readme-images/wireframes/large-3-cart.jpg)

The shopping cart page will list the items the customer has added, with a small image. It will also show selected details, including the price. There will be a quantity selector for physical items, and an extended price. Note, the quantity is set to one and is not selectable for the instructions only digital download. The page will also show the subtotal, shipping cost, and grand total. These will be lined up with the extended totals for consistency, and the checkout button will be directly below to encourage the customer to buy with a clear call to action.

</details>

<details>
<summary>Large screen create item page.</summary>
<br>

![Create item page, large screen](/assets/readme-images/wireframes/large-4-create-item.jpg)

The form to add an item will have it's own page, with a simple form for staff to fill with each field in the item model.

</details>

<details>
<summary>Large screen create SKU page.</summary>
<br>

![Create SKU page, large screen](/assets/readme-images/wireframes/large-5-create-sku.jpg)

The form to add an item's indivdual SKUs will have another page, which will allow the user to add an individual SKU suffix to the item number. The related item number will be chosen from a dropdown menue, as will the SKU suffix. The staff will be able to add information specific to each SKU including price, whether the SKU represents a phyical item, how many are inventory for sale, and what digital instructions would be included with the physical items.

</details>

<details>
<summary>Large checkout success page.</summary>
<br>

![Checkout success page, large screen](/assets/readme-images/wireframes/large-6-success.jpg)

The success page is a simple page indicating that the purchase was successful, with a button to return the user to the index page.

</details>

<details>
<summary>Large screen information item pages</summary>
<br>

![Information pages, large screen](/assets/readme-images/wireframes/large-7-infopages.jpg)

The pages for the FAQ, shipping information, Terms and Conditions, Terms of Service (if applicable) will all be very similar; just extending the base, index template.

</details>

<details>
<summary>Large screen error 404 item page</summary>
<br>

![Error 404 page, large screen](/assets/readme-images/wireframes/large-8-404.jpg)

The site will also have a custom 404 page, which is also quite simple and will feature a button to return the user to the index page.

</details>

</details>
<hr>

#### Mobile Wireframes
<br>

![Index page on mobile screens.](/assets/readme-images/wireframes/mobile-1-index.jpg)

The mobile index page will be similar in structure to the large screen page, except the list of items will be stacked instead of stacks of rows. It will contain the same information, as well as the the sort and filter functionalities as the large screen page. 

Similarly to the larger screen pages, this function became an items page, while the index page holds a block of themed links.

Other large screen wireframes can be seen below:

<details>
<summary>Expand to view mobile wireframes.</summary>
<br>

<details>
<summary>Mobile product items page.</summary>
<br>

![Product detail page, mobile](/assets/readme-images/wireframes/mobile-1-index.jpg)

Just as before with larger screens, the items page became what the index page was initially intended to be. 

The mobile index page will be similar in structure to the large screen page, except the list of items will be stacked instead of stacks of rows. It will contain the same information, as well as the the sort and filter functionalities as the large screen page. 

</details>

<details>
<summary>Mobile product detail page.</summary>
<br>

![Product detail page, mobile](/assets/readme-images/wireframes/mobile-2-detail.jpg)

Continuing with the similar structure and equal functionality, the detail page will be slightly differently organzied, with the three small images below both the larger image and the description. The purchase options will be below the entirety of the description and images, to allow as much room as possible for the add to cart buttons to make it easy for customers to add items to the cart. Note that again, the splash image and news carousel will be omitted, but the navbar and shopping cart will remain at the top of the page.

</details>

<details>
<summary>Mobile shopping cart page.</summary>
<br>

![Shopping cart page, mobile](/assets/readme-images/wireframes/mobile-3-cart.jpg)

The shopping cart page will maintain the structure of keeping the totals to the right, in line, and lined up with the checkout button.

</details>

<details>
<summary>Mobile create item page.</summary>
<br>

![Create item page, mobile](/assets/readme-images/wireframes/mobile-4-create-item.jpg)

Though it's unlikely the site staff will be adding items from a mobile device, there will be a mobile friendly version of the form.

</details>

<details>
<summary>Mobile create SKU page.</summary>
<br>

![Create SKU page, mobile](/assets/readme-images/wireframes/mobile-5-create-sku.jpg)

Though it's unlikely the site staff will be adding items from a mobile device, there will be a mobile friendly version of the form.

</details>

<details>
<summary>Mobile checkout success page.</summary>
<br>

![Checkout success page, mobile](/assets/readme-images/wireframes/mobile-6-success.jpg)

The success page is a simple page indicating that the purchase was successful, with a button to return the user to the index page.

</details>

<details>
<summary>Mobile information item pages.</summary>
<br>

![Information pages, mobile](/assets/readme-images/wireframes/mobile-7-infopages.jpg)

The pages for the FAQ, shipping information, Terms and Conditions, Terms of Service (if applicable) will all be very similar; just extending the base, index template.

</details>

<details>
<summary>Mobile error 404 item page.</summary>
<br>

![Error 404 page, mobile](/assets/readme-images/wireframes/mobile-8-404.jpg)

The site will also have a custom 404 page, which is also quite simple and will feature a button to return the user to the index page.

</details>

</details>

<br>

Wireframes were built in [Balsamiq's online application.](https://balsamiq.cloud/)
<hr>

### Flowchart
<hr>
<br>

A flowchart was developed to track a user or staff member's movement through the site. Their actions ultimately effect the database that stores not only information about the items available, but information about what a customer has purchased. This is important, because some of the purchases are of digital goods which remain available for download on the site when the customer is logged in.

![Bricks Then Made Now Flowchart](/assets/readme-images/flowchart.jpg)

Flowchart was built with [LucidChart.](https://lucid.app/lucidchart/) 
<hr>

### User Stories and Agile Technologies
<hr>
<br>

Progress on this project was tracked using agile technologies. GitHub's built in issues and Kanban board were used for their accessibility and their integration with GitPod, as well as integration with the repository.

During the planning stages, User Stories were developed and written as individual issues. Afterward, these stories were translated into individual tasks. This gave the project necessary redundancy making sure that everything that needed to get done got done. 

Epic stories were developed to further organize the tasks. Each task was assigned at least one label, as well. The labels were developed to indicate which language each task was most associated with, if tasks were related to Stripe integration or deployment, if tasks were MVP, bugs, or enhancement, or if they were part of further project planning. There was also a quickwin label for tasks that should be relatively small fixes so that tasks could be selected based on time and focus available. 

Agile techniques and technologies were used during the initial planning stages and then throughout the entire development process.

There are several Enhancement labels still on the board in the Todo column, most of which are artifacts of the initial planning stages. These were made into future implementations after consultation with mentors and instructors when project scope was discussed.

The Bricks Then Made Now repository hosted in GitHub can be found [here](https://github.com/WSMorrison/BricksThenMadeNow). The Issues in the Bricks Then Made Now repository can be found [here.](https://github.com/WSMorrison/BricksThenMadeNow/issues). The Bricks Then Made Now project and Kanban board can be found [here.](https://github.com/users/WSMorrison/projects/6)
<hr>

## Features
<hr>

### General Features on All Pages

The page has several main pages and some supporting confirmation and information pages. Because of the page construction, a base with a header and footer and so navigation supplements included, there are a few features that are common to almost all pages.

<details>
<summary>General page features, using the index as an example.</summary>
<br>

![General features](/assets/readme-images/features/large-1-index.png)

- At the top of the page, there is a title bar.
  - The title is clickable and will always bring the user to the index page.
  - The search bar will search all item numbers, names, and descriptions.
  - The shopping cart icon will change when items are added to the cart, and a running total will indicate to the customer what their cart consists of.
- The nav bar with the themes and the login links remains on all pages for quick navigation.
- The footer foots all pages.
  - On the left is a button that will take the customer to a form where they can sign up for promotional emails.
  - In the center are a series of links to find Bricks Then Made Now social media or a contact information.
  - On the right are a series of links to informative pages, including a privacy polict, an about page, and a Terms of Service.

</details>

<br>

### Features of Individual Large Screen Pages

Each page necessarily has its own set of features.

<details>
<summary>Index page features</summary>
<br>

![Index page](/assets/readme-images/features/large-1-index.png)

- The index page has all the general page features.
- The splash, title image is prominantly positioned near the top.
- Below the splash image is a carouselle that promotes the page.
- Prominently in the middle of the page is a grid of the themes, plus a square to take the user to their account information.

</details>

<details>
<summary>Items page features</summary>
<br>

![Items page](/assets/readme-images/features/large-2-items.png)

- The items page has all the general page features.
- The splash image and carouselle do not appear on this, or any further pages.
- Below the nav bar is a secondary nav bar in yellow.
  - Text indicates which theme the customer is currently navigated to.
  - On the right, a sort-by dropdown allows the customer to sort by part count. The part count is directly related to price, so it defacto does both functions.
- The items page shows a grid of the items related to the selected theme. It will show all items if the current theme selected is "all."
- Each item is represented by an image, the item name, the item number, the part count, and there is a button to access the item detail page.

</details>

<details>
<summary>Item detail page features</summary>
<br>

![Item detail page](/assets/readme-images/features/large-3-item-detail.png)

- The item detail page has all the general page features.
- The yellow bar displays text showing the theme and item name that the user is navigated to.
- There are more images of the item where applicable, including a picture of the original Lego set, and a detail image showing a different, significant view. If there are not three images, a placeholder fills the space.
- In addition to the item name, number, and part count, an item description is displayed.
- Below the item details, the three Skus are displayed, where applicable.
  - The Instructions Sku displays with the number, and price. 
  - The ModernSet Sku displays with the number, what is included, the inventory, and the price, with a quantity selector. The quantity selector will not allow a user to order more than are in inventory.
  - The FullSet Sku dispalys with the number, what is included, the inventory and the price, with a quantity selector. The quantity selector will not allow the user to order more than are in inventory.
  - If there is no Instructions or ModernSet Sku, a coming soon notice is displayed.
  - If there is not FullSet Sku, nothing is displayed.
- There is a back button that takes the user back to the items list.

![Instructions in cart detail](/assets/readme-images/features/large-4-item-detail-in-cart.png)

If a customer adds any available Sku to their cart, the instructions are shown as in-cart because the instructions download is available with any purchase.

![Item detail sold out detail](/assets/readme-images/features/large-12-sold-out.png)

Items are sold out item detail detail. Also shown here is the download button, where a customer can download the instructions of the items they have purchased. This is actually the crux of the entire website, and is very important.

![Item detail coming soon detail](/assets/readme-images/features/large-13-coming-soon.png)

Items coming soon item detail detail.

![Staff user item and sku control bars detail](/assets/readme-images/features/large-11-staff-item-controls.png)

Logged in staff users can delete and edit items and skus directly from the item detail page.
(Not shown) If there are any items in the cart, the item and sku edit and delete buttons are removed to prevent database errors.

</details>

<details>
<summary>Cart page features</summary>
<br>

![Cart page](/assets/readme-images/features/large-5-cart.png)

- The cart page has all the general page features.
- The yellow bar indicates that the user is navigated to the shopping cart.
- The cart shows all the items in the cart.
  - The customer can change the quantity or remove the item from ther cart.
  - The extended price is shown for each item, adjusted by its quantity.
- The page shows the total number of items to ship. For example, three Instructions and five ModernSets will show five items to ship, even though eight items are in the cart.
- There are buttons to return to shopping and going to checkout.

</details>

<details>
<summary>Checkout page features</summary>
<br>

![Checkout page](/assets/readme-images/features/large-6-checkout.png)

- The checkout page has all the general page features.
- The yellow bar indicates that the user is navigated to checkout.
- There is a small cart displaying to the left, to remind the customer what the heck they're spending all this money on. Toys. Oh boy, toys. Great. Maybe we should grow up.
- To the right, there is a checkout form showing the shipping information information and payment form.
- There is a checkbox that will add the shipping information to the SiteUser account.
- There are buttons to return to shopping and process the payment.

</details>

<details>
<summary>Checkout overlay</summary>
<br>

![Checkout is happening page](/assets/readme-images/features/large-7-dont-touch.png)

- There are no features.

</details>

<details>
<summary>Success page features</summary>
<br>

![Success page](/assets/readme-images/features/large-8-success.png)

- The success page has all the general page features.
- The yellow bar indicates that the user is navigated to the checkout success page.
- There is a message thanking the customer and telling them that their order was successful.
- The return to shopping button was intentionally left off. If the customer is going to make another order, perhaps as a gift, they know how to do it. If they're all done, it's pretty condescending to have the page suggest they continue shopping, isn't it?

</details>

<details>
<summary>Order history page features</summary>
<br>

![Order history page](/assets/readme-images/features/large-9-order-history.png)

- The order history page has all the general page features.
- The yellow bar indicates that the user is navigated to the order history page.
- The order history shows a list of orders made by the logged in account.
- There is only one order here, but be assured, if this customer had made more orders, they would be there.

</details>

<details>
<summary>Error404 page features</summary>
<br>

![Error404 page](/assets/readme-images/features/large-10-error404.png)

- The error 404 page has all the general page features.
- The yellow bar indicates that the user is navigated to a dangerous place!
- The Lego version of the iconic Dennis Nedry mocking .gif mocks the user and tells them what a bad thing they did.
- There is a button to return the customer to the items page.

</details>

<br>

### Features of Individual Small Screen Pages

Mobile screens are identical in function, but are organized slightly differently. A limited selection of mobile screens are shown below.

<details>
<summary>Index page features</summary>
<br>

![Index page](/assets/readme-images/features/mobile-1-index.png)

- The index page has all the general page features, similarly laid out.
  - The title bar is stacked.
- The splash, title image is prominantly positioned near the top.
- Below the splash image is a carouselle that promotes the page.
- Prominently in the middle of the page is a stack of the themes, plus a square to take the user to their account information.
- The footer is reorganized, so that the newsletter signup is above both the social media and the information pages sections of the footer.

</details>

<details>
<summary>Index page features</summary>
<br>

![Items page](/assets/readme-images/features/mobile-2-index.png)

- The items page has all the general page features.
- The splash is not shown, and will not be shown for any other mobile pages.
- The yellow bar indicates that the user is navigated to a particular theme.
  - On the right is the sort drop down, which works identically to the large screen version.
- The items in the theme are stacked.
- Each item has an image, item name, item number, part count and button to view.

</details>

<details>
<summary>Item detail page features</summary>
<br>

![Item detail page](/assets/readme-images/features/mobile-3-item-detail.png)

- The item detail page has all the general page features.
- The yellow bar displays text showing the theme and item name that the user is navigated to.
- There are more images of the item where applicable, including a picture of the original Lego set, and a detail image showing a different, significant view. If there are not three images, a placeholder fills the space.
- In addition to the item name, number, and part count, an item description is displayed.
- Below the item details, the three Skus are displayed, where applicable.
  - The Instructions Sku displays with the number, and price. 
  - The ModernSet Sku displays with the number, what is included, the inventory, and the price, with a quantity selector. The quantity selector will not allow a user to order more than are in inventory.
  - The FullSet Sku dispalys with the number, what is included, the inventory and the price, with a quantity selector. The quantity selector will not allow the user to order more than are in inventory.
  - If there is no Instructions or ModernSet Sku, a coming soon notice is displayed.
  - If there is not FullSet Sku, nothing is displayed.
- There is a back button that takes the user back to the items list.

The additional features, such as the "In Cart" button, "Sold Out" buttons and staff edit and delete bars are similar in form to the large screen, but of course oriented slightly differently.

</details>

<details>
<summary>Cart page features</summary>
<br>

![Cart page](/assets/readme-images/features/mobile-5-cart.png)

- The cart page has all the general page features.
- The yellow bar indicates that the user is navigated to the shopping cart.
- The cart shows all the items in the cart.
  - The customer can change the quantity or remove the item from ther cart.
  - The extended price is shown for each item, adjusted by its quantity.
- The page shows the total number of items to ship. For example, three Instructions and five ModernSets will show five items to ship, even though eight items are in the cart.
- There are buttons to return to shopping and going to checkout.

</details>

<details>
<summary>Checkout page features</summary>
<br>

![Checkout page](/assets/readme-images/features/mobile-6-checkout.png)

- The checkout page has all the general page features.
- The yellow bar indicates that the user is navigated to checkout.
- There is a small cart displaying above the checkout forms.
- Below, there is a checkout form showing the shipping information information and payment form.
- There is a checkbox that will add the shipping information to the SiteUser account.
- There are buttons to return to shopping and process the payment.

</details>

<details>
<summary>Cehckout overlay features</summary>
<br>

![Checkout is happening page](/assets/readme-images/features/mobile-7-dont-touch.png)

</details>

<details>
<summary>Success page features</summary>
<br>

![Success page](/assets/readme-images/features/mobile-8-success.png)

- The success page has all the general page features.
- The yellow bar indicates that the user is navigated to the checkout success page.
- There is a message thanking the customer and telling them that their order was successful.

</details>


### Defensive Design

As with any web application, defensive code is necessary to make sure the page can continue working even during real world usage. Customers and staff both can cause issues with the database by passing bad information. With an e-commerce platform, the issue could be worse than an error 404 or 500, but could cause issues that would charge customers for things they don't receive or ship them items they didn't pay for. Because of this, it is particularly import to consider defensive design throughout the website to ensure that things work not only properly, but smoothly. 

Many defensive features are native to Django forms, like stripping whitespace from CharFields and TextFields and making sure a URL or email address at least follows the standard formats.

When a customer signs up, they are challenged in a handful of ways.
- The email address cannot be blank, and must include an @ symbol with valid characters before and after, and must match with two inputs.
- The username cannot be blank or include trailing or trailing whitespate, and must be at least four valid characters long.
- The password must be at least 8 valid characters long, is not allowed to be all letters or all numbers, mustn't be too similar to the user name, and must match twice, and may not be "too common."

Once logged in, the account details form does not offer challenges about being blank, but does strip leading and trailing whitespace. This is helpful in case a customer does not want to leave their information in the database.

However, the details on the checkout form do challenge the user.
- The usual django form defenses are in place.
- If the customer accidentally puts their fields as all blank spaces, the order fails and they see an order failed page.

Stripe integration has their own defensive code.
- Code validates that card format is acceptable.
- Validates that the expiry date is in the future.
- Validates that zipcode is the correct format.
- If the payment fails, the order fails and the customer sees an order failed page.

There is also a front end functionality for logged in staff to be able to create, edit and delete Items. In addition to the built in Django form field validation, a handful of logic implementations had to be made to prevent issues when using the Add Item form.
- The item number must be five digits. Otherwise, the number is left to the staff member's discretion. For example, MOC items like the 220SPJr will be numbered for "20'22'-checkdigit-'S'cooty'P'uff'Jr'" instead of the 2306534 numbered for "20'23'-checkdigit-'6534'" where 6534 was the original Lego set number for the original Beach Bandit.
- Theme is selected by a choice box to prevent items not getting a theme listed.
- The images are not checked because items can be added without an image.
- The instructions .pdf field is checked to make sure the URL is not only a valid URL but starts with https://res.cloudinary.com/ and ends with .pdf. Knowing that staff is not likely to input malicious files, this is considered good enough validation to prevent errors and failures.

The Add Sku form has some similar safeguards.
- The related item comes from a choice box to make sure it is linked to a valid item.
- The Sku number is limited to 5 digits, but is left to the staff member's discretion for the sake of flexibility. Suggestions are noted in the form.
- The Sku type is a choice box to make sure the Sku type is valid. If the staff member accidentally tries to duplicate the Sku type for an item, the form is returned as invalid for adjustment.

When editing items, some additional safeguards are necessary.
- To make sure to not cause a database issue while working, the Edit Item and Edit Sku buttons are disabled unless the cart is empty.
- The Edit Item form is identical to the Add Item form.
- The Edit Sku form is slightly different.
  - The Sku Item field is not editable.
  - The Sku type field is not editable.
  - If either of these need to be edited, the staff member will need to delete the Sku and start over. This will prevent a Sku froma accidentally getting reassigned incorrectly.

<br>

### Future Implementations

As with any website, or any project, there are always future implemenations to be considered.

- An additional navigable tab for sales or other kinds of specials, in addition to City, Space, Castle, Train and Moc would be a handy way for the business to list any specials or promotions going, or an ability to sell seconds and incomplete sets at appropriate discounts.
- It would be handy for there to a database model that could include a shipping pricing, whichever free-to-download-set was currently linked to the Free-instructions with signup promotion. This model would be not just admin, but front end editable so that staff members wouldn't have to deal with settings or code.
- An early iteration on the site allowed customers to be charged shipping as a flat rate based on the number of shippable items purchased. Passing this charge from the context to the Order Model proved beyond this development period's scope, and this will be implemented in the future.
- Additionally, there is room in the item model for a fourth image, as well as URLs for the images. The additional image and the URLs to very large images would give the customer more detail about what they can expect from their purchase.
- Since customers need to sign up for an account to download their instructions, it would be handy to have a wish list feature, especially as the product base grows.



### Accessibility

Care was taken to make sure the page met accessibility guidelines. Accessibility is important so that everyone is welcome and included on Bricks Then Made Now. 

- All images have alt text, and all links and buttons have aria labels.
- Semantic web structure was maintained, making sure to use headers, footers, body, sections and divs appropriately to organize the page not just visually but for screen readers as well.
- Colors and images were carefully selected to make sure that contrast was great enough so that anyone could read the website. Colors were checked for contrast during development using Coolers' [Color Contrast Checker](https://coolors.co/contrast-checker/0067b2-d2d5da)

![Google Lighthouse scores](/assets/readme-images/lighthouse-score.png)

Accessibility, Best Practices and SEO scores calculated by [Google Lighthouse.](https://developer.chrome.com/docs/lighthouse/overview/)
<hr>

## Search Engine Optmization
<hr>

Search Engine Optimization was planned for and implemented when the site was deployed.

During planning, several short-tail keywords and long-tail phrases were focused on for copy throughout the website. Some examples are below:

**Keywords:**

| Short-tail keywords |               | Long-tail phrases             |
|---------------------|---------------|-------------------------------|
| **Lego related**    | **General**   | **Lego related**              |
| Lego                | playset       | buy vintage lego sets         |
| AFOL                | creative play | vintage lego sets for sale    |
| MOC                 | playability   | Lego MOC                      |
| vintage             | play          | buy updated Lego sets         |
| vintage Lego        | stable        | buy modern Lego sets          |
| custom              | iconic        | buy vintage Lego sets         |
| custom Lego         | kids          | buy Lego instructions         |
| Lego MOC            | toys          | buy custom Lego instructions  |
| genuine             | nostalgia     | where can I find custom Lego  |
| genuine Lego        | nostalgic     | Where can I buy custom Lego   |
| real                | memories      | custom Lego gifts             |
| real Lego           |               | Lego for adults               |
| bricks              |               | AFOL Lego sets                |
| Lego bricks         |               | adult Lego sets               |
| elements            |               | |
| Lego elements       | | |
| printed elements    | | |
| Lego [kit number]   | | |
| classic city        | | |
| Lego classic city   | | |
| classic castle      | | |
| Lego classic castle | | |
| minifig             | | |
| Lego minifig        | | |
| instructions        | | |
| Lego instructions   | | |
| clutch power        | | |

<br>
<hr>

## Marketing
<hr>

As with any business, marketing is paramount for success. A business such as Bricks Then Made Now will be well served by old-fashioned marketing like trade shows, conventions, or other physical and in person forms of marketing. Word of mouth is powerful, as is seeing the products in the plastic. However, the reach of such marketing is limited and without a large, expensive staff will grow the business slowly.

Therefore web marketing will be an important way to grow a web-based business. Fortunately, online spaces have begun to serve the hobbyist community in ways similar to in-person trade shows and conventions. It's almost as easy to to create the relationships online as it is pressing the flesh, and that is a strong advantage for eCommerce. Social media is a particularly powerful tool, so Bricks Then Made Now will position itself to enter the online community that way.

### Facebook

<details>
<summary>Facebook</summary>
<br>

![Facebook](/assets/readme-images/bricks-then-made-now-facebook-mockup.png)

The Facebook page will be a great way for users, fans, and potential customers will to keep up with Bricks Then Made Now. It can be a great way for Bricks Then Made Now to show off not only newly available products, but keep customers informed about upcoming releases. This will help develop excitement. Lego is all about the experience building, and the ability to hide surprises and easter eggs in the build, which would be far too much detail to show on even a website with a huge scope. By keeping customers involved with the development process, they would get to see what they can expect, knowing that these are even just teasers to what will ultimately be available. 

The profile picture and the headline picture would mirror other social media and the main website, helping maintain a common theme through all the online presences.

The feed would showupcoming or current products. It could also show products in-play by customers. Potential customers can also give feedback and engage with each other, hopefully appreciating each other's opinions and Bricks Then Made Now's offerings.

The About section could show the Bricks Then Made Now contact information, and the website so that people can find the information they need to find.

There can be many hosted pictures in the Photos section, where customers can peruse not just products in their official renders, but in progress images and detail images that will help them make decisions and help Bricks Then Made Now build excitement for the brand and products.

It could also show potential customers how well liked the products are, and feature people who like, follow, and even contribute to the site in the Liked-by section.

</details>
<br>

### Instagram

<details>
<summary>instagram</summary>
<br>

![Instagram](/assets/readme-images/bricks-then-made-now-instagram.png)

Instagram will have a similar role in the marketing plan. The unique Instagram layout will make it excellent for showing the old set, the recreation, and them together. Each post could also have copy that discusses each. 

The profile picture would mimic Facebook's. 

The feed is an information packed section, discussing the old kit in significant detail. Why it's cool and why it's important, and why it was chosen to be redeveloped with modern elements and techniques. The second post in each row would be devoted to the modern set. It would explain why certain choices were made, and in which ways the design was updated. The third post in the row would compare the two models, comparing the part count and pricing and pointing out the differences and improvements.

Of course, the about blurb would indicate the website the customer could go to.

The real benefit of Instagram are the hashtags, where it can relate the products and models to others builds, and other communities. This would allow people to discover the models and the website just by being curious about the vintage sets that are being redeveloped, and also help spread the word of mouth in a digital analog to the trade shows and conventions. By following and being followed by other influentual accounts, and by collaborating with other accounts, Bricks Then Made Now can help not only build a following but build the Lego AFOL and MOC community.

The Instagram presence is real and live now, [here.](https://www.instagram.com/bricksthenmadenow/)

</details>

Small business like this can be well served by marketing across many platforms. Not only would the site have a presence on Facebook and Instagram, but it would also advertise on these platforms. This would allow ads to be targeted at appropriate users who are engaging with other Lego content, or who are within the age ranged Bricks Then Made Now intends to sell to. Google ads, and specifically YouTube ads targeting videos of Lego, related content, and even general hobby content would be helpful in engaging new customers. 

Bricks Then Made Now would also be able to market by engaging with online content creators on social media. Having AFOL on Instagram, TikTok, YouTube, Facebook, Twitter, and Threads use or highlight BTMN models would help generate interest, viewers, clicks and sales. There could also be colaboration between BTMN and these creators. BTMN could also collaborate with existing business in the Lego space, for example collaborating with [Brick Sticker Shop](https://www.brickstickershop.com/) could be beneficial for both. Through selling custom sticker sets linked to BTMN instructions, pack-ins of customer stickers in ModernSets, or pack-ins of restoration sticker sets with FullSets, Brick Sticker Shop could build on BTMN success, and with custom or restoration stickers available on Bricks Then Made Now, a mew product line could be added and the fidelity of existing produt lines could be improved.

Also, various unconventional marketing techniques could be used. While new, Bricks Then Made Now could have an eBay store, where they could sell defects, prototypes and incomplete models at a discount. Bricks Then Made Now could be a seller as well as a buyer on Bricklink, allowing excess brick to be sold off so that costs weren't being sunk into dead stock. Both of these would be revenue streams, but would have the added marketing effect of getting Bricks Then Made Now in front of customers who are already willing to spend money, and are doing so on other, established platforms. This is a common practice among small, boutique, hobby focused shops and would be very helpful for Bricks Then Made Now.

<br>
<hr>

## E-Commerce Business Model
<hr>

Bricks Then Made Now is meant to appeal to broad base of Lego enthusiasts. From kids to adults, the appeal of the smartly colored, well designed and eminently playable sets is universal. The modernization of old sets will appeal to adults where nostagia is high. They also focus on themes that are universal; helicopters, motorcycles, space exploration.

The pricing of sets being sold will be based primarily on the price per part as available, with the intention of keeping it near a target of between $0.12 and $0.15 per part. This is slightly higher than Lego's own price per part, but custom sets from a boutique seller can charge a premium, and this is much lower than other custom Lego set eCommerce platforms.

Shipping will be advertised as free, though shipping will just be calculated into the cost of all physical sets.

### Customers

Bricks Then Made Now intend to sell to adult followers of Lego, but also to adults wishing to give their kids a similar, but modern experience, like their own.

- Recreations of sets from the 1970s, '80s, and '90s is focused on users who represent the 35-44 and 45-54 age ranges.
  - The sets will appeal to serious AFOL. 
    - Lego has never left their attention.
    - They may have "always wanted" a particular vintage set. In this case, the FullSet will be what they want, the ModernSet would be a bonus.
    - They may no longer have a bin of Lego to pull from to build consistent colorway MOCs, the ModernSet will be a main driver.
    - They may no longer have the old sets, and wish to share the iconic vintage sets of their youth from their childhood with their own children.
    - Their kids may be dissatisfied with the complexity of the vintage sets compared to contemporary Lego, the ModernSet will solve that.
    - The Fullset conveniently packages both sets in one, so that the customer can have both experiences.
    - These users may be dissatisfied with trying to find the vintage sets on eBay, or not willing to use Bricklink or other second hand Lego sellers.
  - The sets will appeal to casual Lego follower. 
    - The user may have children who are just beginning to play with Lego of their own.
    - They may be reminded of the old sets while in the Lego aisle at Target, and wonder where their old sets went, or why sets are so complex now.
    - They may have memories of Lego, or have memories of the Lego pack-in catalogs full of sets they never had as kids.
    - These casual users may want to remember the past, but not be serious enough to use or even know about BrickLink or other second hand, bulk Lego sellers.
- The iconic designs will appeal to any Lego enthusiast of any age.
  - The sets are designed with high play value.
  - The designs have been built in the real world.
    - This ensures that the builds go together properly.
    - The builds are stable and function properly - they will not fall apart during play, but can be disassembled when desired.
    - The real world look and style matches the appeal of the renders and photographed models.
    - The playability is maintained; it is not too difficult to put a minifig in a drivers' seat, and they fit where intended. In the end, these are play sets.
- The blending of old and new Lego designs, bricks, elements, and techniques will appeal to families wishing to play together.
  - Many adults are engaging with their children - and children engaging with their parents or caretakers - with games and toys.
  - Many vintage toys, particularly video games, may seem rudimentary and uninteresting to modern kids.
  - Lego bricks have remained standard since their inception in the 1960s.
  - Bricks Then Made Now intends to take advantage of that longevity by appealing to nostalgic adults and intereested children alike.
  - Kids may be dissatisfied with the complexity of the vintage sets compared to contemporary Lego. A modern recreation can help kids share the joy with parents or caretakers.

The choice has been made intentionally to use only genuine, high quality used Lego bricks and elements. While Lego has lost court cases allowing other companies to manufacture very similar bricks and elements, leading to a great many low quality imitators, there is no substitute for the clutch power and quality materials Lego uses. Lego can be procured in many ways. Estate sales, local bulk resalers, eBay, BrickLink and Lego Pick a Brick are all ways to get Lego bricks and elements. However, all these methods require considerable time commitments, and unless a user of those services is buying a great deal of Lego, pricing can be prohibitive and make it very difficult to get just the right bricks for a specific build. 

### Pricing

Bricks Then Made Now offers three levels of product to tailor the experience to the user.

- Instructions
  - Just the instructions and parts list.
    - A Lego hobbyist with a lot of brick, or particular purchasing savvy, can buy just the instructions and build with their own Lego. This also allows users to build in whatever colorway they like.
    - The instructions are also priced relatively low, encouraging a user to make a first purchase with BTMN. Referring to the site for downloads will allow BTMN to market new models to the customer.
- ModernSet
  - The instructions and all the necessary bricks to build the modern model.
    - The hard work has been done. Instead of scouring eBay, Bricklink, and the local Lego reseller's tubs of bricks, a user can get just what they need to build what they want.
    - The general target for serious buyers with new Lego sets is about $0.11 per brick, excluding minifigures. 
      - Current Lego sets hover around that, with a range of $0.06 to $0.19 depending on the size, complexity and printing.
      - Vintage Lego sets can vary wildly; the inclusion of parts that are no longer available (most usually in no longer available colors) can make a complete set scarce.
      - Bricks purchased in bulk can be had regularly for less than $0.15 per brick, with some outliers.
        - Bricks Then Made Now tries to build its sets with as many common parts as possible to keep physical item costs down.
        - However, some builds will require scarce parts; 2206357 Stunt 'Copter n' Truck for example, requires an uncommon beam and old style Technic skis, and specific printed doors.
        - Bulk purchasing will help keep the costs spread out across many models.
        - This becomes the real benefit for customers to use Bricks Then Made Now.
- FullSet
  - A limited availabilty package of the downloadable instructions, all the bricks included in the ModernSet, plus the vintage set it was based on.
    - A user customer will not have to build the modern model as a rainbow warrior, or hunt everywhere for just the right parts.
    - The user will also be able to collect the vintage set.
      - Vintage sets can be hard to build with all vintage bricks.
        - Many parts are no longer available in particular colors, or were only available in that color or printing in the one set.
        - Some parts are no longer made at all.
        - Some colors have changed - famously, Lego changed their grays in 2004. This can make it difficult to recreate or purchase a complete old set. A good example is Lego 6357 Stunt 'Copter N' Truck, even the BTMN office model didn't have all the gray parts in Light Gray instead of Light Bluish Gray until recently.
  - Some FullSets can be collectable in other ways.
    - 230CSMP Classic Space Plinth, for example, is a MOC and not based on a vintage set. A VERY limited availibility set could be offered as a FullSet, with all of the officially available Classic Space minifigs. These minifigs are very hard to source a group of - Purple, for example, has to be made from parts from several sets, some of which were uncommon and expensive even when new. And as a special collectable aspect, Bricks Then Made Now could work within the community, and collaborate with a company like Brick Sticker Shop to make a custom sticker sheet to decorate the plinth with custom desings, collector information, or with stickers so that a customer can make fully[custom color space minifigs](https://www.brickstickershop.com/Custom-Sticker-Classic-Space-Torsos) on their own, if they choose.
  - FullSets are necessarily a limited item, and this makes sense from a marketing standpoint as well. It can help drum up interest in sets, and pre-orders could be an option to making sure that more customers could get the FullSet since the in-stock numbers would likely remain low. 

Pricing for each set would need to not only be profitable but consistent. Many users are knowledgeable enough to understand why some sets are more expensive than others. For example, the 230CSMP Cassic Space Plinth is 122 very common bricks and elements while 2206357 Stunt 'Copter N' Truck includes uncommon parts like printed doors, a boom, and technic skis. Consideration has been made to try and keep the sets within the $0.12 to $0.15 per part range. Of course, the pot can be sweetened by including minifigs, which can be a great added value for customrs without much added expense for Bricks Then Made Now.

- Instructions are priced very low for small sets or set recolors. 230SPJr is only 8 parts, and the instructions are just there for downloading by anyone to purchases the ModernSet, or 2306530 Sport Coupe is essentially a recolor of an existing Lego set - the instructions are widely available including on Lego's official website - so the "instructions" are just a handy parts list. These instructions are intentionally inexpensive. Otherwise, instructions generally start at $2.99, and increase by $1.00 for every 100 parts in the set.
  - Since instructions are downloadable on the website, BTMN uses the instructions as a way to overcome a major objection with online stores. Most customers don't want to register an account. However, an account is necessary for customers to return and download isntructions without repurchasing them.
  - By giving away a free set of instructions, BTMN can encourage a user to sign up an account, which will make them more likely to return and purchase from the store.
- ModernSets are priced based on the cost of the parts required. Some sets will have a higher price per part than others, but all efforts are made to keep the sets under $0.15 per part, however that is a guideline more than a rule. Once the price per part target is met, the set is compared to sets available from Lego, and a determination is made wether the set can be priced higher, or if adjustments need to be made to price it lower to keep it in line with Lego's official offerings. This is primarily to meet customer expectations, Bricks Then Made Now cannot compete with Lego's global infrastructure and doesn't intend to anyway. Lego generally sticks with themes (truck and trailer, crane, sports car) as they develop sets, but rarely do they do direct modernizations of sets in nostalgic colorways.
- FullSets are priced based on the ModernSet and what a customer may expect to find a vintage set for elsewhere, because a complete vintage set can be difficult to find. Bricks Then Made Now has an advantage by being able to buy bricks and elements in bulk, but will encounter pricing for individual parts that effect the ultimate price for the fullset similarly to competitors. For example, Lego 889 Radar Truck adds a full $15.00 to the price of the 2300899:1099 FullSet over the 2300899:1066 Modernset even though it is only 29 parts. The scarcity of some of the parts in light gray - instead of light bluish gray - makes it more dear.

### Shipping

While Bricks Then Made Now is not competing with businesses like Amazon, the expectation has been set by the behemoth wholesaler that even small boutique shops offer free shipping. In line with that, Bricks Then Made Now calculated shipping into the cost of all physical items, and advertises as offering free shipping on all items, even though we all know that it's just rolled into the cost of the item anyway.

<br>
<hr>

## Technologies Used
<hr>

### Languages Used

This project uses four programming languages. 
- HTML
- CSS
- [Python](https://www.python.org/)
- Javascript

### Frameworks & Libraries Used

- [Bootstrap](https://getbootstrap.com/)
- Code Institute Gitpod Full Template - Available on request.
- [Django](https://www.djangoproject.com/)
  - [Allauth](https://django-allauth.readthedocs.io/en/latest/)
- [Django Countries](https://github.com/SmileyChris/django-countries)
- [Pillow](https://pillow.readthedocs.io/en/stable/index.html)

### Programs Used

- [AmIResponsive](https://ui.dev/amiresponsive)
- [Balsamiq](https://balsamiq.cloud/)
- [Bulk Resize Photos](https://bulkresizephotos.com/en)
- [Cloudinary](https://cloudinary.com/)
- [Color Contrast Checker](https://coolors.co/contrast-checker/)
- [Color Shates Online Generator](https://gradients.app/en/shades/)
- [Coolers](https://coolors.co/)
- [Elephant SQL](https://www.elephantsql.com/)
- [Favicon.io](https://favicon.io/)
- [GitHub](https://github.com/)
- [GitHub Issues](https://github.com/features/issues)
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [GitPod](https://gitpod.io/)
- [Gnu Image Manipulation Program](https://www.gimp.org/)
- [Google Fonts](https://fonts.google.com/)
- [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- [Gmail](https://mail.google.com/)
- [Heroku](https://www.heroku.com)
- [I(LOVE)PDF](https://www.ilovepdf.com/compress_pdf)
- [LucidChart](https://lucid.app/lucidchart/) 
- [MiniWebtool Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
- [PostgreSQL](https://www.postgresql.org/)
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/)
- [SQLite](https://sqlite.org/index.html)
- [Stud.io](https://www.bricklink.com/v3/studio/download.page)
- [Tables Generator - Markdown](https://www.tablesgenerator.com/markdown_tables)
- [TinyPNG](https://tinypng.com/)
- [XML-Sitemaps](https://www.xml-sitemaps.com/)

<!--Frameworks unused so far (Copy Past above as used)

- [Code Institute Python linter](https://pep8ci.herokuapp.com/)
- [Markup, the native Android photo editing tool](https://www.android.com/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)

-->

<br>
<hr>

## Local Development and Deployment
<hr>

### Local Development

Information on local development can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

### Deployment

Information on deployment can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

### How to Fork or Clone

Information on how to fork or clone the repository can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

<br>
<hr>

## Testing
<hr>

Information on testing can be found in [the testing ReadMe](/TESTING.md)

<br>
<hr>

## Credits
<hr>

### Help and Support

- Code Institute Full Stack lessons for the bulk of the understanding about Django, Bootstrap, and other frameworks. [Code Institute](https://codeinstitute.net/ie/)
- Code Institute instructor Simen Daehlin for almost everything else. [Simen Daehlin Github](https://github.com/Eventyret)
- Code Institute mentor Jubrile Akolade provided guidance on where to focus time building the project and an almost infinite amount of other support.
- All of my Code Institute UCD July 2022 cohort, who have been available to answer questions through Slack.
- Code Institute tutors accessed through the Code Institute LMS have been helpful with understanding various concepts during instruction.
- An explanation about how to have Django/Pillow upladed image files go to a specific folder was found [here.](https://youtu.be/O5YkEFLXcRg) The [Django documentation](https://docs.djangoproject.com/en/4.2/topics/files/) could have been a lot clearer about WHERE the example code goes, which is a frustrating aspect throughout working with Django.
- Big thanks to [Lego](https://www.lego.com/) for having a toy that allows a tremendous amount of aftermarket and web based support, and for just being pretty rad.
- A tremendous amount of Lego research was done on [Bricklink](https://www.bricklink.com/v2/main.page) and [Brickset.](https://brickset.com/sets/6301-1/Town-Mini-Figures)

### Code Used

- The button used throughout is a modified version of Button 13 from CSS Scan's [page of example buttons](https://getcssscan.com/css-buttons-examples), which is in turn attributed to Amazon.
- The countries dropdown menu in the checkout form is by Chris Beaven and can be found [here.](https://github.com/SmileyChris/django-countries)

### Media

- Favicon is "Four Brick, Lego, Blue, Toy, Four" as provided by [ClipArtMax.](https://www.clipartmax.com/middle/m2i8d3Z5H7i8G6i8_four-brick-lego-blue-toy-four-api-icon/)
- Fonts are [Vina Sans](https://fonts.google.com/specimen/Vina+Sans) and [Staatliches](https://fonts.google.com/specimen/Staatliches) for the Bricks Then Made Now logo and [Mina](https://fonts.google.com/specimen/Mina) for the text, the code provided by [Google Fonts.](https://fonts.google.com)
- The original image used as the basis for the splash image is from [Brickset.](https://brickset.com/sets/6301-1/Town-Mini-Figures)
- The rest of the images used for the "Old set" in the item listings are also from [Brickset](https://brickset.com/), from each set's Brickset listing. Some images were modified to fit the screen.
- All computer generated Lego renders are done in [Stud.io.](https://www.bricklink.com/v3/studio/download.page)
- "Scooty Puff Jr" model is named for a [Futurama](https://www.imdb.com/title/tt0149460/) gag, and is based on a simple design by [troublesbricking.](https://www.instagram.com/troublesbricking/).
- The Lego Dennis Nedry mocking .gif image is from Lego set 75932 Jurassic Park Veloceraptor Chase, the image is from [Bricklink](https://www.bricklink.com/v2/catalog/catalogitem.page?P=75932stk01&C=0#T=C&C=0)
- The "No image available" placeholder image is from [Stock Adobe.](https://stock.adobe.com/)
- Terms of service is sampled from [www.websitepolicies.com.](https://www.websitepolicies.com/blog/sample-terms-service-template)
- The Privacy Policy was generated by [Privacy Policy Generator.](https://www.privacypolicygenerator.info/)

### Other Thanks

- The Code Institute tutors. This must be mind-numbing.
- The Code Institute assessment team; I can't imagine what kind of patience and knowledge it would take to look over these projects without losing it.
- Thanks to F. D. C. Lemon-Beckett for useful contributions to the discussion.
- Finally, heartfelt appreciaton to my partner, Stevie, for infinite patience and encouragement. 
<br>
<hr>
For educational purposes only.