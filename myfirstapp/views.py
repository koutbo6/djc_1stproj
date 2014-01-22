 # -*- coding: utf-8 -*-
from django.shortcuts import render

ARABIZI_CHARS_AR = u"ا ب ت ث ج ح خ د ذ ر ز س ش ص د ط ظ ع غ ف ق ك ل م ن ه و ي".split()
ARABIZI_CHARS_EN = u"a b t th j 7 `7 d th r z s sh 9 `9 6 `6 3 `3 f \"9 k l m n h w y".split()
ARABIZI_CHARS = dict(zip(ARABIZI_CHARS_AR, ARABIZI_CHARS_EN))

def convert_arabizi(s):
    return u"".join([ARABIZI_CHARS.get(x,x) for x in s])

def arabizi(request, word=None):
    word = word or request.GET.get("w")
    return render(
        request,
        "arabizi.html",
        {
            "word": word,
            "aword": word and convert_arabizi(word),
        },
    )

# Create your views here.
def hello_world(request, username=None):
    return render(
        request,
        "hello_world.html",
        {
            "name": username,
        },
    )


