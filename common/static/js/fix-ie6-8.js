;
$(document).ready(function(){
    $('input[type]').each(function(){
        $(this).addClass(this.type);
    })

    $('input,textarea').focus(function(){
        $(this).addClass('focus');
    }).blur(function(){
        $(this).removeClass('focus');
    }).hover(function(){
        $(this).addClass('hover');
    },function(){
        $(this).removeClass('hover');
    });
});
