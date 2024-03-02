# buildMeta
python生成群晖Video Station使用的vsmeta文件及emby使用的nfo文件

## 功能
* 生成vsmeta文件，更新Video Station中视频信息
>目前在Video Station 3.1.0版本上是有效的

* 生成nfo文件，更新emby中视频元数据信息

* 支持配置电影标题，副标题，年份，发布日期，类型，作者，导演，摘要，背景图(只在生成vsmeta文件时有效)

## 使用
在命令行中执行脚本，支持以下参数：
```
buildMeta.py [-h] [--vsmeta VSMETA] [--nfo NFO] [--title TITLE] [--subtitle SUBTITLE] [--year YEAR]
                    [--public PUBLIC] [--tags TAGS] [--artist ARTIST] [--director DIRECTOR] [--describe DESCRIBE]
                    [--bgimage BGIMAGE]
```

参数功能：
```
--vsmeta VSMETA
    后面跟文件名，生成vsmeta文件

--nfo NFO
    后面跟文件名，生成nfo文件，可以和--vsmeta同时使用

--title TITLE
    标题

--subtitle SUBTITLE
    副标题

--year YEAR
    年份，如2024

--public PUBLIC
    发布日期，如2024-01-01，注意格式必须是yyyy-mm-dd

--tags TAGS
    标签/类型，标签之间用,隔开

--artist ARTIST
    作者

--director
    导演

--describe
    摘要/简介

--bgimage BGIMAGE
    背景图片的路径，只在生成vsmeta文件时候有用
```

