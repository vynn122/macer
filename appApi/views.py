# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse, HttpRequest
# from django.views.decorators.http import require_http_methods


# import json



# def test_middleware(view_func):
#     def test_operation(request: HttpRequest):
#         print("nice")
#         try:
#             requestData = json.loads(request.body)
#         except Exception as err:
#             print(err)
#         if requestData["username"] and requestData["password"]:
#             # perform database query
#             print("nice")
#         else:
#             return JsonResponse({"Error Message": "failed to validate the user credential"}, status=401)

#         return view_func(request)
#     return test_operation


# @require_http_methods(["GET", "POST", "OPTIONS"])
# @test_middleware
# def testHandler(request: HttpRequest):
#     testdata = {
#         "Message": "Test successfully"
#     }
#     return JsonResponse(testdata)