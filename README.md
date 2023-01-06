# [友情链接](https://www.daoblog.top/friends)

所以，少年，你做好交换友链的觉悟了吗？~~（好尬啊~~

## 基本要求

> 如果你和我很熟了的话，直接[发邮件](mailto:friends@ydlk.cc)吧

- 首先，请确保您已经在您的站点上的友链板块添加了我的网站  
- 其次，**您==不是==本着卖广告的目的来交换**，您的网站属于**个人博客**  
- 网站的域名十分重要，如果**是**免费域名的话就请暂时不要考虑了~~，除非混熟了~~  
    - 免费域名**包括但不限于**下述定义：  
        - 由Freenom公司运营的免费域名后缀，如`.ml`、`.tk`  
        - 中国大陆企业的静态网站托管服务的默认域名，如：  
            - oschina.io  
            - gitee.io  
            - coding.me  
            - coding.io  
            - coding-pages.com  
            - ......  
    - 免费域名**不包括**下述等定义：  
        - 向Freenom公司**付费购买的**`.ml`、`.tk`等域名  
        - 由Automattic公司运营的wordpress.com在线博客服务  
        - 其他任何包含于`Public Suffix List`的免费子域名服务，如`github.io`，`gitlab.io`等  
        - ......  
- 您的网站应至少能从中国香港的網上行寬頻正常访问  
- 我诚恳地希望您的网站不要充斥着广告、洗稿、搬运等低质内容  
    - 网站和博客可以长草，但不要滥竽充数  
    - 最终解释权归我本人所有  
- 您的站点符合中国大陆及中国香港的有关法律法规，不涉及敏感内容  
- 此外，您还必须会使用`Git`与`GitHub`，设置此仓库即意在考验您最基本的使用技巧  

## 开始交换

如果您认为您的站点符合上方的要求，那么欢迎交换！

### 注意：您提交的信息有可能被修改

如果有修改，我会将修改内容在PR中进行告知

- 为了友链相关页面和组件的统一性和美观性，可能会对您的昵称进行缩短处理，例如昵称包含`博客`、`XX的XX`等内容或形式可能会被简化。  
    - 在友链朋友圈的配置中，您的信息会被简化，一视同仁  
- 所有的友链链接要求为博客主页链接，而不是个人主页链接。（为了适配友链朋友圈）  

### 我的友链信息

为了避免可能出现的图床问题，您可以将头像存储到贵站图床。

> 名称：Yandao（或`Yandao's Blog`）  
> 网站：https://daoblog.top/  
> 描述：永远在学习的路上  
> 头像：访问本仓库`src`目录下的`me`文件夹，任选一张自行压缩、存储即可。  
> 订阅：https://daoblog.top/atom.xml  

### 您要准备的

> 您的全部站点信息，包括您的站点本身，均应符合中国大陆及中国香港的有关法律法规，不涉及敏感内容

1. 自己站点的logo  
    - Logo应为正方形或圆形  
    - 使用常见图形文件格式（如`png`、`jpg`、`svg`等，不包括`tiff`、`gif`、`icns`）。  
    - Logo必需符合Gravater`G`分级要求（即适合在**任何网站上**展示给**任何年龄段**的**任何人**）  
    - 您站点的logo会被储存到我站的图床上并进行压缩，更新可能不及时，如需修改请提PR
2. 准备需要展示的站点名称  
    - 站点名称应适合在任何网站上展示给任何年龄段的任何人  
3. 准备一条站点描述（Slogan），不建议太长

### 交换步骤

1. 在`GitHub`上派生(`Fork`)这个仓库  
2. 【可选但强烈建议】在`src/img`目录中提交你的站点logo  
    - 文件名格式为`[domain].[format]`，如`example.com.png`，`blog.example.com.jpg`  
    - `commit`的标题应当名为`Add: [filename] ( [url] )`，如`Add: example.com.png ( https://example.com )`  
    - 原则上应小于`1 MiB`
3. 修改`src/links.yml`文件  
    - 按照如下格式将你的网站信息添加到 links.yml 文件的末尾：  
        ```yml
        "Name": # 名称置于双引号之中
          url: https://example.com/ # 网站的 URL，注意缩进
          img: https://yandao.is-a.dev/Friends/src/img/[YOUR_FILE_HERE] # 网站 Logo 的 URL，将[YOUR_FILE_HERE]换成上面提交的图片
          text: "永远在学习的路上" # 网站的 Slogan，置于双引号之中，注意缩进
        ```  
    - `commit`的标题应为`Add: [sitename] ( [url] )`，如`Add: example blog ( https://example.com )`  
    - 对于logo的链接，如果您执行了第二部，则将`[YOUR_FILE_HERE]`换成上面提交的图片的文件名，否则请填入您自行准备的链接，建议使用稳定的图床
4. 完成上述步骤后，请新建一个`Pull Request`
    - PR标题应为`Add: [sitename] ( [url] )`，如`Add: example blog ( https://example.com )`  
5. 当你发起的`Pull Request`被`Review`并被通过、合并后，你的网站将会在5分钟内显示在[友链页面](https://www.daoblog.top/friends)并加入[友链朋友圈](https://www.daoblog.top/fcircle)。
    - 注意，如果您的站点不提供RSS订阅流或您的站点的订阅文件路径不在友链朋友圈的[抓取规则](https://fcircle-doc.yyyzyyyz.cn/#/settings?id=%e9%a1%b9%e7%9b%ae%e9%85%8d%e7%bd%ae)内，请务必在PR中说明。

## 出现问题的友链

如果友链出现问题会展示在这里，不再进行友链相关审查，如果已解决问题还请主动告知。

```yml
"嗯哒嘿":
  url: https://www.wanglewei.com/
  img: https://img.sdut1.com/blog_yingwu.jpg
  text: "大黑（王乐伟）的博客 | bili UID2475977"
```

## 免责声明

请访问[此链接](https://www.daoblog.top/post/friendlinks-sm/)

---

<sub>本仓库灵感来源于 <a href="https://github.com/SukkaW/Friends">SukkaW/Friends</a> 与 <a href="https://github.com/renbaoshuo/Friends">renbaoshuo/Friends</a> ，Action配置参考自 <a href="https://github.com/Kitcham/hexo-links-json-generation">Kitcham</a> ，在此表示感谢。</sub><br>
<sub>&copy; 2023 Yandao. All rights reserved.</sub>