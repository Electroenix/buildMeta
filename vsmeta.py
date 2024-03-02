import base64
import hashlib
import time
from metadata import MetaData


# 计算vsmeta中数据的校验码
def get_check_code(len):
    if len > 0xff:
        code_h = int(len % 0x80 + 0x80).to_bytes()
    else:
        code_h = len.to_bytes()

    rest = int(len / 0x80)
    if rest > 0xff:
        code_l = get_check_code(rest)
    else:
        code_l = rest.to_bytes()

    if int.from_bytes(code_l) > 0:
        return code_h + code_l
    else:
        return code_h


# 生成vsmeta文件
def make_vsmeta_file(filename, metadata):
    f_vsmeta = open(filename, 'wb')

    # 标题
    f_vsmeta.write(bytes.fromhex('080112'))
    f_vsmeta.write(get_check_code(len(metadata.title.encode())))
    f_vsmeta.write(metadata.title.encode())

    # 标题2
    f_vsmeta.write(bytes.fromhex('1a'))
    f_vsmeta.write(get_check_code(len(metadata.title.encode())))
    f_vsmeta.write(metadata.title.encode())

    if metadata.sub_title:
        # 副标题
        f_vsmeta.write(bytes.fromhex('22'))
        f_vsmeta.write(get_check_code(len(metadata.sub_title.encode())))
        f_vsmeta.write(metadata.sub_title.encode())

    # 年份
    if metadata.year:
        f_vsmeta.write(bytes.fromhex('28'))
        f_vsmeta.write((int(metadata.year) - 0x700).to_bytes())
        f_vsmeta.write(bytes.fromhex('0f'))

    # 发布日期
    if metadata.public_time:
        f_vsmeta.write(bytes.fromhex('32'))
        f_vsmeta.write(get_check_code(len(metadata.public_time.encode())))
        f_vsmeta.write(metadata.public_time.encode())

    # 锁定状态
    f_vsmeta.write(bytes.fromhex('3801'))

    # 简介
    if metadata.describe:
        f_vsmeta.write(bytes.fromhex('42'))
        f_vsmeta.write(get_check_code(len(metadata.describe.encode())))
        f_vsmeta.write(metadata.describe.encode())

    f_vsmeta.write(bytes.fromhex('4a'))
    f_vsmeta.write(get_check_code(len('null'.encode())))
    f_vsmeta.write('null'.encode())

    # 组1数据
    group1 = bytes()
    # 导演
    if metadata.director:
        group1 = bytes.fromhex('12')
        group1 = group1 + get_check_code(len(metadata.director.encode()))
        group1 = group1 + metadata.director.encode()

    # 标签
    if metadata.tag_list:
        for t in metadata.tag_list:
            group1 = group1 + bytes.fromhex('1a')
            group1 = group1 + get_check_code(len(t.encode()))
            group1 = group1 + t.encode()

    # 作者
    if metadata.artist:
        group1 = group1 + bytes.fromhex('22')
        group1 = group1 + get_check_code(len(metadata.artist.encode()))
        group1 = group1 + metadata.artist.encode()

    # 写入组1数据
    if group1:
        f_vsmeta.write(bytes.fromhex('52'))
        f_vsmeta.write(get_check_code(len(group1)))
        f_vsmeta.write(group1)

    f_vsmeta.write(bytes.fromhex('5a00'))

    # 评分
    f_vsmeta.write(bytes.fromhex('60ffffffffffffffffff01'))

    # 组3数据
    if metadata.back_ground_path:
        # 读取背景图
        with open(metadata.back_ground_path, 'rb') as f_bg_image:
            image_data = f_bg_image.read()
            # 背景图转base64编码
            bg_image_base64 = base64.b64encode(image_data)
            # 计算图片md5
            image_md5 = hashlib.md5(image_data).hexdigest()

        # 背景图base64
        group3 = bytes.fromhex('0a')
        group3 = group3 + get_check_code(len(bg_image_base64))
        group3 = group3 + bg_image_base64

        # md5
        group3 = group3 + bytes.fromhex('12')
        group3 = group3 + get_check_code(len(image_md5.encode()))
        group3 = group3 + image_md5.encode()

        # 时间戳
        group3 = group3 + bytes.fromhex('18')
        group3 = group3 + get_check_code(int(time.time()))

        # 写入组3数据
        f_vsmeta.write(bytes.fromhex('aa01'))
        f_vsmeta.write(get_check_code(len(group3)))
        f_vsmeta.write(group3)

    f_vsmeta.close()



