package ceu.dam.ad.ejemplo.service;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.NOT_FOUND)
public class ActorNotFound extends Exception {

	/**
	 * 
	 */
	private static final long serialVersionUID = -4564317123571610892L;

	public ActorNotFound() {
		// TODO Auto-generated constructor stub
	}

	public ActorNotFound(String message) {
		super(message);
		// TODO Auto-generated constructor stub
	}

	public ActorNotFound(Throwable cause) {
		super(cause);
		// TODO Auto-generated constructor stub
	}

	public ActorNotFound(String message, Throwable cause) {
		super(message, cause);
		// TODO Auto-generated constructor stub
	}

	public ActorNotFound(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
		// TODO Auto-generated constructor stub
	}

}
