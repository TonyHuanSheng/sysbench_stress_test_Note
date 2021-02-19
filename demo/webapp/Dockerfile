FROM python:3.7
#設定資料夾
RUN mkdir /webapp
WORKDIR /webapp
#當前目錄下檔案複製
COPY . /webapp
#安裝套件
RUN pip install pipenv
RUN pip install -r requirements.txt
#映射
EXPOSE 5000

CMD ["python","./webapp/app.py"]
