function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function searchRent(parameter) {
    location = '/alquilar/list_section/list/' + parameter;
}

function enterAddress() {
    
}

function showMapWithData() {
    
}

var filterAjaxProperty = null;
function filterProperties(parameter, page) {
     if (!page) {
        $('#loading').removeClass('is-hidden');
        $('#PropertyList').addClass('is-hidden');
        $(window).scrollTop(0);
    }
    filterAjaxProperty = $.ajax({
        type:'POST',
        url:"/alquilar/get_properties/" + (page != undefined ? '?page=' + page : '?page=1'),
        data: {
            'type': parameter
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
            if (filterAjaxProperty != null) {
                if (filterAjaxProperty.readyState != 4) {
                    filterAjaxProperty.abort();
                }
            }
        },
        error: function () {
            //showMessage('error', 'No se han podido cargar los polygonos.')
        },
        success: function (propertyHtml) {
            $('#loading').addClass('is-hidden');
            $('#PropertyList').removeClass('is-hidden');
            nextPage = propertyHtml.nextPage;
            if (page) {
                $('#myproperties').append(propertyHtml.html); //en la url
                currentPage = page;
                if (currentPage == numPages) {
                    $('#scroll-page-property').remove();
                }
                nextLoaded = true;
            } else {
                $('#PropertyList').empty();
                $('#PropertyList').prepend(propertyHtml.html);
            }

        }


    })
}