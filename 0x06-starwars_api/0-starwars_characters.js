#!/usr/bin/node

const request = require('request');

const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) {
      console.error(`Error fetching character ${actors[x]}:`, err);
      return;
    }
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};

const main = () => {
  const filmId = process.argv[2];
  if (!filmId) {
    console.error('Please provide a film ID as the argument.');
    return;
  }

  const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  request(url, function (err, res, body) {
    if (err) {
      console.error('Error fetching film data:', err);
      return;
    }
    const actors = JSON.parse(body).characters;
    exactOrder(actors, 0);
  });
};

main();

