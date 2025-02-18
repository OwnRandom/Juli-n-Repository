package ceu.dam.ad.ejemplo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import ceu.dam.ad.ejemplo.modelo.Actor;

@Repository
public interface ActorRepository extends JpaRepository<Actor, Long>{

	public List<Actor> findByFirstNameContainingOrLastNameContaining(String firstName, String lastName);

	
	
}
