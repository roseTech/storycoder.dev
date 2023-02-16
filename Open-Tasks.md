
Something everyone can do all the time:

- Add a script (a piece of code) to an existing story in any programming language you like. If there is already a script for your programming language, you can still add your own if the implementation differs. But please do not overwrite existing scripts.
- Fix typos or grammatical errors in existing stories.
- Improve the readability of the story, without changing its content or its solutions. Do not change the content of the story, without getting in contact with the author first and/or discuss this on the storycoder.dev Discord server.

# Content

- [ ] Set tags and licenses for all stories
- [ ] Add at least one solution to all stories
- [ ] Add a few hints to all stories
- [ ] Proofread at least all stories once
- [ ] Check if the existing scripts, really solve the problem correctly, according to the solution in the story (if not get in contact with the author, try to fix it, or if not possible, delete the solution after a grace period)

# Front-End

The Front-End currently uses WordPress.

- [ ] Overview for all stories
- [ ] Remove the old stories which were depending on WooCommerce
- [ ] Disable/uninstall unnecessary plugins (WooCommerce, ...)
- [ ] Copy theme from practicecoding.dev
- [ ] Footer on all posts/stories
- [ ] Update plugins (this may be a recurring topic)
- [x] Create playground for testing practicecoding.dev

# Back-End

The Back-End is currently a bunch of JavaScript files, which update WordPress pages and posts.

https://github.com/roseTech/storycoder.dev-backend

- [ ] Update certain WordPress Pages automatically from GitHub (has to be decided which ones)
- [ ] Add the possibility to not show all hints at once
- [ ] Generate https://github.com/neonbjb/tortoise-tts TTS MP3
- [ ] Setup a GitHub action which automatically updates WordPress whenever the main branch of GitHub is updated
- [ ] Use a bit more styling from the template story from practicecoding.dev
- [x] Generate https://coqui.ai TTS MP3
- [x] Generate tags within WordPress
- [x] Upload/link additional images added to stories
- [x] Add a link to every story for translation

# Wishlist

Not decided how to implement.

- [ ] Gamification
- [ ] Translate the stories (cost for deepl are too big at the moment)
