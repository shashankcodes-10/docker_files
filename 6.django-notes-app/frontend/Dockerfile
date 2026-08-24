#------------------builder stage-------------------
FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci 

COPY . .

RUN npm run build 

#------------------runner stage---------------------
FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html

COPY --from=builder /app/default.conf  /etc/nginx/conf.d/default.conf

EXPOSE 80 

CMD ["nginx","-g","daemon off ;"]