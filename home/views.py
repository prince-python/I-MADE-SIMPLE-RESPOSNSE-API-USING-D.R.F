from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(["GET","POST","patch"])
def home(request):
    if request.method == "GET":
        return Response({
            'status':200,
            'message':"hiii from GET working"
        })
    elif request.method == "POST":
        return Response({
            'status':200,
            'message':"hiii from POST working"
        })
    elif request.method == "PATCH":
        return Response({
            'status':200,
            'message':"hiii from patch working"
        })
    else:
        return Response({
            'status':200,
            'message':"invalid method"
        })