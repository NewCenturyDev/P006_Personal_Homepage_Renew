package backend.service;

import backend.dto.auth.LoginDTO;
import backend.dto.auth.ModifyAccountDTO;
import backend.dto.auth.RegisterDTO;
import backend.entity.Auth;

public interface AuthService {
    Auth getAccount(LoginDTO loginDTO) throws Exception;
    Auth createAccount(RegisterDTO registerDTO) throws Exception;
    Auth modifyAccount(ModifyAccountDTO modifyAccountDTO) throws Exception;
    void deleteAccount(LoginDTO loginDTO) throws Exception;
}
