# Text2RenPy
## Introduction
A basic python program utilizing regex that transforms screenplays into Ren'Py game code to promote a better development workflow.

When developing any Ren'Py game, independent developers are often tasked with juggling their game's narrative alongside their code, sound, and music. While some independent developers eventually find their preferred workflow, many solo devs give up due to the sheer amount of things they must manage. To help these struggling devs, I decided to create _Text2RenPy_ which gives developer the ability to turn already written stories into Ren'Py code. This not only formats all narration/dialogue into the expected syntax, it also: automatically handels Character Object creation, creates scene/show statements when necessary, defines character sprite images, generates practical image names, grants the user the ability to control how the resulting code is generated using *Command Statements*, and reports on the resources needed to finish the novel game.

## Important Notes
### Why Screenplays?
Some might be confused as to why screenplays are the only style of writing _currently_ understood by Text2RenPy to produce Ren'Py code, this is because screenplays are very objective compared to more descriptive styles of writing such as novels or poetry. Furthermore, while the formatting is specific, it is not as tedious as writing Ren'Py code manually. Therefore, writing a screenplay allows the developer to focus on their story instead of micromanaging code too.

## Screenplay format
In respect to text2game, there are seven main screenplay conventions you must adhere to in order for Text2RenPy to generate the Ren'Py code correctly. These are:
* Transitions
* Scene Headers
* Action
* Character Names
* Parentheticals
* Dialogue
* Blank Lines

## Screenplay Command Statement (Ren'Py)
As mentioned previously, a user can control how the resulting code is generated using *Command Statements*, but what are *Command Statements*? *Command Statements* are comma-delimited lines of text starting with a forward-slash (/) which tell Text2RenPye how to generate the following:
* When a Character sprite should be shown or hidden.
* When a Character sprite changes their emotion (without dialogue).
* Text presentation style (ADV, NVL, or SB).
* How image show statements are generated (Idle or Sprite).

