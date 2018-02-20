from django.shortcuts import render
from .models import BookInfo

# Create your views here.

def index(request):

    # 查询数据库
    bookinfo = BookInfo.objects.all()
    print(bookinfo)
    context = {'booklist':bookinfo}
    return render(request,'mybook/index.html',context)

#详细页，接收图书的编号，根据编号查询，再通过关系找到本图书的所有英雄并展示
def detail(reqeust, bid):
    #根据图书编号对应图书
    book = BookInfo.objects.get(id=int(bid))
    #查找book图书中的所有英雄信息
    heros = book.heroinfo_set.all()
    #将图书信息传递到模板中，然后渲染模板
    return render(reqeust, 'mybook/detail.html', {'book':book,'heros':heros})