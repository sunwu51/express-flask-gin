var express =require('express');
var app = express();
app.use(express.urlencoded({extended:false}))
app.use(express.json())
app.use("/static",express.static("static"))

app.get('/',function(req,res){
    console.log(req.headers.a)
    res.header("b","c");
    res.send("hello express");
});
//路径参数 查询字符串 表单 json
//纯文本 json 
app.get('/path/:id',function(req,res){
    console.log(req.params.id)
    res.send(req.params.id)
})
app.get('/querystring',function(req,res){
    console.log(req.query)
    res.send(req.query.username)
})
app.post('/form',function(req,res){
    console.log(req.body)
    res.send(req.body.username)
})
app.post('/json',function(req,res){
    console.log(req.body)
    res.json({"a":12,b:"jjjj"})
})
app.listen(3001);