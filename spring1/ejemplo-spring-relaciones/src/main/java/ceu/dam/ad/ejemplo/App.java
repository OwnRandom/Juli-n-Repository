package ceu.dam.ad.ejemplo;

import java.util.Optional;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import ceu.dam.ad.ejemplo.model.Equipo;
import ceu.dam.ad.ejemplo.model.Estadio;
import ceu.dam.ad.ejemplo.model.Jugador;
import ceu.dam.ad.ejemplo.repository.EquipoRepository;
import ceu.dam.ad.ejemplo.repository.JugadorRepository;

@SpringBootApplication
public class App {

	
	
	
	public static void main(String[] args) {
		ConfigurableApplicationContext context = SpringApplication.run(App.class, args);

		EquipoRepository repository = context.getBean(EquipoRepository.class);
		JugadorRepository repositoryJug = context.getBean(JugadorRepository.class);
		
//		Jugador jugador = repositoryJug.findById(3).get();
//		System.out.println(jugador);
		
		
		Optional<Equipo> equipo = repository.findById(1);
		System.out.println(equipo.get());
//		
//		Estadio estadio1 = new Estadio();
//		estadio1.setCapacidad(999);
//		estadio1.setCiudad("barcelona");
//		
//		Equipo milan = new Equipo();
//		milan.setNombre("milan");
//		milan.setEstadio(estadio1);
//		
//		repository.save(milan);
		
	}
}
