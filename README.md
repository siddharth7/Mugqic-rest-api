# Mugqic-rest-api
Gsoc 2016 selection test

#Installation
-	create a folder: `mkdir restapi`
-	enter: `cd restapi`
-	clone repo : `https://github.com/siddharth7/Mugqic-rest-api.git`
-	enter repo:   `cd Mugqic-rest-api-master`
-	create virtual environment: `virtualenv venv`
-	activate: `source venv/bin/activate`
-	install dependencies: `pip install -r requirements.txt`
-	run server: `python run.py`

#Api Endpoints
##GET
- ##curl -X GET http://localhost:5000/users <br />
  return all users in the database with there phone numbers <br />
  example : [{"name": "siddharth", "phone": "9810180107"}, {"name": "rohan", "phone": "9811223342"}, {"name": "ayush", "phone": "9812546732"}]

- ##curl -X GET http://localhost:5000/users/'username' <br />
  return phone number and name corresponding to the name in the request <br />
  example(if name is found) : {"name": "siddharth", "phone": "9810180107", "success": "true"} <br />
          (if name is not found): {"error": "User not found", "success": "false"} <br />

##POST
- curl -X POST -H "Content-Type: application/json" -d '{"name”:"Am", "phone”:"981233"}' http://localhost:5000/users/add
  <br/> Adds to database if not in it, else sends failure message <br />
  Responses recieved <br />
  - {"error": "Already in Db", "success": “false"} <br />
  - {"error": "Name not found", "success": “false"} <br />
  - {"error": "Phone Number not found", "success": “false"} <br />
  - {"name": "Am", "phone": "9812321232", "success": "true"} <br />

##PUT
- curl -X PUT -H "Content-Type: application/json" -d '{"name”:"Am", "phone”:"981233"}' http://localhost:5000/users/add
  <br/> Adds to database if not in it, else sends failure message <br />
  Responses recieved <br />
  - {"error": "Already in Db", "success": “false"} <br />
  - {"error": "Name not found", "success": “false"} <br />
  - {"error": "Phone Number not found", "success": “false"} <br />
  - {"name": "Am", "phone": "9812321232", "success": "true"} <br />

Currently, POST and PUT and behaving same because the problem is that you can't easily control which threads and processes - the list could get corrupted entirely. The whole point of REST server is to keep it stateless. Each request should be totally independent and not share any state in the server. Therefore, I have used database in both methods.

