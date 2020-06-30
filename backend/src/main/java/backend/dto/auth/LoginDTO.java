package backend.dto.auth;

public class LoginDTO {
    protected String username;
    protected String password;

    public LoginDTO(String username, String password) {
        this.username = username;
        this.password = password;
    }
    protected LoginDTO() {}
    public String getUsername() {
        return username;
    }
    public String getPassword() {
        return password;
    }
    public void setUsername(String username) { this.username = username; }
    public void setPassword(String password) { this.username = password; }
}
