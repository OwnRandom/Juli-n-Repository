package ceu.dam.ad.ejemplo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import ceu.dam.ad.ejemplo.model.Equipo;

@Repository
public interface EquipoRepository extends JpaRepository<Equipo, Integer>{

	
	
}
