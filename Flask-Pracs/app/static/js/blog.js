$(document).ready(function() {
    blogServices.GetBlogs();
});

var blogServices = (function($) {

    function GetBlogs() {
        $.ajax({
            url: '/getBlog',
            type: 'GET',
            success: function(res) {
                setBlogHTML(res)
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    function setBlogHTML(res) {
        var blogObj = JSON.parse(res);
        for (var i = 0; i < blogObj.length; i++) {
            var blogHtml = '<div class="list-group"><div class="row"><div class="col-sm-10"><a class="list-group-item active"><h4 class="list-group-item-heading">' + blogObj[i].title + '</h4><p class="list-group-item-text">' + blogObj[i].description + '</p><h5 class="list-group-item-date">Created on:' + blogObj[i].blog_created_on +
                '</h5></a></div><div class="col-sm-2 text-right"><div class="updateBtn"><a href="javascript:void(0)" data-id =' + blogObj[i].id + ' onclick="blogServices.editBlog(this)" class="text-white"><span class="glyphicon glyphicon-pencil"></span></a><a href="/deleteblog/' + blogObj[i].id + '" class="text-white"><span class="glyphicon glyphicon-trash"></span></a></div></div></div></div>'
            $('.jumbotron').append(blogHtml);
        }
    }

    function editBlog(elm) {
        localStorage.setItem('editId', $(elm).attr('data-id'));
        $.ajax({
            url: '/getBlogById',
            data: {
                id: $(elm).attr('data-id')
            },
            type: 'POST',
            success: function(res) {
                // Parse the received JSON string
                var data = JSON.parse(res);
                //Populate the Pop up
                $('#editTitle').val(data[0]['title']);
                $('#editDescription').val(data[0]['description']);

                // Trigger the Pop Up
                $('#editModal').modal('show');
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    $(function() {
        $('#btnUpdate').click(function() {
            $.ajax({
                url: '/updateBlog',
                data: {
                    title: $('#editTitle').val(),
                    description: $('#editDescription').val(),
                    id: localStorage.getItem('editId')
                },
                type: 'POST',
                success: function(res) {
                    console.log(res)
                    $('#editModal').modal('hide');
                    GetBlogs();
                },
                error: function(error) {
                    console.log(error);
                }
            });
        });
    });

    var services = {};
    services.GetBlogs = GetBlogs;
    services.setBlogHTML = setBlogHTML;
    services.editBlog = editBlog;
    return services;

})(jQuery);