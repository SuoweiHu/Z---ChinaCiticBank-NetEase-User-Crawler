# NetEase-User-Crawler

使用Selenium进行登陆操作，和网站建立Session，通过浏览器获得渲染好的页面。通过选定用户的主界面获得歌单ID，递归进入二级歌单页面（获得歌曲ID，三级页面获取歌曲信息，该功能默认为关闭）
需要预先配置本地的MongoDB数据库：Host=localhost, Port=27017, collection='NetEase-Music'
