
FROM nginx:latest

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY ./ /usr/share/nginx/html/
#COPY script.js /usr/share/nginx/html/script.js
#COPY style.css /usr/share/nginx/html/style.css

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
