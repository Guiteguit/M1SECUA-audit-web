const express = require('express');
const crypto = require('crypto');

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Vulnérabilité volontaire : secret hardcodé
const API_KEY = "js-hardcoded-secret-123";

app.get('/health', (req, res) => {
  res.json({ status: 'ok', lab: 'jour4', app: 'js' });
});

app.get('/eval', (req, res) => {
  const code = req.query.code || '1+1';
  // Vulnérabilité volontaire : eval sur entrée utilisateur
  const result = eval(code);
  res.send(String(result));
});

app.get('/redirect', (req, res) => {
  const url = req.query.url || '/';
  // Vulnérabilité volontaire : open redirect
  res.redirect(url);
});

app.post('/render', (req, res) => {
  const name = req.body.name || 'student';
  // Vulnérabilité volontaire : HTML non encodé
  res.send('<h1>Hello ' + name + '</h1>');
});

app.get('/hash', (req, res) => {
  const value = req.query.value || 'password';
  // Vulnérabilité volontaire : MD5
  const h = crypto.createHash('md5').update(value).digest('hex');
  res.json({ md5: h });
});

app.listen(3002, () => {
  console.log('JS lab app listening on port 3002');
});
