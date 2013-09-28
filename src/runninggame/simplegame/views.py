# -*- coding: utf-8 -*-
from django.views import generic as cbv


class IndexGameView(cbv.TemplateView):
    template_name = 'game/index.html'