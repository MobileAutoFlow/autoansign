#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################
# Author : cndaqiang             #
# Update : 2025-06-30            #
# Build  : 2024-08-29            #
# What   : 网站签到         #
##################################
try:
    from airtest_mobileauto.control import *
except ImportError:
    print("模块[airtest_mobileauto]不存在, 尝试安装")
    import pip
    try:
        pip.main(['install', 'airtest_mobileauto', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])
    except:
        print("安装失败")
        exit(1)
import sys


class web_tiyanbi():
    def __init__(self):
        self.prefix = self.__class__.__name__  # 类的名字
        #
        # 静态资源
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, 'assets')
        Settings.figdirs.append(assets_dir)
        seen = set()
        Settings.figdirs = [x for x in Settings.figdirs if not (x in seen or seen.add(x))]
        #
        # device
        self.mynode = Settings.mynode
        self.totalnode = Settings.totalnode
        self.LINK = Settings.LINK_dict[Settings.mynode]
        self.移动端 = deviceOB(mynode=self.mynode, totalnode=self.totalnode, LINK=self.LINK)
        self.设备类型 = self.移动端.设备类型
        # 直接打开领礼包的网址，并将默认的浏览器设置为APPID
        self.url = "https://pvp.qq.com/cp/a20161115tyf/page2.shtml"
        self.移动端.打开网址(self.url)
        self.APPOB = appOB(big=True, device=self.移动端)
        self.Tool = DQWheel(var_dict_file=f"{self.移动端.设备类型}.var_dict_{self.prefix}.yaml",
                            mynode=self.mynode, totalnode=self.totalnode)
        #
        self.dayFILE = f"{self.prefix}.txt"
        self.timelimit = 60*10
        self.运行时间 = [3.0, 4.0]
        self.today = self.Tool.time_getweek()
        self.yesterday = (self.today-1) % 7
    #

    def stop(self):
        self.APPOB.关闭APP()
    #

    def run(self, times=0):
        if not connect_status():
            self.移动端.连接设备()
        if times == 0:
            self.today = self.Tool.time_getweek()
            self.yesterday = (self.today-1) % 7
            try:
                self.yesterday = int(self.Tool.readfile(self.dayFILE)[0].strip())
            except:
                TimeECHO(f"未能从{self.dayFILE}中获取到上次运行时间")
            self.Tool.timelimit(timekey="RUN", limit=self.timelimit, init=True)
        #
        if self.Tool.timelimit(timekey="RUN", limit=self.timelimit, init=False):
            TimeECHO(f"{self.prefix}.运行超时")
            self.Tool.touchfile(self.dayFILE, content=str(self.yesterday))
            return
        #
        if times == 4:
            # 卡顿则重新打开浏览器
            self.APPOB.重启APP()
            self.移动端.打开网址(self.url)
        if times > 8:
            TimeECHO("失败次数太多，停止")
            self.Tool.touchfile(self.dayFILE, content=str(self.yesterday))
            return
        #
        times = times + 1
        #
        # ------------------------------------------------------------------------------
        # 不存在对应图片则设置为None
        主页logo = Template(r"tpl1751264772613.png", record_pos=(-0.304, -0.136), resolution=(960, 540))
        主页入口 = Template(r"tpl1751264596196.png", record_pos=(-0.223, 0.013), resolution=(960, 540))
        网站主页元素 = [主页logo, 主页入口]
        # ------------------------------------------------------------------------------
        # 打开网站
        # 检测是否打开成功
        # 因为在init时已经打开过了，这里直接检测
        存在, 网站主页元素 = self.Tool.存在任一张图(网站主页元素, self.prefix+"网站主页元素")
        if not 存在:
            sleep(30)
            存在, 网站主页元素 = self.Tool.存在任一张图(网站主页元素, self.prefix+"网站主页元素")
            if not 存在:
                sleep(30)
                self.移动端.打开网址(self.url)
                return self.run(times)
        # ------------------------------------------------------------------------------
        #
        pos = self.Tool.cal_record_pos((0.249, -0.023), self.移动端.resolution)
        碎片奖励 = Template(r"tpl1751265051281.png", record_pos=(0.249, -0.023), resolution=(960, 540))
        奖励位置 = False
        for i in range(20):
            sleep(1)
            奖励位置 = exists(碎片奖励)
            if 奖励位置:
                break
            else:
                TimeECHO(f"寻找碎片奖励中{i}")
            swipe(pos, vector=[0.0, -0.5])
        if not 奖励位置:
            TimeECHO("没找到体验币")
            return self.run(times)
        #
        touch(奖励位置)
        sleep(1)
        touch(奖励位置)
        #
        # 无论领取成功与否, 都会弹窗，因此, 这里不再判断是否领取成功

        return
    #

    def looprun(self, times=0):
        times = times + 1
        startclock = self.运行时间[0]
        endclock = self.运行时间[1]
        while True:
            leftmin = self.Tool.hour_in_span(startclock, endclock)*60.0
            if leftmin > 0:
                TimeECHO("剩余%d分钟进入新的一天" % (leftmin))
                self.APPOB.关闭APP()
                self.移动端.重启重连设备(leftmin*60)
                continue
            times = times+1
            TimeECHO("="*10)
            self.run()

def main():
    config_file = ""
    if len(sys.argv) > 1:
        config_file = str(sys.argv[1])
    Settings.Config(config_file)
    ce = web_tiyanbi()
    ce.run()
    ce.stop()
    exit()

if __name__ == "__main__":
    main()
