# Poems

Curated poems from the public domain. Written in markdown.

## Workflow

Editor logins into [prose.io](http://prose.io/#Facjure) and creates a new file. Each file consists of a poem
based on markdown syntax, along with YAML frontmatter that contains basic meta data.

Editor saves the poem and logs out of the app or creates ten other poems the same way.

A github hook picks up a new save and run jekyll generate. This process does a few steps:
1. For each file it creates a post under /_posts/ with a data-id-50-char-title filename. 
2. The filename is parsed with default makrdown converter except for the following exceptions: it adds two white space
 at the end of a line and ignores formatting four or more whitespaces at the beginning of each line.
3. A site is generated out of the base template. Th site lists all authors, sorted by alpha, on home page 
   with a count in the bracket. 
4. Clicking on each link should fetch a paginated view of ten poems. 
5. This poem should be responsive.
6. There should be simple text based search to look for duplicates.


