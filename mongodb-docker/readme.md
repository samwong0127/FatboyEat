# Launch the MongoDB Server container.
```
docker-compose up
```

# Launched a bash shell  into mongodb container and check that the database and collections are initialized
```
docker exec -it project_gp5_db bash
```

```
mongo -u comp3122_gp5 -p 12345
show dbs;
use restaurant
show collections;
db.store.find()
```

# Stop and remove mongodb container and volumes
```
docker-compose down -v
```
