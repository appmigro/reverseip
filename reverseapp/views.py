from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from reverseapp.models import ReversedIPRecord

@method_decorator(csrf_exempt, name='dispatch')
class ReverseIPView(View):
    def get(self, request, *args, **kwargs):
        # Get the user's IP address from the request
        user_ip = self.get_client_ip(request)

        # Reverse the IP address
        reversed_ip = '.'.join(user_ip.split('.')[::-1])

        # Print the reversed IP address to the console
        print(f"Reversed IP: {reversed_ip}")

        # Save the reversed IP in the MongoDB database
        ReversedIPRecord.objects.create(ip=reversed_ip)

        # Return a response to the user
        return HttpResponse(f"Your reversed IP: {reversed_ip}")

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip