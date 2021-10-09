import os
from PIL import Image, ImageSequence


def parseGIF(gifname):
    # 将gif解析为图片
    # 读取GIF
    im = Image.open(gifname)
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(im)
    # 获取文件名
    file_name = gifname.split(".")[0]
    index = 1
    # 判断目录是否存在
    pic_dirct = "imgs/{0}".format(file_name)
    mkdirlambda = lambda x: os.makedirs(
        x) if not os.path.exists(x) else True  # 目录是否存在,不存在则创建
    mkdirlambda(pic_dirct)
    # 遍历图片流的每一帧
    for frame in iter:
        print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
        frame.save("imgs/%s/frame%d.png" % (file_name, index))
        index += 1

    # frame0 = frames[0]
    # frame0.show()

    # 把GIF拆分为图片流
    # imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]
    # 把图片流重新成成GIF动图
    # imgs[0].save('out.gif', save_all=True, append_images=imgs[1:])

    # # 图片流反序
    # imgs.reverse()
    # # 将反序后的所有帧图像保存下来
    # imgs[0].save('./reverse_out.gif', save_all=True, append_images=imgs[1:])


if __name__ == "__main__":
    parseGIF("3.gif")