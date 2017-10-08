let express = require('express')
let app = express()
const KerasJS = require('keras-js')
let bodyParser = require('body-parser')
app.use(bodyParser.json())
let cors = require('cors')
app.use(cors())
const model = new KerasJS.Model({
    filepaths: {
        model: '../cervical_cancer_model.json',
        weights: '../Cervical_cancer_weights_weights.buf',
        metadata: '../Cervical_cancer_weights_metadata.json'
    },
    gpu : false
  })
  model.ready()
  .then(() => {
    // input data object keyed by names of the input layers
    // or `input` for Sequential models
    // values are the flattened Float32Array data
    // (input tensor shapes are specified in the model config)
    const inputData = {'input_1': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    console.log(model)
})
  
app.post('/', (req,res) => {
    let spawn = require("child_process").spawn;
    x = JSON.stringify(req.body["x"])    
    console.log(x)
    let process = spawn('python3',["../cervical_cancer_loaded.py",x]);
    process.stdout.on('data', function (data){
          res.json((data.toString('utf8')))
    });
    process.stderr.on('err', err=>{
        console.log((err.toString('utf8')))
    })
})
app.get('/', (req,res) => {
    console.log(req)
    res.send("k")
})
app.listen(3000)  