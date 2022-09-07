from infra.repository.filems_repository import FilmesRepository

repo = FilmesRepository()
repo.insert('Jumanji', 'Aventura', '1999')
repo.delete('Superman')
data = repo.select()

print(data)