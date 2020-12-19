from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import DBShorts
from lxml import etree


# Create your views here.


def index(request):
    shorts_list = DBShorts.objects.all()
    error_msg = ''

    # 如果有数据，就渲染
    if shorts_list:
        movie_name = shorts_list[0].movie_name
        return render(request, 'index.html', locals())

    # 没有数据，就爬取存入
    else:
        douban_spider = DoubanSpider(30292777)
        douban_spider.get_shorts()
        douban_spider.save_to_model()
        return HttpResponse('hello, no data')


class DoubanSpider(object):
    def __init__(self, id):
        self.ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        self.headers = {"User-Agent": self.ua}
        self.info = []
        self.id = id

    def get_shorts(self):

        user_names = []
        stars_list = []
        shorts_list = []
        i = -1

        if len(self.info) < 20:

            i = i + 1
            start = i * 20
            url = f'https://movie.douban.com/subject/{self.id}/comments?start={start}&limit=20&status=P&sort=time'
            # print(url)
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                selector = etree.HTML(res.text)

                # 电影名称
                movie_name = selector.xpath('//div[@id="content"]/h1/text()')[0]
                # movie_name = 'hello'
                # 评论用户昵称
                user_names = user_names + selector.xpath('//div[@class="comment"]/h3/span[2]/a/text()')
                # 获取评分
                stars_list = stars_list + selector.xpath('//div[@class="comment"]/h3/span[2]/span[2]/@class')
                # 获取短评
                shorts_list = shorts_list + selector.xpath('//div[@class="comment"]/p/span/text()')

                for i in range(len(stars_list)):
                    star = stars_list[i].split(' ')[0][7]
                    # 过滤评分低于3的
                    if int(star) > 3:
                        item = {'movie_id': self.id, 'movie_name': movie_name, 'user_name': user_names[i],
                                'short': shorts_list[i], 'star': star}
                        self.info.append(item)
            else:
                return None

    def save_to_model(self):
        data_list = []
        for item in self.info:
            data_list.append(
                DBShorts(
                    movie_id=item['movie_id'],
                    movie_name=item['movie_name'],
                    user_name=item['user_name'],
                    info=item['short'],
                    star=item['star']
                )
            )
        DBShorts.objects.bulk_create(data_list)
        print('添加完成')


def search(request):
    keywords = request.GET.get('search')
    error_msg = ''

    if not keywords:
        error_msg = '提示: 请输入关键词'
        return render(request, 'index.html', locals())

    shorts_list = DBShorts.objects.filter(info__icontains=keywords)
    if len(shorts_list) != 0:
        movie_name = shorts_list[0].movie_name
    else:
        none_msg = '没有查到对应内容'

    return render(request, 'index.html', locals())


if __name__ == '__main__':
    DoubanSpider().get_shorts()
