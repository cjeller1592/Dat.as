# Dat.as
A script to export your Write.as blog to the p2p web via Beaker Browser

Beaker Browser, the premiere Dat protocol browser, has this nifty feature of rendering Markdown within it. This allows you to create your own Markdown sites which look awesome. Their [guide](https://beakerbrowser.com/docs/guides/create-a-markdown-site) inspired me to find a way to take my Write.as blog and put it on the p2p web. The script is such an attempt!

## Examples
Check out what the end result looks like with the following blogs. The one's other than my own are tests and not a reflection of their author's intent:

dat://cjeller.hashbase.io

dat://365-rfcs-test.hashbase.io

dat://matt-test.hashbase.io

## Dependencies

1) Write.as API Client Library
```
pip install writeasapi
```

2) [Beaker Browser](https://beakerbrowser.com/)

## Getting Started

1) Open up Beaker Browser. Click on the top right tab  to Create New -> Empty Project. Open your new project and name it however you'd like.

2) Now click the '+' and 'Create File' within your project to add 'index.md'. This will act as your home page for your blog. Edit however you wish.

3) Click the '+' and 'Create File' again to add 'posts.md'. Leave it blank. This will act as the place for all your posts to be listed.

4) Guess what? We are clicking that '+' again to create 'nav.md'. Edit the file and we will add links like this:

```
[Home](/index.md)

[Posts](/posts.md)

```
This will act as a navigation bar so that no matter where you are on the blog, you can access the home and posts page.

5) One more thing to add! Click '+' and 'Create Folder'. Name the folder 'posts'. This will be where all the posts live once exported.

6) Now we need to set up the blog so that our script will reflect changes on it. From the top tab go to 'Settings' and click 'Set Local Folder' to whatever you want.

7) Copy that path. Go into the script and replace the empty path with the one you just copied.

8) Now add the collection name of your Write.as blog to the script. For https://write.as/matt, the collection would be 'matt'. 

9) Save the script and run it! Go to your settings and note the unpublished changes. That means the script worked! Click into the Unpbulished changes and confirm them.

10) Now check out your Write.as blog on the p2p web!!! Note that you can run this script again and again to update your blog with each new post you add from Write.as.
