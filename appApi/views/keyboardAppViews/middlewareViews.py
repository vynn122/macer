import json
import jwt
from django.http import HttpRequest, JsonResponse
from keyboardApp.models import User_info as keyboardApp_user_info
from appApi.util.retrieveKey import get_JWT_key
from django.shortcuts import redirect



def Crediential_validate_middleware(view_func):
    """
    Validate whether the user crediential is match what inside the database or not.
        True:   it pass down the data to main view
        False:  it response with status 401 error
    """
    def test_operation(request: HttpRequest):
        try:
            requestData = json.loads(request.body)
        except Exception as err:
            return JsonResponse({"Error_Message": "failed to load user request", "Dev_Message": str(err)}, status=400)
        if requestData["username"] and requestData["password"]:
            # perform database query
            queried_user = keyboardApp_user_info.objects.filter(user_name=requestData["username"])
            if queried_user:
                if requestData["password"] != queried_user[0].user_password:
                    return JsonResponse({"Error_Message": "something went wrong, Username / password is incorrect"}, status=401)
                request.user_info = queried_user[0]
            else:
                return JsonResponse({"Error_Message": "user not found"}, status=404)
        else:
            return JsonResponse({"Error_Message": "Please provide info to proceed"}, status=400)

        return view_func(request)
    return test_operation


def Cookie_validation_middleware(view_func):
    """
    Checking whether the cookie are legit or not, if not it response with status 401 error. If it is legit 
    it will pass down the data to its actual view.

        If cookie doesn't exist it will response to client with status 401
    """
    def validate_the_cookie(request: HttpRequest):
        jwt_token = request.COOKIES.get("auth_token")
        if not jwt_token:
            return JsonResponse({"Error_Message": "cookie not found"}, status=401)        
        try:
            jwt_payload = jwt.decode(
                jwt=jwt_token,
                key=get_JWT_key("public_key"),
                algorithms=["RS256"]
            )
            request.user_info = jwt_payload
        except Exception as err:
            return JsonResponse({"Error_Message": "token not valid", "Dev_Message": str(err)}, status=401)
        return view_func(request)
    
    return validate_the_cookie

