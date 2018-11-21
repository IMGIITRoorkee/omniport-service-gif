from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class Roulette(GenericAPIView):
    """
    Return the URL to a random GIF from the assortment of provided GIFs
    """

    def get(self, request, *args, **kwargs):
        """
        View to serve GET requests
        :param request: the request that is to be responded to
        :param args: arguments
        :param kwargs: keyword arguments
        :return: the response for request
        """

        response = {
            'count': 15
        }

        # HTTP_418_IM_A_TEAPOT not present in DRF, so using integer status code
        return Response(response, status=418)
