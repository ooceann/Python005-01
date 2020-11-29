# -*- coding: utf-8 -*-

import logging
import os
import time
from pathlib import Path


def call_fun():
    today = time.strftime('%Y-%m-%d')
    path = Path('/var/log/ipython-%s' % (today))
    if not path.exists():
        path.mkdir()
    # 切换路径
    os.chdir(path)

    logging.basicConfig(
        filename='call_fun.log',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    )

    logging.warning('被调用了')


if __name__ == '__main__':
    call_fun()
