# Poetroid-Poems - Curate Poems Together

Thousands of poems in the public domain lay scattered, burried in sites, yet we don't have a single library for humans or machines.

Let's build one.

## Overview

To restore poems, we must write them in a new format, one that can be read by humans and machines alike.

Poems will be written in plain text in notepad (pc) or textedit (mac) or (insert your favorite plain text editor) and saved in [UTF-8](http://en.wikipedia.org/wiki/UTF-8). Saving a file in UTF-8 is a necessary, important step to preserve foreign-language characters across machines.


```
Every time I say "joy," joyous thing,
you will know that I am talking about you,
for you are the joy of all joyous beauty
and the joy of all joyous and beautiful pleasures,
```

Metadata will be curated *inline*, above the poem, for storing metadata and tags, to inform humans and machines with semantic data for further analysis.

```
---
title: Untitled
type: Sonnet
author: Guitton D'Arezzo
curator: Ata Moharerri
period: 1230-1294
country: Italy
tags:
- joy
- happiness
---
```

Note the `---` before and after the metadata.

Filenames are saved as `last-name-title-first-five-words.txt`

The current format for metdata is [YAML](http://en.wikipedia.org/wiki/YAML), a human readable format.

This format may change soon to [edn](https://github.com/edn-format/edn), in which case old poems will  be upgraded, automatically.

This format, the poems, their metadata, and all their revisions are protected in (git)hub, for free, forever.

## Example

```
---
title: Untitled
type: Sonnet
author: Guitton D'Arezzo
curator: Ata Moharerri
period: 1230-1294
country: Italy
tags:
- joy
- happiness
---

Every time I say "joy," joyous thing,
you will know that I am talking about you,
for you are the joy of all joyous beauty
and the joy of all joyous and beautiful pleasures,

and the joy in which a joyous future resides,
the joy of adornments and the joy of a thoughtful heart,
the joy which I gaze at and so loving a joy
that it is a joyous joy to look at it.

joy of desire ad joy of reflection,
and joy of speech and joy of happiness
and joy of all joyous movements:

and so, joyous joy, I find myself
so desirous of you that I will never know any joy
if my heart does not rest in the midst of your joy.

```

## Poetrod-Platform

Poetroid is built using an open-source platform to discover poetry together. Currently in *research & development*, this platform will bring together web, print, and mobile distribution of public domain poetry in a unified [Api](http://en.wikipedia.org/wiki/Application_programming_interface).

For more information, visit [Poetroid](http://poetroid.com/#/page/about.md).

## Status, Roadmap

An early prototype (without the platform), showcasing the poems with a basic search exists [here](http://poetroid.com/). After querying for a poem by title or author, the page shows the restored poem, aligned typographically, line endings intact to fit the shape of your screen. Tags and metadata can be clicked naturally to discover similar poems' metadata. An in-line, [Markdown](http://daringfireball.net/projects/markdown/) based editor with live preview, inspired from [Medium](https://medium.com/), is also available to approved curators.

The first two thousand poems were curated by hand.

The rest will be worked in conjunction with web crawlers, poets, and admirers of poetry, like you.

An alpha of Poetroid with additional *petadata*, will launch on Kickstarter, beginning 2014.

## History

Previous versions of this app were written in [Python](http://www.python.org/) and [Javascript](http://en.wikipedia.org/wiki/JavaScript), now archived, and available on request.

## Resources

- [Project Gutenberg](http://www.gutenberg.org)
— [Public Domain Poetry](http://www.public-domain-poetry.com)

## Contributers

- [Priyatam Mudivarti](www.priyatam.com): writer, engineer, and founder of [Facjure LLC](http://www.facjure.com),
- Ata Moharreri: poet, teacher, and former managing editor of [The Massachusetts Review](http://www.massreview.org/editors)
- Sreeharsha Mudivarti: musician, engineer, and survivor of a space ship crash.

If you're a developer and want to move literature forward, fork us, add new poems in the prescribed format, send a pull request.

If you're a student, poet, publisher, or an educator interested in poetry, request access by sending an email to priyatam@facjure.com and signup for a free [github](https://github.com/) account. We will help you get up and running.

Help us, let's create the world's largest open platform for poetry from the public domain.

## Copyright & License

Copyright (c) Facjure LLC. All rights reserved.

The use and distribution terms for this software are covered by [Eclipse Plugin License v 1.0]((http://opensource.org/licenses/eclipse-1.0.php)), which can be found in the file LICENSE at the root of this distribution.

By using this software in any fashion, you are agreeing to be bound by the terms of this license. You must not remove this notice, or any other, from this software.
