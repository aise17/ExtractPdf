


### STAGE 2: Setup ###

FROM nginx:1.14.1-alpine

RUN mkdir /ng-app 

WORKDIR /ng-app

COPY . .



## Copy our default nginx config
COPY ./default.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From ‘builder’ stage copy over the artifacts in dist folder to default nginx public folder
COPY /ng-app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
