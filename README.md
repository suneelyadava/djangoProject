Steps to run :

1- Install Django plugin 
2- Install restapi framework 
3- Install python 
4-Run python manage.py makemigrations. ---> To adapt db chnages 
5- To run server --> python3 manage.py runserver
6- Now go to browser and paste and then hit enter http://localhost:8000/admin/courses/course/
7- Here your service is fully functional 


Request :
http://localhost:8000/courses/

Sample Res:

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "url": "http://localhost:8000/courses/1/",
        "name": "jasdbjasb",
        "language": "java",
        "price": "20"
    },
    {
        "id": 2,
        "url": "http://localhost:8000/courses/2/",
        "name": "Python",
        "language": "Python",
        "price": "39"
    }
]

