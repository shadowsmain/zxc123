from django.shortcuts import render


def index(request):
    return render(request, 'basketapp/basket.html')



def add(request, course_id):
 #    basket_item = Basket
     CourseBasket.objects.get_or_create(
         user=request.user,
         course_id=course_id
  #       course=course
    )
     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       #  reverse('mainapp:catalog_section',
         #        kwargs={'category_pk': course.category_id})

