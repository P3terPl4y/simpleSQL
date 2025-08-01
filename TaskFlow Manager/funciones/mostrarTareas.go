package funciones

import (
	"TaskFlowManager/datos"
	"database/sql"
	"fmt"
	"log"

	"github.com/gofiber/fiber/v3"
)

func MostrarTareas(c fiber.Ctx, db *sql.DB) error {
	rows, err := db.Query("SELECT * FROM tareas;")

	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	var tareas []datos.Datos

	for rows.Next() {
		var tarea datos.Datos

		if err := rows.Scan(&tarea.Tarea, &tarea.Plaso); err != nil {
			log.Fatal(err)
			continue
		}
		tareas = append(tareas, tarea)

	}
	fmt.Println(tareas)
	return c.JSON(tareas)
}
