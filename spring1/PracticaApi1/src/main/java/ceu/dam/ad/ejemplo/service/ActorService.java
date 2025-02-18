package ceu.dam.ad.ejemplo.service;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import ceu.dam.ad.ejemplo.model.Actor;
import ceu.dam.ad.ejemplo.repository.ActorRepository;

@Service
public class ActorService {

	@Autowired
	private ActorRepository repository;
	
	public Actor consultaActor(Long id) throws ActorNotFound {
		Optional<Actor> actorOp = repository.findById(id);
		if(actorOp.isEmpty()) {
			throw new ActorNotFound("No existe actor con el id indicado");
		}
		return actorOp.get();
	}

	public List<Actor> buscarNombreApellido(String nombre, String apellido) {
		return repository.findByFirstNameAndLastNameContaining(nombre, apellido);
	}
	
	public List<Actor> buscarFecha(LocalDate fechaIni, LocalDate fechaFin) {
		return repository.findByLastUpdateBetween(fechaIni, fechaFin);
		
	}
	
	@Transactional
	public Actor crearActor(Actor actor) {
		return repository.save(actor);
	}
	
	@Transactional
	public Actor actualizarActor(Actor actor) throws ActorNotFound {
		consultaActor(actor.getActorId());
		return repository.save(actor);
	}
	
	@Transactional
	public void borrarActor(Long id) throws ActorNotFound {
		consultaActor(id);
		repository.deleteById(id);
		
	}

}
