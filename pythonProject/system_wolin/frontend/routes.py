from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os


def register_frontend_routes(app: FastAPI):
    """
    注册前端路由
    
    Args:
        app: FastAPI 实例对象
    """
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir, 'static')
    
    # 挂载静态文件
    app.mount("/frontend/static", StaticFiles(directory=static_dir), name="frontend-static")
    
    # 前端页面路由
    @app.get("/frontend", tags=["前端"])
    async def frontend_index():
        """
        学生管理系统前端页面
        """
        index_path = os.path.join(current_dir, 'index.html')
        return FileResponse(index_path)
    
    @app.get("/frontend/", tags=["前端"])
    async def frontend_index_slash():
        """
        学生管理系统前端页面（带斜杠）
        """
        index_path = os.path.join(current_dir, 'index.html')
        return FileResponse(index_path)
