# Poetroid - Discover Poetry Together

There are tens of thousands of poems in the public domain, and yet no single repository for humans and machines.

Let's build one.

## Overview

Poems are written in plain text in [UTF-8](http://en.wikipedia.org/wiki/UTF-8) format to preserve foreign & special characters across machines.

```
Every time I say "joy," joyous thing, 
you will know that I am talking about you, 
for you are the joy of all joyous beauty 
and the joy of all joyous and beautiful pleasures,
```

Metadata will be written inline for storing tags and semantic analysis to inform humans and machines with more data for further analysis. 

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
 
This format might soon change to [edn](https://github.com/edn-format/edn), at which point, old poems will automatically be upgraded.

The format, the poems, the metadata, and all their revisions are protected in git forever and available for free so no one can break in.
 
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

## Platform

Poetroid is a platform, currently in active development, built to search, discover, and share poetry together. It's written entirely in [Clojure](http://clojure.org/) and [Clojurescript](https://github.com/clojure/clojurescript) and can hence, run on any virtual machine like android, mac, or pc, or any modern browser like firefox, safari, and chrome. In short, it's built for web, mobile, and print.

Once a larger repository of poems exist they will be fed into our [ai](http://en.wikipedia.org/wiki/Artificial_intelligence) engine running on the cloud, clustered and distributed across nodes, where each node analyzes, transforms, and writes a taxonomy of poetry built by artists and poets. An early prototype (no ai server), showcasing the poems with a basic search exists [here](http://poetroid.com/). It shows a poem per page, line endings saved, aligned typographically to the size of your screen. Tags and metada can be clicked naturally to discover similar poems' metadata. An in-line, [markdown](http://daringfireball.net/projects/markdown/) based editor with live preview, inspired from [Medium](https://medium.com/), is also available to approved curators.

## Status, Roadmap

Previous versions of this app (now arhived), written in [Python](http://www.python.org/) and [Javascript](http://en.wikipedia.org/wiki/JavaScript), are available on request.

The repo and the poetroid platform is currently in *research & development*.

An early set of poems were curated by hand. Web crawlers we built are now busy scraping the rest from the public domain. 

An alpha will launch on Kickstarter, early 2014.

## Resources

- [Project Gutenberg](http://www.gutenberg.org)
— [Public Domain Poetry](http://www.public-domain-poetry.com)

## Contributers

- [Priyatam Mudivarti](www.priyatam.com): writer, engineer, and founder of [Facjure LLC](http://www.facjure.com), 
- Ata Moharreri: poet, teacher, and former managing editor of [The Massachusetts Review](http://www.massreview.org/editors)
- Sreeharsha Mudivarti: musician, engineer, and survivor of a space ship crash.

If you're a developer and want to move literature forward, fork us, add new poems, send a pull request.

If you're a poet, publisher, or educator, or student interested in poetry, request access by sending an email to priyatam@facjure.com and signup for a free [github](https://github.com/) account. We will help you get up and running.

Help us, please, to create the world's largest open platform for poetry from the public domain and *beyond*.

## Copyright & License

Copyright (c) Facjure LLC. All rights reserved.
 
The use and distribution terms for this software are covered by [Eclipse Plugin License v 1.0]((http://opensource.org/licenses/eclipse-1.0.php)), which can be found in the file epl-v10.html at the root of this distribution.

By using this software in any fashion, you are agreeing to be bound by the terms of this license. You must not remove this notice, or any other, from this software.
