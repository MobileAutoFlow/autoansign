# autotask_android

基于[airtest_mobileauto](https://pypi.org/project/airtest-mobileauto)的安卓自动化任务脚本

![GitHub forks](https://img.shields.io/github/forks/MobileAutoFlow/autoansign?color=60c5ba&style=for-the-badge)![GitHub stars](https://img.shields.io/github/stars/MobileAutoFlow/autoansign?color=ffd700&style=for-the-badge)


## 脚本开发环境说明
* 本脚本基于分辨率`960x540`, dpi`160`的安卓模拟器开发
* dpi或者分辨率不同很容易识别失败。
* 有的模拟器打开特定APP会闪退

安装

```
python -m pip install autoansign --upgrade
```

## 当前开发项目
### 基于url的签到
* `web_url`,直接打开特定url,实现签到, **适配任意的安卓设备**
* 将url存储到`web_url.txt`,下面是我常用的url
```
none
```

### 基于浏览器的签到
* *注: 本脚本于via-5.9.0测试通过, 需开启桌面模式、全屏、浏览器标识(windows/chrome),其他浏览器自行替换图片资源*
* **脚本现在通过打开url执行, 而不是打开浏览器, 再点击网页, 因此需要配置via为默认的浏览器**
* 只能在境内的模拟器/容器内执行, 这些网站在不同地区显示的内容不同.
* `web_ablesci`, [科研通](https://www.ablesci.com/)每日签到
* `web_muchong`, ~~[小木虫](https://muchong.com/bbs/)每日签到~~
* `web_tiyanbi`, [王者荣耀](https://pvp.qq.com/cp/a20161115tyf/page2.shtml)体验币兑换皮肤碎片

![连续签到50天](https://private-user-images.githubusercontent.com/174871503/397235351-c1a55b1f-a8f0-4370-aec5-211ef40a1564.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQ1ODY3NzUsIm5iZiI6MTczNDU4NjQ3NSwicGF0aCI6Ii8xNzQ4NzE1MDMvMzk3MjM1MzUxLWMxYTU1YjFmLWE4ZjAtNDM3MC1hZWM1LTIxMWVmNDBhMTU2NC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxOVQwNTM0MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NWE2NDU5ZjVmNzQxODgzNmQ5YjJkNTg2NzAxNzFkMWZhNTE5NmM0OTRmZGM4NDA2NmFmMjM0OGExNGI4NTZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.dt6sksZbmDukgtwRmvqSPf9T0mvvmhLL7F_ZIMtU88w)

### 基于app的签到
* `app_alicloud`, 阿里云盘每日签到(横屏版960x540)




## 运行
* 创建`tag.txt`则开启领取`tag.py`中定义的礼包

```
python run.py config.win.yaml
```

我的配置文件 `config.win.yaml`
```
mynode: 10
MuMudir: 'D:\Program Files\Netease\MuMu Player 12\shell'
MuMu_Instance:
  10: "0"
LINK_dict:
  10: Android:///127.0.0.1:16384
figdir: assets
logfile:
  10: result.ce.txt
prefix: "autotask"
```


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=MobileAutoFlow/autoansign&type=Date)](https://star-history.com/#MobileAutoFlow/autoansign&Date)
