# Poetroid - Discover Poetry Together

There are tens of thousands of poems in the public domain, yet no single repository. Let's build one.

## Spec

Poems are written in plain text in [UTF-8](http://en.wikipedia.org/wiki/UTF-8) format to preserve foreign & special characters.

```
Every time I say "joy," joyous thing, 
you will know that I am talking about you, 
for you are the joy of all joyous beauty 
and the joy of all joyous and beautiful pleasures,
```

Metadata will be associated with [YAML](http://en.wikipedia.org/wiki/YAML), another plain text format, for storing tags and addititonal info on the poem. These metadata inform the nature of poem for further analysis by humans or machines. 

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

If the format changes, which should occur rarely, to something ike [edn](https://github.com/edn-format/edn), then the format must be compatible with YAML, to upgrade the old poems to new.

The format, the poems, the metadata, and their revisions are protected in git forever for free so no one can break in.

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

## Poetroid Platform

Poetroid is a platform built to search, discover, and share poetry together. 

It's written entirely in [Clojure](http://clojure.org/) and [Clojurescript](https://github.com/clojure/clojurescript) and can hence, run on any virtual machine like android, mac, or pc, or any modern browser like firefox, safari, and chrome. In short, it's built for web, mobile, and print (more on this later).

Once a large repository of poems are entered, they will be fed into our [ai](http://en.wikipedia.org/wiki/Artificial_intelligence) engine, poetroid, running on the cloud, clustered and distributed across nodes, where each node analyzes, transforms, and writes a taxonomy of poetry built by artists and poets.

An early prototype, showcasing the poems with a simple search engine (no ai) exists [here](http://poetroid.com/). Petroid shows a poem per page, line endings saved, aligned typographically to thne size of your screen. There's also an in-line, markdown based editor with live preview available to curators and educators. They can edit a poem in the above raw format, save, and view the updated poem on the site in 30 seconds or less. 

An early version of this app, written in [Python](http://www.python.org/) and [Javascript](http://en.wikipedia.org/wiki/JavaScript), is available on request.

## How to become a Curator

If you're interested in becoming a curator, request access by sending an email to priyatam@facjure.com and signup for a free [github](https://github.com/) account.

## Status & Roadmap

The repo and the poetroid platform is currently in *research & development*.

An early poems were curated by humans. Currently, we're writing web crawlers to scrape poems from the public domain. The alpha will launch on Kickstarter in early 2014.

## Resources

- [Project Gutenberg](http://www.gutenberg.org)
— [Public Domain Poetry](http://www.public-domain-poetry.com)

## Contributers

- [Priyatam Mudivarti](www.priyatam.com): writer, engineer, and founder of [Facjure LLC](http://www.facjure.com), 
- Ata Moharreri: poet, teacher, and former managing editor of [The Massachusetts Review](http://www.massreview.org/editors)
- Sreeharsha Mudivarti: musician, engineer, and survivor of a space ship attack.

If you're a developer who wants to move literature forward, and interested to join, fork us, send a pull request.

If you're a poet, publisher, or educator, help us in creating the world's largest open platform for poetry.

## Copyright & License

Poetroid is built by Facjure LLC, released under the Opensource Eclipse Plugin License v 1.0. Your use of this repo is subject to terms and conditions on the license.
