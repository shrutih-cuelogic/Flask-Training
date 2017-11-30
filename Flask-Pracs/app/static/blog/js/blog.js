$(document).ready(function() {
    blogServices.GetBlogs();
});

var blogServices = (function($) {
    var selected_blog_id = 0;

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
        var blogHtml = '';
        for (var i = 0; i < blogObj.length; i++) {
            blogHtml += '<div class="list-group" id="id-list-' + blogObj[i].id + '"><div class="row" id="blog_' + blogObj[i].id + '"><div class="col-sm-10"><a class="list-group-item active"><h4 class="list-group-item-heading" id="id-title-' + blogObj[i].id + '">' + blogObj[i].title + '</h4><p class="list-group-item-text" id="id-desc-' + blogObj[i].id + '">' + blogObj[i].description + '</p><h5 class="list-group-item-date" id="id-createdon">Created on:' + blogObj[i].blog_created_on +
                '</h5></a></div><div class="col-sm-2 text-right"><div class="updateBtn"><a href="javascript:void(0)" data-id =' + blogObj[i].id + ' onclick="blogServices.editBlog(this)" class="text-white"><span class="glyphicon glyphicon-pencil"></span></a><a href="javascript:void(0)" data-id =' + blogObj[i].id + ' onclick="blogServices.confirmDelete(this)" class="text-white"><span class="glyphicon glyphicon-trash"></span></a></div></div></div></div>';
        }

        var mainDiv = '<div id="list-blog">' + blogHtml + '</div>';
        $('.blogList').append(mainDiv);
    }

    function editBlog(elm) {
        selected_blog_id = $(elm).attr('data-id');
        $.ajax({
            url: '/getBlogById',
            data: {
                id: selected_blog_id
            },
            type: 'POST',
            success: function(res) {
                // Parse the received JSON string
                var data = JSON.parse(res);
                //Populate the Pop up
                $('#editTitle').val(data[0]['title']);
                $('#editDescription').val($("<div>").html(data[0]['description']).text());
                // Trigger the Pop Up
                $('#modalError').remove();
                $('#modalDescError').remove();
                $('#editModal').modal('show');
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    function updateBlogdetails(blog_id) {
        $('#id-title-' + blog_id).html($('#editTitle').val());
        $('#id-desc-' + blog_id).html($('#editDescription').val());
    }

    $(function() {
        $('#btnUpdate').click(function() {
            if(!$('#editTitle').val()){
                if(!$('#titleId').length){
                    return $('#titleId').append('<span class="error">Please enter blog title.</span>');
                }
            }
            if (!$('#editDescription').val()) {
               if(!$('#descriptionId').length){
                    return $('#descriptionId').append('<span class="error">Please enter blog description.</span>');
                }
            }
            $.ajax({
                url: '/updateBlog',
                data: {
                    title: $('#editTitle').val(),
                    description: $('#editDescription').val(),
                    id: selected_blog_id
                },
                type: 'POST',
                success: function(res) {
                    updateBlogdetails(selected_blog_id);
                    selected_blog_id = 0;
                    $('#editModal').modal('hide');
                    $('#modalError').remove();
                    $('#modalDescError').remove();
                },
                error: function(error) {
                    console.log(error);
                }
            });
        });
    });

    function confirmDelete(elm) {
        selected_blog_id = $(elm).attr('data-id');
        $('#deleteModal').modal();
    }

    function deleteBlogdetails(blog_id) {
        $('#id-list-' + blog_id).remove();
    }

    function deleteBlog() {
        $.ajax({
            url: '/deleteBlog',
            data: { id: selected_blog_id },
            type: 'POST',
            success: function(res) {
                var result = JSON.parse(res);
                if (result.status == 'OK') {
                    $('#deleteModal').modal('hide');
                    deleteBlogdetails(selected_blog_id);
                    selected_blog_id = 0;
                } else {
                    alert(result.status);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    var services = {};
    services.GetBlogs = GetBlogs;
    services.setBlogHTML = setBlogHTML;
    services.editBlog = editBlog;
    services.deleteBlog = deleteBlog;
    services.confirmDelete = confirmDelete;
    services.deleteBlog = deleteBlog;
    return services;

})(jQuery);