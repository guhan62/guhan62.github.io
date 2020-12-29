# guhan62.github.io
My online space ... 


## Updating Coursework & Portfolio
* `<ProjectRoot>/data/courses.json` - Update Courses or College Info
* `<ProjectRoot>/data/projects.json` - Update Project Info

## Updating Reads
* `cd scripts`
* Visit `https://openlibrary.org/` and get the Book ISBN10 or ISBN13 Code. Look for editions with Book Cover Art.
* `isbs.json` - Enter the *value* under the *key **isbns***
* Run `python book_scrape.py` - Enter the relevant details of book.
* Run `python book_sorter.py` - To sort and place the books in `<ProjectRoot>/data/books.json`

## Pushing Src
* **Switch to src branch**
* Follow Git push mantra

## Publishing Site
* **Switch to master branch**
* `./deploy.sh "Commit Message (Optional)"`
[Reference](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

## References:
* [Go Templating Docs](https://golang.org/pkg/text/template/)
* [GoHUGO Docs](https://gohugo.io/documentation/)
