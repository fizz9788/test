# 使用官方 Python 运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# 安装系统依赖（如果需要）
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件（如果存在 requirements.txt）
COPY requirements.txt* ./

# 安装 Python 依赖
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# 复制应用代码
COPY . .

# 暴露端口（根据你的应用调整）
EXPOSE 8000

# 设置启动命令
CMD ["python", "wlstu_system.py"]

# 或者如果使用 Gunicorn:
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "wlstu_system:app"]
