package ceu.dam.ad.mondongo.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import ceu.dam.ad.mondongo.model.Descansito;
import java.util.List;

@Repository
public interface DescansitoRepository extends MongoRepository<Descansito, String>, CustomDescansitoRepository{

	public List<Descansito> findByProfesor(String profesor);
	
}
