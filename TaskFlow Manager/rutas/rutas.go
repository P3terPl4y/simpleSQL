package rutas

import (
	"TaskFlowManager/database"
	"TaskFlowManager/funciones"

	"github.com/gofiber/fiber/v3"
)

func Rutas(app *fiber.App) {
	app.Get("/",func(c fiber.Ctx)error{
		return c.SendFile("tareas.html")
	})
	app.Get("/tareas", func(c fiber.Ctx) error {
		return funciones.MostrarTareas(c, database.DB)
	})
	app.Post("/crear", func(c fiber.Ctx) error {
		return funciones.CrearTareas(c, database.DB)
	})
	app.Delete("/eliminar", func(c fiber.Ctx) error {
		return funciones.EliminarTareas(c, database.DB)
	})
}
