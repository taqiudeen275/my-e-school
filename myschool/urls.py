from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include('blog.urls')),
    path("", include('account.urls')),
    path("", include('home.urls')),
    path("", include('academics.urls')),
    path("staff/", include('staff.urls')),
    path("students/", include('student.urls')),
    path("others/", include('others.urls')),
    path("results/", include('result.urls')),
    path("staff-user/", include('staffUser.urls')),
    path("student-user/", include('studentUser.urls')),
    path("parent-user/", include('parent.urls')),
    path("message/", include('message.urls')),

    #third-party
    path('froala_editor/', include('froala_editor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    