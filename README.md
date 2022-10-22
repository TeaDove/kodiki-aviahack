### Structure
- backend: FastAPI бекэнд сервис
- terraform: terraform+terragrunt деплоймент в Yandex Cloud с использованием
Yandex Cloud Serverless Functions и Yandex Cloud Api Gateway
- ml: дата процессинг

### Deployment to Yandex Cloud
go to `terraform` directory and read `README.md`

### Local run
```shell
docker-compose up
# go to http://localhost:8080/docs во swagger

# prediction
curl -X GET http://localhost:8080/...
```
