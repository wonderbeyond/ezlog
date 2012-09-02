;"use strict";
if(!window.console){window.console={log:function(){}};}

// 简单的字符串格式化方法:
// Example: "{0}, {1}".format("Hello", "world");
String.prototype.format = function() {
    var context = arguments;
    /* replace 的第二个参数是一个函数, 其返回的字符串将作为替换文本. */
    return this.replace(/\{(\d+)\}/g, function(_match,index,_occur) {
                            return context[index];
                        } );
};

jQuery.extend({
    scrollTo: function($elem, duration) {
        // (垂直)滚动到指定元素位置
        // Usage: $.scrollTo($('selector'))
        if(!duration) {
            duration = "fase";
        }
        var offset = $elem.offset();
        if( jQuery.browser.webkit || jQuery.browser.mozilla ) {
            jQuery('html,body').animate({scrollTop: offset.top}, duration);
        } else {
            jQuery(document).scrollTop(offset.top);
        }
        return this;
    }
});

jQuery.fn.extend({
    locate: function(duration) {
        // 定位到当前元素
        jQuery.scrollTo(this, duration);
        return this;
    },

    appear: function() {
        // 如果元素不在可视范围内, 则通过滚动使其可见
        // 尚未实现, 调用 locate 替代
        $(this).locate();
        return this;
    }
});

// copied from huanpub/pub/static/js/pub/ware.js
function plain2html(text) {
    return text.replace(/([a-zA-z]+:\/\/[^\s]*[\w\/])/g, '<a href="$1" target="_blank">$1</a>')
               .replace(/(.+[\n]+)/gm, '<p>$1</p>');
}

(function($){
    /** 可放大展示的图片, 应用于img标签. **/

    // 获取(创建)用来展示图片的元素
    var $hungOut = $('#hung-out');
    if(! $hungOut.length) {
        // 初次创建展示框
        $hungOut = $('<div id="hung-out"><div class="mask"></div><img/></div>').css({
            'display': 'none'
        });

        $(document).ready(function(){
            $hungOut.appendTo($('body'));
        });
    }
    var $img = $hungOut.find('img');

    var doHangOut = function() {
        // 图片加载后...
        $img.data('src-node').removeClass('loading');
        console.log('Now hang out!');

        var scrollTop = $(document).scrollTop();
        var wWidth  = $(window).width();
        var wHeight = $(window).height();
        var iWidth  = $img[0].width;
        var iHeight = $img[0].height;

        var imageDiaplayWidth = Math.min(iWidth, wWidth*0.9);
        var imageToTop = wHeight>iHeight? (scrollTop+(wHeight-iHeight)*0.38): (scrollTop+10);
        var imageToLeft = wWidth>iWidth? (wWidth-iWidth)*0.45: 6;

        $hungOut.css({
            'width': '100%',
            'height': $(document).height()
        });
        $img.css({
            'top': imageToTop,
            'left': imageToLeft,
            'width': imageDiaplayWidth
        });
        $hungOut.show();
    };

    $img.load(function(){
        console.log('img loaded');
        doHangOut();
    });

    $.fn.magnifiable = function(opts) {

        var settings = $.extend({
            'loadingCallback': $.noop,
            'loadedCallback': $.noop
        }, opts);

        $hungOut.bind('click keyup', function() {
            console.log('Destroy...');
            $(this).hide();
        });

        return this.click(function() {
            var $srcNode = $(this);
            var origSrc = $srcNode.data('orig-src') || $srcNode.attr('src');
            $img.data('src-node', $srcNode);

            if($hungOut.find('img').attr('src') == origSrc) {
                console.log("Just re display");
                doHangOut();
            } else {
                console.log('loading...');
                $srcNode.addClass('loading');
                settings.loadingCallback();
                $img.attr('src', origSrc);
            }
        });
    };
})(jQuery);

(function($){
    $.fn.pagination = function(num_pages, current_page, current_url, opts){
        var settings = $.extend({
            page_arg: 'page', // URL中指定页面的参数名
            num_display_pages: 10 // 共显示的页面链接数
        }, opts);

        if(this.length > 1) {return false;}

        var page_arg = settings.page_arg;
        var num_display_pages = settings.num_display_pages;

        var $pagination = $('<ul/>').appendTo(this);

        console.log('Total pages:', num_pages,
                    'Current page:', current_page,
                    'Display pages:', num_display_pages);

                    if(num_pages <= 1) {return false;}

                    var pg_from = current_page - parseInt(num_display_pages/2);
                    if(pg_from < 1) {
                        pg_from = 1;
                    }
                    console.log('From:', pg_from);

                    var pg_to = pg_from + num_display_pages - 1;
                    if(pg_to > num_pages){
                        pg_to = num_pages;
                    }
                    console.log('To:', pg_to);

                    if( (pg_to - pg_from + 1) < num_display_pages ) {
                        var cnt = pg_to - pg_from + 1;
                        var need = num_display_pages - cnt;
                        console.log('Need:', need);
                        pg_from -= need;
                        if(pg_from < 1) {
                            pg_from = 1;
                        }
                    }
                    console.log('So from:', pg_from, 'To:', pg_to);

                    for(var i=pg_from; i<=pg_to; i++) {
                        var href;
                        if(current_url.indexOf('?') < 0) {
                            href = current_url + '?page=' + i;
                        } else if(current_url.indexOf('page=') >= 0) {
                            href = current_url.replace(/page=\d+/, 'page=' + i);
                        } else {
                            href = current_url.replace('?', '?page=' + i + '&');
                        }

                        var $page = $('<li></li>').append( $('<a>').attr('href', href).text(i) );
                        if(i == current_page) {
                            $page.addClass('active');
                        }
                        $page.appendTo($pagination);
                    }


    };
})(jQuery);

$(document).ready(function(){
    // 把公告板中的纯文本内容转换为HTML
    var $broadcast_content = $('.panel.broadcast .panelbody');
    $broadcast_content.html(plain2html($broadcast_content.text()));

    $('.global-nav .toggle-button').click(function(){
        $('.global-nav').toggleClass('horizontal').toggleClass('vertical');
    });
});

