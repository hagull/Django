import os
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse
from django.conf import settings
class PostListView1(View):
    def get(self, request):
        name = '남태식'
        html = self.get_template_string().format(name = name)
        return HttpResponse(html)
    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 장고 어쩌구</p>
        '''
    pass
post_list1 = PostListView1.as_view()
#템플릿 이름을 넣은 함수 post_list1함수 발생
class PostListView2(TemplateView):
    template_name = '/dojo/post_list.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '남태식'
        return context
    pass
post_list2 = PostListView2.as_view()
#post_list2 에 as_view의 함수 반환
class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})
    def get_data(self):
        return {
            'message' : '안녕 파이썬 &장고',
            'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
        }
    pass
post_list3 = PostListView3.as_view()

class ExcelDownloadView(View):
    excel_path = os.path.join(settings.BASE_DIR, 'excel.xls')

    def get(self, request):
        excel_name = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            # 필요한 응답헤더 세팅
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(excel_name)
            return response
    pass
excel_download = ExcelDownloadView.as_view()