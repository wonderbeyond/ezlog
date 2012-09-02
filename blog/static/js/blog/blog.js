;$(document).ready(function(){
    var $blog_pics = $('.article.complete img'); // 文章配图
    var $covers = $('.article.summary img.cover'); // 摘要中的封面图


    // 删除通过Ckeditor插入的图片的style标签,
    // 文章img的img样式在css文件中同一设置.
    $blog_pics.removeAttr('style');

    $blog_pics.magnifiable();
    $covers.magnifiable();
});
