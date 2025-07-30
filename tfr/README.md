# tfr - The telefactor CLI

## Directory structure

- `{ROOT}/` - The root directory the GM uses to manage thier game with Tfr.
  - `tfr.yml`
  - `.git`, `.gitignore` - The root directory can be tracked in git.
  - `repos/`
    - `phase-0/`
      - GM reference implementation goes here.
      - `{source}` - Includes source files (structure chosen by GM).
      - `{tests}` - Includes test files (structure chosen by GM).
      - `.git` - Tracked as its own git repo.
    - `phase-{1,3,...N}/`
      - `{source N-1}` - Includes source from previous phase.
      - `{tests N}` - Player writes tests for this phase.
      - `.git` - Tracked as its own git repo (or private branch).
    - `phase-{2,4,...M}/`
      - `{source M}` - Player writes implementaiton for this phase.
      - `{tests M-1}` - Includes tests from previous phase.
      - `.git` - Tracked as its own git repo (or private branch).

## Dev notes

I initially set up a bunch of CLI commands that modify the game state. That makes
the Click command system the main "application" and the TfrApp is really just
a holder of some shared state as opposed to being an API entrypoint. Kind of
regretting that from a testing standpoint. Would like the CLI parts to just
be responsible for I/O formatting and have the logic live in the app.
