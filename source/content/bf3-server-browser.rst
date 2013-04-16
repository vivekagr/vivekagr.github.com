About BF3 Server Browser I wrote
==========================================

:date: 2013-04-15
:tags: games, python


Recently I wrote a `Battlefield 3 server browser application`_ in Python. With over `330 hours logged`_ in Battlefield 3, I think its fair to say that I play it a lot (though not much since I found programming to be more fun). I'm on a 512kbps connection with the country's worst ISP so I always have to look for servers with lowest ping time. Half of the times, I'm unable to play and keep getting either timed out or kicked out of servers for having high ping. And being on a slow connections creates another problem. Battlefield 3's web browser based server browser takes too long (10-30 seconds) to load and then the ping function isn't called for some reason. So, I always had to copy the server IP addresses and manually ping them via command prompt.

I started learning Python in January 2013, so I thought of using my newly acquired skills to do myself some good. I tried implementing the ping function with the help of `subprocess`_ module. But routing each request via different processes and parsing out the result was very slow and inefficient. I looked for pure ping implementation in Python but couldn't find any and eventually forgot about this idea. After a couple of weeks, I came across `this gist`_ and began working on the project. First, I made a `Flask`_ based interface over the core functions and it worked well. But running the python script each time over the cmd felt cumbersome (even more so on Windows). Then I remembered getting a Python GUI development course coupon on `this reddit thread`_ months ago. Bogdan Milanovich gave away `his course`_ for free. I started going through the videos and then worked on making the GUI. The course videos were fantastic.

`PySide`_ (Python bindings to the Qt framework) was used during the course. There also exists `PyQt`_ which is more mature than PySide and similar to it. The major difference being the license, PySide is under LGPL and PyQt under GPL (discussed in-depth `here`_). I didn't spend time choosing one between the two and just went with the course's choice. Qt Designer (part of Qt Creator) is an amazing tool to quickly design the GUI which can then be used in any language which has bindings for Qt. I could have used it to ease the process and just incorporated it with previously written core part, but I chose to code everything by hand. Having recently learned Python, I wanted to write as much as I could in it and also, I wanted to get familiar with Qt. Even though PySide is not that mature and parts of it's documentation are incomplete, it wasn't that hard to find the answers. For most of the queries, I got back the answer for PyQt and C++ versions, but since the classes and methods are very similarly named, it was not a problem. This `blog post`_ praises About and describes why Qt rocks. I also tried TkInter and wxPython GUI frameworks but PySide felt much better than both of these.

For showing the results, I used the Jinja2 template I earlier made for the Flask based interface. I couldn't find any good way to show the result within the application itself. Using the table widgets provided by Qt wasn't good enough. Also, one would still need to open browser to join the game server. So why not just show the result in the browser itself and reduce the distance between the result page and server join page.

For freezing a python script into a standalone executable, there are quite a few options like `cx_Freeze`_, `py2exe`_ and `PyInstaller`_. PyInstaller seemed to be the best choice for freezing Qt applications. It produced the smallest sized exe, of around 11MB containing the script, Python itself and necessary Qt files. I will cover this part in depth in another post. With cx_Freeze, freezing especially Qt apps isn't straightforward. I wasn't able to properly do it after spending an hour and still the output exe was well over 30MB in size (I assume that even after getting it to work, it wouldn't shrink down).

And just to make it a complete package, I used `Inno Setup`_ to make the installer. Finally, to distribute the binaries I uploaded them to SourceForge.net. I really wish Github had the option to upload binaries. Well they had but `it was deprecated`_. I hope it comes back in future.

One thing I learned is that it takes more effort to design the user interface than to build the core part of a software. Actually I learned many other things too while making this. It can scrape data for and ping 500 servers under a minute on my sluggish connection. I don't think anyone uses it except myself and a friend of mine but still I'm incredibly proud of it.

Source and download links are available at - https://github.com/vivekagr/bf3sb


.. _Battlefield 3 server browser application: https://github.com/vivekagr/bf3sb
.. _330 hours logged: http://battlelog.battlefield.com/bf3/soldier/mpheus/stats/372749077/
.. _subprocess: http://docs.python.org/2/library/subprocess.html
.. _this gist: https://gist.github.com/pklaus/856268
.. _Flask: https://github.com/mitsuhiko/flask
.. _this reddit thread: http://redd.it/14453f
.. _his course: https://www.udemy.com/python-gui-programming
.. _PySide: http://qt-project.org/wiki/Category:LanguageBindings::PySide
.. _PyQt: http://www.riverbankcomputing.com/software/pyqt/intro
.. _here: http://www.devilsan.com/1/post/2013/01/choosing-between-pyside-or-pyqt-license-consideration.html
.. _blog post: http://www.codinguser.com/2012/07/i-miss-qt-or-what-cute-documentation-looks-like/
.. _cx_Freeze: http://cx-freeze.sourceforge.net/
.. _py2exe: http://www.py2exe.org/
.. _PyInstaller: http://www.pyinstaller.org/
.. _Inno Setup: http://www.jrsoftware.org/isinfo.php
.. _it was deprecated: https://github.com/blog/1302-goodbye-uploads
