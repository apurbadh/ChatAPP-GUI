
const express = require("express");
const app = express();

const myarr = [];

app.get('', (req, res)=> {
    let name = req.query.name;
    let message = req.query.message;
    myarr.push({"name" : name, "message" : message});
})

app.get('/show', (req, res)=> {
    res.json(myarr)
})

app.listen(8000, ()=> console.log("The server has started at port 8000."))






