from django.conf.urls import url
from tastypie import http
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from dropbox.models import Media
from lecture.api.authorization import UserObjectsOnlyAuthorization


class MediaResource(ModelResource):
    class Meta:
        queryset = Media.objects.all()
        resource_name = 'media'
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        always_return_data = True

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/upload_file/(?P<pk>\w[\w/-]*)/$" % self._meta.resource_name, self.wrap_view('upload_file'), name="api_upload_file"),
        ]

    def upload_file(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        self.is_authenticated(request)

        try:
            report = self._meta.queryset._clone().get(pk=kwargs['pk'])
        except self._meta.object_class.DoesNotExist:
            return http.HttpNotFound()

        bundle = self.build_bundle(obj=report, request=request)

        self.authorized_update_detail(None, bundle)

        file = request.FILES.get('file', None)
        if not file:
            return self.error_response(request, {"error": "No field called file found"}, response_class=http.HttpBadRequest)

        bundle.obj.file.save(file.name, file)
        bundle.obj.save(update_fields=['file'])

        bundle = self.full_dehydrate(bundle)

        return self.create_response(request, bundle, response_class=http.HttpAccepted)