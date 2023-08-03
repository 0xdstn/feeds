# Feeds

I previously decided to use an app on my computer to subscribe to RSS feeds with the intent of logging on once a week or so to read any posts. I kept not doing this, so I decided to create my own tool. This is a feed reader that generates HTML files of the post contents.

This is by no means top quality coding, it was thrown together to solve a problem.

This requires PHP and python to run.

**Project page:** [l:https://tilde.town/~dustin/projects/feeds](l:https://tilde.town/~dustin/projects/feeds)

## Setup

Place the contents of the repo in a directory called **feeds** inside your root web directory (such as **/var/www/html/feeds**).

Create a `key.txt` file one directory up from your root web directory (such as **/var/www**). _This should not be accessible via a browser_.

Create a `data.txt` file and a `feeds.txt` file in the feeds directory.

Set up a cron job for the scraper. I have it set up to run every hour like so:

```
% 0 * * * * cd /var/www/html/feeds && ./scrape.py >/dev/null 2>&1
```

The cron job takes any URL that hasn't been scraped in `data.txt`, pulls the title and the contents for it via web scraping, updates `data.txt` with the title, and generates an HTML file of the contents in the `articles` directory.

## Usage

Navigating to the **/feeds?key=YOURKEY** directory on your webserver will display a list of articles from `data.txt`. Replace **YOURKEY** with the contents of the `key.txt` file. If the articles have been added, it will display the titles and link to the local HTML file for it.

You can subscribe to a feed by clicking **Add feed**, which will give you a box to fill in a URL and a submit button. This adds the provided URL to `feeds.txt`.

When reading an article, there is a **mark read** link at the top and bottom which you can click to mark it as read, removing it from the list on the index page.

This app is really light weight, so it works well in the web browser of a kindle.
