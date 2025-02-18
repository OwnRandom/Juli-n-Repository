package ceu.dam.ad.ejemplo.api;

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

import ceu.dam.ad.ejemplo.model.Coche;
import ceu.dam.ad.ejemplo.service.CocheNotFoundException;
import ceu.dam.ad.ejemplo.service.CocheService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import jakarta.validation.Valid;

@RestController
@SecurityRequirement(name = "Authorization")
public class CocheApiService {

	@Autowired
	private CocheService service;

	// get-consultar post-crear put-actualizar delete-borrar
	
	@GetMapping("/coches/{id}")
	@Operation(summary = "consulta de coches", description = "consultar coche a partir de id")
	public Coche consultar(@PathVariable Long id) throws CocheNotFoundException {
		return service.consultarCoche(id);
	}

	@GetMapping("/marcaCoches/{marca}")
	@Operation(summary = "busqueda de coches", description = "busqueda coches a partir de marca")
	public List<Coche> consultarByMarca(@PathVariable(required = false) String marca) {
		return service.buscarCoches(marca);
	}

	@PostMapping("/coches")
	@Operation(summary = "crear coche", description = "crear coche")
	public Coche crear(@Valid @RequestBody Coche coche) {

		return service.crearCoche(coche);

	}

	@PutMapping("/coches")
	@Operation(summary = "actualizador de coches", description = "actualizar coche")
	public Coche actualizar(@Valid @RequestBody Coche coche) throws CocheNotFoundException {

		return service.actualizarCoche(coche);

	}

	@DeleteMapping("/coches/{id}")
	@Operation(summary = "borrador coches", description = "borrar coche a partir de id")
	public void borrar(@PathVariable Long id) throws CocheNotFoundException {
		service.borrarCoche(id);
	}

}
