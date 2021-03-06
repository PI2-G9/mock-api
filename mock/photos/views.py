from django.http import JsonResponse

def get_photos_and_users(request):
    data = [
        {
            'name': 'Luis Gustavo',
            'image': 'https://i.imgur.com/qDNSM88.jpg'
        },
        {
            'name': 'Matheus Barcelos',
            'image': 'https://i.imgur.com/EPVD4cn.jpg'
        },
        {
            'name': 'Pedro',
            'image': 'https://i.imgur.com/pA7Yjyt.jpg'
        }
    ]

    return JsonResponse(data, safe=False)