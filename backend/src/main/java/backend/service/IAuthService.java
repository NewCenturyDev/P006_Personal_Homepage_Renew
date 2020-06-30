package backend.service;

import backend.dto.auth.LoginDTO;
import backend.dto.auth.ModifyAccountDTO;
import backend.dto.auth.RegisterDTO;
import backend.entity.Auth;
import backend.persistence.AuthRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;

@Service
public class IAuthService implements AuthService {
    @Autowired
    private AuthRepository authRepository;

    public Auth getAccount(LoginDTO loginDTO) throws Exception {
        Auth targetAccount = authRepository.findByUsername(loginDTO.getUsername());
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        if (targetAccount == null) {
            throw new Exception("1: Wrong Username");
        }
        if (targetAccount.getPassword().equals(passwordEncoder.encode(loginDTO.getPassword()))) {
            return targetAccount;
        } else {
            throw new Exception("2: Wrong Password");
        }
    }
    public Auth createAccount(RegisterDTO registerDTO) throws Exception {
        if (!_validateUsername(registerDTO.getUsername())) {
            throw new Exception("1: Username must shorter than 20 chars");
        }
        if (!_validatePassword(registerDTO.getPassword())) {
            throw new Exception("2: Password must has 6~19 chars");
        }
        if (!_validatePermission(registerDTO.getPermission())) {
            throw new Exception("3: Invalid permission type");
        }
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        registerDTO.setPassword(passwordEncoder.encode(registerDTO.getPassword()));

        Auth newAccount = new Auth(registerDTO);
        authRepository.save(newAccount);

        return newAccount;
    }
    public Auth modifyAccount(ModifyAccountDTO modifyAccountDTO) throws Exception {
        Auth targetAccount = authRepository.findByUsername(modifyAccountDTO.getOriginalUsername());
        if (targetAccount == null) {
            throw new Exception("1: Account not exist");
        }
        if (!_validateUsername(modifyAccountDTO.getUsername())) {
            throw new Exception("2: Username must shorter than 20 chars");
        }
        if (!_validatePassword(modifyAccountDTO.getPassword())) {
            throw new Exception("3: Password must has 6~19 chars");
        }
        if (!_validatePermission(modifyAccountDTO.getPermission())) {
            throw new Exception("4: Invalid permission type");
        }
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        modifyAccountDTO.setPassword(passwordEncoder.encode(modifyAccountDTO.getPassword()));

        targetAccount.setUsername(modifyAccountDTO.getUsername());
        targetAccount.setPassword(modifyAccountDTO.getPassword());
        targetAccount.setPermission(modifyAccountDTO.getPermission());
        authRepository.save(targetAccount);
        return targetAccount;
    }
    public void deleteAccount(LoginDTO loginDTO) throws Exception {
        Auth targetAccount = authRepository.findByUsername(loginDTO.getUsername());
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        if (targetAccount == null) {
            throw new Exception("1: Account not exist");
        }
        if (targetAccount.getPassword().equals(passwordEncoder.encode(loginDTO.getPassword()))) {
            authRepository.deleteByUsername(loginDTO.getUsername());
        } else {
            throw new Exception("2: Wrong Password");
        }
    }
    private Boolean _validateUsername(String username) {
        return username.length() < 20;
    }
    private Boolean _validatePassword(String password) {
        return 6 <= password.length() && password.length() < 20;
    }
    private Boolean _validatePermission(String permission) {
        ArrayList<String> permissionList = new ArrayList<String>(Arrays.asList("admin","author","user"));
        return permissionList.contains((permission));
    }
}
