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

Here's a preview of the readme for each app: [APP_README_PREVIEW.md](APP_README_PREVIEW.md)

### Language: TypeScript (3.7)

Before the game starts I would suggest you install [NVM](http://nvm.sh) and Node 12.4.0.

### Repositories

[game.yaml](game.yaml)
