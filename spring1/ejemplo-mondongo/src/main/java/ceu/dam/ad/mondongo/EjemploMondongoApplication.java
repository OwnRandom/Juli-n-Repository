package ceu.dam.ad.mondongo;

import java.util.ArrayList;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import ceu.dam.ad.mondongo.model.Alumno;
import ceu.dam.ad.mondongo.model.Descansito;
import ceu.dam.ad.mondongo.service.DescansitoService;
import ch.qos.logback.core.util.SystemInfo;

@SpringBootApplication
public class EjemploMondongoApplication {

	public static void main(String[] args) {
		ConfigurableApplicationContext context = SpringApplication.run(EjemploMondongoApplication.class, args);
		DescansitoService service = context.getBean(DescansitoService.class);
		
		Descansito d = new Descansito();
		
		d.setProfesor("juan");
		d.setDuracion(40);
		d.setAutorizado(true);
		d.setAlumnos(new ArrayList<>());
		d.getAlumnos().add(new Alumno("Irene", 22, true));
		d.getAlumnos().add(new Alumno("Nemo", 22, true));
		
		//System.out.println(service.crearDescanso(d)); 
		//service.findByProfesor("Rodrigo").forEach(System.out::println);
		System.out.println(service.buscarPorNumAlumnos(2));
		service.buscarPorEdadAlumnos(22).forEach(System.out::println);
	}

}
