package ceu.dam.ad.libros.test;

import java.util.ArrayList;

import ceu.dam.ad.libros.model.Autor;
import ceu.dam.ad.libros.model.Libro;
import ceu.dam.ad.libros.model.Pais;



public class GeneradorAutores {

	/** Puedes llamar a este método estático para generar autores de test */
	public static Autor generarAutorTest(int año, String nombre, String codPais, String pais) {
		Autor autor = new Autor();
		autor.setAñoNacimiento(año);
		autor.setNombre(nombre);
		autor.setObra(new ArrayList<>());
		autor.setOrigen(new Pais());
		autor.getOrigen().setCodigo(codPais);
		autor.getOrigen().setNombre(pais);
		for (int i = 0; i < 3; i++) {
			Libro libro = new Libro();
			libro.setAñoEdicion(año + i);
			libro.setIsbn("TEST" + año + "X" + i);
			libro.setTitulo("Libro de prueba " + i);
			autor.getObra().add(libro);
		}
		return autor;
	}

}
