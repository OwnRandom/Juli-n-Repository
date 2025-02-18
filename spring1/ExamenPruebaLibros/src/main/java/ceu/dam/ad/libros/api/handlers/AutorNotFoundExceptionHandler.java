package ceu.dam.ad.libros.api.handlers;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import ceu.dam.ad.libros.service.AutorNotFoundException;

@ControllerAdvice
public class AutorNotFoundExceptionHandler {

	@ExceptionHandler(AutorNotFoundException.class)
	public ResponseEntity<String> handle(AutorNotFoundException e){
		return ResponseEntity.status(HttpStatus.NOT_FOUND.value()).body(e.getMessage());
	}
}
