import writeas
import os
import json

# SET UP BEFORE RUNNING
# Add name of Write.as blog here (for ex: '365-rfcs' for 'https://write.as/365-rfcs')
collection = ''
# Add the complete folder path to your Dat blog here (for ex: '/Users/cjeller/Sites/365-rfcs-test')
path = ''

# Then the write.as business logic begins
c = writeas.client()

list = []

# I assume 200 posts is more than generous!
for i in range(1,20):
# Iterate through the pages...
    cposts = c.retrieveCPosts(collection, i)
    posts = cposts['posts']
# If the posts are not an empty list, take each post and put it in a list!
# That way it catches pages that don't have 10 posts
    if posts != []:
        for post in posts:
# Append to the list of posts
            list.append(post)
    else:
        break
# This is so that when each post added to the posts.md file, it will appear in chronological order
list.reverse()

# Now grab the metadata for each post
for p in list:
    title = p['title']
    body = p['body']
    slug = p['slug']
    date = p['created']

    blog = '{}/posts'.format(path)
    new = '{}/{}.md'.format(blog, slug)

# If post is not in the post folder, create the Markdown file
    if not os.path.exists(new):
        with open(new, 'w+') as f:
# If post has no title, just write the body into Markdown file
            if title == '':
                post = '{}'.format(body)
                f.write(post)
# Else take the title and body and create the Markdown file
            else:
                post = '# {} \n\n{}'.format(title, body)
                f.write(post)
                f.close()

# Now prepend to the index (ie: the posts.md file)
    index = '{}/posts.md'.format(path)
    with open(index, 'r') as a:
# Grab what is there already
        p = a.read()
        a.close()

# Prepend the new stuff to the file
    with open(index, 'w') as b:
# If the post has no title, use the date as the hyperlink text
        if title == '':
            b.write('\n[{}](/posts/{}.md)\n'.format(date, slug))
# Else use the title as the hyperlink text
        else:
            b.write('\n[{}](/posts/{}.md)\n'.format(title, slug))

# Append what was already there to the new stuff
# That way posts appears in order from most recent to oldest
    with open(index, 'a') as c:
        c.write(p)
        c.close()

print('Complete! Check it out!')
