FROM alpine:3.20 AS builder
WORKDIR /build
COPY *.html ./
COPY style.css ./
COPY js/ ./js/

ARG NGINX_VERSION
FROM nginx:alpine
LABEL version=$NGINX_VERSION

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/default.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /build/ /usr/share/nginx/html/

RUN mkdir -p /tmp/nginx-cache && chown nginx:nginx /tmp/nginx-cache

EXPOSE 80
