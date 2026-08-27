FROM dhi.io/nginx:1-alpine3.23

WORKDIR /app

COPY . /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx","-g","daemon off;"]

