# QueueTicketingApplication
Backend application for queue & ticket system. Built with FastAPI. 
You may use any part of my code as reference, as long as credit is given.

!!IMPORTANT
1. If nothing works on the front end, the back end may require a fresh. Open the developer console and check if there is a message "Failed to load resource: the server responded with a status of 404 ()". If so, please head to https://queue-ticketing-application.herokuapp.com/docs#/ and refresh the page. It should fix the issue.
2. Free hosting options have timeouts, so the data sent to the front end may be in its default/initial state every few intervals. Please understand that this is not intended behaviour and is the best way I can replicate WebSocket behaviour now. This would NOT be an issue if a WebSocket connection can be established.

Note: This project is still a work in progress. Due to deployment issues WebSocket function is not supported unless both ends of the application run on localhost.

How do I access the application?
This repository only contains the backend. Due to time constraints, I did not build a front end from scratched and built new pages as extensions
of my existing website. You can access the application using these two links and open them in two different tabs or devices:

https://naomikho.github.io/CustTicket

https://naomikho.github.io/CounterView
