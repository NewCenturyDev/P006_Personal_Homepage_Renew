package backend;

import backend.dto.ResponseDTO;
import backend.dto.auth.AuthResponseDTO;
import backend.dto.auth.LoginDTO;
import backend.dto.auth.RegisterDTO;
import backend.service.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.context.HttpSessionSecurityContextRepository;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpSession;

@RestController
public class AuthController {
    @Autowired
    AuthenticationManager authenticationManager;

    @Autowired
    private AuthService authService;

    @PostMapping("/auth/login")
    public AuthResponseDTO login(@RequestBody LoginDTO loginDTO, HttpSession session) {
        AuthResponseDTO response = new AuthResponseDTO();
        try {
            response.setSuccess(true);
            response.setAccount(authService.getAccount(loginDTO));
            UsernamePasswordAuthenticationToken token = new UsernamePasswordAuthenticationToken(
                loginDTO.getUsername(), loginDTO.getPassword()
            );
            Authentication authentication = authenticationManager.authenticate(token);
            SecurityContextHolder.getContext().setAuthentication(authentication);
            session.setAttribute(
                HttpSessionSecurityContextRepository.SPRING_SECURITY_CONTEXT_KEY,
                SecurityContextHolder.getContext()
            );
            response.setToken(token);
        } catch (Exception e) {
            response.setSuccess(false);
            response.setError(e.getMessage());
        }
        return response;
    }

    @PostMapping("/auth/register")
    public AuthResponseDTO register(@RequestBody RegisterDTO registerDTO) {
        AuthResponseDTO response = new AuthResponseDTO();
        try {
            response.setSuccess(true);
            response.setAccount(authService.createAccount(registerDTO));
        } catch (Exception e) {
            response.setSuccess(false);
            response.setError(e.getMessage());
        }
        return response;
    }

    @PostMapping("/auth/modify")
    public AuthResponseDTO modify(@RequestBody RegisterDTO registerDTO) {
        AuthResponseDTO response = new AuthResponseDTO();
        try {
            response.setSuccess(true);
            response.setAccount(authService.createAccount(registerDTO));
        } catch (Exception e) {
            response.setSuccess(false);
            response.setError(e.getMessage());
        }
        return response;
    }

    @PostMapping("/auth/resign")
    public ResponseDTO resign(@RequestBody LoginDTO loginDTO) {
        ResponseDTO response = new ResponseDTO();
        try {
            response.setSuccess(true);
            authService.deleteAccount(loginDTO);
        } catch (Exception e) {
            response.setSuccess(false);
            response.setError(e.getMessage());
        }
        return response;
    }
}
