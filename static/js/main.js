
$(document).ready(function ($) {
    "use strict";
    $('nav.main a').on('click', function(event){
        if($('#trans-wrap').hasClass('flipped') == true){
            $.pjax.click(event, {container: $('#wrap-front')});
        } else {
            $.pjax.click(event, {container: $('#wrap-back')});
        }
        $("#trans-wrap").toggleClass('flipped');
    });

});
