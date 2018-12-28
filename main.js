var express = require('express');
var path = require('path');
var child_process = require('child_process');

const app = express();
var rgb = "FFFFFF";
var status = false;

app.get('/',(req,res) => {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/on', (req,res) => {
    if(status == false) {
        var execString = "killall python3;python3 on.py "+rgb+"";
        var subprocess = child_process.exec(execString);
        console.log("Switching on light with colour "+rgb);
        status = true;
    } else {
        console.log("System is already on try to off it or change color");
    }
    res.redirect('/')
});

app.get('/off', (req,res) => {
    if(status == true) {
        var execString = "killall python3;python3 off.py";
        var subprocess = child_process.exec(execString);
        console.log("Turning off light");
        status = false;
    } else {
        console.log("System is already off try to on it");
    }
    res.redirect('/')
});

app.get('/color/:value', (req,res) => {
    rgb = req.params.value;
    status = false;
    res.redirect('/on');
});

app.get("*", (req,res) => {
    res.redirect('/');
});

app.listen(3000,() => {
    console.log("Service started on port 3000 ");
});