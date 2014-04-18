# Public Domain Poetry

Thousands of poems in the public domain live buried in school libraries, archaic websites, journals gone out of print. We don't have a free, unified access. An open library.

Let's build one.

## Overview

Three parts: format, metadata, scripts.

1. Restore poems with a new format: for humans and machines.
2. Curate poems adding metadata, inline: humans and machines.
3. Run scripts to find, see, and print poem, offline.

### Poem format

See [Zendown](https://github.com/poetroid/zendown).

## Scripts

Scripts provide a convenient way to read, evaluate, and print the results of a single, or a directory of poems.

They require Python 2.7.x and pip to manage dependencies. Detailed installation instructions
are beyond the scope of this document. However if you're a web developer and have a mac, get
[brew](http://brew.sh/), and run `brew install python` and you're ready to go.

If you're on linux you already know what to do.

## Status

40k poems available in this git repo. However future poems will be curated in [Elasticsearch](http://elasticsearch.org/) for better scalability, and realtime performance characteristics.

## Contributers

Thanks to the original sites that curated thousands of poems from the public domain:

- [Project Gutenberg](http://www.gutenberg.org)
- [Public Domain Poetry](http://www.public-domain-poetry.com)

- Priyatam Mudivarti: writer, engineer, and founder of [Facjure LLC](http://www.facjure.com)
- Sreeharsha Mudivarti: musician, programmer, and survivor of a space ship crash.
- Ata Moharreri: poet, professor, and former managing editor of [The Massachusetts Review](http://www.massreview.org/editors)

## Copyright & License

Copyright (c) Facjure LLC. All rights reserved.

Poems are available for free for personal or commerical use, provided [Zendown's](https://github.com/poetroid/zendown/blob/master/LICENSE) BSD-style license is retained.

Scripts are available for free using Apache 2 Opensource License.
