# 使用Python 3.8作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . .

# 安装所需的Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口号（如果需要）
EXPOSE 80

# 运行Python脚本
CMD ["python", "TGouyichax.py"]
