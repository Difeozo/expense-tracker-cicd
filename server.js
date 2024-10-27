const express = require("express");
const bodyParser = require("body-parser");
const app = express();

let users = {};
let transactions = [];

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.send("This is the official Expense Tracker!");
});

app.get("/register", (req, res) => {
  res.sendFile(__dirname + "/views/register.html");
});

app.post("/register", (req, res) => {
  const username = req.body.username;
  if (!users[username]) {
    users[username] = { balance: 0, transactions: [] };
    res.redirect("/");
  } else {
    res.send("User already exists!");
  }
});

app.get("/balance/:username", (req, res) => {
  const username = req.params.username;
  if (users[username]) {
    res.send(`${username}'s balance: ${users[username].balance}`);
  } else {
    res.send("User not found!");
  }
});

app.get("/transactions/:username", (req, res) => {
  const username = req.params.username;
  if (users[username]) {
    res.send(
      `${username}'s transaction history: ${users[username].transactions}`
    );
  } else {
    res.send("User not found!");
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

#test