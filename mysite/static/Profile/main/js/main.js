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

var proffessionalList = null;

function getProffesionals(page) {
    console.log('entre')
    proffessionalList = $.ajax({
        type: "GET",
        url: '/profile/get_proffesionals/',
        data: {

        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
            if (proffessionalList != null) {
                if (proffessionalList.readyState != 4) {
                    proffessionalList.abort();
                }
            }
        },
        error: function (e) {
            console.log('Ajax error',e);
        },
        success: function (proffesionals) {
            $('#proffesionals-catalog').append(proffesionals);
        }
    });
}

function editProfessional(professionalId) {
    console.log('Edit Professional, TODO : ', professionalId)
}