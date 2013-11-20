# Curate Poems Together

Thousands of poems in the public domain are burried in sites, yet we don't have a central library for humans or machines.

Let's build one.

## Overview

To restore poems, we need a new format that can be read by humans and machines alike.

[Plain Text](http://en.wikipedia.org/wiki/Plain_text) is an excellent format supported by most editors by default: notepad, textedit, [iAWriter](http://www.iawriter.com/mac/), and others, as long as they're saved in [UTF-8](http://en.wikipedia.org/wiki/UTF-8) 'encoding'--a setting available as options in the 'Save As' file-dialog. Saving a file in UTF-8 is a necessary, important step to preserve foreign-language characters across machines.


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

This format may change soon to [edn](https://github.com/edn-format/edn), and old poems will be upgraded, automatically.

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

This library will include scripts to help scholars, students, publishers, and developers working together to build an open poetry library for print and web, together.

## Status and Roadmap

Currently in *research & development*. 

This work is being done in parallel to Poetroid, an open platform to discover poetry together with a unified [api](http://en.wikipedia.org/wiki/Application_programming_interface) for web, mobile, and print.

A basic prototype (without the platform), showcasing two thousand poems exists [here](http://www.poetroid.com). It is being used internally by our editors and continuous integration of content, code, design, on the fly.

When a poet searches for a poem by title or author, the page shows the restored poem, aligned typographically, line endings intact, to fit the shape of their screen. Tags and metadata can be clicked naturally to discover similar poems' metadata. An in-line, Markdown based editor with live preview, inspired from Medium, is also available to approved curators.

For more information, visit [Poetroid](http://poetroid.com/#/page/about.md).

## Resources

- [Project Gutenberg](http://www.gutenberg.org)
- [Public Domain Poetry](http://www.public-domain-poetry.com)

## Contributers

- Priyatam Mudivarti: writer, engineer, and founder of [Facjure LLC](http://www.facjure.com)
- Ata Moharreri: poet, teacher, and former managing editor of [The Massachusetts Review](http://www.massreview.org/editors)
- Sreeharsha Mudivarti: musician, engineer, and survivor of a space ship crash.

If you're a developer,[fork](https://help.github.com/articles/fork-a-repo), add new poems, and send a [pull](https://help.github.com/articles/using-pull-requests) request.

If you're a scholar, student, or publisher interested in curating poetry, request access by sending an email to priyatam@facjure.com, and signup for a free [github](https://github.com/) account. We'll help you get up and running with scripts, editors, and even a browser interface.

## Copyright & License

Copyright (c) Facjure LLC. All rights reserved.

The use and distribution terms for this software are covered by [Eclipse Plugin License v 1.0]((http://opensource.org/licenses/eclipse-1.0.php)), which can be found in the file LICENSE at the root of this distribution.

By using this software in any fashion, you are agreeing to be bound by the terms of this license. You must not remove this notice, or any other, from this software.
