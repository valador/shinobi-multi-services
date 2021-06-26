FROM node:12-alpine

ENV SHINOBI_INSTALL_DIRECTORY=/opt/shinobi
ENV DOCKER_SHINOBI_INSTALL_DIRECTORY=/opt/docker-shinobi

RUN apk add --update --no-cache ffmpeg \ 
    python3-dev \
    pkgconfig \
    make \
    g++ \
    jpeg-dev \
    git \
    ttf-freefont \
    mariadb-client \
    wget \
    tar \
    xz \
    socat \
    gnutls \
    x264 \
    libssh2 \
    bzip2 \
    jq \
    openssl \
    ca-certificates

RUN update-ca-certificates
# # For Canvas
# RUN apk add --no-cache sudo \
#         curl \
#         libpng \
#         libpng-dev \
#         pango-dev \
#         cairo-dev \
#         cairo \
#         giflib-dev \
#         imagemagick

# Install ffmpeg static build version from cdn.shinobi.video
RUN wget -q https://cdn.shinobi.video/installers/ffmpeg-release-64bit-static.tar.xz \
    && tar xpf ./ffmpeg-release-64bit-static.tar.xz -C ./ \
    && cp -f ./ffmpeg-3.3.4-64bit-static/ff* /usr/bin/ \
    && chmod +x /usr/bin/ff* \
    && rm -f ffmpeg-release-64bit-static.tar.xz \
    && rm -rf ./ffmpeg-3.3.4-64bit-static

#Install dependecies for Google Coral Shinobi Integration
# RUN pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime \
# 	&& pip3 install pillow

# Install build dependencies, fetch shinobi, and install
RUN apk add --virtual build-deps --no-cache \ 
  build-base \ 
  coreutils \ 
  nasm \
  python \
  make \
  pkgconfig \
  wget \
  freetype-dev \ 
  gnutls-dev \ 
  lame-dev \ 
  libass-dev \ 
  libogg-dev \ 
  libtheora-dev \ 
  libvorbis-dev \ 
  libvpx-dev \ 
  libwebp-dev \ 
  opus-dev \ 
  rtmpdump-dev \ 
  x264-dev \ 
  x265-dev \ 
  yasm-dev

# #  add glibc and install canvas
# RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
#     wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.33-r0/glibc-2.33-r0.apk && \
#     apk add glibc-2.33-r0.apk
#     #npm install canvas@2.5.0

ARG SHINOBI_REPOSITORY_URL=https://gitlab.com/Shinobi-Systems/Shinobi.git
ARG SHINOBI_REPOSITORY_BRANCH=master
ARG SHINOBI_REPOSITORY_COMMIT

RUN git clone --branch="${SHINOBI_REPOSITORY_BRANCH}" "${SHINOBI_REPOSITORY_URL}" "${SHINOBI_INSTALL_DIRECTORY}" \
    && cd "${SHINOBI_INSTALL_DIRECTORY}" \
    && if [ "${SHINOBI_REPOSITORY_COMMIT}" != "" ]; then \
           git checkout "${SHINOBI_REPOSITORY_COMMIT}"; \
       fi \
    && npm i npm@latest -g \
    # && npm i -g node-gyp \
    && npm install pm2 -g \
    # && npm install canvas@2.7.0 moment --unsafe-perm \
    && npm install \
    && apk del build-deps

COPY generate-config.py "${DOCKER_SHINOBI_INSTALL_DIRECTORY}/"
COPY generate-super-config.sh "${DOCKER_SHINOBI_INSTALL_DIRECTORY}/"
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN mkdir -p /config
COPY config.default.json /config/
COPY pm2Shinobi.yml "${SHINOBI_INSTALL_DIRECTORY}/"


RUN chmod +x \
    /docker-entrypoint.sh \
    "${DOCKER_SHINOBI_INSTALL_DIRECTORY}/generate-config.py" \
    "${DOCKER_SHINOBI_INSTALL_DIRECTORY}/generate-super-config.sh"

EXPOSE 8080

ENTRYPOINT ["/docker-entrypoint.sh"]

WORKDIR /opt/shinobi
CMD ["pm2-docker", "pm2Shinobi.yml"]

# # HEALTHCHECK --interval=10m --start-period=30s \
# #     CMD curl -f http://localhost:8080 || exit 1
