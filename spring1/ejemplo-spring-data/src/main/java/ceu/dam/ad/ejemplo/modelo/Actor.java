package ceu.dam.ad.ejemplo.modelo;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Data;

@Data
@Entity
//En caso de que la tabla se llame de otra manera = @Table(name = "actores")
public class Actor {
		
		@Id
		@GeneratedValue(strategy = GenerationType.IDENTITY)
		@Column(name = "actor_id")
		private Long id;
		
		//Cuando se utiliza camelCase la base de datos detecta que lo que los separa es un _ entonces no hace falta cambiarla
		private String firstName;
		private String lastName;
		
		
}
