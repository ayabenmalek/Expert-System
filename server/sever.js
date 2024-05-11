const express = require('express')
const { spawn } = require('child_process');
const bodyParser = require('body-parser');
const app = express();


app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000'); // Autoriser les requêtes depuis http://localhost:3000
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'); // Autoriser les méthodes HTTP
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization'); // Autoriser les en-têtes HTTP
    next();
});
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.post('/run', (req, res) => {
    const { mealtype, preference, occasion } = req.body;
    
    const inputData = [mealtype, preference, occasion];
    console.log(inputData)
    const inputString = inputData.join(',');
    console.log('a envoy',typeof(inputString))
    const pythonProcess = spawn('python', ['expertsystem.py', inputString]);
    let result = '';
    let valuesArray;
    pythonProcess.stdout.on('data', (data) => {
      console.log('data',data)
      result += data.toString();

      console.log('result',result)
      // valuesArray = result.match(/(?<=x:\s*)\w+(?=\s*})/g);
      // console.log(valuesArray)
      console.log(typeof(result))
    });
  
    pythonProcess.stdout.on('end', () => {
      res.send(result)
      console.log('end')
    });
  
    pythonProcess.stdin.end();
  });
app.listen(7000,()=>{
    console.log('listening on port 7000')
})