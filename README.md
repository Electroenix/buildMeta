# create_vsmeta
python实现群晖Video Station套件中视频文件的vsmeta文件生成

## 功能
通过脚本生成vsmeta文件，修改Video Station中视频信息，目前可以修改电影项目的标题，标语，年份，发布日期，类型，作者，导演，摘要，海报图这几项，基本包含了电影项目的所有信息，其他类型项目暂时还没用到，所以没做
>目前在Video Station 3.1.0版本上是有效的

## 使用
修改代码中下列值，背景图需要修改背景图的路径名，将背景图放在设置的路径下，然后运行脚本就会生成vsmeta文件
```
if __name__ == '__main__':

    metadata = MetaData()

    metadata.title = '标题'
    metadata.sub_title = '标语'
    metadata.year = '2024'
    metadata.public_time = '2024-02-26'  # 注意发布时间的格式必须是yyyy-mm-dd
    metadata.tag_list = ['类型1', '类型2', '类型3']
    metadata.artist = '作者'
    metadata.director = '导演'
    metadata.describe = '摘要'
    metadata.back_ground_path = './test_background.jpg'  # 背景图片的路径
    

    make_vsmeta_file('test.mp4.vsmeta', metadata)  # 第一个参数是生成的vsmeta文件的名字，必须是视频文件全名包含后缀名+.vsmeta
```

替换vsmeta文件可以先将视频文件改名，再放入vsmeta文件，再将视频文件还原，就可以刷新信息
