package ceu.dam.ad.libros.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Service;

import ceu.dam.ad.libros.model.Autor;
import ceu.dam.ad.libros.repository.AutorRepository;
import jakarta.transaction.Transactional;

@Service
public class AutoresServiceImp implements AutoresService {

	@Autowired
	private AutorRepository repository;

	@Override
	@Transactional
	public void guardarAutores(List<Autor> autores) throws AutorServiceException {
		try {
			repository.saveAll(autores);
		} catch (DataAccessException e) {
			throw new AutorServiceException("Error al acceder a la base de datos: " + e);
		}

	}

	@Override
	public Autor consultarAutor(Long id) throws AutorNotFoundException, AutorServiceException {
		try {
			
//			Pasar optional a un objeto
//			Optional<Autor> autor = repository.findById(id);
//			Autor autor1 = autor.get();
		
			return repository.findById(id)
					.orElseThrow(() -> new AutorNotFoundException("Autor no encontrado con ID: " + id));

		
			
		} catch (DataAccessException e) {
			throw new AutorServiceException("Autor no encontrado con ID: " + id);
		}
	}

}
