package ceu.dam.ad.ejemplo;

import java.util.ArrayList;
import java.util.List;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import ceu.dam.ad.ejemplo.modelo.Actor;
import ceu.dam.ad.ejemplo.service.ActorNotFoundException;
import ceu.dam.ad.ejemplo.service.ActorService;
import ceu.dam.ad.ejemplo.service.ActorServiceException;

@SpringBootApplication
public class App {

	public static void main(String[] args) {
		ConfigurableApplicationContext context = SpringApplication.run(App.class, args);
		
		ActorService service = context.getBean(ActorService.class);
		
		try {
			System.out.println(service.consultarActor(4L));
		} catch (ActorNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		//actualizar
		//En caso de que solo quiera cambiar el apellido primero consulto para rellenar y lo actualizo
		Actor c = new Actor();
		c.setId(200L);
		c.setFirstName("Blas 1");
		c.setLastName("de los montes 2");
		
		service.actualizarActor(c);
		
		
		
		//insertar
		Actor a = new Actor();
		a.setFirstName("Blas 1");
		a.setLastName("de los montes 2");
		
		Actor b = new Actor();
		b.setFirstName("Blas 2");
		b.setLastName("de los montes 2");
		
		List<Actor> lista = new ArrayList<Actor>();
		lista.add(a);
		lista.add(b);
		
		try {
			service.crearActor(lista);
		} catch (ActorServiceException e) {
			System.out.println("error al insertar actor");
		}
		System.out.println(a);
		
		
		
	}

}
