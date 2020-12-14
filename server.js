const translate = require('translation-google');
const express = require("express");
const app = express();

app.get("/translate", function(req, resp) {

    fromLan = req.query.before;
    afterLan = req.query.after;
    word = req.query.word;

    translate(word, {from: fromLan, to: afterLan}).then(res => {
        resp.send(JSON.stringify({translated: res.text}));
    }).catch(err => {
        console.error(err);
    });

})

app.listen(3000, function(){
    console.log("Server Listening At http://localhost:3000");
})
