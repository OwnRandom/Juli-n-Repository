package ceu.dam.ad.ejemplo.repository;

import java.time.LocalDate;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import ceu.dam.ad.ejemplo.model.Actor;

@Repository
public interface ActorRepository extends JpaRepository<Actor, Long>{

	public List<Actor> findByFirstNameAndLastNameContaining(String nombre, String apellido);

	public List<Actor> findByLastUpdateBetween(LocalDate fechaIni, LocalDate fechaFin);
	
}
