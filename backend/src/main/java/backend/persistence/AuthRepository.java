package backend.persistence;

import backend.entity.Auth;
import org.springframework.data.repository.CrudRepository;

public interface AuthRepository extends CrudRepository<Auth, Integer> {
    Auth findByUsername(String username);
    void deleteByUsername(String username);
}
