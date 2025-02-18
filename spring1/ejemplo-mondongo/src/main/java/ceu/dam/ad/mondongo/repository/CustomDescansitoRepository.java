package ceu.dam.ad.mondongo.repository;

import java.util.List;

import org.springframework.stereotype.Repository;

import ceu.dam.ad.mondongo.model.Descansito;
@Repository
public interface CustomDescansitoRepository {

	public List<Descansito> buscarPorNumeroAlumnos(Integer minNumAlumnos);
	
	public List<Descansito> buscarPorEdadAlumnos(Integer edad);

	
}
