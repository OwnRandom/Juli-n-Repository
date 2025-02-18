package ceu.dam.ad.ejemplo.service;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.NOT_FOUND)
public class CocheNotFoundException extends Exception {

	/**
	 * 
	 */
	private static final long serialVersionUID = 8654491808670298168L;

	public CocheNotFoundException() {
		// TODO Auto-generated constructor stub
	}

	public CocheNotFoundException(String message) {
		super(message);
		// TODO Auto-generated constructor stub
	}

	public CocheNotFoundException(Throwable cause) {
		super(cause);
		// TODO Auto-generated constructor stub
	}

	public CocheNotFoundException(String message, Throwable cause) {
		super(message, cause);
		// TODO Auto-generated constructor stub
	}

	public CocheNotFoundException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
		// TODO Auto-generated constructor stub
	}

}
