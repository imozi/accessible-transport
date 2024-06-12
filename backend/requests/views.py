from rest_framework import generics

from requests.models import Request, RequestStatus
from requests.serializers import RequestSerializer, RequestDetailSerializer, RequestStatusSerializer, \
    RequestChangeStatusSerializer


class RequestListAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestDetailSerializer


class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestReadAPIView(generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestDetailSerializer


class RequestUpdateAPIView(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDeleteAPIView(generics.DestroyAPIView):
    queryset = Request.objects.all()


class PassengerRequestListAPIView(generics.ListAPIView):
    serializer_class = RequestDetailSerializer

    def get_queryset(self):
        passenger_id = self.kwargs.get('passenger_id')
        if passenger_id is not None:
            return Request.objects.filter(passenger__id=passenger_id)
        else:
            return Request.objects.none()


class RequestStatusListAPIView(generics.ListAPIView):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer


class RequestChangeStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestChangeStatusSerializer
