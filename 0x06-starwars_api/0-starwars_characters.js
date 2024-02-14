#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getResponse (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

getResponse(url)
  .then(body => {
    const jsonResponse = JSON.parse(body);
    const characterUrls = jsonResponse.characters;

    const characterPromises = characterUrls.map(characterUrl => {
      return getResponse(characterUrl).then(body => JSON.parse(body));
    });

    return Promise.all(characterPromises);
  })
  .then(characters => {
    characters.forEach(character => {
      console.log(character.name);
    });
  })
  .catch(error => {
    console.log(error);
  });
