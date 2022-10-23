FROM node:16

RUN npm install -g pnpm

COPY . .

RUN pnpm install

RUN pnpm build

RUN pnpm export
