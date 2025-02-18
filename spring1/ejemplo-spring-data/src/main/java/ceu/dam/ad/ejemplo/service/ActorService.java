package ceu.dam.ad.ejemplo.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import ceu.dam.ad.ejemplo.modelo.Actor;
import ceu.dam.ad.ejemplo.repository.ActorRepository;

@Service
public class ActorService {

	@Autowired
	private ActorRepository repository;

	public Actor consultarActor(Long id) throws ActorNotFoundException {
		Optional<Actor> actor = repository.findById(id);
//		Esto es lo mismo que lo de abajo
//		actor.orElseThrow(() -> new ActorNotFoundException("No existe actor con esta id"));

		if (!actor.isPresent()) {

			throw new ActorNotFoundException("No existe actor con esta id");

		}
		return actor.get();

	}

	// Consultar todos los actores con su filtro de nombre o apellido especifico
	public List<Actor> consultarActores(String filtro) {

		return repository.findByFirstNameContainingOrLastNameContaining(filtro, filtro);

	}

//	En caso de que queramos que entren o todos o ninguno
	@Transactional
	public void crearActor(List<Actor> actores) throws ActorServiceException {
		try {

			actores.forEach(a -> repository.save(a));

			// Esto es lo mismo que hacerlo transactional
//				repository.saveAll(actores);

//				for (Actor actor : actores) {
//					repository.save(actor);
//				}

		} catch (DataAccessException e) {
			throw new ActorServiceException("Error al intertar", e);
		}
	}

	public void actualizarActor(Actor actor) {

		repository.save(actor);

	}

	public void borrarActor(Long id) {
//Hay muchos tipos como estos
//		repository.delete(actor);
//		repository.deleteAll();
//		repository.deleteAllById(null);

		repository.deleteById(id);

	}

}
