"use strict";

$(window).on("load", function() {
    setTimeout(function() {
        $(".page-loader").fadeOut()
    }, 300)
});



$(document).ready(function() {
    $('.login input').addClass('form-control');
    $('.scrollbar-inner')[0] && $('.scrollbar-inner').scrollbar().scrollLock();
    $('body').on('click', '[data-action]', function(e) {
        e.preventDefault();
        var $t = $(this), a = $t.data('action'), b = $t.data('target');
        switch ($t.data('action')) {
            case 'aside-open':
                $t.addClass('toggled'), $(b).addClass('toggled'), $('.navbar-header').append('<div class="backdrop" data-action="aside-close" data-target=' + b + '/>');
                break;
            case 'aside-close':
                $('[data-action="aside-open"], ' + b).removeClass('toggled'), $('.navbar-header').find('.backdrop').remove();
        }
    });
    $('#sidebar-toggle').on('click', function(e) {
        e.preventDefault();
        var $t = $(this), $s = $('#sidebar'), $m = $('#main');
        $t.toggleClass('sidebar-toggled');
        $s.toggleClass('sidebar-toggled');
        $m.toggleClass('sidebar-toggled');
        if ($t.hasClass('sidebar-toggled')) {
            $.cookie('sidebar_toggled', true, { expires: 365, path: '/' });
        } else {
            $.cookie('sidebar_toggled', false, { expires: 365, path: '/' });
        }
    })
    $('[title]').tooltip();
    $('select[name=action]').addClass('form-control');
    $('fieldset .related-widget-wrapper>select').select2();
    $('#changelist-filter').find('select').each(function() {
        var $s = $(this)
        $s.on('change', function() {
            var $o = $s.find('option:selected'), url = $o.data('url');
            if (url) {
                document.location = url;
            }
        });
    });
});
