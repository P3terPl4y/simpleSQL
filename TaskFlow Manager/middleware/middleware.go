package middleware

import (
	"log"

	"github.com/gofiber/fiber/v3"
)

func Middleware(c fiber.Ctx) error {
	log.Println(c.Method(), c.Path(), c.Hostname(), c.Port())

	return c.Next()
}
