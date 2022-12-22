# Билд докерфайла
    docker build . -t bot-image
# Деплой
    docker run --env TOKEN="TOKEN" -d bot-image 
