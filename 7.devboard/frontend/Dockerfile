#-------------------------builder------------------------
FROM dhi.io/node:26-dev AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci --legacy-peer-deps

COPY . .

RUN npm run build

#--------------------------runner-----------------------
FROM nginx:alpine    

COPY --from=builder /app/default.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx","-g","daemon off;"]