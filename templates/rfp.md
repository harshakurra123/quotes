### Proposal for smile maker application
- Smile maker application is an entertainment app, in which user can browse the jokes. Home page shows joke after every refresh. If user wants list of jokes, we provide button on home page to direct to list of jokes. 
- Authentication is required for user to post or edit the content in the joke.
- Application is developed in python with Django framework using postgresql as database.
- Application uses Restful api’s for serving the data.


### Project Title
- Smile Maker

### Schedule & Sprints for the application development
- Sprint 1
    - Gather all the requirements for developement.
    - Design sketches for UI pages.
    - Setup for the backend development.
    - Decide the tables for the Database Design.
- Sprint 2
    - Models for the Database.
    - UI pages for all the screens.
    - API's for implementing functionalities.
    - Test views for code complexity.
- Sprint 3
    - Code reviews and code refactoring.
    - Test cases for all the api's.
    - Integrate backend api's with frontend pages.
    - Manual tests after integration(Both backend and frontend).
- Spring 4
    - Deployment setup for the application.
    - Host application in the browser.
    - Release application for the first time.
    - Review application for the final time.


- Schedule & sprints are set by the GDP semesters (about every 2-weeks = a sprint)
- Budget is set by the size of the development team * average expected hours per developer per week
- Scope of work should be clearly divided into sprint buckets of time

### Budget
| Team Member                   | Cost per hour | Cost per week | Total Budget(Total weeks * Cost per week) | Email                  |
| ----------------------------- | ------------- | ------------- | ------------ |----------------------- |
| Harshavardhan Kurra           | 30$           | 1200$         | 19200$       | s542409@nwmissouri.edu |
| Hemanth Venkata Reddy Telluri | 30$           | 1200$         | 19200$       | s542393@nwmissouri.edu |


### Team Members
1. Harshavardhan Kurra - Backend Development
2. Hemanth Venkata Reddy Telluri - Frontend Development


- User adds the jokes by entering joke_title, joke_description. Joke data is stored in joke table with logged in user_id
- User can browse jokes and like them, likes of users are stored in joke_likes.


### Technology Stack
- Backend language + framework: Python, Django
- Backend free app host: Heroku
- Data host + type: Postgresql
- Front-end page plan: server-side views
- Front-end responsive design: Bootstrap


### User Stories
1. User can browse through the joke.
2. User clicks on SEE MORE button to see list of jokes.
3. User can login to the application.
4. User can add a joke.
5. User can edit a joke.
6. User can like or comment on jokes.




```
[
    {
        "joke_title": "MAKE ME A SANDWICH",
        "joke_description": "My husband and I were daydreaming about what we would do if we won the lottery. I started: I’d hire a cook so that I could just say, ‘Hey, make me a sandwich!’ Thomas shook his head. Not me. I already have one of those.",
        "joke_user": {}
    },
    {
        "joke_title": "MADE MY OWN GRANDKIDS",
        "joke_description": "With a patient in my medical exam room Me: How old are your kids? Patient: Forty-four and 39 from my wife who passed away, and from my second wife, 15 and 13. Me: That’s quite the age difference! Patient: Well, the older ones didn’t give me any grandkids, so I made my own.",
        "joke_user": {}
    }
]
```
## References
- <https://docs.djangoproject.com/en/3.2/intro/tutorial01/> 
- <https://www.django-rest-framework.org/tutorial/quickstart/>

