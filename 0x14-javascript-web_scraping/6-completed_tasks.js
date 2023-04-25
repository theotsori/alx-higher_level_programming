#!/usr/bin/node
'use script';

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.error(error);
        return;
    }

    const tasks = JSON.parse(body);
    const completed = {};

    tasks.forEach((task) => {
        if (task.completed) {
            if (completed[task.userId] === undefined) {
                completed[task.userId] = 1;
            } else {
                completed[task.userId]++;
            }
        }
    });

    console.log(completed);
});
