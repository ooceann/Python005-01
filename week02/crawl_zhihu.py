# -*- coding: utf-8 -*-
# @FileName: crawl_zhihu.py
# @Time    : 2020/12/6 3:49 下午
# @Author  : zhan

import requests
import time
import os
from pathlib import Path
import json


def get_answer(myurl):
    """
    爬取问题答案
    :param myurl:问题链接
    :return:
    """
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    cookie = 'q_c1=c3e4cf3c1c41493186e5099607c653ca|1577860872000|1568097109; _zap=397710ca-2bcb-4118-aa2c-a5c3b235ea7c; d_c0="AEBk5WuLBhCPTjOiQVTMF6pOG1e-A0RiV4s=|1568097108"; _xsrf=B5BoGURoX1qvXFP0Y7kGNM7buQSB9es6; _ga=GA1.2.206583049.1582687341; z_c0="2|1:0|10:1592557358|4:z_c0|92:Mi4xeWdQUUJRQUFBQUFBUUdUbGE0c0dFQ1lBQUFCZ0FsVk5MczNaWHdBQ1dZVmxPMWFfZHFZTUd3QUtGUXlYZTVueDhB|f54dd6d7da598005e944b8c4de376b0c5fd1abd43d7995d60a3cdc98d0720b4c"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1606403147,1606664348,1607012184,1607184613; q_c1=f281fd2ab86748b78d350bfc96d422f3|1607184621000|1569288678000; tst=h; tshl=digital; SESSIONID=z5FcJtmvLRM0CJyEDTGNp9RmqSN1FA0djdqgsmJ9BuA; JOID=UFgUA0PkaD5EIgMsbuawaDzgp7R8nFx5L2J1QBmiOHJ1aUNXKj7f_BkqACxnako7WUdCI2RYEuZKZq-CCWd0qG4=; osd=V14dB0vjbjdAKgQqZ-K4bzrpo7x7mlV9J2VzSR2qP3R8bUtQLDfb9B4sCShvbUwyXU9FJW1cGuFMb6uKDmF9rGY=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1607186695; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1607186717|1607184610'
    header = {'user-agent': ua, 'cookie': cookie}
    response = requests.get(myurl, headers=header)

    answer_info = response.json()['data']

    answers = {'title': answer_info[0]['question']['title'], 'answer': {}}
    for index, item in enumerate(answer_info):
        answers['answer'][index + 1] = {}
        answers['answer'][index + 1][item['author']['name']] = item['content']

    save_data(answers)


def save_data(data_dict):
    """
    将爬取结果以json文件保存，并以当前脚本名命名
    :param data_dict: 答题用户与答案内容组成的字典
    :return: None
    """
    p = Path(__file__)

    file_suffix = '.json'
    cur = time.strftime("%Y-%m-%d", time.localtime())
    file_name = os.path.join(p.parent, p.stem) + '_' + cur
    file_abs = file_name + file_suffix
    with open(file_abs, "a+") as f:
        json.dump(data_dict, f, ensure_ascii=False)


if __name__ == '__main__':
    num = 15
    # 为什么看电子书要用 Kindle 而不是 iPad
    url = f'https://www.zhihu.com/api/v4/questions/295529932/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bsettings.table_of_content.enabled%3B&offset=&limit={num}&sort_by=default&platform=desktop'
    get_answer(url)
