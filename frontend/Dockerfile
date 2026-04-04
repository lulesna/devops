FROM alpine:3.20 AS build
WORKDIR /build
COPY *.html ./
COPY style.css ./
COPY js/ ./js/

FROM nginx:1.27-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/default.conf /etc/nginx/conf.d/default.conf

COPY --from=build /build/ /usr/share/nginx/html/

RUN mkdir -p /tmp/nginx-cache && chown nginx:nginx /tmp/nginx-cache

EXPOSE 80
