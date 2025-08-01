package funciones

import (
	"TaskFlowManager/datos"
	"database/sql"
	"log"

	"github.com/gofiber/fiber/v3"
)

func EliminarTareas(c fiber.Ctx, db *sql.DB) error {
	tarea := new(datos.Datos)
	err := c.Bind().Body(tarea)
	if err != nil {
		log.Fatal(err)
	}
	result, err := db.Exec("DELETE FROM tareas WHERE tarea=?", tarea.Tarea)

	if err != nil {
		log.Fatal(err)
	}
	return c.JSON(result)
}
