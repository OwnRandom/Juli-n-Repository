package ceu.dam.ad.libros.service;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.NOT_FOUND)
public class AutorNotFoundException extends Exception {

	public AutorNotFoundException() {
		// TODO Auto-generated constructor stub
	}

	public AutorNotFoundException(String message) {
		super(message);
		// TODO Auto-generated constructor stub
	}

	public AutorNotFoundException(Throwable cause) {
		super(cause);
		// TODO Auto-generated constructor stub
	}

	public AutorNotFoundException(String message, Throwable cause) {
		super(message, cause);
		// TODO Auto-generated constructor stub
	}

	public AutorNotFoundException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
		// TODO Auto-generated constructor stub
	}

}
