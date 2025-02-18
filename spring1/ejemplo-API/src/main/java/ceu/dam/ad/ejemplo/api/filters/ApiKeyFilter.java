package ceu.dam.ad.ejemplo.api.filters;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import io.swagger.v3.oas.annotations.enums.SecuritySchemeIn;
import io.swagger.v3.oas.annotations.enums.SecuritySchemeType;
import io.swagger.v3.oas.annotations.security.SecurityScheme;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Component
@SecurityScheme(
		name = "Authorization",
		type = SecuritySchemeType.APIKEY,
		in = SecuritySchemeIn.HEADER,
		paramName = "API-KEY"
		)
public class ApiKeyFilter extends OncePerRequestFilter{
	
	@Value("${api.key}")
	private String apiKey;
	
	@Override
	protected boolean shouldNotFilter(HttpServletRequest request) {
		String requestURI = request.getRequestURI();
		return (requestURI.startsWith("/swagger") || requestURI.startsWith("/api-dos"));
		
	}
	
	@Override
	protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
			throws ServletException, IOException {
		String apiKeyRequest = request.getHeader("API-KEY");
		String path = request.getRequestURI();
		if (path.startsWith("/swagger") || path.startsWith("/api-doc") || apiKey.equals(apiKeyRequest)) {
		    filterChain.doFilter(request, response);
		}else {
			response.setStatus(HttpStatus.UNAUTHORIZED.value());
			response.getWriter().write("Vete a tu casa!!");
		}
	}

	

}
