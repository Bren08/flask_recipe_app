# My Recipe Cookbook - My Third Milestone Project 

The website that I have developed here is a multiple page website with full CRUD functionality as was requested. You can Create (add), Read (view), Update (edit) and Delete within the confines of the website. I have used the skills I've learned in previous modules and currently the Data Centric Module to create a Flask Website which utilises a MongoDB database to handle back end data and Python, HTML and CSS code to also handle the back end functionality and front end functionality, as well as styling the front end.<br>There is also a search field to search through recipes. You can search by just typing any keyword that might be attached to any recipe, whether its an ingredient, a way of cooking or even a food category, for e.g. Breakfast, Lunch, Dinner, Dessert or even the humble Snack.<br>So in essence the user has full functionality to view, add, edit, or delete a recipe within the website. The project can be viewed here <a href="https://flask-recipe-app.herokuapp.com">https://flask-recipe-app.herokuapp.com</a> 

## UX
<hr>

Firstly, let me direct you to the UX directory above where you will find the Strategy, Scope, Structure and Skeleton (wireframes).

This website is an online Recipe Cookbook and is fully operational in it's current state. The site gives the user the ability to search a recipe by typing a keyword into the search field, view a recipe, add their own recipe, edit their own recipe or even edit somebody else's recipe (at the moment there is no login required to use these features, see <strong>Features</strong> section below for more information) <br>
On the home page each recipe uses a card-style information container, which contains an image of the recipe and a short description. There are Edit and Delete buttons under each recipe on show, so the user can locate and utilise these functions as they see fit. The edit and add pages are very user-friendly and just need input to either add your own recipe or edit the same recipe after it is submitted.<br>
Once the user has chosen a recipe to view, the recipe will open up on a new page showcasing an image (if uploaded from a URL) &amp; a list of the content which has been inserted for e.g. recipe title, ingredients, method etc.
To gauge popularity, each recipe has it's very own view counter which will tell the user which recipes on show are the most popular.

## Features
<hr>

First and foremost we have a very minimal aspect to navigate through. On the home page there are three links, Home, Add Recipe and Dashboard.
<ol>
<li><strong>Home:</strong> From anywhere on the webpage from the sticky navbar to the footer section, the home link can be found, clicking this will automatically take you back to the main viewing page. On the main viewing page is where most of the functionality occurs. Here we also have: 
<ul><br><li>Search:<br>There is a search function by way of an input field just under the main header. The user can type in a keyword to find their selection within a given recipe, whether that be to check for certain ingredients because of allergies or just their own preference/favourite ingredient or even their dislike of an ingredient, the user can search here to save them some time.</li><br><li>View an individual Recipe:<br>From here the recipe is displayed in a card styled container, when the image or hyperlink is clicked the recipe chosen opens up on a new page for the user to view, the option to edit and delete is also available from here too. When each recipe is viewed the view counter is updated and increases by one, this can show how popular a recipe actually is by how many hits it gets.<br><br>
</li>
<li>Edit Recipe:<br>From here the user can update or edit an existing recipe.<br><br></li>
<li>Delete Recipe:<br>From here the user can delete an existing recipe. When they choose this option, before the operation is complete a modal will pop up asking them "are they sure they want to delete", this can stop a deletion if it was done in error, it gives the user the opportunity to cease the action.</li><br></ul></li>

<li><strong>Add Recipe:</strong> This function allows the user to insert their very own recipe which adds the users data to the database when it is submitted, this in turn, is then transferred to the main viewing page for all users to see.</li><br>

<li><strong>Dashboard:</strong> I have added a dashboard page just for aesthetics but I have not wired it up to get any relative data from the information that is provided to the database in MongoDB.</li></ol>

### Future plans include:

<ul><li>To create a secure username, password login, sign-up &amp; registration page so as to gain full access to the Edit or Delete your recipe functionality of the website, this will give the end user more peace of mind that their data they enter is safe and secure. It will give added confidence and maybe entice more users to try out My Recipe Cookbook.</li><br>
<li>There is also an online cookery utensils/equipment store currently being devised and we hope to have that up and running within a few weeks, alongside the login/registration entry criteria.</li></ul>

## Database Structure
    recipes: {
    _id: 5d51ff781c9d4400001efb6d
    img_url: "https:goodhousekeeping.fetcha.co.za/  wp-contenuploads/2019/03/beef-stroganoff.jpg"
    recipe_category: "Dinner "
    title: "Beef Stroganoff "
    ingredients: "string"
    method: "string"
    nutrition: "string"
     cooking_time: "40 mins "
    author: "string"
    views: 108
    }
    
    categories: {
    _id: 5d2d0a381c9d4400002da8f0
    category_name: "Lunch "
    }

 ## Technologies Used
 
 ### Frameworks, Libraries, Languages:
 <hr>

 <ul><li><a href="https://www.w3schools.com/">HTML5</a> was used as the mark up language for the website.</li>
 <li><a href="https://www.w3schools.com/css/">CSS3</a> was used to style the website.</li>
 <li><a href="https://getbootstrap.com">Bootstrap</a> and <a href="https://materializecss.com">Materialize</a> were the frameworks used for the layout.</li>
 <li><a href="http://archives.materializecss.com/0.100.2/icons.html">Materialize Icons</a> were used for the icons.</li>
 <li><a href="https://code.visualstudio.com">Virtual Studio Code</a> was the editor used.</li>
 <li><a href="https://git-scm.com">Git</a> &amp; <a href="https://github.com">GitHub</a> were used for Version Control.</li>
 <li><a href="https://www.mongodb.com">MongoDB</a> was used as the NoSql database for the storage of user data/recipes.</li>
 <li><a href="https://www.python.org/downloads/">Python3</a> was used to compile and utilise the logic for the project.</li>
 <li><a href="https://jquery.com">jQuery</a> is a JavaScript library which was used for event handling.</li>
 <li><a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja2</a> was used as the templating language for Python.</li>
 <li><a href="https://flask.palletsprojects.com/en/1.0.x/">Flask</a> is a Python web framework used for developing web apps.</li>
 <li><a href="https://www.heroku.com/">Heroku</a> This is a cloud platform where the project is deployed to.</li>
 </ul>

 ## Testing
<hr>

 Each area of the website has been tested and it seems to work well on all viewports from desktop to mobile. The user should be able to achieve their goal as the site intends, depending on whatever they choose to do when they visit.<br>I have used Dev tools in Google Chrome to test the responsiveness of the website and it appears to render well.<br>Each link is working as it should within the navigation bar and the footer then takes you to where you require to go to. Within the search function when you type in a keyword, or several keywords, you get the result back that you requested. It will return a result for the keyword that was entered and as it finds a match in as many recipes as it possibly can.<br>Each button is functioning as it should from the search bar to the edit and delete buttons. When the delete button is activated the modal created works well and flashes up a warning asking you if you intend to go ahead with your request, before the deletion takes place.<br>
 The edit and add recipe sections were tested and they perform well, a recipe that is added through the front end to the back end gets transported to the MongoDB database for storage and when that recipe is requested back again for editing, it can be edited and the after editing it populates the main viewing page (the home page) for viewing.
 Furthermore, I have used <a href="https://validator.w3.org"> W3C Code Validator</a> to verify there are no errors in my HTML or CSS. I have tried to keep the code as semantic as possible too. I have tested the website on Google Chrome, Edge and Android, so it is not tested on Safari and IOS.

 ## Deployment
<hr>

 The project is deployed on the Heroku Cloud Platform  by using a local Git repository linked to Heroku. A MongoDB database was utilised and setup inside the Heroku platform. Credentials of the database connection are inside the requirements.txt file, it uses the os environ method to tell Heroku to look inside its own config variable (MONGOBD_URI) in order to make sure the production database connection string is not on-show and kept secret.<br>
 A Procfile is required, it is a text file named "Procfile" placed in the root of the application that lists the process types that are needed in an application. 

## Credits
<hr>

### Media:

Most of the recipes and images are taken from <a href="https://www.goodhousekeeping.com/food-recipes/">www.goodhousekeeping.com</a> 

### Disclaimer:
*This project is for educational purposes only*

## Acknowledgements
<hr>

I would like to thank everyone on the Code Institute Tutor team, the Slack Channels and most of all my mentor Spencer Barriball, who has directed me in the right direction on every topic we discussed regarding my project.
