
## Setting up a good big family
```

Added person: John
Added person: Paul
Added person: George
Added person: Ringo
Added person: Bart
Added person: Lisa
Added person: Maggy
Added person: Homer
Added person: Marge
Added person: Grampa Simpson
Added person: Smoobles I
Added person: Smoobles II
Added person: Smoobles III
Added person: Smoobles IIII
Added person: Smoobles IIIII
Added Paul & George as parents of John
Added Ringo & Smoobles IIIII as parents of Paul
Added Maggy & Smoobles IIIII as parents of Ringo
Added Smoobles IIIII as parents of George
Added Marge & Homer as parents of Bart
Added Marge & Homer as parents of Lisa
Added Marge & Homer as parents of Maggy
Added Grampa Simpson as parents of Homer
Added Smoobles IIIII as parents of Grampa Simpson
Added Smoobles IIII as parents of Smoobles IIIII
Added Smoobles III as parents of Smoobles IIII
Added Smoobles II as parents of Smoobles III
Added Smoobles I as parents of Smoobles II
Added  as parents of Smoobles I

```
## Running queries
```

John
Paul
George
Ringo
Smoobles IIIII
Smoobles IIIII
Maggy
Smoobles IIIII
Smoobles IIII
Smoobles IIII
Marge
Homer
Smoobles IIII
Smoobles III
Smoobles III
Grampa Simpson
Smoobles III
Smoobles II
Smoobles II
Maggy
Marge
Homer
Grampa Simpson
Smoobles IIIII
Smoobles IIII
Smoobles III

```
## final file
```json

{
  "John": [
    "Paul",
    "George"
  ],
  "Paul": [
    "Ringo",
    "Smoobles IIIII"
  ],
  "George": [
    "Smoobles IIIII"
  ],
  "Ringo": [
    "Maggy",
    "Smoobles IIIII"
  ],
  "Bart": [
    "Marge",
    "Homer"
  ],
  "Lisa": [
    "Marge",
    "Homer"
  ],
  "Maggy": [
    "Marge",
    "Homer"
  ],
  "Homer": [
    "Grampa Simpson"
  ],
  "Marge": [

  ],
  "Grampa Simpson": [
    "Smoobles IIIII"
  ],
  "Smoobles I": [

  ],
  "Smoobles II": [
    "Smoobles I"
  ],
  "Smoobles III": [
    "Smoobles II"
  ],
  "Smoobles IIII": [
    "Smoobles III"
  ],
  "Smoobles IIIII": [
    "Smoobles IIII"
  ]
}
```

