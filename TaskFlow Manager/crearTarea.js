fetch("http://127.0.0.1:8000/crear",{
                method: "POST",
                headers:{"Content-Type":"application/json"},
                body: JSON.stringify({
                    Tarea: "Saludar",
                    Plaso:"no se"
                })
            })
