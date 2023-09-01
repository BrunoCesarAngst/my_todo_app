

ls tests/test_services.py | entr pytest tests/test_services.py

ls my_todo_app/main.py | entr python my_todo_app/main.py

quando se quer executar todos os testes de uma vez só, pode-se usar o comando:

```bash
pytest tests/unit
pytest tests/integration
pytest tests/ui
pytest tests/performance
pytest tests/database
pytest tests/security
```
