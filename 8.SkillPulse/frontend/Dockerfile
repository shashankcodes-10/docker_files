FROM dhi.io/nginx:1-alpine3.23

COPY index.html /usr/share/nginx/html/
COPY css/ /usr/share/nginx/html/css/
COPY js/ /usr/share/nginx/html/js/

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

