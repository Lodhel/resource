#!/bin/sh

start() {
    docker-compose -f docker-compose.yml up -d
}

stop() {
    docker-compose -f docker-compose.yml down
}

if [ -n "$1" ]; then
    case "$1" in
    build) docker-compose -f docker-compose.yml up --build -d ;;
    init) docker exec flask sh entrypoint_db.sh ;;
    makemigrations) docker exec flask sh entrypoint_db_create_migrate.sh ;;
    start) start ;;
    stop) stop ;;
    backup) docker exec -t postgres pg_dumpall -c -U postgres >dump_$(date +%d-%m-%Y"_"%H_%M_%S).sql ;;
    restore) cat "$2" | docker exec -i postgres psql -U postgres ;;
    migrate) docker exec flask flask db migrate -m "$2" && docker exec flask flask db upgrade ;;
    shell) docker exec -it flask flask shell ;;
    *) echo "$1 is not an option." ;;
    esac
else
    echo "No parameters found."
fi
