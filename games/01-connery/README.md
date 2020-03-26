# Telefactor Game 01: Connery

## Game structure

In this game we will work on two seperate apps that will be worked on in parallel.

These command-line apps will start small, each with a single main entrypoint function
that the CLI hooks into.

Each player will get a chance to be _sourcerer_ for one of the apps and an _examiner_
for the other. The order will be determined randomly and then follow the schedule below.
This means that by the end of the game **each player will have worked on two different repositories at two different times**.

### Schedule

**Example**

| Week | Role | App 1 | App 2 |
| ---  | ---  | ---   | ---   |
| 0    | GM   | GM    | GM    |
| 1    | Ex   | Alice | Diane |
| 1.5  | Src  | Bob   | Eddy  |
| 2    | Ex   | Carl  | Fred  |
| 2.5  | Src  | Diane | Alice |
| 3    | Ex   | Eddy  | Bob   |
| 3.5  | Src  | Fred  | Carl  |

### Why structure it this way?

Here are the main pieces of feedback from Fam (Game 00):

1. Having the core functionality of the app require several entrypoints discouraged
   players from adding their own _je ne sais quoi_.
2. Examiners wanted to try writing source code, sourcerers wanted to try writing tests.
3. Giving each player a whole week means the first few players forget about the game by the end.

I think that splitting the game into two smaller apps will addess #1 & #2 nicely.
Want to throw in some additional CLI commands? Well, I'll let them pass to the next
round, warts and all.

As for #3, the new schedule will still make the whole game take 1 week per person.
However, the chance to play twice will mean there will be less of a gap between the
earlist players and the finale. Hopefully this will be more engaging.

## The code

Here's a boilerplate you can clone and get started on!: [connery-boilerplate](https://github.com/telefactor/connery-boilerplate)

### Language: TypeScript (3.7)

Before the game starts I would suggest you install [NVM](http://nvm.sh) and Node 12.4.0.

### Repositories

|name|url|
|--  |-- |
|analbumcover-00 |https://github.com/ssangervasi/analbumcover-00.git|
|analbumcover-01 |https://github.com/ssangervasi/analbumcover-01.git|
|analbumcover-02 |https://github.com/ssangervasi/analbumcover-02.git|
|analbumcover-03 |https://github.com/ssangervasi/analbumcover-03.git|
|analbumcover-04 |https://github.com/ssangervasi/analbumcover-04.git|
|analbumcover-05 |https://github.com/ssangervasi/analbumcover-05.git|
|analbumcover-06 |https://github.com/ssangervasi/analbumcover-06.git|
|analbumcover-07 |https://github.com/ssangervasi/analbumcover-07.git|
|analbumcover-08 |https://github.com/ssangervasi/analbumcover-08.git|
|analbumcover-09 |https://github.com/ssangervasi/analbumcover-09.git|
|shawn-00 |https://github.com/ssangervasi/shawn-00.git|
|shawn-01 |https://github.com/ssangervasi/shawn-01.git|
|shawn-02 |https://github.com/ssangervasi/shawn-02.git|
|shawn-03 |https://github.com/ssangervasi/shawn-03.git|
|shawn-04 |https://github.com/ssangervasi/shawn-04.git|
|shawn-05 |https://github.com/ssangervasi/shawn-05.git|
|shawn-06 |https://github.com/ssangervasi/shawn-06.git|
|shawn-07 |https://github.com/ssangervasi/shawn-07.git|
|shawn-08 |https://github.com/ssangervasi/shawn-08.git|
|shawn-09 |https://github.com/ssangervasi/shawn-09.git|


# Shortest impl:
sh02 	64
Nickie

# Longest test desc:
ab01 65
it does not return anything if the minimum word-length is onerous

