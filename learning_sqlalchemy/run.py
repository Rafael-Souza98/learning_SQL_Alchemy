from infra.repository.atores_repository import AtoresRepository
from infra.repository.filmes_repository import FilmesRepository



repo2 = FilmesRepository()
response2 = repo2.select()
filme = response2[0]
print(filme.atores)
print(filme.titulo)