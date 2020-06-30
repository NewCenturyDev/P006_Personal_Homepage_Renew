package backend.dto.auth;

public class RegisterDTO extends LoginDTO {
    protected String permission;

    public RegisterDTO(String username, String password, String permission) {
        this.username = username;
        this.password = password;
        this.permission = permission;
    }
    protected RegisterDTO() {}
    public String getPermission() {
        return permission;
    }
    public void setPermission(String permission) { this.permission = permission; }
}
