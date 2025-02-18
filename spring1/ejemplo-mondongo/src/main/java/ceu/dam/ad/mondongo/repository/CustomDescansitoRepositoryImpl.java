package ceu.dam.ad.mondongo.repository;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Repository;

import ceu.dam.ad.mondongo.model.Descansito;
@Repository
public class CustomDescansitoRepositoryImpl implements CustomDescansitoRepository{

	@Autowired
	private MongoTemplate mongoTemplate;
	
	@Override
	public List<Descansito> buscarPorNumeroAlumnos(Integer minNumAlumnos) {
		Query query = new Query();
		
		query.addCriteria(Criteria.where("alumnos").gte(minNumAlumnos));
		//query.addCriteria(Criteria.where("autorizado").is(true));
		
		//esto es para concadenar criterias
		//query.addCriteria(new Criteria().orOperator(
		//		Criteria.where("alumnos").gte(minNumAlumnos),
		//		Criteria.where("autorizado").is(true)
		//		));
		
		return mongoTemplate.find(query, Descansito.class);
		//En caso de ser un unico elemento seria asi
		//mongoTemplate.findOne(query, Descansito.class);
		
		
	}

	@Override
	public List<Descansito> buscarPorEdadAlumnos(Integer edad) {
		Query query = new Query();
		
		query.addCriteria(Criteria.where("alumnos.edad").is(edad));

		return mongoTemplate.find(query, Descansito.class);
	}

}
