# QueueTicketingApplication
Backend application for queue & ticket system. Built with FastAPI and python. 
You may use any part of my code as reference, as long as credit is given.

Here is the Swagger UI for the API : https://queue-ticketing-application.herokuapp.com/docs

Main functions: On the customer ticket view, you can take a new ticket and view counter & queue status. On the counter view, you can use call next to call the first person in the queue over, and use comp curr to complete the current ticket that you are processing. You can also make the counters go offline and clear the queue and reset the counters to their default state.  

Note: Due to deployment issues the WebSocket function is not supported. Free hosting options do not support Websocket while there are a CORS issues on localhost(where a CORS proxy solution doesn't work). 

!!IMPORTANT
1. If nothing works on the front end, the back end may require a fresh as Heroku's hostings go to sleep without interaction. I am using Kaffeine to keep it awake now, but I'll keep this note just in case. Open the developer console and check if there is a message "Failed to load resource: the server responded with a status of 404 ()". If so, please head to https://queue-ticketing-application.herokuapp.com/docs#/ and refresh the page. It should fix the issue. 
2. Heroku has timeouts and runs very slow, so the data sent to the front end may be in its default/initial state. Please understand that this is not intended behaviour, and a refresh will normally fix it. Please also refrain from sending requests too frequently & quickly to the API because it processes requests very slowly. Wait for at least a couple of seconds before you execute the next function. 
3. Referring to the above point, similar issues will occur with the Swagger UI. If you download the repo and host the API yourself, then these issues will not occur. However localhosting the API will not allow the proxy to work and will cause CORS policy issues. To localhost the repo download/clone the folder, then open a terminal in this folder directory and type python -m uvicorn main:app --host 0.0.0.0 --reload (Note that you must have python 3, fastapi and uvicorn installed)

Q1. How do I access the application?

This repository only contains the backend. Because I can only host one website with GitHubWebPages on my account, I did not build a front end from scratch and built new pages as extensions of my existing website. You can access the application using these two links and open them in two different tabs or devices. Right now you have to force a refresh on the Customer Ticket page to see updates as there is no WebSocket support. 

https://naomikho.github.io/CustTicket

https://naomikho.github.io/CounterView

Q2. Where is the front end code for this application? 

The code for the front end can be found on my other repo https://github.com/Naomikho/Naomikho.github.io in the master branch. Go into src > pages and you will find CustTicket.js and CounterView.js. Since they are built as part of my website, the routing is handled by App.js and all the css is under App.css. 

The API call functions are under HelperFunc > QueueTicketAPI.js. 
