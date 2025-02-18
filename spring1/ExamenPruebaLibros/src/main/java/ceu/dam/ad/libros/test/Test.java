package ceu.dam.ad.libros.test;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import ceu.dam.ad.libros.model.Autor;
import ceu.dam.ad.libros.service.AutorNotFoundException;
import ceu.dam.ad.libros.service.AutorServiceException;
import ceu.dam.ad.libros.service.AutoresService;


public class Test {

	private AutoresService service;
	
	public void test() {
		// ATENCIÓN, ANTES DE VOLVER A EJECUTAR EL TEST POR SEGUNDA VEZ, LANZA ESTOS DELETEs EN TU BBDD  <<-------------
		/* 	DELETE FROM libros;
			DELETE FROM autores;
			DELETE FROM paises;
		*/
		try (Scanner scanner = new Scanner(System.in)) {
			System.out.println(">>>> Si ya has ejecutado el test, borra antes lo que tengas en BBDD con los DELETEs !!!");
			if (!continuar(scanner)) {
				return;
			}
			System.out.println(">>>> Probando método guardarAutores()....");
			List<Autor> autores = new ArrayList<>();
			autores.add(GeneradorAutores.generarAutorTest(1990, "Blas", "CH", "China"));
			autores.add(GeneradorAutores.generarAutorTest(2000, "Blau", "VT", "Vietnam"));
			autores.add(GeneradorAutores.generarAutorTest(2010, "Laura", "NZ", "Nueva Zelanda"));

			try {
				service.guardarAutores(autores);
				System.out.println(autores);
				System.out.println(">>>> Prueba OK!! Revisa si se ha insertado todo en BBDD: 3 autores, 3 países y 9 libros");
			} catch (AutorServiceException e) {
				System.out.println(">>>> Algo no funciona bien....");
				e.printStackTrace();
			}
			if (!continuar(scanner)) {
				return;
			}

			System.out.println(">>>> Probando método consultarAutor()....");
			System.out.println(">>>> Dime el ID del actor que quieres consultar: ");
			Long id = scanner.nextLong();
			scanner.nextLine();
			try {
				Autor autor = service.consultarAutor(id);
				System.out.println(autor);
				System.out.println(">>>> Prueba OK!! Autor consultado. Revisa que todos los datos están OK");
			} catch (AutorServiceException | AutorNotFoundException e) {
				System.out.println(">>>> Algo no funciona bien....");
				e.printStackTrace();
			}
			
			if (!continuar(scanner)) {
				return;
			}
			try {
				service.consultarAutor(99999L);
				System.out.println(">>>> No funciona: no lanzas excepción cuando no existe el actor");
			} catch (AutorServiceException e) {
				System.out.println(">>>> Algo no funciona bien....");
				e.printStackTrace();
			} catch (AutorNotFoundException e) {
				System.out.println(">>>> Prueba OK!! Se lanza excepción cuando no existe el actor");
			}
			System.out.println("\n TEST FINALIZADO");
		}

	}

	private static boolean continuar(Scanner scanner) {
		System.out.println("\n¿Continuar el TEST? (S/N)");
		return scanner.nextLine().trim().equalsIgnoreCase("S");
	}


}
