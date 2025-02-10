# YUMMY TUMMY

## Overview

Yummy Tummy is a delightful recipe suggestion application built with Django and styled using Bootstrap 5. It is my final project for Code Institute's 16-weeks Full Stack Development Bootcamp course. It offers a seamless user experience with full CRUD functionality, allowing users to effortlessly create, read, update, and delete their comments. This project aims to provide a centralized, user-friendly platform for food enthusiasts to discover and manage recipes, enhancing culinary exploration and enjoyment.

We addresses the challenge of meal planning by offering users the option to categorize recipes by meal type (breakfast, lunch, dinner). This feature helps users to relax and plan their meals accordingly, ensuring a well-organized and enjoyable cooking experience.

[Live View](https://yummy-tummy-582bc957dc87.herokuapp.com/)

## Responsive
Yummy Tummy is fully responsive, ensuring a seamless experience across various devices, including desktops, tablets, and mobile phones. The design adapts to different screen sizes, providing an optimal viewing experience whether you're at home or on the go.
![Am I Responsive](static/images/readme/responsive.png)

## User Expereince

Throughout the development of Yummy Tummy, **Agile methodology** was employed to ensure iterative progress and continuous improvement. This approach facilitated regular feedback and allowed for adaptive planning, ultimately leading to a more refined and user-centric application.

### User Goals

Users want a platform that:
- Provides a wide variety of recipes to explore.
- Allows easy categorization and search of recipes by meal types
- Includes user reviews and ratings to help in selecting recipes.
- Easy navigation

### Site Owner Goals

The site owner aims to:
- Create a comprehensive and user-friendly recipe management platform.
- Encourage user engagement through interactive features like comments and ratings.
- Continuously update the recipe database with new and diverse recipes.
- Foster a community of food enthusiasts who can collaborate by sharing new recipes.
- Maintain a high standard of UX/UI design to enhance user satisfaction.

### Link to User Stories in GitHub Projects:

I have used the MoSCoW technique to prioritize and complete my project requirements effectively. This technique helped me to categorize the features into Must-Have, Should-Have, and Could-Have, ensuring that the most critical functionalities were implemented first, while also considering additional enhancements for future development.

Here is the link to my [Project Board](https://github.com/users/SonaliP11/projects/8)

#### MoSCoW Tecnhique

I have implemented all Must-have and Should-have features. Could-have are for future implementations.

![MoSCoW Technique](static/images/readme/moscow.png)

## UX Design

### Wireframes

The wireframes for Yummy Tummy were created using Balsamiq  to create clear, visual layouts of the site's design. While the initial designs provided a solid foundation, some elements evolved during development to enhance the overall user experience. These changes, though different from the original wireframes, resulted in a more polished and user-friendly application.

- [Click here for desktop wireframe](static/images/readme/wireframe-desktop.png)
- [Click here for tablet wireframe](static/images/readme/wireframe-tablet.png)
- [Click here for mobile wireframe](static/images/readme/wireframe-mobile.png)

### Logo

- [logo](static/images/readme/logo.jpeg)

### Color Palette
![palette](static/images/readme/color.png)

- #3F2B56 - Navigation and footer background
- #F9B114 - Background of Buttons and card-title
- #2C0703 - Heading text and box-shadow
- #F5F2F2 - Forms background
- #000000 - Text color

### Typography 

![font style](static/images/readme/fonts.png)
 - Heading - 'EB Garamond', serif
 - Body - 'Roboto', serif

## Features

### Authentication

- **Sign-In**: Users can sign in to their accounts to access personalized features such as adding ratings and reviews.
![Sign-In](static/images/readme/log-in.png)

- **Sign-In Success** : Once log-in, user will see success message.
![Sign-in success](static/images/readme/login-sucess.png) 

- **Register**: New users can register for an account to start collaborating and sharing their recipes.
![Register](static/images/readme/register.png)

- **Sign-out** : In the header, if you are logged in, you can press the 'Logout' button which will take you to the sign-out page.
![Sign-out](static/images/readme/sign-out-confirm.png) 

### Collaboration

- **Share Recipes**: Users can share their own recipes with the community, fostering a collaborative environment. 
![Join Us](static/images/readme/join-us-form.png)

- **Write Reviews**: Users can write reviews and rate recipes, helping others to choose the best recipes.
![Reviw](static/images/readme/crud-view.png)

- **Awaiting approval**: Users will receive apporoval awaiting text after editting their own comment.
![Approval Awaiting](static/images/readme/approval-awaiting.png)

- **Comment Approved**: Admin will approve comment from dashboard.
![Comment Approved](static/images/readme/comment-approved.png)

- **Comment Updated**: Users will be able to see their comments updated.
![Comment updated](static/images/readme/comment-updated.png)

### Admin panel Database

The database for Yummy Tummy is designed to efficiently manage and store user data, recipes, comments, and ratings. It uses PostgreSQL, a powerful, open-source relational database system, which ensures data integrity and supports complex queries.

![Admin panel](static/images/readme/admin.png)



