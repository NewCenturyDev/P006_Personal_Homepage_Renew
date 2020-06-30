package backend.dto.auth;

public class ModifyAccountDTO extends RegisterDTO {
    protected String originalUsername;

    public ModifyAccountDTO(String originalUsername, RegisterDTO newAccount) {
        this.originalUsername = originalUsername;
        this.username = newAccount.username;
        this.password = newAccount.password;
        this.permission = newAccount.permission;
    }
    protected ModifyAccountDTO() {}

    public String getOriginalUsername() {
        return originalUsername;
    }
}
