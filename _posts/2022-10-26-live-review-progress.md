---
toc: true
layout: post
description: Week 2 Final Progress Week 2
categories: [markdown]
title: Live Review Progress
---
## Our goals for the start of the week

In Week 1, we managed to create an api that would be able to display the defination of a word unknown to the user. Along with this, framework for the letters and the hangman were created. This week, some of our goals were to...

* Make each letter tangible/clickable.
* Create a space where the length unknown word would be shown 
* Create a space where incorrect guesses, which are not included in the word, are placed
* Make the program look more presentable for the user and take into consideration users with disabilities
* Keep on updating the word list for our API
* Make it so the hangman can "grow" body parts as the user guesses incorrect letters

## Updates/Progress

While we are still working on the frontend aspect of our code, our backend logic is basically fully complete. As our backend developer, I coded the logic for multiple different user input types in python. I created a dictionary which will store various variables such as the randomly generated session ID, the actual word, the defenition, and all of the user's guesses. This makes it very easy to use if statements and verify if the user's guess is in the word or not.

## Problems we ran into

* Merge conflicts - We fixed this by researching on stackoverflow and running the following commands:

git merge --abort
git pull
git add file
git fetch --all
git reset --hard origin/master
git merge --continue
git reset --hard origin/trunk
rm -rf .git/MERGE*
git pull origin master
git pull origin main
git push -f origin comments demo:main
git pull -f origin comments demo:main
git pull

* How to code the backend logic in python and link it to the HTML frontend file - We resolved this issue by coding it in a python file, and then using the framework 'Vue' to connect both the frontend and the backend.

## Proof of Commits

![]({{ site.baseurl }}/images/commitgraph.png "Photo of our team's commit history")