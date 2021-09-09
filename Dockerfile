FROM python:3.8
WORKDIR /home/notebooks
RUN pip install numpy \
                pandas \
                scikit-learn \
                seaborn \ 
                jupyter \ 
                notebook     
COPY . .
EXPOSE 8888
ENTRYPOINT ["jupyter", "notebook","--ip=0.0.0.0","--allow-root", "--no-browser"]