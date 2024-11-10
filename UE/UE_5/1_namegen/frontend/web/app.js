const express = require('express')
const bodyParser = require('body-parser');
const cors =  require('cors')
const path = require('path');
const http = require('http');

const port = 3000
const app = express()
app.use(cors())

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});


app.get('/name', function(req, res) {
    var options = {
  	host: "namegen",
	port: 5000,
	path: '/name',
	method: 'GET'
    };
    console.log("Fetching information from backend")
    http.request(options, function(response) {
 	response.on('data', function (data) {
        console.log('Data received: ',data)
	   res.send(data);
      });
    }).end();
});


app.listen(port, () => console.log(`NameWeb started at port ${port}!`))
