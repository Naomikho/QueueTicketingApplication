# QueueTicketingApplication
Backend application for queue & ticket system. Built with FastAPI. 
You may use any part of my code as reference, as long as credit is given.

Here is the Swagger UI for the API : https://queue-ticketing-application.herokuapp.com/docs

!!IMPORTANT
1. If nothing works on the front end, the back end may require a fresh as Heroku's hostings go to sleep without interaction. I am using Kaffeine to keep it awake now, but I'll keep this note just in case. Open the developer console and check if there is a message "Failed to load resource: the server responded with a status of 404 ()". If so, please head to https://queue-ticketing-application.herokuapp.com/docs#/ and refresh the page. It should fix the issue. 
2. Free hosting options have timeouts, so the data sent to the front end may be in its default/initial state once in a while. Please understand that this is not intended behaviour. You may refresh the page again if the data has suddenly reverted to its default state(although you have not used the clear function).

Note: Due to deployment issues WebSocket function is not supported unless both ends of the application run on localhost.

Q1. How do I access the application?

This repository only contains the backend. Due to time constraints, I did not build a front end from scratch and built new pages as extensions
of my existing website. You can access the application using these two links and open them in two different tabs or devices. Right now you have to force a refresh on the Customer Ticket page to see updates as there is no WebSocket support. 

https://naomikho.github.io/CustTicket

https://naomikho.github.io/CounterView

Q2. Where is the front end code for this application? 

The code for the front end can be found on my other repo https://github.com/Naomikho/Naomikho.github.io in the master branch. Go into src > pages and you will find CustTicket.js and CounterView.js. Since they are built as part of my website, the routing is handled by App.js and all the css is under App.css. 
