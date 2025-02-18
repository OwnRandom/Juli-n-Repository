package ceu.dam.ad.ejemplo.api;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import ceu.dam.ad.ejemplo.model.Actor;
import ceu.dam.ad.ejemplo.service.ActorNotFound;
import ceu.dam.ad.ejemplo.service.ActorService;
import io.swagger.v3.oas.annotations.Operation;
import jakarta.validation.Valid;

@RestController
public class ActorApiService {
	
	@Autowired
	private ActorService service;
	
	@GetMapping("/actores/{id}")
	@Operation(summary = "consulta de actores", description = "consulta de actores por la id")
	public Actor consultar(@PathVariable Long id) throws ActorNotFound {
		return service.consultaActor(id);
	}

	@GetMapping("/actores")
	@Operation(summary = "busqueda de actores", description = "busqueda de actores por nombre y apellidos")
	public List<Actor> buscarActorNombreApellido(@RequestParam String nombre,@RequestParam String apellido) {
		return service.buscarNombreApellido(nombre, apellido);
	}
	
	//comprobar funcionamiento en casa
	@GetMapping("/actores/fechas")
	@Operation(summary = "busqueda de actores", description = "busqueda de actores por fecha entre las seleccionadas")
	public List<Actor> buscarActorFecha(@RequestParam LocalDate fechaIni,@RequestParam LocalDate fechafin){
		return service.buscarFecha(fechaIni, fechafin);
	}
	
	@PostMapping("/actores")
	@Operation(summary = "crear actor" , description = "creador de actores")
	public Actor crearActor(@Valid @RequestBody Actor actor) {
		return service.crearActor(actor);
	}
	
	@PutMapping("/actores")
	@Operation(summary = "actualizar actor", description = "actualizar de actores ya creados")
	public Actor actualizarActor(@Valid @RequestBody Actor actor) throws ActorNotFound {
		return service.actualizarActor(actor);
	}
	
	@DeleteMapping("/actores/{id}")
	@Operation(summary = "borrar actor", description = "borrador de actores por la id")
	public void borrarActor(@PathVariable Long id) throws ActorNotFound {
		service.borrarActor(id);
	}
	
}
