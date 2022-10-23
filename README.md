### Structure
- backend: FastAPI бекэнд сервис
- terraform: terraform+terragrunt деплоймент в Yandex Cloud с использованием
Yandex Cloud Serverless Functions и Yandex Cloud Api Gateway
- ml: дата процессинг, в Dockerfile описан процесс установки зависимостей для debian-slims
- frontend: статический фронтенд на `next.js`

### Deployment to Yandex Cloud
перейдите в директорию `terraform` и изучите `README.md`

### Local run
```shell
docker-compose up
# go to http://localhost:8080/docs во swagger

# prediction
curl -X GET http://localhost:8080/...
```
