# Static-site-generator

Built for a [guided project](https://www.boot.dev/courses/build-static-site-generator-python)
on [boot.dev](https://www.boot.dev?bannerlord=vilebile17)

## Usage

**Step 1** - Clone the repo

```bash
git clone https://github.com/vilebile17/Static-site-generator
```

**Step 2** - Static files

Place all **none-markdown** files inside of the `/static` directory. These will
all be copied over to the `/docs` directory. Feel free to use sub-directories
inside of it, e.g. `/static/images/cool_img.png`

**Step 3** - Markdown files

Place all of the **markdown (.md)** files into the `/content` directory.
Again, sub-directories are permitted and those will create sub-pages.
E.g. `/contact` or `/blog/blog-post1`. Note that for these sub-pages
to work, each directory will need it's own `index.md` files. Take
a look at the current `content` directory as a reference

**Step 4** - Generation

This is the last step! All you need to do is to run one of the `.sh` scripts.
If you're forking and going to have the site set up on github pages, then
run `build.sh` which will build all of the `.html` files and store them in
`/docs` accordingly.

If however, you just want to run the site locally, just run `main.sh` which
will host the site on `localhost:8888`
