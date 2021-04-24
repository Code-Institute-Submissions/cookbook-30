# Cogi 

## Contents

* User and Site owner goals, Data schema and planning
* UX Design and planning
* Testing and compatibility
* Deployment
* Credits 
---
![alt Mockup](/static/images/readme/mockup.jpg)

I have created a data centric and interactive website for a fictional food company, Cogi (which translates to ‘to cook’ in Welsh), that allows a user to view recipes submitted by other users and themselves, register and log in and out, and registered users can create, view, update and delete their own recipes. Registered users are also able to publish comments on any recipe meaning they can see how popular, successful or obtain other feedback on a recipe. View the live project here [Cogi Cookbook](https://cogi-cookbook.herokuapp.com/)

The Website is fully responsive and uses Mongo DB to hold a users collection, a recipes collection and a comments collection. The comments use the recipe ID to link to that recipe page only. Any user (logged in or not) can search for recipes using the search box which is a text search on recipe names, keywords, tags and ingredients. 

Each recipe card in search results can be clicked onto and that will load the single recipe page which shows the entire recipe entry. If the logged in user created that recipe they will see buttons to be able to edit and delete the recipe.

Main Use case: Browse and search for recipes a user wants to recreate.  

External user goal: The site’s main users, and derived from the main use case, are for users looking to search for and view a recipe. They can register to use the site as a space to add their own recipes and view, update and delete them as the user sees fit.  They are in the demographic of young professional to older person that may not be a digital native or tech savvy. This means the site should be intuitive and give clear feedback on user’s interactions.  

Site owner/business goal: More recipes on the site means more users searching and clicking. The brand wants to increase users viewing recipes and registration and use the site for their own recipes. The brand wants the site to be lucrative and includes links to cooking homeware, where clicks and purchases to third parties result in a profit for them. More users on the Cogi site means more potential homeware purchases. They want the information to be clear and intuitive and the site to be a friction-free experience. 

---

## User and Site owner goals, Data schema and planning

### Navigation and Landing Page 
The site’s homepage has a search index of recipes, with links to register or log in. The search searches the database on recipe title, ingredients and tags, the idea being the user will search for keywords such as ‘Italian’, ‘vegetarian’ etc. The menu options take the user through the key sections of the site and change if the user is logged in (they have the option to add a recipe and log out for example). I have created the site with conventional global navigation to suit the multiple user demographics and technical capabilities, as its better to stay within convention for intuitively. The navigation is responsive and at small devices includes a slider menu to make room for the website content. 
The homepage includes a brief text about the company and their mission and links to external third-party cookware for sale. 
### View Recipe 
When a user clicks the view button on recipe card, they are taken to a recipe page which displays, the title, an image, the time taken for recipe creation, tags for similar themes, ingredients, and method. 
From benchmarking, these are staples of a recipe and should be on any recipe page. There is purposefully a lot of white space so the recipe instructions are easy to follow with no visual distractions on the page. 
### Add a Recipe
Only a registered and logged in user can add a recipe. If a non-registered or non-logged in user clicks ‘Add recipe’ they are redirected to the register page where they can register or log in. This is so the site can gain more registered users. 
### Edit a Recipe
Users can update recipes that they have created, and only the creator of that recipe can edit it so it is defensively programmed. They can do this from the recipe cards on their profile or from recipes displayed on the wider search. It has been defensively programmed so only the creator of the recipe can edit it.
### Delete a Recipe
A user can delete a recipe and on delete are asked if they are sure they want to proceed – to mitigate any potential accidental deletes.
### Add comments
Registered users can comment on any recipe regardless of who created it. This is so the site offers members to create a dialogue on a recipe and build that community. If a user attempts to comment without being logged in, they are redirected to do so. 
### Search 
The search function has been created with a text index on the recipe collection, on recipe names, ingredients, and tags as per common recipe searches use cases with users searching by a key word or ingredient to generate ideas. The recipe card click actions are different on a profile than on the all recipes search. This is so a creator of that recipe can see which is theres from the edit button, and for consistency have kept a view button in line with an edit button. 
If there are no search results, a flash messages displays notifying the user and offers to add a recipe – a subtle UX trick to aim for increased recipes and engagement. 
### Data Schema
3 collections were created using a non-relational database MongoDB; recipes, users and comments. Comments includes the recipe ID so that comments about a particular recipe are shown on the page. 
### Register, Log in and Out 
Users can register, log in and out securely. 
### Profile 
When logging in a user is taken to their profile page, with a welcome flash message and shown the recipes that they have created. 
### Footer and links to homeware 
Each page has a footer with contact details of the company and social media links that open in a new tab. 

All CRUD actions have been manually tested and checked in the database to ensure they are saving correctly which they are. This was done throughout development to ensure the data types were correct and code was written correctly. Users were asked to add their own test recipes to ensure it was fully usable.

---
## User Experience (UX)
* Strategy Plane

Value provided:

The site shows recipes created by registered users that are searchable by any user and viewable. A registered user can create, update, delete or view their recipe. Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.

The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner would also benefit from the collection of the dataset as a whole. 

The site is responsive as more than 70% of users initial browse and search the internet via mobile phones and has been designed with a mobile first approach. When cooking 59% of people use a smart device to find and view a recipe, therefore the site has been designed with this in mind, the recipe view page is clear and easy to follow on all devices. 

[The Digital Kitchen Trend](https://www.thinkwithgoogle.com/future-of-marketing/digital-transformation/cooking-trends-among-millennials/)

The age of the demographic is varied and will include many who might not be particularly tech-savvy. The site has been made so that it is very intuitive with global navigation and clear call to actions so the user can navigate through creating, viewing, updating and deleting a recipe. The design is simple with the key elements easy to find. The text through the site explains the companies offering, how to interact so it’s all there for users. 

Competitive Benchmark: 

What is the companies USP? 

I compared several large online recipe sites to compare the way they work with input data allow users to view recipes and if they allow users to create, edit and delete their own how they visually displayed their recipes and collections from a UX and UI perspective. 

[BBC GoodFood](https://www.bbcgoodfood.com/recipes)

BBC Good Food it the ultimate recipe browsing and finding tool. Its landing page it topical to season (Eg. Summer – BBQ meals) and allows a user to search by ingredient or keyword. The search results are shown on individual cards that contain a recipe image, recipe summary, prep time and difficulty level. They are key indicators that give a user a quick over view if its something they want to recreate themselves. The recipe page itself is very informative and includes nutritional advice, links to buy ingredients from online stores, method and ingredients displayed well. There are a lot of adverts around the recipe that over populates the page, there is not a lot of whitespace and feels very busy. Currently BBC Good Food does not allow users to add their own recipes when registered, although this is a feature the site says that they are working on including. This will be an important feature of this Cogi website development. 

[BigOven](https://www.bigoven.com/)

BigOven has a large search function call to action on landing page. The site contains a lot of large inviting imagery and visually is very pleasing. There is a lot of whitespace around the recipe cards and feels easy to navigate. As you scroll down there are images that animate on hover suggesting on click you find further information about the recipe categories. Their individual recipe pages are much easier to read than BBC Good Food as they are less busy and have lots of space making the instructions and ingredients very clear. Underneath the recipe they include links to similar recipes to keep the user clicking through the site. BigOven allows users to sign up and create, edit and delete their own recipes. 

[ChefTap](https://cheftap.com/)


Cheftap is aimed at amateur home cooks. Its an app for iOS and andriod rather than a responsive site however it’s design quick, intuitive and easy search function for recipes. It allows users to create, edit and delete their own reciepes. This use of data manipulation for a user is a strong feature of these sites. 
	
[Paprika App](https://www.paprikaapp.com/)

Paprika App, like the ChefTap is an iOS and android application only and is much more up market, it has elegnent imagery and font but is pricey at £30 for users. The business owner’s goal here is different to what Cogi’s will be. They will gain profits when a user joins, whereas Cogi will profit when a user clicks a homeware link. This app is designed for very frequent users who are more than an amateur home cook. 

From this brand comparison, it is apparent that the most common use case is searching for recipes by keyword or ingredient and viewing it. Following, it is for a user to have an account and to create and save their own recipes for viewing again later. Users must also be able to edit/update and delete their own recipes as they wish.

Key tasks/cases for the site are as below in this strategy trade off: 

|   | Features | Importance | Viability |
| :-: | --------------------------------- |:-------------:| :--------:|
| A | Search function for recipes by keyword or ingredient | 5 | 5 |
| B | View recipe page with method and ingredients | 5 | 5 |
| C | Information about the Cogi brand | 5 | 5 |
| D | Secure user registration and log in and out functionality | 5 | 5 |
| E | Ability to create, read, edit and delete recipe | 5 | 5 |
| F | User profile with a list of own recipes | 4 | 4 |
| G | Follow along videos | 3 | 1 |
| H | User comment on recipes functionality | 3 | 3 |
| I | Dashboard of recipe statistics | 2 | 2 |
| J | Advertise cookware products | 4 | 4 |
| K | Include links social media food content influencers | 2 | 2 |
| H | User ability to save and/or like recipes | 3 | 2 |
|   |  *Total* | 49 | 43 |

As the importance is higher than the viability this is going to work. The features that are that are the most important and achievable are: 

* | A | Search function for recipes by keyword or ingredient 
* | B | View recipe page with method and ingredients 
* | C | Information about the Cogi brand 
* | D | Secure user registration and log in and out functionality
* | E | Ability to create, read, edit and delete recipe
* | F | User profile with a list of own recipes
* | H | User comment on recipes functionality
* | J | Advertise cookware products

With the other features as possibilities for future iterations and releases. Follow along videos, likes and saves and dashboard statistics are not viable at this time. 

From the point of view of the user, they expect to have a clear, consistent, and professional website that allows them to easily find a recipe by keyword or ingredient, view and follow its instructions. They want to be able to write their own and come back and view it as they wish and share it with other members. 

Navigation should be intuitive and simple. Global navigation will be used for conventionality and therefore intuitive. Key use cases such as adding, editing and deleting a recipe will have clear call to actions as well as being a part of the navigation. 

Registered users will be able to comment on recipes. The idea being that users viewing the recipe will be able to partake in discussions, suggesting tips and feedback of their experience of the recipe. 

Information about the brand and its recipes will be included. Links and images of external brand cookware will be included as the site owners means of making the site feasible. This will also add to make the brand appear trustworthy by affiliation. 

* Scope Plane

Based on the strategy plane, the key features that are the most important for users and the most achievable are providing information about the brand and the service, a search function that allows a user to browse particular recipes by keyword or ingredient such as ‘Lasagne’, ‘Cheese, ‘Vegan’ or ‘Snack’. These are the key word examples that the recipe creators are most likely to include in their recipe name, ingredients, and tags. The results are shown on cards that give a little information on the recipe, which the user can then click into to view a recipe page. Users can register, then create, edit, and delete their own recipes, and thus log in and out thereafter. Registered users can comment on recipes and form a dialogue. Redirects have been purposefully created so that if a non-registered user selects ‘Add a recipe’, they are taken to the registration page to prompt the user to register/or log in. Likewise, if an unregistered user tries to add a comment they are redirected to registration. This feeds into the site owners goal of increasing users. 

The site needs to appear trustworthy and intuitive. It wants to be as helpful and knowledgeable as it can to users by enticing new users, being easy to use for return users so that the number of recipes increases. The company requires a website that expresses its professionality, reliability and trustworthy. 

The website must be a clear showcase of the brand. It should have contemporary features and aesthetic that appeals to home and amateur cooks. 

* Structure Plane

Of the key elements that were determined important, they should be put in this logical order on the site: 

* Information about the brand’s service
* Search function for recipes 
* Recipe cards with clickable ‘view’ links  
* Ability to register/log in 
* Profile
* Ability to create, edit and delete own recipes  

The main page will be the landing page with search function and recipe cards. This top navigation will have links to register/log in, and once logged in to add recipes. A user will have a profile page, where they can view their own recipes as a list and update or delete as needed. 

Evolving from the Structure plane, the about information will be in text and a brief explanation of the company’s mission. 

Edit and delete buttons will be near each other although distinguishable as they are closely related. Recipe cards will be together on the main page as well as the user’s profile. 

Feedback will inform the user if they have not completed the add recipe form-fields validly or if they are missing a required field. When the user submits, a message appears advising the recipe has been created and they are redirected to the main recipe page giving the user feedback that the recipe has been successfully created. 

Buttons and links change visual style on hover, so that a user knows it is actionable.

For the links that lead to an external page (e.g social media or amenity websites) will open in a new tab, so the user will not be navigated off this site with the ability to return. 

Links to external cookware products will be included. 

* Skeleton Plane 

Figma has been use d to design the layout. My wireframes can be viewed here: 

![alt Wireframes](/static/images/readme/wireframes.png)

The user actions and recipes will each have the same visual style for consistency. They will have the same colour theme, the same typography, and a similar percentage of content and whitespace, padding and margins. Components will have enough space around them to breath and remain digestible for users. 
It will be designed responsibly, mobile first, so that these components are visually consistent across devices but suitable for that screen. 
The final design is an iteration from the original wireframes. 

* Surface Plane 

A subtle colour palette has been deliberately used so the recipe cards have sufficient white space around them. Text, links, and navigation have consistent colours and the typography is too. 
Design decisions are discussed further below. 

Headings, text, images and components are designed with a relevant size to work in harmony and to be sufficient in their own right. 
Sources of design research came from Dribble, Pinterest and UXPlanet as well as competitor brands. 
[UX Planet – Family recieps](https://uxplanet.org/roots-creating-a-platform-that-keeps-family-recipes-alive-5e747aae30b2)

### Design and UI

The initial design was created in Figma, with small iterations as it was built and tested as seen in the Skeleton section of this document. 

A subtle colour palette has been deliberately used so the recipe cards have sufficient white space around them and the navigation stands out. The landing page image has been purposefully chosen as a minimal image with lots of white so the other elements stand out, the chopping board links to wanting to cook. Text, links, and navigation have consistent colours, change on hover and the typography is too. 

### Typography
I used Google Font’s ‘Poppins’ as it is contemporary and stylish. Its lightweight, thin characters compliment the website aesthetic and work for titles as well as text. It’s sans-serif characters are legible and modest. I used a light font-weight too to compliment that contemporary aesthetic. 
Different font sizes were used for the various heading types (H1, H2..etc) and text as hierarchy dictates. 
### User stories 
First time user goals: 
* I want to search for a recipe and follow it
* I want to add my own recipe 
* I would like to create an account and register

Returning visitor goals: 
* I want to add and view my recipes when I want to
* I want to connect with other users and comment on their and my own recipes to give suggestions, feedback and form a dialogue 
* I want to log in securely 
* I want to search for other members’ recipes and try them

### Features
The key features of the site are search for and view recipe, register, log in and out, create, update, delete a recipe and add comments. 
Note purposefully added 'add recipe; on main home page with register link to increase click rate and users.
### Features to implement 
As per the UX strategy scope, I think the site would be improved with follow along videos, likes and save ability, further password security. This would require further time to implement. I would also like to have users take their own photo and upload an image of their meal as a file for better UX. 
* Extra security at log in and out with a second password request at registration. Forgot and reset password prompts 
* Search function on user profile (only currently on all recipes)
* Search function results not ordered – future release could be alphabetical or by most viewed 
* Pagination on recipe pages for comment history
* Pagination on recipe search pages
* Prep time input is text – future release could be a range picker 
* Users could edit or delete their own comments – would need to check security breaches
--- 
## Technologies 
### Languages 
* HTML5
* CSS3
* JavaScript
* Python
* Flask
* MongoDB
### Frameworks, libraries, and software used
* Google Materialize
* Google fonts
* Font Awesome 4.7.0
* Google Material Design
* Figma
* jQuery
* Git
* GitHub
* GitPod
* Chrome DevTools
* Lighthouse
---
## Testing
### Functionality 

All CRUD actions have been tested on the site and in the database by myself and some test users. The informtion saves correctly in the database and is visable on the site correctly via the db.

All navigation, create recipe, edit, delete, log in and out and registration links have been checked and they all work correctly. 

Social media and third-party links all take the user to a new tab and have been checked. 

The scroll functions smoothly and the site has been tested for responsivity using DevTools. 

I created and tested a 404 error page using a recipe ID from a deleted recipe and works correctly. 

The HTML and CSS were validated with [HTML Validator](https://validator.w3.org/)  for each page via link and [CSS Validator](https://jigsaw.w3.org/css-validator/) for the CSS file.  

HTML: errors found and rectified throughout. These included misaligned div containers, heading hierarchy and the link to the phone number in the footer.

CSS: found no errors.  

I tested JavaScript while compiling using console.log to check if the code and functions were being called correctly. 

### User Story Testing

The site has been tested on multiple device types and asked others to test it too. 

Testers were able to intuitively search for and view recipes and/or register or log in and add, edit or delete their own recipes. They understood the legible text and how to navigate through the menu.

First time user story testing:
* I want to search for a recipe and follow it

Users (registered and non-registered) can visit the homepage and search for a recipe immediately by recipe type, keyword or ingredient. From the results they can click to view a recipe on its own page. This shows an image, the prep-time, ingredients, method and any comments members have written about the recipe.
* I want to add my own recipe

There are many ‘add recipe’ call to actions where a registered user can add their recipe, or a non-registered user is taken to the registration page and from there can add a recipe. The user can fill a form and populate full recipe details and view, edit and delete it. 

* I would like to create an account and register

From the main menu a user can register and create an account. They are able to create a unique username and a secure password. When registered and logged in they are taken to their profile page which holds an add recipe button and recipes they have made. 

Returning visitor story testing: 

* I want to log in securely 

Users can safely log in securely as it has been built using the password hasher. Their usernames are unique. 

* I want to search for other members’ recipes and try them

All recipes can be searched for on the main homepage search function. From there they can click and each recipe is shown on one page. 

* I want to add and view my recipes when I want to

Users can register and create an account and add and later view their own recipes. 

* I want to connect with other users and comment on their and my own recipes to give suggestions, feedback and form a dialogue 

Each recipe page has a comment section so users can write their thoughts and feedback and create a dialogue. 

### Compatibility Testing
Testing the accessibility with [Wave]( https://wave.webaim.org/) showed showed that the view buttons on recipe cards need to be more contrasting. It also notes that some heading sizes have been skipped this is because of the base template and what is needed on individual pages. 
I tested the website on multiple browsers:
* Chrome
* Firefox
* Internet Explorer
* Safari
It was also tested on multiple devices through Chrome DevTools with various mobile, iPads, tablets up to large screen monitors. 

### Performance testing 
I used Google’s Page speed [Google page speed](https://developers.google.com/speed/pagespeed/insights/) to test the site speed for desktop and mobile, and used Google’s mobile friendly tester [Mobile tester](https://search.google.com/test/mobile-friendly)to determine it’s mobile performance level.

![alt Desktop speed](/static/images/readme/desktopspeed.JPG) ![alt Mobile speed](/static/images/readme/mobilespeed.JPG)

It works well on desktop but at a slower speed on mobile. This is due to unused Materialize CSS and jQuery. 

It has been deemed however to be mobile friendly for the time being. 

![alt Mobile Friendly](/static/images/readme/mobilefriend.JPG) 

In using Google Lighthouse – 

![alt Google Lighthouse desktop](/static/images/readme/desktopperformance.JPG) ![alt Google Lighthouse mobile](/static/images/readme/mobileperformance.JPG)

Lighthouse suggested using the rel=noopener attribute on external links for security which I have added. Mobile performance would improve without unused Materialze CSS and adding a meta description will improve SEO rate. 

### Bugs 

Bugs were picked up and tested throughout development. 

* Timezone is GMT and therefore behind an hour for the current time (BST!). 

* I tried to create add_comment functionality within the recipe method however I could not so I created its own add_comment method. This took a few iterations to correctly work within MongoDB. 

* There was a logical bug in CSS which caused a misalignment of the index page, but it has since been centered. 

* Tags – any more than 2 tags per recipe card skewes up the order and size, so I have included a for and if loop so only 2 appear. 

* The image sizes on recipe cards are forced to fit using CSS, depending on the users choice of image this may crop or cut unsightly. 

* Image url takes a string and has no web address check or validation 

--- 
## Deployment 
### GitHub and Heroku

A MongoDB database was used and setup inside Heroku. The details of the database connection are found inside the requirements.txt - it uses the os class environ method to point Heroku to its own config variable (MONGOBD_URI) in order to keep the production database connection string secret.

A Procfile is also used to help Heroku know what commands are run by the application and how to run various pieces of the app including the starting point app.py

Heroku's deployment from Github repository function was used to deploy.

Upon the app running I then manually loaded the database using the 'add recipe' functionality.

--- 
## Credits
Images
* Landing page: https://unsplash.com/photos/29h2n639YDA
* Image URLS are input by users for each recipe card. 

