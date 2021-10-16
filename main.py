# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 18:21:08 2021

@author: info
"""

import time
from plyer import notification


if __name__=="__main__":
    while True:
        notification.notify(
            title= "Please take a short break",
            message =" its good to take break and have a coffee...........",
            app_icon= "Custom-Icon-Design-Mono-Business-2-Coffee.ico",
            timeout=10
            )
        time.sleep(1500)