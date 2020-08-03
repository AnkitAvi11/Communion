
window.addEventListener('DOMContentLoaded', () => {

    let likebutton = document.getElementById('like');
    likebutton.addEventListener('click', function() {
        let csrf_token = document.querySelector("input[type=hidden]").value;
        let blog_id = likebutton.getAttribute('blog_id');
        let form = new FormData()
        form.append('blog_id', blog_id)
        fetch('http://127.0.0.1:8000/blog/like/', {
            method : "POST", 
            body : form,
            headers : {
                "X-CSRFToken" : csrf_token
            }
        }).then(res => res.json())
        .then(data => {
            likebutton.textContent = data.message;
            document.getElementById('likecount').textContent=data.likes
        })
        .catch(err => console.log(err))
    }, false);

}, false);

