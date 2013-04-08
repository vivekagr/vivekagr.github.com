# Hello World

- date: 2013-04-03
- tags: blogging

----------------------

So, I finally decided to start blogging. The obvious solution was to use Wordpress as I have in the past for other sites. But I wanted to try something else this time. Github Pages for free hosting was very enticing but that can only serve static files which meant I had to use a static blog generator.

[Jekyll](https://github.com/mojombo/jekyll) is kind of popular these days with a lot of features. But it's written in Ruby (which I don't know at this point) and I'm a Python guy, so I looked for other options so that I can easily modify the code to suit my needs. [Pelican](https://github.com/getpelican/pelican) seemed good and to try it out, I started porting my Scala notes from Evernote to markdown format. I had a few questions and Justin was out there on freenode at #pelican to assist me. It was all good, until I discovered [Nikola](http://nikola.ralsina.com.ar/) which seemed much better and simple than Pelican. It also supported markdown format so I had to change basically nothing to try out my notes on Nikola. There were many themes to choose from and it looked wonderful. But there was no category support in Nikola. Sigh, I had to start looking for something else.

Fast forward a few days, I stumbled upon [this post](http://tshepang.net/favorite-pelican-themes) while searching for themes for Pelican and Nikola. But his blog was using something else and it was looking very good. It was [Felix Felicis](http://lab.lepture.com/liquidluck/) (in case you don't know, the [term](http://harrypotter.wikia.com/wiki/Felix_Felicis) is from Harry Potter universe which means liquid luck potion). I had found the perfect static blog generator I was looking for. Setting it up was quick since it is not cluttered with too many useless features, straight to the point and also supports markdown format for posts.

The domain was hosted on a shared Hostgator account with MX entries for Google apps. To use this domain with Github, I made an A record pointing to the IP address provided by Github and the MX entries (again) on the domain registrar's end (since I wanted to get rid of dependency on Hostgator which was useless at this point).

Deciding to go with static blog generator in place of Wordpress sure took much longer than I anticipated but I hope it'll be worth it in the long run.