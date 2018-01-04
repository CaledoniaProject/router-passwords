# 路由器默认密码

数据来自 [http://routerpasswords.com/](http://routerpasswords.com/)，只是这个网站实在是太慢了，还要发POST请求才能看到密码，所以我做个单页面版本，可以在本地实时查询

最后同步时间 2018.1.4

# 用法

复制 `src` 到 web 目录，e.g

```
cp -R src /var/www/html/router-passwords/
```

浏览器打开 `http://xxxx/router-passwords` 即可，完全离线查询

![screenshot](https://raw.githubusercontent.com/CaledoniaProject/router-passwords/master/screenshots/webui.jpg)
