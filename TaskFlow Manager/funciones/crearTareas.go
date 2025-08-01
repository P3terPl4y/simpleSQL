package funciones

import (
	"TaskFlowManager/datos"
	"database/sql"
	"fmt"
	"log"

	"github.com/gofiber/fiber/v3"
)

func CrearTareas(c fiber.Ctx, db *sql.DB) error {
	tarea := new(datos.Datos)

	if err := c.Bind().Body(tarea); err != nil {
		log.Fatal(err)
	}

	result, err := db.Exec("INSERT INTO tareas (tarea,plaso) VALUES (?,?)", tarea.Tarea, tarea.Plaso)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(tarea.Tarea, tarea.Plaso)
	return c.JSON(result)
}
