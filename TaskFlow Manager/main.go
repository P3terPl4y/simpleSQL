package main

import (
	"TaskFlowManager/database"
	"TaskFlowManager/middleware"
	"TaskFlowManager/rutas"
	"log"

	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/middleware/cors"
	"github.com/gofiber/fiber/v3/middleware/logger"
)

func main() {

	database.Connect()
	defer database.DB.Close()

	app := fiber.New()

	app.Use(cors.New())
	app.Use(logger.New())

	app.Use(middleware.Middleware)

	rutas.Rutas(app)

	log.Fatal(app.Listen(":8000"))

}
