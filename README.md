## Introduction

Minimalist Reading is a web application created for my Milestone Project Three at the Code Institute.
The project was inspired by an article posted on['The School Of Life'](https://www.theschooloflife.com/thebookoflife/how-to-read-fewer-books/)


Minimalist Reading is designed to be a responsive and accessible web application, making it easy to navigate for potential users on a range of devices.

Click the link below to run my project in the live environment:

[Minimalist Reading](https://minimalist-reading-ms3.herokuapp.com/)

### Project Purpose 

  **Build a book review and recommendation site**

1. External user’s goal:
   Find books they would like to read.

2. Site owner's goal:
   Earn money on each book purchased via a link from the site.


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.
        3. As a First Time Visitor, I want to locate the social media links to stay connected with the site.

    -   #### Returning User Goals

        1. As a Returning User, I want to check to see if there are any newly added book recommendations.
        2. As a Returning User, I want to check to see if there are any newly added features to the site.
        3. As a Returning User, I want to be able to edit and delete my submission.

     -   #### Site Owner Goals
        
        1. As a site owner I want to earn money on each book purchased via a link from the site.


-   ### Design
    -   #### Colour Scheme
        -   The three main colours used throughout the site are white, grey and black.
        -   The site is based on the ideas of Minimalism and so a simple colour pallette was chosen to keep things crisp and clean.
    -   #### Typography
        -   Clean, modern and minimalist.
    -   #### Imagery
        -   The main image for the site is a large,background hero image.
        -   The image of a girl reading a book with a sunset backdrop is designed to reflect the minimalist aesthetic which ties in        with the purpose of the site.

*   ### Wireframes
    -   I drew the Wireframes for this project as I find drawing them allows for more detailed notes as well as being a more efficient     use of time.

    -   Home Page Wireframe - [View](https://github.com/jmurrii/MS3/blob/master/static/img/wireframe-index.jpg)

    -   Mobile Wireframe - [View](https://github.com/jmurrii/MS3/blob/master/static/img/wireframe-mobile.jpg)

    -   Submit Page Wireframe - [View](https://github.com/jmurrii/MS3/blob/master/static/img/wireframe-submit.jpg)

    -   Browse Page Wireframe - [View](https://github.com/jmurrii/MS3/blob/master/static/img/wireframe-browse.jpg)

## Features

-   Responsive on all device sizes.

-   Submit, Edit and Delete operations to manage book recommendations.

-   About page with link to article which inspired the project plus clear instructions on how to proceed.

### Future Features 

 # Login System
- A User Login System would open up the possibility of users being able to login and edit their uploads securely.

 # Chart System
- When enough users have submitted books to the site I would like to implement a chart system recording the most popular books. This     would enhance the user experience and make the site more useful.

 # Upload Image with Book Submissions
- Providing the possibility to upload an image/link to the book cover would make the site more visually appealing.



## Technologies Used

- Design: Photoshop, Logomakr, GoogleFonts, FontAwesome
- Frontend: HTML, CSS, JavaScript, Bootstrap, 
- Backend: Python, Flask, PyMongo, Jinja, 
- Database: MongoDB
- Hosting: Heroku
- Version Control: Git, GitHub

## Testing


### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.
- [view](https://github.com/jmurrii/MS3/blob/master/documentation/PEP8%20Validation.png)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page      of their choice. 
        2. Underneath the Hero Image the site's philosophy is written in clear unobstructed font.
        3. How to use the site is then condensed into three easy to follow cards.

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has a clear, simple Navbar fixed to the top of each page.  This makes it easy for the user to navigate to any destination on the site at any time.
        2. The main cards on the homepage also provide links to the other pages on the site giving the user more options.
    

    3.  As a First Time Visitor, I want to locate the social media links to stay connected with the site.
        
        1. The user can also scroll to the bottom of any page on the site to locate social media links in the footer.
       

-   #### Returning Visitor Goals

    1. As a Returning User, I want to check to see if there are any newly added book recommendations.

        1. New user recommendations are added to the Browse page making it easy for users to search through the database.
        

    2. As a Returning User, I want to check to see if there are any newly added features to the site.

        1. New features such as a user login will be added to the Navbar making it easy to see for returning users.
        2. The footer contains links to the site's Social Media to keep up to date to what's happening.
        3. Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
       


-   #### Site Owner Goals
        
    1. As a site owner I want to earn money on each book purchased via a link from the site.

       1. Building up a community of people passionate about books and providing a space where they can share recommendations could       lead to an opportunity to affiliate with some online book store.
 

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site to point out any bugs and/or user experience issues.

### Known Bugs

-   Hamburger icon in Navbar stretches over Hero Image on small screens.

## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. 


To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Run the `snap install --classic heroku` command in the terminal window to instal heroku in my local workspace.
3. Ran the `heroku login -i` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git.
5. Linked the Heroku app as the remote master branch.
6. Created a requirements.txt file.
7. Created a Procfile
8. Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
9. Ran the `heroku ps:scale web=1` command in the terminal window to run the app in Heroku.
10. Entered the following Config Var in Heroku:

    ```MONGO_URI : <link to MongoDB>```


The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Minimalist Reading](https://minimalist-reading-ms3.herokuapp.com/)


### Forking the GitHub Repository

#### Note:
- For Secret Key contact me @ jonmurrii@gmail.com

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Start Bootstrap](https://startbootstrap.com/) Clean Blog Theme was used to provide a structure for the website so as to be able to quickly focus on the site's functionality and backend code.

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.


### Content

-   All content was written by the developer.

-   Format of README.md followed *[this](https://github.com/Code-Institute-Solutions/SampleREADME#code-institute-website)* example.

-   I took much inspiration from this [MS3 project](https://github.com/Pysched/MS3-DM)

### Media

-   All Images used in the site were taken from [Pexels](https://www.pexels.com/).

-   Favicon created at [Logomakr](https://logomakr.com/).

### Acknowledgements

-   My Mentor Aaoron Sinnott for helpful feedback and advice throughout.

-   Tutor support at Code Institute for their support.