package database

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

var DB *sql.DB

func Connect() {
	var err error
	DB, err = sql.Open("sqlite3", "Tareas.db")

	if err != nil {
		log.Fatal(err)
	}

	if err = DB.Ping(); err != nil {
		log.Fatal(err)
	}
	fmt.Println("Conexion Exitosa")
	_, err = DB.Exec("CREATE TABLE IF NOT EXISTS tareas (tarea TEXT NOT NULL,plaso TEXT NOT NULL);")

	if err != nil {
		log.Fatal(err)
	}
}
