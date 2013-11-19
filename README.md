# Curate Poems Together

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

Poetroid is built using an open-source platform to discover poetry together. Currently in *research & development*, this platform will bring together web, print, and mobile distribution of public domain poetry in a unified language, written in [Clojure](http://clojure.org).

The platform will include web crawlers in conjunction with poets, students, and publishers helping us to build the world's largest open poetry library, together.

For more information, visit [Poetroid](http://poetroid.com/#/page/about.md).

## Resources

- [Project Gutenberg](http://www.gutenberg.org)
- [Public Domain Poetry](http://www.public-domain-poetry.com)

## Contributers

- Priyatam Mudivarti: writer, engineer, and founder of [Facjure LLC](http://www.facjure.com)
- Ata Moharreri: poet, teacher, and former managing editor of [The Massachusetts Review](http://www.massreview.org/editors)
- Sreeharsha Mudivarti: musician, engineer, and survivor of a space ship crash.

If you're a developer and want to move literature forward, [fork](https://help.github.com/articles/fork-a-repo), add new poems, send a [pull](https://help.github.com/articles/using-pull-requests) request.

If you're a student, poet, publisher, or an educator interested in poetry, request access by sending an email to priyatam@facjure.com and signup for a free [github](https://github.com/) account.

We'll help you get up and running.

## Copyright & License

Copyright (c) Facjure LLC. All rights reserved.

The use and distribution terms for this software are covered by [Eclipse Plugin License v 1.0]((http://opensource.org/licenses/eclipse-1.0.php)), which can be found in the file LICENSE at the root of this distribution.

By using this software in any fashion, you are agreeing to be bound by the terms of this license. You must not remove this notice, or any other, from this software.
