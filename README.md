# REST Yahoo-Finance Service
<h2>Describe</h2>
This application automatically creates tables and imports the company's financial statements from *.CSV files to DB. Next, the micro service REST is implemented to provide information in the form of JSON. The service API has also been successfully deployed to server in two implementations (slow online and fast local).
<h2>Results</h2>
I developed the REST service to present data from a database. This application automatically has two implementations. The first variant is the use of an online free database based on PostgreSQL (attention - slowly). The second varia is using the local Sqlite database (fast).

The result can be viewed at these links:

1) <i>Realization of the program with an online database</i>

<i>https://testtask1234.herokuapp.com/api/</i>  - main entrypoint (data form all the tables)

<i>https://testtask1234.herokuapp.com/api/cldr</i> - Single company info

<i>https://testtask1234.herokuapp.com/api/docu

https://testtask1234.herokuapp.com/api/pd

https://testtask1234.herokuapp.com/api/pins

https://testtask1234.herokuapp.com/api/run

https://testtask1234.herokuapp.com/api/zm

https://testtask1234.herokuapp.com/api/zuo</i>

-------------------------------------------
2) <i>Realization of the program with a local database</i>

<i>https://applocal123.herokuapp.com/api/</i>  - main entrypoint (data form all the tables)

<i>https://applocal123.herokuapp.com/api/cldr</i> - Single company info

<i>https://applocal123.herokuapp.com/api/docu

https://applocal123.herokuapp.com/api/pd

https://applocal123.herokuapp.com/api/pins

https://applocal123.herokuapp.com/api/run

https://applocal123.herokuapp.com/api/zm

https://applocal123.herokuapp.com/api/zuo</i>

I also tried to containerize the application using <b>Docker</b>. The result of the link:

<i>https://hub.docker.com/r/6fbe083a40f9/task-flask-serv</i>
<h2>Installation</h2>

    $ mkdir <temp> && cd <temp>
    $ gil clone <this_repo> && cd <this_repo>
    $ pip install -r requirements.txt
    $ python app.py
