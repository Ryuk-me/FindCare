FROM mhart/alpine-node:16
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn
COPY . .

RUN yarn build
FROM mhart/alpine-node:slim-16

WORKDIR /app

COPY --from=0 /app .
COPY . .
ENV TZ=Asia/Kolkata
EXPOSE 3000
CMD ["node", "./build"]