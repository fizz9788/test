from fastapi import FastAPI,Depends
import uvicorn

app = FastAPI()

stu1 = {"id":1,"name":"张亮","age":21,'sex':'男'}
stu2 = {"id":2,"name":"张迪","age":20,'sex':'男'}
stu3 = {"id":3,"name":"董俊","age":8,'sex':'男'}
stu4 = {"id":4,"name":"昂多","age":18,'sex':'女'}
stu5 = {"id":5,"name":"丽莎","age":19,'sex':'女'}
stu6 = {"id":6,"name":"张朝辉","age":18,'sex':'男'}
stus = [stu1,stu2,stu3,stu4,stu5,stu6]

teacher1 = {"id":1,"name":"张亮","age":21,'sex':'男'}
teacher2 = {"id":2,"name":"张迪","age":20,'sex':'男'}
teacher3 = {"id":3,"name":"董俊","age":8,'sex':'男'}
teacher4 = {"id":4,"name":"昂多","age":18,'sex':'女'}
teacher5 = {"id":5,"name":"丽莎","age":19,'sex':'女'}
teacher6 = {"id":6,"name":"张朝辉","age":18,'sex':'男'}
teachers = [teacher1,teacher2,teacher3,teacher4,teacher5,teacher6]

def check_lines(skip:int,limit:int):
    return {'skip':skip,'limit':limit}

@app.get("/student")
def get_student(comment=Depends(check_lines)):
    return stus[comment.get('skip'):comment.get('skip')+comment.get('limit')]

@app.get("/teacher")
def get_student(comment=Depends(check_lines)):
    return teachers[comment.get('skip'):comment.get('skip') + comment.get('limit')]

if __name__ == '__main__':
    uvicorn.run("0313依赖注入:app",host="127.0.0.1",port=8000)