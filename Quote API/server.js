const express = require('express');
const app = express();

const { quotes } = require('./data');
const { getRandomElement } = require('./utils');

const PORT = process.env.PORT || 4001;

app.use(express.static('public'));

app.get("/api/quotes/random", (req, res, next) => {
  const randomQuote = getRandomElement(quotes);
  if (randomQuote) { res.send({quote: randomQuote}); }
  else { res.status(404).send(); }
});

app.get("/api/quotes", (req, res, next) => {
  const person = req.query.person;
  const personQuotes = [];
  for (let quote of quotes) {
    if (quote.person === person) {
      personQuotes.push(quote.quote);
    }
  }
  res.send({quotes: personQuotes});
});

app.post("/api/quotes", (req, res, next) => {
  const person = req.query.person;
  const quote = req.query.quote;
  let newQuote = {};
  if (person && quote) {
    newQuote.quote = quote;
    newQuote.person = person;
    quotes.push(newQuote);
  }
  res.send({quote: newQuote});
});