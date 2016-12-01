The Website:
I have created my Sinlge Page Application from a wesbite that I am currently designing for my group project. I took sections of my website and put them into the different pages contained in the templates folder. 


The Index page:
This page contains the header, navigation bar and footer which will appear on every page. The only part that will change is the section between the {% block content %}  {% endblock %} blocks. 
Also, on the index page is the jQuery that links the other pages to the index page and that of the server.py python page.
I also made a connection to the pouchdb database on this page. It will get text that I have put into the database and return it to the index page in the starter-template section(div) on the index page.


The Static page:
This contains the bootstrap styling, css styling, fonts, images used throughout the site and pluggins. Nothing in this page will change.


The about, home & protoype page:
All of these pages have content set in between the {% block content %}  {% endblock %} blocks. This is the only content that changes in each page but it does not refresh the page.

The contact & map page:
Like the other pages, the only content that changes in these pages is the content that sits between {% block content %}  {% endblock %} blocks. But because both of these pages contain iframes, the page must refresh.


The server.py page:
This contains the python code that tells the pages what path they are at. For example, the about page's path is 


Cmder:
In the Cmder prompt window, you must navigate to your Single Page Application folder. My is on my desktop and is in a folder called SPA. I changed directory(cd) to desktop, then changed directory to SPA so the path it is at is C:\Users\Teresa\Desktop\SPA.
To run the python server page, you type in python server.py. Then the command prompt will return the URL for your website which is 127.0.0.1:5000 eg * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit). Other pages, for example, the about page will be found at 127.0.0.1:5000\about. It gets this information from the server.py page.


Windows command prompt:
Go to start menu and type in cmd to open the comand prompt window. Then, navigate to the node folder which I have saved on my C drive. The path that you are looking for here is C:\node\node>. Then put in C:\node\node>pouchdb-server to run the pouchdb database.


NOTES:
I attempted to put in a back button but I couldn't get it to work properly.


References:
https://www.youtube.com/watch?v=0fKg7e37bQE
https://www.youtube.com/watch?v=LXoWxrTdXkM
https://www.youtube.com/watch?v=E8TXME3bzNs
https://www.youtube.com/watch?v=ven5f4wCE4k
https://www.youtube.com/watch?v=kjdpswy9xJk
https://nolanlawson.com/2016/02/08/how-to-think-about-databases/
https://github.com/nolanlawson/pokedex.org/blob/master/src/js/worker/databaseService.js#L12-L20
https://developer.mozilla.org/en-US/docs/Web/API/History_API




User notes:

C:\Users\G00164894
? cd desktop

C:\Users\G00164894\Desktop
? cd flask

C:\Users\G00164894\Desktop\Flask (master)
? ls
hello.py  readme.md  readme2.txt  static/  templates/

C:\Users\G00164894\Desktop\Flask (master)
? python hello.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
