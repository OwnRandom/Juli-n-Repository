package ceu.dam.ad.mondongo.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import ceu.dam.ad.mondongo.model.Descansito;
import ceu.dam.ad.mondongo.repository.DescansitoRepository;


@Service
public class DescansitoService {
	
	
	@Autowired
	private DescansitoRepository repository;
	
	
	public Descansito crearDescanso(Descansito descanso) {
		return repository.save(descanso);
	}
	
	public List<Descansito> findByProfesor(String profesor) {
		return repository.findByProfesor(profesor);
		
	}
	
	public List<Descansito> buscar(String profesor) {
		return repository.findByProfesor(profesor);
		
	}
	
	public List<Descansito> buscarPorNumAlumnos(Integer num) {
		return repository.buscarPorNumeroAlumnos(num);
		
	}
	
	public List<Descansito> buscarPorEdadAlumnos(Integer edad) {
		return repository.buscarPorEdadAlumnos(edad);
		
	}
	
}
