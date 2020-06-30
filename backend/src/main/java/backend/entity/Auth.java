package backend.entity;

import backend.dto.auth.RegisterDTO;

import javax.persistence.*;

@Entity
@Table(name = "AUTH")

public class Auth {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "USERNAME")
    private String username;

    @Column(name = "PASSWORD")
    private String password;

    @Column(name = "PERMISSION")
    private String permission;

    protected Auth() {}

    public Auth(RegisterDTO registerDTO) {
        this.username = registerDTO.getUsername();
        this.password = registerDTO.getPassword();
        this.permission = registerDTO.getPermission();
    }
    public Integer getAccountID() {
        return this.id;
    }
    public String getUsername() {
        return this.username;
    }
    public String getPassword() {
        return this.password;
    }
    public String getPermission() {
        return this.permission;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    public void setPermission(String permission) {
        this.permission = permission;
    }
}
