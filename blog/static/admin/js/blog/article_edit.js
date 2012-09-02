(function($){
    $(document).ready(function(){

        // 标准化用户输入的标签序列
        $('input#id_tags').change(function(){
            console.log("CHANGE");
            $(this).val($(this).val().replace(/[\s,，]+/g, ', ')
                        .replace(/^,\s|,\s$/g,'') );
        });
    });
}) (django.jQuery)
