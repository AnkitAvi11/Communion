//  for follow or unfollow a user
window.addEventListener('load', function() {
    let followButton = document.getElementById('follow');
    
    followButton.addEventListener('click', function(e) {
        let follow_to = followButton.getAttribute('user_id');
        let csrf_token = document.querySelector('input[type="hidden"]').value;
        let form = new FormData()
        form.append("follow_to", follow_to)
        fetch("http://127.0.0.1:8000/account/followuser/", {
            method : "POST",
            body : form,
            headers : {
                "X-CSRFToken" : csrf_token
            }
        }).then(res => res.json())
        .then(data => {
            followButton.textContent = data.message;
        })
        .catch(err => console.log(err))
        
    }, false);

}, false)
