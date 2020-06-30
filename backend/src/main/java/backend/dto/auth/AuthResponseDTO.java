package backend.dto.auth;

import backend.dto.ResponseDTO;
import backend.entity.Auth;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;

public class AuthResponseDTO extends ResponseDTO {
    private Auth account;
    private UsernamePasswordAuthenticationToken token;

    public Auth getAccount() {
        return account;
    }
    public void setAccount(Auth account) {
        this.account = account;
    }
    public UsernamePasswordAuthenticationToken getToken() {
        return token;
    }
    public void setToken(UsernamePasswordAuthenticationToken token) {
        this.token = token;
    }
}
