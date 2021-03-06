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
            'name': 'Vivek Agarwal',
            'website': 'http://vivek.im',
            'email': 'me@vivek.im',
        }
    }
}

#: active readers
reader = {
    'active': [
        'liquidluck.readers.markdown.MarkdownReader',
        'liquidluck.readers.restructuredtext.RestructuredTextReader',
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
    'name': 'default',
    'vars': {
        'disqus': 'vivekagr',
        # 'analytics': '',
        'allow_comment_on_secret_post': True,

        'navigation': [
            # {'title': 'Blog', 'link': '/archive'},
            # {'title': 'Life', 'link': '/life/'},
        ],
        'elsewhere': [
            {'name': 'GitHub', 'link': 'https://github.com/vivekagr'},
            {'name': 'Contact', 'link': 'mailto:me@vivek.im'},
        ],
    }
}
