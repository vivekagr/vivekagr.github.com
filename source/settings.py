# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
site = {
    'name': 'vivek agarwal',
    'url': 'http://vivek.im',
    # 'feed': '',
}

config = {
    'source': 'content',
    'output': '../',
    'static': '../static',
    #'static_prefix': '/static/',
    'permalink': '{{date.year}}/{{filename}}',
    'relative_url': False,
    'timezone': '+05:30',
}


author = {
    'default': 'vivekagr',
    'vars': {
        'vivekagr': {
            'name': 'Vivek agarwal',
            'website': 'http://vivek.im',
            'email': 'me@vivek.im',
        }
    }
}

#: active readers
reader = {
    'active': [
        'liquidluck.readers.markdown.MarkdownReader',
        # 'liquidluck.readers.restructuredtext.RestructuredTextReader',
    ],
}

#: active writers
writer = {
    'active': [
        'liquidluck.writers.core.PostWriter',
        'liquidluck.writers.core.PageWriter',
        'liquidluck.writers.core.ArchiveWriter',
        'liquidluck.writers.core.ArchiveFeedWriter',
        'liquidluck.writers.core.FileWriter',
        'liquidluck.writers.core.StaticWriter',
        'liquidluck.writers.core.YearWriter',
        'liquidluck.writers.core.CategoryWriter',
        'liquidluck.writers.core.CategoryFeedWriter',
        'liquidluck.writers.core.TagWriter',
        # 'liquidluck.writers.core.TagCloudWriter',
    ],
    'vars': {
        # 'archive_output': 'archive.html',
    }
}

#: theme variables
theme = {
    'name': 'moment',
    'vars': {
        # 'disqus': 'your_short_name',
        # 'analytics': 'UA-21475122-1',
        'allow_comment_on_secret_post': True,

        'navigation': [
            # {'title': 'Blog', 'link': '/archive'},
            # {'title': 'Life', 'link': '/life/'},
        ],
        'elsewhere': [
            {'name': 'GitHub', 'link': 'https://github.com/vivekagr'},
            {'name': 'Contact', 'link': 'mailto:me@vivek.im'},
        ],

        'descriptions': {
            'life': u'生命是一襲華美的袍，爬滿了虱子 －－ 張愛玲',
            'work': 'works in python, javascript, vim, and everything else'
        },
    }
}
