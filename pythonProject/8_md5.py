# #对文件进行唯一身份操作
# import uvicorn
# from  fastapi import  FastAPI,UploadFile
#
# import hashlib
#
#
# app = FastAPI()
#
#
# @app.post('/UploadF')
# def  add_file(file:UploadFile):
#     content=  file.file.read()
#     # content 是二进制的文件内容
#     # .md5(参数是一个二进制数据)
#     filename = hashlib.md5(content).hexdigest()
#     # 母兔子.jpg
#     # new_filename = filename +'.'+ file.filename.split('.')[1]
#     with open(f'{filename}.{file.filename.split(".")[1]}','wb') as f:
#         f.write(content)
#     return "上传结束"
#
# if __name__ == '__main__':
#     uvicorn.run("8_md5:app",host='127.0.0.1',port=8010)
#




list_1=[{'a':1},{'c':3},{'b':2}]
new_list=sorted(list_1,key=lambda x:list(x.values())[0])
print(new_list)
