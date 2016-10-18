# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginator(query_set, page_num, page_length=60):
    paginator_obj = Paginator(query_set, page_length)

    try:
        return_obj = paginator_obj.page(page_num)
    except PageNotAnInteger:
        return_obj = paginator_obj.page(1)
    except EmptyPage:
        return_obj = paginator_obj.page(paginator_obj.num_pages)

    return return_obj
