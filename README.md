
# Telefactor - The refactoring party game

## About

This is a team programming exercise I came up with, inspired by the party game Telestrations
and Sandi Metz's talk about refactoring the Gilded Rose "code kata".
The original game is a portmanteau of "telephone" and "illustrations", wherein everyone draws
and describes increasingly bizarre variations of an original idea.
Check out the [links](#inspiration-links) below for more details, if you like.

Thus, the name: Telefactor -- ["Telephone Refactoring"](#a-clumsy-portmanteau)

## How to play

1. The Game Master (GM) writes a small application with some moderately complex behavior which is fully tested.
2. The GM copies the app source and deletes all of the tests. (The full source remains hidden until the end.)
3. Timed rounds begin. Time per round is 3 days for this game.
4. The GM shares the untested app with player #1, the first "examiner."
5. Player #1 writes as many tests as they feel necessary to describe the behavior of the app.
6. When the time is up, player #1 hands the tested code back to the host, no matter the state.
7. The GM takes the tested app and deletes all source, leaving player #1's tests and any boilerplate "run the app" code.
8. The GM gives the tests-only app to player #2, the first "sourcerer."
9. Player #2 must write app code (with no tests) to satisfy player #1's tests, then hand it back to the GM.
10. Rounds of steps 2-9 repeat, where odd-numbered players write tests and even players write app code.

These steps will be carried out remotely, with the code sent through GitHub, Discord, and/or email until everyone has had a turn.

Then all the repositories will be made public and sent out to the whole group, with the original fully-tested app to compare against.

Finally, we'll all meet up to discuss how the game went, laugh about the best "features" of the final app,
and warm-heartedly blame each other for mistakes made up and down the chain of custody.

## This repository

This repo is acts an archive of starting apps and rounds of the games being played.

If you're a host looking to reuse one of the games, make sure your players know not to go poking
around for spoilers. I prefer to keep each player's code in a private repo which isn't made public
until after the game is finished.

## Completed games

0. [Fam](/games/00-fam/README.md) - The first completed game. A good starting point for templating
how a came should run.
1. [Connery](https://github.com/telefactor/telefactor/tree/hamster/games/01-connery#readme) - A playthrough of the game with two apps developed in parallel, so that every player got to write some features as well as some tests.

## Inspiration links

- Telestrations: https://en.wikipedia.org/wiki/Telestrations
- Sandi Metz - All the little things (Gilded Rose): https://www.youtube.com/watch?v=8bZh5LMaSmE
- Gilded Rose repo: https://github.com/emilybache/GildedRose-Refactoring-Kata
- Code Kata: https://en.wikipedia.org/wiki/Kata_(programming)

#### A clumsy portmanteau
https://comedybangbang.fandom.com/wiki/Al_A._Peterson
