=================
EZLog
=================


**Easy Blog System**


简介
======

EZLog是用 `Django <https://www.djangoproject.com/>`_ 开发的个人博客系统，
也可以用来做个人网站。欢迎试用！


示例站点
=========

- http://ezlog.sinaapp.com/
- http://hoiyeung.sinaapp.com/


特性
======

- `响应式的WEB页面设计 <http://en.wikipedia.org/wiki/Responsive_web_design>`_, 能够自适应不同尺寸的屏幕

- 通过标签和分类来管理文章

- 可选择使用 Markdown_ 或者 HTML 撰写博客，并分别提供对应的编辑器组件

- 集成 `多说社会化评论框 <http://duoshuo.com/>`_

- 集成 `Google Analytics <http://www.google.cn/intl/zh-CN_ALL/analytics/>`_

- 最近访客跟踪

- 使用 `Django Grappelli <https://github.com/sehmaschine/django-grappelli>`_
  优化后台管理界面

- 使用 `Django FileBrowser <https://github.com/sehmaschine/django-filebrowser>`_
  管理上传的文件

- 层次化的页面管理

- 可配置的站点导航栏

- 通过WEB界面配置站点参数

- 站点地图


依赖关系
========

- Python2.7 或更高版本

- libxml2-dev libxslt1-dev (needed by lxml)

- libjpeg-dev libfreetype6-dev (needed by PIL)

依赖的python模块
----------------

- Django==1.4.1

- pyquery
  
- lxml>=2.3.4(needed by pyquery&compressor.parser.LxmlParser)

- BeautifulSoup<4.0(needed by compressor.parser.LxmlParser)

- django-taggit(SAE环境下需要修改代码)

- django-grappelli

- django-filebrowser

- PIL(needed by django-filebrowser)

- django-compressor

- django-mptt

- Markdown

可选模块
~~~~~~~~

- cssmin_ (used to compress css file)


测试运行
========

- 获取EZLog代码::

    $ git clone https://github.com/wonderbeyond/ezlog.git

- 安装某些python模块所需的库文件(以Ubuntu环境为例)::

    $ sudo apt-get install libxml2-dev libxslt1-dev

- 安装python模块::

    $ cd ezlog
    $ pip install -r requirements.txt

- 初始化数据库::

    $ make syncdb

  请在命令执行过程中根据提示创建超级用户。

- 搜集静态文件到 settings.STATIC_ROOT 文件夹::

    $ make collectstatic
    $ make compressstatic  #如果没有启用静态文件压缩，则不用执行该命令。

OK，现在可以测试运行了。
这里使用Django提供测试服务器来运行，请不要应用于生产环境中！
生产环境下的部署方案请参考Django文档: https://docs.djangoproject.com/en/1.4/howto/deployment/

::

    $ python manage.py runserver 8000

如果看到如下提示::

    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

说明网站运行成功！打开浏览器，访问 http://127.0.0.1:8000/ 查看效果，
访问 http://127.0.0.1:8000/admin/ 可执行后台管理, 
需要使用刚刚创建的superuser登录。

在实际使用时，请访问 http://localhost:8000/ezsettings/
并根据需要修改站点参数，在admin管理界面可以看到该链接。

.. Note:: 如果你在测试或部署EZLog时遇到了问题，
    可以先看看我的 开发笔记_
    里面有没有提到对应问题的解决方法。
    也可以在新浪微博上 `@workwonder <http://weibo.com/wber>`_ 向我反馈,
    或者在这里留言: http://ezlog.sinaapp.com/20/#comments.


配置
====

设置 sites.site
-----------------

为了保证各个模块获得正确的信息（比如站点地图要生成网站的链接），
请访问 http://localhost:8000/admin/sites/site/,
然后把域名 *example.com* 修改为你正在使用的域名。

Django settings
----------------

EZLog项目中，settings.py被拆分成一个包，由__init__.py负责导入所有设置。

- base.py: 提供基本设置，优先级最低

- for_heroku.py: 提供针对Heroku环境的设置

- for_sae.py: 提供针对SAE环境的设置

- dev.py: 提供特定于测试环境下的设置

- production.py: 提供特定于生产环境下的设置

- switcher.py: 用来切换生产环境和测试环境的设置

- local.py: 提供你针对自己网站的设置，优先级最高


配置 django settings
~~~~~~~~~~~~~~~~~~~~~

请在 ezlog/settings/local.py 中配置自己的django settings.
在 local.py 中出现的配置项将会覆盖 base.py 中相同项目的默认值。
  
可以执行如下命令根据样例创建local.py::

      $ cp ezlog/settings/local.sample ezlog/settings/local.py

具体django有哪些可配置的项目，请参考 `Django settings文档
<https://docs.djangoproject.com/en/1.4/topics/settings/>`_

下面这些配置项特定于EZLog自身的：

- MARKUP_LANGUAGE: 撰写Blog时使用的标记语言，
  可选择 "markdown", "html". 并会分别为它们提供友好的在线编辑器。
  你也可以选择使用其它标记语言，比如 restructuredtext,
  但需要在 MEDIA_FOR_POST_EDITOR 中指定创建对应在线编辑器
  所要使用的JS和CSS文件。

- MEDIA_FOR_POST_EDITOR：创建在 MARKUP_LANGUAGE
  中设置的标记语言对应的在线编辑器所需要的css和js文件。
  
  设置示例如下，其中css和js的URL是相对于 MEDIA_URL 的。

  ::

        MEDIA_FOR_POST_EDITOR = {
            'html': {
                'js': ('ckeditor/ckeditor.js',
                       'ckeditor/config.js',
                       'js/ckeditor-setup.js',
                       'filebrowser/js/FB_CKEditor.js',
                      ),
                'css': (),
            },

            'markdown': {
                'js': ('wmd/showdown.js',
                       'wmd/wmd.js',),
                'css': ('wmd/wmd.css',),
            },

            'restructuredtext': {
                'js': (),
                'css': (),
            }
        }


下面这些配置项是一些依赖模块用到的：

- COMPRESS_ENABLED：启用静态文件压缩功能。
  启用后，请在部署前执行 `make compressstatic` 命令压缩静态文件。



EZLog 设置
----------

除了Django settings, EZLog自身还包括了一个灵活的配置管理模块。

EZLog的配置管理模块提供了一个友好的WEB界面来动态配置站点参数，
URL是 */ezsettings/*.

可以配置的项目包括:

- 站点标题

- 站点箴言：显示在站点标题附近

- 公告信息：将显示在公告板中，置空则不显示公告板

- 多说短域名：多说短域名。
  EZLog集成了多数社会化评论系统，你可以到这里
  http://duoshuo.com/create-site/
  申请一个多说短域名为你的网站接入多说评论服务。


TODO
====

- add full **toc** support for blog entry


.. _开发笔记: https://github.com/wonderbeyond/ezlog/blob/master/doc/dev_notes.rst
.. _Markdown: http://zh.wikipedia.org/wiki/Markdown

.. _cssmin: https://github.com/zacharyvoase/cssmin
