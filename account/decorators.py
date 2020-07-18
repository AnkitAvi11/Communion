
from django.shortcuts import redirect
from django.contrib.auth import logout, authenticate

#   decorator function to check if the user is loggedin or not
def isLoggedin(view_function) : 
    def wrapperfunction(request, *args, **kwargs) : 
        if request.user.is_authenticated : 
            return redirect("/")
        else : 
            return view_function(request, *args, **kwargs)

    return wrapperfunction
