from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from basketapp.models import CourseBasket
from mainapp.models import Course




def index(request):
    items = CourseBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }


    return render(request, 'basketapp/last.html', context)


def add(request, course_id):
    course = Course.objects.get(pk=course_id)
    CourseBasket.objects.get_or_create(
        user=request.user,
        # course_id=course_id
        course=course
    )
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(
        reverse('mainapp:catalog_section',
                kwargs={'category_pk': course.category_id})
    )


def remove(request, course_basket_id):
    item = CourseBasket.objects.get(id=course_basket_id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))